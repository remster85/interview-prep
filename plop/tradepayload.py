from enum import Enum
from datetime import datetime, date
from typing import Iterator, Optional


class TradeDirection(Enum):
    Asset = "Asset"
    Liability = "Liability"
    NoCash = "NoCash"


@dataclass
class Trade:
    id: str
    book: str
    enteredAt: datetime
    tradeDate: date
    endDate: Optional[date]
    counterpartyId: str
    ficcCleared: bool
    sponsored: bool
    isin: str
    startDate: date
    money: float
    quantity: int
    tradeType: str
    cashDirection: TradeDirection
    closeDate: Optional[date] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TradePayload:
    # ... all previous fields ...

    @property
    def isValid(self) -> bool:
        p = self.product
        return any([
            p.repo is not None,
            p.tripartyRepo is not None,
            p.securityLendingWithCash is not None,
            p.collateralPool is not None
        ])

    def get_trade(
        self,
        isin: str,
        start_date: date,
        money: float,
        quantity: int,
        trade_type: str,
        cash_direction: TradeDirection,
        id: Optional[str] = None
    ) -> Trade:
        return Trade(
            id=id or self.id,
            book=self.book.code,
            enteredAt=self.inputTimeUtc,
            tradeDate=self.tradingDay,
            endDate=self.riskMaturityDate if self.riskMaturityDate != date.max else None,
            counterpartyId=(self.initialParty or self.party).code,
            ficcCleared=self.party.code == "FIXEDINC",
            sponsored=self.properties.isSponsored or False,
            isin=isin,
            startDate=start_date,
            money=money,
            quantity=quantity,
            tradeType=trade_type,
            cashDirection=cash_direction,
            closeDate=None
        )

    def get_trades(self) -> Iterator[Trade]:
        p = self.product

        if p.repo and p.repo.cash:
            sec = p.repo.securities[0]
            cash_subtype = p.repo.cash.subType
            cash_direction = {
                "ReverseRepo": TradeDirection.Asset,
                "Repo": TradeDirection.Liability
            }.get(cash_subtype)
            if cash_direction is None:
                raise ValueError(f"Unexpected cash subtype: {cash_subtype}")

            yield self.get_trade(
                isin=sec.security.bond.isin,
                start_date=sec.startDate,
                money=p.repo.cash.startCashAmount or 0,
                quantity=p.repo.cash.nominalParFill or 0,
                trade_type="Repo",
                cash_direction=cash_direction
            )

        if p.securityLendingWithCash and p.securityLendingWithCash.cash:
            sec = p.securityLendingWithCash.securities[0]
            we_borrow = p.securityLendingWithCash.lendingDetails.weBorrow
            cash_direction = TradeDirection.Asset if we_borrow else TradeDirection.Liability

            yield self.get_trade(
                isin=sec.security.bond.isin,
                start_date=sec.startDate,
                money=p.securityLendingWithCash.cash.notional or 0,
                quantity=sec.nominal or 0,
                trade_type="SecurityLendingWithCash",
                cash_direction=cash_direction
            )

        if p.collateralPool:
            for i, sec in enumerate(p.collateralPool.securities):
                cash_direction = TradeDirection.Asset if sec.isCollateralTaken else TradeDirection.Liability
                yield self.get_trade(
                    isin=sec.security.bond.isin,
                    start_date=sec.startDate,
                    money=0,
                    quantity=sec.nominal or 0,
                    trade_type="CollateralPool",
                    cash_direction=cash_direction,
                    id=f"{self.id}_{i}"
                )
