from pydantic import BaseModel, Field

try:
    from enum import EnumType
except ImportError:
    from enum import EnumMeta as EnumType


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


class EnumTypeBase(EnumType):
    def __getitem__(cls, name):  # noqa: N805
        try:
            return super().__getitem__(name)
        except KeyError as err:
            raise ValueError(f'"{name}" is not a valid {cls.__qualname__}') from err
