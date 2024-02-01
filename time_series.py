"""
    Strawberry GraphQL schema for the TimeSeriesType and TimeSeriesAdjustedType classes.
"""
from typing import Literal, List
from os import getenv
import strawberry
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries

load_dotenv()
key = getenv("AV_KEY")
av = TimeSeries(key=key)


@strawberry.type
class TimeSeriesType:
    """The TimeSeriesType class represents a time series data with open, high, low, close, and volume
    attributes."""

    open: float = strawberry.field()
    high: float = strawberry.field()
    low: float = strawberry.field()
    close: float = strawberry.field()
    volume: float = strawberry.field()


@strawberry.type
class TimeSeriesAdjustedType:
    """
    The code is defining a class called `TimeSeriesAdjustedType` using the `@strawberry.type`
    decorator. Inside the class, there are several attributes defined using the `open`, `high`,
    `low`, `close`, `adjusted_close`, `volume`, and `dividend_amount` names. Each attribute is
    assigned a type of `float` and is decorated with `strawberry.field()`.
    """

    open: float = strawberry.field()
    high: float = strawberry.field()
    low: float = strawberry.field()
    close: float = strawberry.field()
    adjusted_close: float = strawberry.field()
    volume: float = strawberry.field()
    dividend_amount: float = strawberry.field()


def process_timeseries_adjusted(data: Literal) -> TimeSeriesAdjustedType:
    """
    The function `process_timeseries_adjusted` takes in a dictionary of time series data and returns a
    list of `TimeSeriesAdjustedType` objects with the data converted to the appropriate data types.

    :param data: The `data` parameter is a dictionary containing time series data. Each key in the
    dictionary represents a day, and the corresponding value is another dictionary containing the
    following keys:
    :type data: Literal
    :return: The function `process_timeseries_adjusted` returns a list of `TimeSeriesAdjustedType`
    objects.
    """
    x = [
        TimeSeriesAdjustedType(
            open=float(data[day]["1. open"]),
            high=float(data[day]["2. high"]),
            low=float(data[day]["3. low"]),
            close=float(data[day]["4. close"]),
            adjusted_close=float(data[day]["5. adjusted close"]),
            volume=float(data[day]["6. volume"]),
            dividend_amount=float(data[day]["7. dividend amount"]),
        )
        for day in data
    ]
    return x


def process_timeseries(data: Literal) -> TimeSeriesType:
    """
    The function `process_timeseries` takes in a dictionary of time series data and converts it into a
    list of `TimeSeriesType` objects.

    :param data: The `data` parameter is expected to be a dictionary containing time series data. Each
    key in the dictionary represents a day, and the corresponding value is another dictionary containing
    the open, high, low, close, and volume values for that day
    :type data: Literal
    :return: a list of TimeSeriesType objects.
    """
    x = [
        TimeSeriesType(
            open=float(data[day]["1. open"]),
            high=float(data[day]["2. high"]),
            low=float(data[day]["3. low"]),
            close=float(data[day]["4. close"]),
            volume=float(data[day]["5. volume"]),
        )
        for day in data
    ]
    return x


@strawberry.type(name="TimeSeriesAdjusted")
class TIME_SERIES_ADJUSTED:

    """The code block you provided defines a GraphQL type called `TIME_SERIES_ADJUSTED` using the
    `@strawberry.type` decorator. This type has three fields: `daily`, `monthly`, and `weekly`. Each
    field is decorated with `@strawberry.field` and has its own resolver function. The resolver functions
    """

    @strawberry.field
    def daily(
        self, symbol: str, outputsize: str = "compact"
    ) -> List[TimeSeriesAdjustedType]:
        """
        The function `daily` retrieves daily adjusted stock data for a given symbol and returns it as a
        processed time series.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to identify a specific stock in the financial market
        :type symbol: str
        :param outputsize: The `outputsize` parameter is used to specify the size of the output. It can
        have two possible values:, defaults to compact
        :type outputsize: str (optional)
        :return: a list of TimeSeriesAdjustedType objects.
        """
        data, _ = av.get_daily_adjusted(symbol, outputsize)
        return process_timeseries_adjusted(data)

    @strawberry.field
    def monthly(self, symbol: str) -> List[TimeSeriesAdjustedType]:
        """
        The function `monthly` retrieves monthly adjusted time series data for a given stock symbol and
        processes it.

        :param symbol: The `symbol` parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the monthly adjusted time series data for that
        particular stock
        :type symbol: str
        :return: a list of TimeSeriesAdjustedType objects.
        """
        data, _ = av.get_monthly_adjusted(symbol)
        return process_timeseries_adjusted(data)

    @strawberry.field
    def weekly(self, symbol: str) -> List[TimeSeriesAdjustedType]:
        """
        The function `weekly` retrieves weekly adjusted time series data for a given stock symbol and
        processes it.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the weekly adjusted time series data for that
        particular stock
        :type symbol: str
        :return: a list of TimeSeriesAdjustedType objects.
        """
        data, _ = av.get_weekly_adjusted(symbol)
        return process_timeseries_adjusted(data)


@strawberry.type(name="TimeSeries")
class TIME_SERIES:
    """
    The code defines four functions for retrieving intraday, daily, monthly, and weekly time series
    data for a given stock symbol.

    :param symbol: The "symbol" parameter is a string that represents the stock symbol or ticker
    symbol of a company. It is used to identify the specific stock for which you want to retrieve
    the time series data
    :type symbol: str
    :param interval: The "interval" parameter specifies the time interval for the intraday data. It
    can be set to values like "1min", "5min", "15min", "30min", or "60min". This determines the
    frequency at which the data is collected throughout the day, defaults to 15min
    :type interval: str (optional)
    :param outputsize: The `outputsize` parameter determines the amount of data to be returned by
    the Alpha Vantage API. It can have two possible values:, defaults to compact
    :type outputsize: str (optional)
    :return: The functions `intraday`, `daily`, `monthly`, and `weekly` are returning a list of
    `TimeSeriesType` objects.
    """

    @strawberry.field
    def intraday(
        self, symbol: str, interval: str = "15min", outputsize: str = "compact"
    ) -> List[TimeSeriesType]:
        """
        The `intraday` function retrieves intraday stock data for a given symbol, interval, and output
        size, and then processes the data.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of the company whose intraday data you want to retrieve. For example, "AAPL" represents
        Apple Inc
        :type symbol: str
        :param interval: The "interval" parameter specifies the time interval between each data point in
        the intraday time series. It can be set to values like "1min", "5min", "15min", "30min", or
        "60min", depending on the desired granularity of the data, defaults to 15min
        :type interval: str (optional)
        :param outputsize: The `outputsize` parameter determines the amount of data to be returned. It
        can have two possible values:, defaults to compact
        :type outputsize: str (optional)
        :return: a list of TimeSeriesType objects.
        """
        data, _ = av.get_intraday(symbol, interval, outputsize)
        return process_timeseries(data)

    @strawberry.field
    def daily(self, symbol: str, outputsize: str = "compact") -> List[TimeSeriesType]:
        """
        The function `daily` retrieves daily stock data for a given symbol and returns it as a list of
        time series.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the daily stock data for that particular company
        :type symbol: str
        :param outputsize: The "outputsize" parameter is used to specify the size of the output. It can
        have two possible values: "compact" or "full", defaults to compact
        :type outputsize: str (optional)
        :return: a list of TimeSeriesType objects.
        """
        data, _ = av.get_daily(symbol, outputsize)
        return process_timeseries(data)

    @strawberry.field
    def monthly(self, symbol: str) -> List[TimeSeriesType]:
        """
        The function retrieves monthly time series data for a given stock symbol and processes it.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the monthly time series data for that particular
        stock
        :type symbol: str
        :return: a list of TimeSeriesType objects.
        """
        data, _ = av.get_monthly(symbol)
        return process_timeseries(data)

    @strawberry.field
    def weekly(self, symbol: str) -> List[TimeSeriesType]:
        """
        The function `weekly` retrieves weekly time series data for a given stock symbol and processes
        it.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the weekly time series data for that particular
        stock
        :type symbol: str
        :return: a list of TimeSeriesType objects.
        """
        data, _ = av.get_weekly(symbol)
        return process_timeseries(data)
