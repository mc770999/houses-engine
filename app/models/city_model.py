from pydantic import BaseModel


class City(BaseModel):
    city: str
    code: str
    pages: int
    page: int = 1



