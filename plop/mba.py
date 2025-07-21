'''
{
  "Count": 3,
  "Items": [
    {
      "Product": {
        "Repo": {
          "Value": "13"
        }
      }
    },
    {
      "Product": {
        "Collateral": {
          "Value": "27"
        }
      }
    },
    {
      "Product": {
        "TriParty": {
          "Value": "42"
        }
      }
    }
  ]
}

'''

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, config
from typing import List, Union, Optional


# === Product Type Models ===
@dataclass_json
@dataclass
class Repo:
    value: str = field(metadata=config(field_name="Value"))

@dataclass_json
@dataclass
class Collateral:
    value: str = field(metadata=config(field_name="Value"))

@dataclass_json
@dataclass
class TriParty:
    value: str = field(metadata=config(field_name="Value"))


# === Product Wrapper ===
@dataclass_json
@dataclass
class Product:
    repo: Optional[Repo] = field(default=None, metadata=config(field_name="Repo"))
    collateral: Optional[Collateral] = field(default=None, metadata=config(field_name="Collateral"))
    tri_party: Optional[TriParty] = field(default=None, metadata=config(field_name="TriParty"))


# === Trade Item ===
@dataclass_json
@dataclass
class Trade:
    product: Product = field(metadata=config(field_name="Product"))


# === Root Response ===
@dataclass_json
@dataclass
class TradeResponse:
    count: int = field(metadata=config(field_name="Count"))
    items: List[Trade] = field(metadata=config(field_name="Items"))
# === Load from file ===
from datamodel import TradeResponse


def load_trade_response(file_path: str) -> TradeResponse:
    with open(file_path, 'r') as f:
        content = f.read()
    return TradeResponse.from_json(content)


# === Example usage ===
if __name__ == "__main__":
    trade_response = load_trade_response("otResponse.json")
    print(trade_response)
