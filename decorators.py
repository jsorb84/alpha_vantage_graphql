from typing import Tuple, Callable, List
from os import getenv
from requests import get
from dotenv import load_dotenv
from strawberry.types.info import Info as _Info, RootValueType
from strawberry_permissions import GraphQLContext
from strawberry_interfaces import TimeSeriesInterface, TimeSeriesData, TimeSeriesAdjustedData, TimeSeriesMetadata, TimeSeriesAdjustedInterface, DigitalCurrencyIntradayInterface, CommoditiesInterface, CommodoitiesDataInterface, DigitalCurrencyInterface, DigitalCurrencyMetadata, DigitalCurrencySeries

type ReturnTuple = Tuple[str | None, str | None, str | None]
type Info = _Info[GraphQLContext, RootValueType]
type TSeries = TimeSeriesAdjustedInterface | TimeSeriesInterface
load_dotenv()

def _extract_time_series_adjusted[**P](fn: Callable[P, dict]) -> Callable[P, TimeSeriesAdjustedInterface]: #! pylint: disable=e0602
    """
    This function creates a wrapper function that extracts the adjusted time series data from the Alpha Vantage API response.

    Args:
        fn (Callable[P, dict]): The function that returns the Alpha Vantage API response.

    Returns:
        Callable[P, TimeSeriesAdjustedInterface]: A function that returns the adjusted time series data.
    """
    def _make_metadata(series: dict[str, str]) -> TimeSeriesMetadata:
        """
        This function creates a TimeSeriesMetadata object from the given series data.

        Args:
            series (dict[str, str]): The series data.

        Returns:
            TimeSeriesMetadata: The TimeSeriesMetadata object.
        """
        n = TimeSeriesMetadata(
            information=series.get("1. Information"),
            symbol=series.get("2. Symbol"),
            last_refreshed=series.get("3. Last Refreshed"),
            output_size=series.get("4. Output Size"),
            time_zone=series.get("5. Time Zone"),
        )
        return n
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> TimeSeriesAdjustedInterface:
        """
        This function is the wrapper function that calls the given function and extracts the adjusted time series data.

        Args:
            args: The arguments to pass to the given function.
            kwargs: The keyword arguments to pass to the given function.

        Returns:
            TimeSeriesAdjustedInterface: The adjusted time series data.
        """
        data: dict = fn(*args, **kwargs)
        vals = list(data.values())
        metadata: dict[str,str] = vals[0]
        assert metadata is not None, "No Meta Data found"
        series: dict[str, dict[str,float]] = vals[1]
        assert series is not None, "No Time Series found"
        series_items = series.items() # date -> {series}
        made_metadata: TimeSeriesMetadata = _make_metadata(metadata)
        l: List[TimeSeriesAdjustedData] = []
        for date, time_series in series_items:
            l.append(
                TimeSeriesAdjustedData(
                    date=date,
                    open=time_series.get("1. open"),
                    high=time_series.get("2. high"),
                    low=time_series.get("3. low"),
                    close=time_series.get("4. close"),
                    adjusted_close=time_series.get("5. adjusted close"),
                    volume=time_series.get("6. volume"),
                    dividend_amount=time_series.get("7. dividend amount"),
                )
            )
        return TimeSeriesAdjustedInterface(
            metadata=made_metadata,
            data=l
        )
    return wrapper

def _extract_time_series[**P](fn: Callable[P, dict]) -> Callable[P, TimeSeriesInterface]: # !! pylint: disable=e0602
    """
    This function creates a wrapper function that extracts the time series data from the Alpha Vantage API response.

    Args:
        fn (Callable[P, dict]): The function that returns the Alpha Vantage API response.

    Returns:
        Callable[P, TimeSeriesInterface]: A function that returns the time series data.
    """
    def _make_metadata(series: dict[str, str]) -> TimeSeriesMetadata:
        """
        This function creates a TimeSeriesMetadata object from the given series data.

        Args:
            series (dict[str, str]): The series data.

        Returns:
            TimeSeriesMetadata: The TimeSeriesMetadata object.
        """
        n = TimeSeriesMetadata(
            information=series.get("1. Information"),
            symbol=series.get("2. Symbol"),
            last_refreshed=series.get("3. Last Refreshed"),
            output_size=series.get("4. Output Size"),
            time_zone=series.get("5. Time Zone"),
        )
        return n
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> TimeSeriesInterface:
        """
        This function is the wrapper function that calls the given function and extracts the time series data.

        Args:
            args: The arguments to pass to the given function.
            kwargs: The keyword arguments to pass to the given function.

        Returns:
            TimeSeriesInterface: The time series data.
        """
        data: dict = fn(*args, **kwargs)
        vals = list(data.values())
        metadata: dict[str,str] = vals[0]
        assert metadata is not None, "No Meta Data found"
        series: dict[str, dict[str,float]] = vals[1]
        assert series is not None, "No Time Series found"
        series_items = series.items() # date -> {series}
        made_metadata: TimeSeriesMetadata = _make_metadata(metadata)
        l: List[TimeSeriesData] = []
        for date, time_series in series_items:
            l.append(
                TimeSeriesData(
                    date=date,
                    open=time_series.get("1. open"),
                    high=time_series.get("2. high"),
                    low=time_series.get("3. low"),
                    close=time_series.get("4. close"),
                    volume=time_series.get("5. volume"),
                )
            )
        return TimeSeriesInterface(
            metadata=made_metadata,
            data=l
        )
    return wrapper

def _extract_crypto_intraday[**P](fn: Callable[P, dict]) -> Callable[P, DigitalCurrencyIntradayInterface]:  #! pylint: disable=e0602
    """
    This function extracts the intraday data for a digital currency from the Alpha Vantage API response.

    Args:
        fn (Callable[P, dict]): The function that returns the Alpha Vantage API response.

    Returns:
        Callable[[P], DigitalCurrencyIntradayInterface]: A function that returns the intraday data for a digital currency.
    """
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> DigitalCurrencyIntradayInterface:
        data: dict = fn(*args, **kwargs)
        metadata: dict = data.get("Meta Data")
        assert metadata is not None, "No Meta Data found"
        interval: str | None = kwargs.get("interval")
        assert interval is not None, "No interval specified"
        ts_key = f"Time Series Crypto ({interval})"
        series: dict | None = data.get(ts_key)
        assert series is not None, "No Time Series found"
        series_items: dict = series.items()
        l: List[TimeSeriesInterface] = []
        for k, v in series_items:
            n = TimeSeriesInterface(
                date=k,
                open=v.get("1. open"),
                high=v.get("2. high"),
                low=v.get("3. low"),
                close=v.get("4. close"),
                volume=v.get("5. volume"),
            )
            l.append(n)
        n = DigitalCurrencyIntradayInterface(
            metadata=DigitalCurrencyMetadata(
                information=metadata.get("1. Information"),
                digital_currency_code=metadata.get("2. Digital Currency Code"),
                digital_currency_name=metadata.get("3. Digital Currency Name"),
                market_code=metadata.get("4. Market Code"),
                market_name=metadata.get("5. Market Name"),
                last_updated=metadata.get("6. Last Refreshed"),
                time_zone=metadata.get("9. Time Zone"),
            ),
            series=l,
        )
        return n
    return wrapper

def _extract_digital_currencies[**P](fn: Callable[P, dict]) -> Callable[P, DigitalCurrencyInterface]:  #! pylint: disable=e0602
    """
    This function extracts the intraday data for a digital currency from the Alpha Vantage API response.

    Args:
        fn (Callable[..., dict]): The function that returns the Alpha Vantage API response.

    Returns:
        Callable[..., DigitalCurrencyInterface]: A function that returns the intraday data for a digital currency.
    """
    def _get_series(d: dict) -> dict | None:
        if d.get("Time Series (Digital Currency Monthly)") is not None:
            return d.get("Time Series (Digital Currency Monthly)")
        if d.get("Time Series (Digital Currency Weekly)") is not None:
            return d.get("Time Series (Digital Currency Weekly)")
        if d.get("Time Series (Digital Currency Daily)") is not None:
            return d.get("Time Series (Digital Currency Daily)")
        return None
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> DigitalCurrencyInterface:
        data: dict = fn(*args, **kwargs)
        metadata: dict = data.get("Meta Data")
        assert metadata is not None, "No Meta Data found"
        series: dict | None = _get_series(data)
        assert series is not None, "No Time Series found"
        series_items: dict = series.items()
        l: List[DigitalCurrencySeries] = []
        market: str | None = kwargs.get("market")
        assert market is not None, "No market specified"
        for k, v in series_items:
            n = DigitalCurrencySeries(
                date=k,
                open_market=v.get(f"1a. open ({market.upper()})"),
                open_usd=v.get("1b. open (USD)"),
                high_market=v.get(f"2a. high ({market.upper()})"),
                high_usd=v.get("2b. high (USD)"),
                low_market=v.get(f"3a. low ({market.upper()})"),
                low_usd=v.get("3b. low (USD)"),
                close_market=v.get(f"4a. close ({market.upper()})"),
                close_usd=v.get("4b. close (USD)"),
                volume=v.get("5. volume"),
                market_cap_usd=v.get("6. market cap (USD)"),
            )
            l.append(n)
        n = DigitalCurrencyInterface(
            metadata=DigitalCurrencyMetadata(
                information=metadata.get("1. Information"),
                digital_currency_code=metadata.get("2. Digital Currency Code"),
                digital_currency_name=metadata.get("3. Digital Currency Name"),
                market_code=metadata.get("4. Market Code"),
                market_name=metadata.get("5. Market Name"),
                last_updated=metadata.get("6. Last Refreshed"),
                time_zone=metadata.get("7. Time Zone"),
            ),
            series=l,
        )
        return n
    return wrapper
def _extract_commodoties[**P](fn: Callable[P, dict]) -> Callable[P, CommoditiesInterface]:  #! pylint: disable=e0602
    """
    This function extracts the intraday data for a digital currency from the Alpha Vantage API response.

    Args:
        fn (Callable[[P], dict]): The function that returns the Alpha Vantage API response.

    Returns:
        Callable[[P], CommoditiesInterface]: A function that returns the intraday data for a digital currency.
    """
    def _process_data(l: List[dict]):
        return [
            CommodoitiesDataInterface(date=v.get("date"), value=v.get("value"))
            for v in l
        ]
    
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> CommoditiesInterface:
        data: dict = fn(*args, **kwargs)
        n = CommoditiesInterface(
            name=data.get("name"),
            interval=data.get("interval"),
            unit=data.get("unit"),
            data=_process_data(data.get("data")),
        )
        return n
    return wrapper
            

def _make_api_call[**P](fn: Callable[P, ReturnTuple]):  # ! pylint: disable=e0602
    """
    This function wraps the API call to Alpha Vantage and handles the response.

    Args:
        fn (Callable[..., ReturnTuple]): The function that makes the API call.

    Returns:
        Callable[..., ReturnTuple]: The wrapped function.
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs):
        """
        This function is the inner wrapper that makes the API call and handles the response.

        Args:
            args: The arguments to pass to the function that makes the API call.
            kwargs: The keyword arguments to pass to the function that makes the API call.

        Returns:
            The return value of the function that makes the API call.
        """
        uri = getenv("AV_URL")
        info: Info | None = kwargs.get("info") if kwargs.get("info") else None
        api_key = (
            info.context.request.headers.get("ALPHAVANTAGE_API_KEY") if info else None
        )
        assert info, "API Key and URI are required"
        _args = kwargs.items()
        uri += f"?apikey={api_key}"
        # ? https://alphavantage.co/query?apikey={apikey}function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo
        for k, v in _args:
            if k == "apikey" or k == "validation_model" or k == "info":
                continue
            uri += f"&{k}={v}"
        response = get(uri, timeout=10)
        as_json: dict = response.json()
        assert as_json.get("Error Message") is None, f"Error: {as_json.get("Error Message")}"
        a, b, c = fn(*args, **kwargs)
        current = as_json

        if a is not None:
            assert as_json.get(a), f"Expected {a} in response"
            current = as_json[a]
        if b is not None:
            assert current[b] is not None, f"Expected {b} in {a} response"
            current = current[b]
        if c is not None:
            assert current[c] is not None, f"Expected {c} in {b} response"
            current = current[c]
        if kwargs.get("validation_model") is not None:
            val_model: type(kwargs.get("validation_model")) = kwargs.get(
                "validation_model"
            )
            current: type(val_model) = val_model.model_validate(current)
        return current

    return wrapper
