from os import getenv
from typing import (
    Tuple,
)

from dotenv import load_dotenv
from strawberry.types.info import Info as _Info, RootValueType
from strawberry_permissions import GraphQLContext
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.alphavantage import AlphaVantage


load_dotenv()

type ReturnTuple = Tuple[str | None, str | None, str | None]
type Info = _Info[GraphQLContext, RootValueType]


class Vantage:
    """Wrapper for all Alpha Vantage APIs"""

    av_url = getenv("AV_URL")
    info: Info | None = None

    def __init__(self, strawberry_info: Info) -> None:
        self.info = strawberry_info
        context = strawberry_info.context
        key = context.request.headers.get("ALPHAVANTAGE_API_KEY")
        assert (
            key is not None
        ), "Alpha Vantage API key is not set. Set `ALPHAVANTAGE_API_KEY` in the request headers."
        self.key = key
        self._time_series = TimeSeries(key=self.key)
        self._tech_indicators = TechIndicators(key=self.key)
        self._fundamental_data = FundamentalData(key=self.key)
        self._crypto_currencies = CryptoCurrencies(key=self.key)
        self.alpha_vantage = AlphaVantage(key=self.key)

    @property
    def time_series(self) -> TimeSeries:
        """Alpha Vantage Time Series API.

        Returns:
            TimeSeries: Alpha Vantage Time Series API object.
        """
        return self._time_series

    @property
    def tech_indicators(self) -> TechIndicators:
        """Alpha Vantage Technical Indicators API.

        Returns:
            TechIndicators: Alpha Vantage Technical Indicators API object.
        """
        return self._tech_indicators

    @property
    def fundamental_data(self) -> FundamentalData:
        """Alpha Vantage Fundamental Data API.

        Returns:
            FundamentalData: Alpha Vantage Fundamental Data API object.
        """
        return self._fundamental_data

    @property
    def crypto_currencies(self) -> CryptoCurrencies:
        """Alpha Vantage Crypto Currencies API.

        Returns:
            CryptoCurrencies: Alpha Vantage Crypto Currencies API object.
        """
        return self._crypto_currencies
