from pydantic import BaseModel, Field


class UnitBase(BaseModel):
    alpha_3: str = Field(
        min_length=3,
        max_length=3,
    )
    numeric: str = Field(
        min_length=3,
        max_length=3,
    )
    name: str
