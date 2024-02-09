from typing import Literal, Annotated, List
from os import getenv
import strawberry
from pydantic import BaseModel, Field
from strawberry.types.info import Info as _Info, RootValueType
from strawberry_permissions import GraphQLContext


type Info = _Info[GraphQLContext, RootValueType]
type Intervals = Literal["monthly", "annual", "quarterly"]
type IntervalType = Annotated[Intervals, strawberry.union("IntervalType")]


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
class TimeSeriesMetadata:
    information: str = strawberry.field(
        description="Information about the time series."
    )
    symbol: str = strawberry.field(description="The symbol of the time series.")
    last_refreshed: str = strawberry.field(
        description="The last refreshed timestamp of the time series."
    )
    output_size: str = strawberry.field(
        default="compact", description="The output size of the time series."
    )
    time_zone: str = strawberry.field(description="The time zone of the time series.")


@strawberry.type
class CommodoitiesDataInterface:
    """
    This class represents the data for a commodity.

    Args:
        date (str): The date of the data point.
        value (str): The value of the commodity on the given date.
    """

    date: str = strawberry.field(default="XXXX-XX-XX")
    value: str = strawberry.field(default="0.00")


@strawberry.type
class CommoditiesInterface:
    """
    This class represents a commodity.

    Args:
        name (str): The name of the commodity.
        interval (str): The interval of the data points.
        unit (str): The unit of the commodity.
        data (List[CommoditiesDataInterface]): The list of data points for the commodity.
    """

    name: str = strawberry.field(default="")
    interval: str = strawberry.field(default="monthly")
    unit: str = strawberry.field(default="")
    data: List[CommodoitiesDataInterface] = strawberry.field(default_factory=list)


@strawberry.type
class DigitalCurrencyMetadata:
    """
    This class represents the metadata for a digital currency.

    Args:
        information (str): A general overview of the digital currency.
        digital_currency_code (str): The code for the digital currency.
        digital_currency_name (str): The name of the digital currency.
        market_code (str): The code for the market where the digital currency is traded.
        market_name (str): The name of the market where the digital currency is traded.
        last_updated (str): The date and time when the metadata was last updated.
        time_zone (str): The time zone of the market where the digital currency is traded.
    """

    information: str = strawberry.field(default="")
    digital_currency_code: str = strawberry.field(default="")
    digital_currency_name: str = strawberry.field(default="")
    market_code: str = strawberry.field(default="")
    market_name: str = strawberry.field(default="")
    last_updated: str = strawberry.field(default="")
    time_zone: str = strawberry.field(default="")


@strawberry.type
class DigitalCurrencySeries:
    """
    This class represents the intraday data for a digital currency.

    Args:
        date (str): The date of the data point.
        open_market (float): The open price of the digital currency in the base currency of the market.
        open_usd (float): The open price of the digital currency in USD.
        high_market (float): The highest price of the digital currency in the base currency of the market.
        high_usd (float): The highest price of the digital currency in USD.
        low_market (float): The lowest price of the digital currency in the base currency of the market.
        low_usd (float): The lowest price of the digital currency in USD.
        close_market (float): The closing price of the digital currency in the base currency of the market.
        close_usd (float): The closing price of the digital currency in USD.
        volume (float): The trading volume of the digital currency.
        market_cap_usd (float): The market capitalization of the digital currency in USD.
    """

    date: str
    open_market: float = strawberry.field(default=0.0)
    open_usd: float = strawberry.field(default=0.0)
    high_market: float = strawberry.field(default=0.0)
    high_usd: float = strawberry.field(default=0.0)
    low_market: float = strawberry.field(default=0.0)
    low_usd: float = strawberry.field(default=0.0)
    close_market: float = strawberry.field(default=0.0)
    close_usd: float = strawberry.field(default=0.0)
    volume: float = strawberry.field(default=0.0)
    market_cap_usd: float = strawberry.field(default=0.0)


@strawberry.type
class DigitalCurrencyInterface:
    """
    This class represents a digital currency.

    Args:
        metadata (DigitalCurrencyMetadata): The metadata for the digital currency.
        series (List[TimeSeriesInterface]): The list of time series data for the digital currency.
    """

    metadata: DigitalCurrencyMetadata = strawberry.field()
    series: List[DigitalCurrencySeries] = strawberry.field(default_factory=list)


@strawberry.type
class TimeSeriesData:
    """The TimeSeriesType class represents a time series data with open, high, low, close, and volume
    attributes."""

    date: str = strawberry.field(default="")
    open: float = strawberry.field()
    high: float = strawberry.field()
    low: float = strawberry.field()
    close: float = strawberry.field()
    volume: float = strawberry.field()


@strawberry.type
class DigitalCurrencyIntradayInterface:
    """
    This class represents the intraday data for a digital currency.

    Args:
        metadata (DigitalCurrencyMetadata): The metadata for the digital currency.
        series (List[TimeSeriesInterface]): The list of time series data for the digital currency.
    """

    metadata: DigitalCurrencyMetadata = strawberry.field()
    series: List[TimeSeriesData] = strawberry.field(default_factory=list)


@strawberry.type
class TimeSeriesAdjustedData(TimeSeriesData):
    """
    The code is defining a class called `TimeSeriesAdjustedType` using the `@strawberry.type`
    decorator. Inside the class, there are several attributes defined using the `open`, `high`,
    `low`, `close`, `adjusted_close`, `volume`, and `dividend_amount` names. Each attribute is
    assigned a type of `float` and is decorated with `strawberry.field()`.
    """

    adjusted_close: float = strawberry.field()
    dividend_amount: float = strawberry.field()


@strawberry.type
class TimeSeriesInterface:
    metadata: TimeSeriesMetadata = strawberry.field()
    data: List[TimeSeriesData] = strawberry.field(default_factory=list)


@strawberry.type
class TimeSeriesAdjustedInterface:
    metadata: TimeSeriesMetadata = strawberry.field()
    data: List[TimeSeriesAdjustedData] = strawberry.field(default_factory=list)
