from datetime import date
from pydantic import BaseModel


class Foods(BaseModel):
    food_id: str
    name: str

    class Config:
        orm_mode = True


class Garage(BaseModel):
    user_id: str
    food_id: str
    quantity: int
    limit_at: date


class GaragePost(BaseModel):
    name: str
    quantity: int
    limit_at: date


class GarageResponse(BaseModel):
    food_id: str
    name: str
    quantity: int
    limit_at: date