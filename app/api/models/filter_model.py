import dataclasses
from typing import List
from pydantic import BaseModel
from app.api.models.min_max_model import MinMax
from app.api.models.property_group_model import PropertyGroup

filteres= {
    "city":"0070",
    "propertyGroup": [
        "apartments",
        "2Chouses"
        ],
    "price":"-1-3000000",
    "squaremeter":"-1-200",
    "floor":"-1-3",
    "imageOnly":1,
    "priceOnly":1
}

["apartments", "houses", "misc"]


class FilterApi(BaseModel):
    city: str
    page: int
    propertyGroup: PropertyGroup = PropertyGroup()
    imageOnly: bool = 0
    priceOnly: bool = 0
    squaremeter: MinMax = MinMax(min=30,max=1000)
    price: MinMax = MinMax(min=200000,max=20000000)
    floor: MinMax = MinMax(min=0,max=100)

    def __str__(self):
        return (f"city={self.city}&"
                f"page={self.page}&"
                f"imageOnly={int(self.imageOnly)}&"
                f"priceOnly={int(self.priceOnly)}&"
                f"{self.squaremeter.squaremeter()}&"
                f"{self.price.price()}&"
                f"{self.floor.floor()}&"
                f"{str(self.propertyGroup)}")

