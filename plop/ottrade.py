from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase
from typing import Optional, List, Iterable
from datetime import date, datetime


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BondPayload:
    isin: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SecurityPayload:
    bond: Optional[BondPayload] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TriPartySecurityPayload:
    startDate: Optional[date] = None
    security: Optional[SecurityPayload] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LendingDetailsPayload:
    startDate: date
    weBorrow: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CashPayload:
    startCashAmount: Optional[float] = None  # decimal in C#
    notional: Optional[float] = None
    nominalParFill: Optional[int] = None
    subType: Optional[str] = None
    noticePeriod: Optional[int] = None
    security: Optional[SecurityPayload] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SecuritiesItemPayload:
    startDate: date
    security: Optional[SecurityPayload] = None
    isCollateralTaken: Optional[bool] = None
    nominal: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RepoPayload:
    securities: Optional[List[SecuritiesItemPayload]] = None
    cash: Optional[CashPayload] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CollateralPoolPayload:
    securities: List[SecuritiesItemPayload]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TripartyRepoPayload:
    cash: Optional[CashPayload] = None
    security: TriPartySecurityPayload = field(default_factory=TriPartySecurityPayload)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SecurityLendingWithCashPayload:
    securities: List[SecuritiesItemPayload]
    cash: Optional[CashPayload] = None
    lendingDetails: LendingDetailsPayload = field(default_factory=LendingDetailsPayload)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ProductPayload:
    repo: Optional[RepoPayload] = None
    collateralPool: Optional[CollateralPoolPayload] = None
    tripartyRepo: Optional[TripartyRepoPayload] = None
    securityLendingWithCash: Optional[SecurityLendingWithCashPayload] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PropertiesPayload:
    isSponsored: Optional[bool] = None
    cdr: Optional[int] = None  # Maps from JSON key "CDR"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PartyPayload:
    code: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BookPayload:
    code: str
    properties: PropertiesPayload


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TradePayload:
    id: str
    contractId: int
    settlementDate: date
    status: str
    tradeType: str
    inputTimeUtc: datetime
    tradingDay: date
    riskMaturityDate: date
    book: BookPayload
    product: ProductPayload
    party: PartyPayload
    initialParty: Optional[PartyPayload] = None
    properties: PropertiesPayload = field(default_factory=PropertiesPayload)

    # Property to check if product has any of these non-null
    @property
    def isValid(self) -> bool:
        p = self.product
        return any([
            p.repo is not None,
            p.tripartyRepo is not None,
            p.securityLendingWithCash is not None,
            p.collateralPool is not None
        ])

    # You can implement methods like GetTrades() similarly in Python
    # Here just a stub, detailed logic depends on your business needs
