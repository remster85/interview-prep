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
# === Load from file ===
from datamodel import TradeResponse

from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from typing import List, Optional
import json


# === Data Models ===

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Repo:
    value: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Collateral:
    value: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TriParty:
    value: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Product:
    repo: Optional[Repo] = None
    collateral: Optional[Collateral] = None
    triParty: Optional[TriParty] = None  # camelCase matches converted key

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Trade:
    product: Product

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TradeResponse:
    count: int
    items: List[Trade]


# === PascalCase → camelCase recursive converter ===
def pascal_to_camel(obj):
    if isinstance(obj, list):
        return [pascal_to_camel(item) for item in obj]
    elif isinstance(obj, dict):
        return {
            k[0].lower() + k[1:] if k and isinstance(k, str) and k[0].isupper() else k: pascal_to_camel(v)
            for k, v in obj.items()
        }
    else:
        return obj


# === Load and parse ===
def load_trade_response(file_path: str) -> TradeResponse:
    with open(file_path, 'r') as f:
        raw_json = json.load(f)
    converted_json = pascal_to_camel(raw_json)
    return TradeResponse.from_dict(converted_json)


# === Example Usage ===
if __name__ == "__main__":
    trade_response = load_trade_response("otResponse.json")
    print(trade_response)



