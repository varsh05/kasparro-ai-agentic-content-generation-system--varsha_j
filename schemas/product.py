from pydantic import BaseModel, Field
from typing import List


class ProductPageSchema(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=20)
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    safety_information: str
    price: float
