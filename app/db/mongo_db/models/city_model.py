import dataclasses
from bson import ObjectId
from typing import Optional
@dataclasses.dataclass
class City:
    name: str
    code: str
    pages: int

@dataclasses.dataclass
class CityUpdate:
    name: str
    pages: int

