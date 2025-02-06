import json
from dataclasses import dataclass, asdict
from typing import Optional

# Dataclass definitions (same as before)
@dataclass
class House:
    number: Optional[int]
    floor: Optional[int]

@dataclass
class Coords:
    lon: Optional[float]
    lat: Optional[float]

@dataclass
class Address:
    city: Optional[str]
    area: Optional[str]
    neighborhood: Optional[str]
    street: Optional[str]
    house: Optional[House]
    coords: Optional[Coords]

@dataclass
class PropertyCondition:
    id: Optional[int]


@dataclass
class AdditionalDetails:
    property: Optional[str]
    roomsCount: Optional[int]
    squareMeter: Optional[int]
    propertyCondition: Optional[PropertyCondition]

@dataclass
class Ad:
    address: Optional[Address]
    subcategoryId: Optional[int]
    categoryId: Optional[int]
    adType: Optional[str]
    price: Optional[int]
    token: Optional[str]
    additionalDetails: Optional[AdditionalDetails]


# Deserialize JSON with .get()
data = {
    "address": {
        "city": {"text": "ירושלים"},
        "area": {"text": "אזור ירושלים"},
        "neighborhood": {"text": "הרובע היהודי"},
        "street": {"text": "משגב לדך"},
        "house": {"number": 54, "floor": 0},
        "coords": {"lon": 35.232796, "lat": 31.77553},
    },
    "subcategoryId": 1,
    "categoryId": 2,
    "adType": "private",
    "price": 3990000,
    "token": "qhj6yyev",
    "additionalDetails": {
        "property": {"text": "תיירות ונופש"},
        "roomsCount": 2,
        "squareMeter": 50,
        "propertyCondition": {"id": 2},
    },
}



