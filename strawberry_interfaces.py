import strawberry


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
