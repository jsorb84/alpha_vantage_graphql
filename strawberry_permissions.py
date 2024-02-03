import os
import logging
from typing import Any
from strawberry.permission import BasePermission
from strawberry.fastapi import BaseContext
from strawberry.types.info import Info, RootValueType
from functools import cached_property
from requests import get

header_field = "ALPHAVANTAGE_API_KEY"


def ping_auth(key: str) -> bool:
    """
    This function is used to test the API key provided by the user.

    Args:
        key (str): The API key provided by the user.

    Returns:
        bool: Returns True if the API key is valid, False otherwise.
    """
    uri = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={key}"
    response: dict = get(uri, timeout=10).json()
    assert response["Error Message"] is None, response["Error Message"]
    assert response["Information"] is not None, response["Information"]
    if response["Global Quote"]:
        logging.info("Successfully authenticated")
        return True
    return False


class GraphQLContext(BaseContext):
    """GraphQL context.

    Args:
        BaseContext (BaseContext): FastAPI BaseContext.
    """

    @cached_property
    def api_key(self) -> str | None:
        """Get the API key from the request headers.

        Returns:
            The API key or None if it is not present in the headers.
        """
        if self.request.headers.get("ALPHAVANTAGE_API_KEY") is None:
            return None
        key = self.request.headers.get("ALPHAVANTAGE_API_KEY")
        tested: bool | None = os.environ.get("ALPHAVANTAGE_TESTED")
        if tested is False or None:
            if ping_auth(key):
                os.environ.update({"ALPHAVANTAGE_TESTED": "True"})
            else:
                logging.error(f"Invalid API key: {key}")
                return None
        os.environ.update({"ALPHAVANTAGE_API_KEY": key})
        return key


class IsAuthenticated(BasePermission):
    """IsAuthenticated permission class."""

    message: str = "You must be authenticated to access this resource."

    def has_permission(
        self, source: Any, info: Info[GraphQLContext, RootValueType], **kwargs: Any
    ) -> bool:
        """
        Check if the user is authenticated.

        Args:
            source: The source object being accessed.
            info: The request information.
            **kwargs: Additional arguments.

        Returns:
            True if the user is authenticated, False otherwise.
        """
        context = info.context
        key: str | None = context.request.headers.get(header_field)
        if key is None:
            return False

        return True
