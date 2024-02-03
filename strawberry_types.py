from typing import List, Literal, Unpack
import strawberry
from strawberry.types.info import Info as _Info, RootValueType
from vantage_wrapper import Vantage
from strawberry_interfaces import (
    TimeSeriesAdjustedInterface,
    TimeSeriesInterface,
    API_Parameters,
)
from strawberry_permissions import GraphQLContext
from strawberry_permissions import IsAuthenticated
from pydantic_schemas import (
    CurrencyExchangeRateSchema,
    TechIndicatorMetadataSchema,
    CryptoMetadataSchema,
    OverviewSchema,
    IncomeStatementSchema,
    CashFlowSchema,
    BalanceSheetSchema,
    GlobalQuoteSchema,
)
from decorators import _make_api_call
from pandas import DataFrame

type Intervals = Literal["1min", "5min", "15min", "30min", "60min"]
type Info = _Info[GraphQLContext, RootValueType]


@strawberry.experimental.pydantic.type(CurrencyExchangeRateSchema, all_fields=True)
class CurrencyExchangeRateType:
    """
    The CurrencyExchangeRateType class defines the type of the response returned by the `exchange_rate` method.
    """


@strawberry.type(name="TimeSeriesAdjusted")
class TIME_SERIES_ADJUSTED:
    """The code block you provided defines a GraphQL type called `TIME_SERIES_ADJUSTED` using the
    `@strawberry.type` decorator. This type has three fields: `daily`, `monthly`, and `weekly`. Each
    field is decorated with `@strawberry.field` and has its own resolver function. The resolver functions
    """

    def process_timeseries_adjusted(self, data: Literal) -> TimeSeriesAdjustedInterface:
        """
        The function `process_timeseries_adjusted` takes in a dictionary of time series data and returns a
        list of `TimeSeriesAdjustedInterface` objects with the data converted to the appropriate data types.

        :param data: The `data` parameter is a dictionary containing time series data. Each key in the
        dictionary represents a day, and the corresponding value is another dictionary containing the
        following keys:
        :type data: Literal
        :return: The function `process_timeseries_adjusted` returns a list of `TimeSeriesAdjustedInterface`
        objects.
        """
        x = [
            TimeSeriesAdjustedInterface(
                date=day,
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

    @strawberry.field
    def daily(
        self,
        info: Info,
        symbol: str,
        outputsize: str = "compact",
    ) -> List[TimeSeriesAdjustedInterface]:
        """
        The function `daily` retrieves daily adjusted stock data for a given symbol and returns it as a
        processed time series.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to identify a specific stock in the financial market
        :type symbol: str
        :param outputsize: The `outputsize` parameter is used to specify the size of the output. It can
        have two possible values:, defaults to compact
        :type outputsize: str (optional)
        :return: a list of TimeSeriesAdjustedInterface objects.
        """

        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.time_series.get_daily_adjusted(symbol, outputsize)
        return self.process_timeseries_adjusted(data)

    @strawberry.field
    def monthly(self, info: Info, symbol: str) -> List[TimeSeriesAdjustedInterface]:
        """
        The function `monthly` retrieves monthly adjusted time series data for a given stock symbol and
        processes it.

        :param symbol: The `symbol` parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the monthly adjusted time series data for that
        particular stock
        :type symbol: str
        :return: a list of TimeSeriesAdjustedInterface objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.time_series.get_monthly_adjusted(symbol)
        return self.process_timeseries_adjusted(data)

    @strawberry.field
    def weekly(self, info: Info, symbol: str) -> List[TimeSeriesAdjustedInterface]:
        """
        The function `weekly` retrieves weekly adjusted time series data for a given stock symbol and
        processes it.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the weekly adjusted time series data for that
        particular stock
        :type symbol: str
        :return: a list of TimeSeriesAdjustedInterface objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.time_series.get_weekly_adjusted(symbol)
        return self.process_timeseries_adjusted(data)


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
    `TimeSeriesInterface` objects.
    """

    def process_timeseries(self, data: Literal) -> TimeSeriesInterface:
        """
        The function `process_timeseries` takes in a dictionary of time series data and converts it into a
        list of `TimeSeriesInterface` objects.

        :param data: The `data` parameter is expected to be a dictionary containing time series data. Each
        key in the dictionary represents a day, and the corresponding value is another dictionary containing
        the open, high, low, close, and volume values for that day
        :type data: Literal
        :return: a list of TimeSeriesInterface objects.
        """
        x = [
            TimeSeriesInterface(
                date=day,
                open=float(data[day]["1. open"]),
                high=float(data[day]["2. high"]),
                low=float(data[day]["3. low"]),
                close=float(data[day]["4. close"]),
                volume=float(data[day]["5. volume"]),
            )
            for day in data
        ]
        return x

    @strawberry.field
    def intraday(
        self,
        info: Info,
        symbol: str,
        interval: str = "15min",
        outputsize: str = "compact",
    ) -> List[TimeSeriesInterface]:
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
        :return: a list of TimeSeriesInterface objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.time_series.get_intraday(symbol, interval, outputsize)
        return self.process_timeseries(data)

    @strawberry.field
    def daily(
        self, info: Info, symbol: str, outputsize: str = "compact"
    ) -> List[TimeSeriesInterface]:
        """
        The function `daily` retrieves daily stock data for a given symbol and returns it as a list of
        time series.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the daily stock data for that particular company
        :type symbol: str
        :param outputsize: The "outputsize" parameter is used to specify the size of the output. It can
        have two possible values: "compact" or "full", defaults to compact
        :type outputsize: str (optional)
        :return: a list of TimeSeriesInterface objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.time_series.get_daily(symbol, outputsize)
        return self.process_timeseries(data)

    @strawberry.field
    def monthly(self, info: Info, symbol: str) -> List[TimeSeriesInterface]:
        """
        The function retrieves monthly time series data for a given stock symbol and processes it.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the monthly time series data for that particular
        stock
        :type symbol: str
        :return: a list of TimeSeriesInterface objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.time_series.get_monthly(symbol)
        return self.process_timeseries(data)

    @strawberry.field
    def weekly(self, info: Info, symbol: str) -> List[TimeSeriesInterface]:
        """
        The function `weekly` retrieves weekly time series data for a given stock symbol and processes
        it.

        :param symbol: The symbol parameter is a string that represents the stock symbol or ticker
        symbol of a company. It is used to retrieve the weekly time series data for that particular
        stock
        :type symbol: str
        :return: a list of TimeSeriesInterface objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.time_series.get_weekly(symbol)
        return self.process_timeseries(data)


@strawberry.experimental.pydantic.type(TechIndicatorMetadataSchema, all_fields=True)
class TechIndicatorMetadataType:
    """The TechIndicatorMetadata class defines the metadata of a technical indicator."""

    pass


@strawberry.type
class TechIndicatorAnalysis:
    """
    ### AlphaVantage Equivlent Structure
    ```json
    {
        "2021-09-10": {
            "EMA": "150.0000"
        }
    }
    ```
    ### `TechIndicatorAnalysis` Structure
    ```json
    {
        "date": "2021-09-10",
        "average": "150.0000"
    }
    ```
    """

    date: str = strawberry.field(description="The date of the data.", default="")
    average: str = strawberry.field(description="The average of the data.")


@strawberry.type
class TechIndicator:
    """The TechIndicator class defines several methods that return technical indicators."""

    metadata: TechIndicatorMetadataType = strawberry.field(name="MetaData")
    analysis: List[TechIndicatorAnalysis] = strawberry.field(name="Analysis")


type DataTuple = tuple[dict[str, dict[str, str]], dict[str, str]]


@strawberry.type
class TECHNICAL_AVERAGES:
    """GraphQL Schema for Technical Averages."""

    def process(self, data_tuple: DataTuple, average_key: str = "EMA") -> TechIndicator:
        """Process the data and metadata into a TechIndicator object.

        Args:
            data_tuple (DataTuple): `data, metadata` tuple.
            average_key (str, optional): The key of the technical average to use. Defaults to "EMA".

        Returns:
            TechIndicator: GraphQL Schema object.
        """
        data, metadata = data_tuple
        items = data.items()
        as_model = TechIndicatorMetadataSchema.model_validate(metadata)
        # !! This is a hack to get around the fact that pydantic does not support nested fields. !!
        # !! pylint: disable=no-member
        as_gql = TechIndicatorMetadataType.from_pydantic(as_model)
        analysis_list: List[TechIndicatorAnalysis] = [
            TechIndicatorAnalysis(date=date, average=values[average_key])
            for date, values in items
        ]
        return TechIndicator(metadata=as_gql, analysis=analysis_list)

    @strawberry.field
    def sma(
        self,
        info: Info,
        symbol: str,
        interval: str = "weekly",
        time_period: int = 60,
        series_type: str = "open",
    ) -> TechIndicator:
        """
        The function `sma` returns the Simple Moving Average (SMA) of a stock.
        :param symbol: the symbol of the stock.
        :param interval: the interval of the data.
        :return: the SMA of the stock.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, metadata = vantage.tech_indicators.get_sma(
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type,
        )
        return self.process((data, metadata), "SMA")

    @strawberry.field
    def ema(
        self,
        info: Info,
        symbol: str,
        interval: str = "weekly",
        time_period: int = 60,
        series_type: str = "open",
    ) -> TechIndicator:
        """
        The function `ema` returns the Exponential Moving Average (EMA) of a stock.
        :param symbol: the symbol of the stock.
        :param interval: the interval of the data.
        :return: the EMA of the stock.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, metadata = vantage.tech_indicators.get_ema(
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type,
        )
        return self.process((data, metadata), "EMA")

    @strawberry.field
    def wma(
        self,
        info: Info,
        symbol: str,
        interval: str = "weekly",
        time_period: int = 60,
        series_type: str = "open",
    ) -> TechIndicator:
        """
        The function `wma` returns the Weighted Moving Average (WMA) of a stock.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, metadata = vantage.tech_indicators.get_wma(
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type,
        )
        return self.process((data, metadata), "WMA")

    @strawberry.field
    def dema(
        self,
        info: Info,
        symbol: str,
        interval: str = "weekly",
        time_period: int = 60,
        series_type: str = "open",
    ) -> TechIndicator:
        """
        The function `dema` returns the Double Exponential Moving Average (DEMA) of a stock.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, metadata = vantage.tech_indicators.get_dema(
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type,
        )
        return self.process((data, metadata), "DEMA")

    @strawberry.field
    def tema(
        self,
        info: Info,
        symbol: str,
        interval: str = "weekly",
        time_period: int = 60,
        series_type: str = "open",
    ) -> TechIndicator:
        """
        The function `tema` returns the Triple Exponential Moving Average (TEMA) of a stock.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, metadata = vantage.tech_indicators.get_tema(
            symbol=symbol,
            interval=interval,
            time_period=time_period,
            series_type=series_type,
        )
        return self.process((data, metadata), "TEMA")


@strawberry.experimental.pydantic.type(CryptoMetadataSchema, all_fields=True)
class CryptoMetadataType:
    """
    The CryptoMetadataType class defines the type of the response returned by the `metadata` method.
    """

    pass


@strawberry.type
class CryptoIntraday:
    """
    The CryptoIntraday class defines the type of the response returned by the `intraday` method.
    """

    metadata: CryptoMetadataType
    series: List[TimeSeriesInterface]


@strawberry.type
class CRYPTO_SERIES:
    @strawberry.field
    def exchange_rate(
        self, info: Info, from_currency: str, to_currency: str
    ) -> CurrencyExchangeRateType:
        """
        The function `exchange_rate` returns the exchange rate between two currencies.
        :param from_currency: the currency to convert from.
        :param to_currency: the currency to convert to.
        :return: the exchange rate between the two currencies.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.crypto_currencies.get_digital_currency_exchange_rate(
            from_currency=from_currency, to_currency=to_currency
        )
        data: dict[str, str]
        as_model = CurrencyExchangeRateSchema.model_validate(data)
        # !! This is a bug in the schema. !!
        # !! pylint: disable=no-member
        as_gql = CurrencyExchangeRateType.from_pydantic(as_model)
        return as_gql

    @_make_api_call
    def _get_intraday(
        self, *args, **kwargs: Unpack[API_Parameters[TimeSeriesInterface]]
    ):
        """
        The function `_get_intraday` is a decorator that makes an API call to the Alpha Vantage API
        """
        return (None, None, None)

    @strawberry.field
    def intraday(
        self,
        info: Info,
        symbol: str,
        market: str = "USD",
        interval: str = "5min",
    ) -> CryptoIntraday:
        """
        Returns the intraday data for a given cryptocurrency.

        :param info: The info parameter is a context object that contains information about the
        request, including the user's authentication credentials.
        :type info: Info
        :param symbol: The symbol parameter is a string that represents the cryptocurrency symbol
        for which you want to retrieve intraday data.
        :type symbol: str
        :param market: The "market" parameter is a string that represents the fiat currency in which
        you want the data to be returned. It can be set to any of the supported fiat currencies,
        including "USD", "EUR", "GBP", and "JPY". The default value is "USD".
        :type market: str
        :param interval: The "interval" parameter specifies the time interval between each data point
        in the intraday time series. It can be set to values like "1min", "5min", "15min", "30min",
        or "60min", depending on the desired granularity of the data. The default value is "5min".
        :type interval: str
        :return: The function returns a CryptoIntraday object, which contains the metadata and the
        time series data.
        """
        data = self._get_intraday(
            info=info,
            symbol=symbol,
            function="CRYPTO_INTRADAY",
            interval=interval,
            market=market,
        )
        md_schema = CryptoMetadataSchema.model_validate(
            data["Meta Data"]  # !! pylint: disable=E1126
        )
        ts_list: dict[str, dict[str, str]] = data[f"Time Series Crypto ({interval})"]
        ts_items = ts_list.items()
        l: List[TimeSeriesInterface] = [
            TimeSeriesInterface(
                date=k,
                open=float(v["1. open"]),
                close=float(v["4. close"]),
                high=float(v["2. high"]),
                low=float(v["3. low"]),
                volume=float(v["5. volume"]),
            )
            for k, v in ts_items
        ]
        final = CryptoIntraday(metadata=md_schema, series=l)

        return final


@strawberry.experimental.pydantic.type(IncomeStatementSchema, all_fields=True)
class IncomeStatementType:
    """The class "IncomeStatementType" is defined."""

    pass


@strawberry.experimental.pydantic.type(CashFlowSchema, all_fields=True)
class CashFlowType:
    """
    The class "CashFlowType" is defined.
    """

    pass


@strawberry.experimental.pydantic.type(BalanceSheetSchema, all_fields=True)
class BalanceSheetType:
    """The class BalanceSheetType is defined."""

    pass


@strawberry.experimental.pydantic.type(OverviewSchema, all_fields=True)
class OverviewType:
    """
    The class OverviewType is defined.
    """

    pass


@strawberry.experimental.pydantic.type(GlobalQuoteSchema, all_fields=True)
class GlobalQuoteType:
    """The class GlobalQuoteType is defined."""

    pass


@strawberry.type
class FundementalDataType:
    def manipulate_cf(self, data: DataFrame) -> List[CashFlowType]:
        """
        The function `manipulate_cf` takes a DataFrame as input, converts it to a dictionary, validates the
        data using a CashFlowSchema model, and then converts the validated data to a list of CashFlowType
        objects.

        :param data: The `data` parameter is a DataFrame object
        :type data: DataFrame
        :return: The function `manipulate_cf` returns a list of `CashFlowType` objects.
        """

        as_json = data.to_dict(orient="index")
        items = as_json.values()
        l: List[CashFlowType] = []
        for i in items:
            pymodel = CashFlowSchema.model_validate(i)
            # !! pylint: disable=no-member
            gqltype: CashFlowType = CashFlowType.from_pydantic(pymodel)
            l.append(gqltype)
        return l

    def manipulate_is(self, data: DataFrame) -> List[IncomeStatementType]:
        """
        The function `manipulate_is` converts a DataFrame into a list of IncomeStatementType objects by
        validating the data and converting it into the appropriate format.

        :param data: The `data` parameter is a DataFrame object
        :type data: DataFrame
        :return: The function `manipulate_is` returns a list of `IncomeStatementType` objects.
        """
        as_json = data.to_dict(orient="index")
        items = as_json.values()
        l: List[IncomeStatementType] = []
        for i in items:
            pymodel = IncomeStatementSchema.model_validate(i)
            # !! pylint: disable=no-member
            gqltype: IncomeStatementType = IncomeStatementType.from_pydantic(pymodel)
            l.append(gqltype)
        return l

    def manipulate_bs(self, data: DataFrame) -> List[BalanceSheetType]:
        """
        The function `manipulate_bs` takes a DataFrame as input, converts it to a dictionary, validates the
        data using a BalanceSheetSchema model, and then converts the validated data to a list of BalanceSheetType
        objects.

        :param data: The `data` parameter is a DataFrame object
        :type data: DataFrame
        :return: The function `manipulate_bs` returns a list of `BalanceSheetType` objects.
        """

        as_json = data.to_dict(orient="index")
        items = as_json.values()
        l: List[BalanceSheetType] = []
        for i in items:
            pymodel = BalanceSheetSchema.model_validate(i)
            # !! pylint: disable=no-member
            gqltype: BalanceSheetType = BalanceSheetType.from_pydantic(pymodel)
            l.append(gqltype)
        return l

    @strawberry.field
    def get_balance_sheet_annual(
        self, info: Info, symbol: str
    ) -> List[BalanceSheetType]:
        """
        The function `get_balance_sheet_annual` retrieves annual balance sheet data for a given stock symbol and
        returns a manipulated version of the data.

        :param symbol: The symbol parameter is a string that represents the stock symbol of a company.
        It is used to retrieve the balance sheet data for that specific company
        :type symbol: str
        :return: a list of BalanceSheetType objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.fundamental_data.get_balance_sheet_annual(symbol)
        data: DataFrame
        return self.manipulate_bs(data)

    @strawberry.field
    def get_balance_sheet_quarterly(
        self, info: Info, symbol: str
    ) -> List[BalanceSheetType]:
        """
        The function `get_balance_sheet_quarterly` retrieves quarterly balance sheet data for a given stock symbol
        and returns a manipulated version of the data.

        :param symbol: The "symbol" parameter is a string that represents the stock symbol of a company
        :type symbol: str
        :return: a list of BalanceSheetType objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.fundamental_data.get_balance_sheet_quarterly(symbol)
        data: DataFrame
        return self.manipulate_bs(data)

    @strawberry.field
    def get_company_overview(self, info: Info, symbol: str) -> OverviewType:
        """
        The function `get_company_overview` retrieves company overview data for a given symbol and
        returns it in a GraphQL-compatible format.

        :param symbol: The `symbol` parameter is a string that represents the stock symbol of a company
        :type symbol: str
        :return: an object of type `OverviewType`.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.fundamental_data.get_company_overview(symbol)
        data: dict[str, str]

        pymodel = OverviewSchema.model_validate(data)
        # !! This is a bug in the schema.!!!!
        # !! pylint: disable=no-member
        gqltype: OverviewType = OverviewType.from_pydantic(pymodel)

        return gqltype

    @strawberry.field
    def get_cash_flow_annual(self, info: Info, symbol: str) -> List[CashFlowType]:
        """
        The function `get_cash_flow_annual` retrieves annual cash flow data for a given stock symbol and
        returns a manipulated version of the data.

        :param symbol: The symbol parameter is a string that represents the stock symbol of a company.
        It is used to retrieve the cash flow data for that specific company
        :type symbol: str
        :return: a list of CashFlowType objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.fundamental_data.get_cash_flow_annual(symbol)
        data: DataFrame
        return self.manipulate_cf(data)

    @strawberry.field
    def get_cash_flow_quarterly(self, info: Info, symbol: str) -> List[CashFlowType]:
        """
        The function `get_cash_flow_quarterly` retrieves quarterly cash flow data for a given stock symbol
        and returns a manipulated version of the data.

        :param symbol: The "symbol" parameter is a string that represents the stock symbol of a company
        :type symbol: str
        :return: a list of CashFlowType objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.fundamental_data.get_cash_flow_quarterly(symbol)
        data: DataFrame
        return self.manipulate_cf(data)

    @strawberry.field
    def get_income_statement_annual(
        self, info: Info, symbol: str
    ) -> List[IncomeStatementType]:
        """
        The function `get_income_statement_annual` retrieves annual income statement data for a given
        stock symbol and returns a manipulated version of the data.

        :param symbol: The symbol parameter is a string that represents the stock symbol of a company.
        It is used to retrieve the income statement data for that specific company
        :type symbol: str
        :return: a list of IncomeStatementType objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.fundamental_data.get_income_statement_annual(symbol)
        data: DataFrame
        return self.manipulate_is(data)

    @strawberry.field
    def get_income_statement_quarterly(
        self, info: Info, symbol: str
    ) -> List[IncomeStatementType]:
        """
        The function `get_income_statement_quarterly` retrieves quarterly income statement data for a
        given stock symbol and returns a manipulated version of the data.

        :param symbol: The "symbol" parameter is a string that represents the stock symbol of a company
        :type symbol: str
        :return: a list of IncomeStatementType objects.
        """
        vantage = Vantage(info)
        # !! pylint: disable=W0632
        data, _ = vantage.fundamental_data.get_income_statement_quarterly(symbol)
        data: DataFrame
        return self.manipulate_is(data)

    @_make_api_call
    def _global_quote(self, *args, **kwargs: Unpack[API_Parameters[GlobalQuoteSchema]]):
        """
        The function `_global_quote` is a decorator that makes an API call to the Alpha Vantage API
        """
        return ("Global Quote", None, None)

    @strawberry.field
    def global_quote(self, info: Info, symbol: str) -> GlobalQuoteType:
        """Returns the global quote for a given stock symbol."""

        as_model = self._global_quote(
            info=info,
            symbol=symbol,
            function="GLOBAL_QUOTE",
            datatype="json",
            validation_model=GlobalQuoteSchema,
        )

        # !! pylint: disable=no-member
        as_type: GlobalQuoteType = GlobalQuoteType.from_pydantic(as_model)
        return as_type


# @strawberry.type
# class AlphaVantageAPIKey:
#     """
#     The class `AlphaVantageAPIKey` represents an AlphaVantage API key.
#     """

#     api_key: str = strawberry.field(description="The API key.", name="apikey")


@strawberry.type
class QueryType:
    """
    The Query class defines the root query fields for the GraphQL schema. It provides methods for
    - `getFundementalData`
    - `getCrypto`
    - `getTechnicalAverages`
    - `getTimeSeries`
    - `getTimeSeriesAdjusted`
    """

    @strawberry.field(permission_classes=[IsAuthenticated])
    def get_fundemental_data(self) -> FundementalDataType:
        """
        Returns the fundamental data for the stocks.

        Returns:
            FundementalDataType: The fundamental data for the stocks.
        """
        return FundementalDataType()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def get_crypto(self) -> CRYPTO_SERIES:
        """
        Returns the crypto data for the stocks.

        Returns:
            CRYPTO_SERIES: The crypto data for the stocks.
        """
        return CRYPTO_SERIES()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def get_technical_averages(self) -> TECHNICAL_AVERAGES:
        """
        Returns the technical averages for the stocks.

        Returns:
            TECHNICAL_AVERAGES: The technical averages for the stocks.
        """

        return TECHNICAL_AVERAGES()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def get_time_series(self) -> TIME_SERIES:
        """
        Returns the time series data for the stocks.

        Returns:
            TIME_SERIES: The time series data for the stocks.
        """
        return TIME_SERIES()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def get_time_series_adjusted(self) -> TIME_SERIES_ADJUSTED:
        """
        Returns the adjusted time series data for the stocks.

        Returns:
            TIME_SERIES_ADJUSTED: The adjusted time series data for the stocks.
        """
        return TIME_SERIES_ADJUSTED()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def test(self) -> bool:
        """
        A testing endpoint.
        """
        return True
