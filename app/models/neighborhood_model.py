from pydantic import BaseModel


class Neighborhood(BaseModel):
    city: str
    neighborhood: str
