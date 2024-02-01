from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import Literal
from alpha_vantage.timeseries import TimeSeries
from time_series import TIME_SERIES, TIME_SERIES_ADJUSTED
from info_series import INCOME_STATEMENT, CASH_FLOW, BALANCE_SHEET

app = FastAPI()
key = getenv("AV_KEY")
av = TimeSeries(key=key)

type SeriesType = Literal["intraday", "daily", "weekly", "monthly"]


@strawberry.type
class Query:
    """The `Query` class defines several methods that return instances of different classes related to
    financial statements."""

    @strawberry.field
    def time_series(self) -> TIME_SERIES:
        """
        The function `time_series` returns an instance of the `TIME_SERIES` class.
        :return: an instance of the TIME_SERIES class.
        """
        return TIME_SERIES()

    @strawberry.field
    def time_series_adjusted(self) -> TIME_SERIES_ADJUSTED:
        """
        The function `time_series_adjusted` returns an instance of the `TIME_SERIES_ADJUSTED` class.
        :return: an instance of the TIME_SERIES_ADJUSTED class.
        """
        return TIME_SERIES_ADJUSTED()

    @strawberry.field
    def income_statement(self) -> INCOME_STATEMENT:
        """
        The function "income_statement" returns an instance of the INCOME_STATEMENT class.
        :return: an instance of the INCOME_STATEMENT class.
        """
        return INCOME_STATEMENT()

    @strawberry.field
    def cash_flow(self) -> CASH_FLOW:
        """
        The function cash_flow returns an instance of the CASH_FLOW class.
        :return: an instance of the CASH_FLOW class.
        """
        return CASH_FLOW()

    @strawberry.field
    def balance_sheet(self) -> BALANCE_SHEET:
        """
        The function returns a balance sheet.
        :return: an instance of the BALANCE_SHEET class.
        """
        return BALANCE_SHEET()


schema = strawberry.Schema(query=Query)
gql_app = GraphQLRouter(schema, path="/graphql", debug=True)

app.include_router(gql_app)
