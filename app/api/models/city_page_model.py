from pydantic import BaseModel

class CityPage(BaseModel):
    city: str
    pages: int
    page: int = 1

    def __str__(self):
        return (f"city={self.city}&"
                f"page={self.page}")

