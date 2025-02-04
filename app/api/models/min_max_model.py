import dataclasses
from pydantic import BaseModel


class MinMax(BaseModel):
    min: int
    max: int

    def floor(self):
        return f"minFloor={self.min}&maxFloor={self.max}"

    def price(self):
        return f"minPrice={self.min}&maxPrice={self.max}"

    def squaremeter(self):
        return f"minSquaremeter={self.min}&maxSquaremeter={self.max}"

