from typing import Tuple, Callable, TypeVar
from os import getenv
from requests import get
from dotenv import load_dotenv
from strawberry.field import StrawberryField
from strawberry.types.info import Info as _Info, RootValueType
from strawberry_permissions import GraphQLContext

type ReturnTuple = Tuple[str | None, str | None, str | None]
type Info = _Info[GraphQLContext, RootValueType]
load_dotenv()


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
