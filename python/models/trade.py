from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional, List, Union

@dataclass
class BondPayload:
    isin: str

@dataclass
class SecurityPayload:
    bond: Optional[BondPayload]

@dataclass
class SecuritiesItemPayload:
    start_date: date
    security: Optional[SecurityPayload]
    is_collateral_taken: Optional[bool]
    nominal: Optional[int]

@dataclass
class CashPayload:
    start_cash_amount: Optional[float]
    notional: Optional[float]
    nominal_par_fill: Optional[int]
    sub_type: Optional[str]
    notice_period: Optional[int]
    security: Optional[SecurityPayload]

@dataclass
class TriPartySecurityPayload:
    start_date: Optional[date]
    security: Optional[SecurityPayload]

@dataclass
class RepoPayload:
    securities: Optional[List[SecuritiesItemPayload]]
    cash: Optional[CashPayload]

@dataclass
class CollateralPoolPayload:
    securities: List[SecuritiesItemPayload]

@dataclass
class LendingDetailsPayload:
    start_date: date
    we_borrow: Optional[bool]

@dataclass
class SecurityLendingWithCashPayload:
    securities: List[SecuritiesItemPayload]
    cash: Optional[CashPayload]
    lending_details: LendingDetailsPayload

@dataclass
class TripartyRepoPayload:
    cash: Optional[CashPayload]
    security: TriPartySecurityPayload

@dataclass
class ProductPayload:
    repo: Optional[RepoPayload]
    collateral_pool: Optional[CollateralPoolPayload]
    triparty_repo: Optional[TripartyRepoPayload]
    security_lending_with_cash: Optional[SecurityLendingWithCashPayload]

@dataclass
class PropertiesPayload:
    is_sponsored: Optional[bool]
    cdr: Optional[int]

@dataclass
class BookPayload:
    code: str
    properties: PropertiesPayload

@dataclass
class PartyPayload:
    code: str

class TradeDirection:
    Asset = "Asset"
    Liability = "Liability"
    NoCash = "NoCash"

@dataclass
class Trade:
    id: str
    book: str
    entered_at: datetime
    trade_date: date
    end_date: Optional[date]
    counterparty_id: str
    ficc_cleared: bool
    sponsored: bool
    isin: str
    start_date: date
    money: float
    quantity: int
    trade_type: str
    cash_direction: str
    close_date: Optional[date] = None

@dataclass
class TradePayload1:
    id: str
    contract_id: int
    settlement_date: date
    status: str
    trade_type: str
    input_time_utc: datetime
    trading_day: date
    risk_maturity_date: date
    book: BookPayload
    product: ProductPayload
    party: PartyPayload
    initial_party: Optional[PartyPayload]
    properties: PropertiesPayload

    @property
    def is_valid(self) -> bool:
        return any([
            self.product.repo is not None,
            self.product.triparty_repo is not None,
            self.product.security_lending_with_cash is not None,
            self.product.collateral_pool is not None
        ])

    def get_trades(self) -> List[Trade]:
        match self.product:
            case ProductPayload(repo=repo) if repo and repo.cash:
                sec = repo.securities[0]
                return [self._get_trade(
                    isin=sec.security.bond.isin,
                    start_date=sec.start_date,
                    money=repo.cash.start_cash_amount or 0,
                    quantity=repo.cash.nominal_par_fill or 0,
                    trade_type="repo",
                    cash_direction=self._repo_cash_direction(repo.cash.sub_type)
                )]
            case ProductPayload(security_lending_with_cash=slwc) if slwc and slwc.cash:
                sec = slwc.securities[0]
                return [self._get_trade(
                    isin=sec.security.bond.isin,
                    start_date=sec.start_date,
                    money=slwc.cash.notional or 0,
                    quantity=sec.nominal or 0,
                    trade_type="security_lending_with_cash",
                    cash_direction=TradeDirection.Asset if slwc.lending_details.we_borrow else TradeDirection.Liability
                )]
            case ProductPayload(collateral_pool=cp):
                return [
                    self._get_trade(
                        isin=s.security.bond.isin,
                        start_date=s.start_date,
                        money=0,
                        quantity=s.nominal or 0,
                        trade_type="collateral_pool",
                        cash_direction=TradeDirection.Asset if s.is_collateral_taken else TradeDirection.Liability,
                        id=f"{self.id}_{i}"
                    )
                    for i, s in enumerate(cp.securities)
                ]
            case ProductPayload(triparty_repo=tr):
                return [self._get_trade(
                    isin=tr.security.security.bond.isin,
                    start_date=tr.security.start_date,
                    money=tr.cash.start_cash_amount or 0,
                    quantity=int(tr.cash.start_cash_amount or 0),
                    trade_type="triparty_repo",
                    cash_direction=self._repo_cash_direction(tr.cash.sub_type)
                )]
            case _:
                return []

    def _repo_cash_direction(self, sub_type: Optional[str]) -> str:
        match sub_type:
            case "ReverseRepo":
                return TradeDirection.Asset
            case "Repo":
                return TradeDirection.Liability
            case _:
                return TradeDirection.NoCash

    def _get_trade(self, isin: str, start_date: date, money: float, quantity: int, trade_type: str,
                   cash_direction: str, id: Optional[str] = None) -> Trade:
        return Trade(
            id=id or self.id,
            book=self.book.code,
            entered_at=self.input_time_utc,
            trade_date=self.trading_day,
            end_date=self.risk_maturity_date if self.risk_maturity_date != date.max else None,
            counterparty_id=(self.initial_party or self.party).code,
            ficc_cleared=self.party.code == "FIXEDINC",
            sponsored=self.properties.is_sponsored or False,
            isin=isin,
            start_date=start_date,
            money=money,
            quantity=quantity,
            trade_type=trade_type,
            cash_direction=cash_direction
        )
