from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from strawberry_types import (
    FundementalDataType,
    TECHNICAL_AVERAGES,
    TIME_SERIES,
    TIME_SERIES_ADJUSTED,
    CRYPTO_SERIES,
)

app = FastAPI()


@strawberry.type
class Query:
    """
    The Query class defines the root query fields for the GraphQL schema. It provides methods for
    - `getFundementalData`
    - `getCrypto`
    - `getTechnicalAverages`
    - `getTimeSeries`
    - `getTimeSeriesAdjusted`
    """

    @strawberry.field
    def get_fundemental_data(self) -> FundementalDataType:
        """
        Returns the fundamental data for the stocks.

        Returns:
            FundementalDataType: The fundamental data for the stocks.
        """
        return FundementalDataType()

    @strawberry.field
    def get_crypto(self) -> CRYPTO_SERIES:
        """
        Returns the crypto data for the stocks.

        Returns:
            CRYPTO_SERIES: The crypto data for the stocks.
        """
        return CRYPTO_SERIES()

    @strawberry.field
    def get_technical_averages(self) -> TECHNICAL_AVERAGES:
        """
        Returns the technical averages for the stocks.

        Returns:
            TECHNICAL_AVERAGES: The technical averages for the stocks.
        """
        return TECHNICAL_AVERAGES()

    @strawberry.field
    def get_time_series(self) -> TIME_SERIES:
        """
        Returns the time series data for the stocks.

        Returns:
            TIME_SERIES: The time series data for the stocks.
        """
        return TIME_SERIES()

    @strawberry.field
    def get_time_series_adjusted(self) -> TIME_SERIES_ADJUSTED:
        """
        Returns the adjusted time series data for the stocks.

        Returns:
            TIME_SERIES_ADJUSTED: The adjusted time series data for the stocks.
        """
        return TIME_SERIES_ADJUSTED()


schema = strawberry.Schema(query=Query)
gql_app = GraphQLRouter(schema, path="/graphql", debug=True)

app.include_router(gql_app)
