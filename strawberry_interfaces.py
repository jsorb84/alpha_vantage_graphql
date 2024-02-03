import strawberry
import dataclasses
from os import getenv
from typing import Optional, Required, TypedDict
from pydantic import BaseModel, Field
from strawberry.types.info import Info as _Info, RootValueType
from strawberry_permissions import GraphQLContext

# @dataclasses.dataclass
# class API_Parameters[M: BaseModel | None]:
#     """Wrapper for all Alpha Vantage APIs"""

#     apikey: str = dataclasses.field(default=getenv("AV_KEY"))
#     function: str = dataclasses.field(default="TIME_SERIES_WEEKLY")
#     symbol: str | None = dataclasses.field(default=None)
#     interval: str | None = dataclasses.field(default=None)
#     maturity: str | None = dataclasses.field(default=None)
#     datatype: str = dataclasses.field(default="json")
#     validation_model: type[M] | None = dataclasses.field(default=None)
type Info = _Info[GraphQLContext, RootValueType]


class API_Parameters[M: BaseModel](BaseModel):
    """Wrapper for all Alpha Vantage APIs"""

    apikey: str = Field(default=getenv("AV_KEY"))
    function: str = Field(default="TIME_SERIES_WEEKLY")
    symbol: str | None = Field(default=None)
    interval: str | None = Field(default=None)
    maturity: str | None = Field(default=None)
    datatype: str = Field(default="json")
    validation_model: type[M] | None = Field(default=None)
    info: Info | None = Field(default=None)


@strawberry.type
class TimeSeriesInterface:
    """The TimeSeriesType class represents a time series data with open, high, low, close, and volume
    attributes."""

    date: str = strawberry.field(default="")
    open: float = strawberry.field()
    high: float = strawberry.field()
    low: float = strawberry.field()
    close: float = strawberry.field()
    volume: float = strawberry.field()


@strawberry.type
class TimeSeriesAdjustedInterface(TimeSeriesInterface):
    """
    The code is defining a class called `TimeSeriesAdjustedType` using the `@strawberry.type`
    decorator. Inside the class, there are several attributes defined using the `open`, `high`,
    `low`, `close`, `adjusted_close`, `volume`, and `dividend_amount` names. Each attribute is
    assigned a type of `float` and is decorated with `strawberry.field()`.
    """

    adjusted_close: float = strawberry.field()
    dividend_amount: float = strawberry.field()
