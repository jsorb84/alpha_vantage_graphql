from ..app import Query
import strawberry
from typing import Literal

schema = strawberry.Schema(query=Query)

type Times = Literal["intraday", "daily", "weekly", "monthly"]


def test_intraday():
    q = """
    {
        getTimeSeries {
            intraday(symbol:"AAPL") {
                open
                close
            }
        }
    }
    """
    result = schema.execute_sync(q)
    assert not result.errors
    assert result.data.get("getTimeSeries") is not None
    assert result.data.get("getTimeSeries").get("intraday") is not None
    arr: list = result.data.get("getTimeSeries").get("intraday")
    assert len(arr) > 0


def test_daily():
    q = """
    {
        getTimeSeries {
            daily(symbol:"AAPL") {
                open
                close
            }
        }
    }
    """
    result = schema.execute_sync(q)
    assert not result.errors
    assert result.data.get("getTimeSeries") is not None
    assert result.data.get("getTimeSeries").get("daily") is not None
    arr: list = result.data.get("getTimeSeries").get("daily")
    assert len(arr) > 0


def test_weekly():
    q = """
    {
        getTimeSeries {
            weekly(symbol:"AAPL") {
                open
                close
            }
        }
    }
    """
    result = schema.execute_sync(q)
    assert not result.errors
    assert result.data.get("getTimeSeries") is not None
    assert result.data.get("getTimeSeries").get("weekly") is not None
    arr: list = result.data.get("getTimeSeries").get("weekly")
    assert len(arr) > 0


def test_monthly():
    q = """
    {
        getTimeSeries {
            monthly(symbol:"AAPL") {
                open
                close
            }
        }
    }
    """
    result = schema.execute_sync(q)
    assert not result.errors
    assert result.data.get("getTimeSeries") is not None
    assert result.data.get("getTimeSeries").get("monthly") is not None
    arr: list = result.data.get("getTimeSeries").get("monthly")
    assert len(arr) > 0
