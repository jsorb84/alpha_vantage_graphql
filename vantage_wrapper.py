from os import getenv
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.cryptocurrencies import CryptoCurrencies

load_dotenv()


class Vantage:
    """Wrapper for all Alpha Vantage APIs"""

    key = getenv("AV_KEY")

    def __init__(self) -> None:
        self._time_series = TimeSeries(key=self.key)
        self._tech_indicators = TechIndicators(key=self.key)
        self._fundamental_data = FundamentalData(key=self.key)
        self._crypto_currencies = CryptoCurrencies(key=self.key)

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
