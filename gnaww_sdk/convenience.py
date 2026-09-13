"""Thin curated Gnaww helpers over the generated official Python SDK."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Generic, TypedDict, TypeVar, cast

from gnaww_sdk.api.interpretation_api import InterpretationApi
from gnaww_sdk.api.recipes_api import RecipesApi
from gnaww_sdk.api_client import ApiClient
from gnaww_sdk.configuration import Configuration
from gnaww_sdk.exceptions import ApiException
from gnaww_sdk.models.continue_interpretation_request_v02 import (
    ContinueInterpretationRequestV02,
)
from gnaww_sdk.models.interpret_print_requirement_request import (
    InterpretPrintRequirementRequest,
)
from gnaww_sdk.models.interpretation_result_v02 import InterpretationResultV02
from gnaww_sdk.models.match_recipe_request import MatchRecipeRequest
from gnaww_sdk.models.resolve_recipe_request import ResolveRecipeRequest

T = TypeVar("T")


class GnawwClarificationAnswer(TypedDict):
    """One public continuation answer keyed by a Gnaww question identity."""

    question_id: str
    value: str


@dataclass(frozen=True)
class GnawwResponse(Generic[T]):
    """One SDK result with public trace identifiers."""

    data: T
    status: int
    request_id: str | None
    correlation_id: str | None


@dataclass(frozen=True)
class GnawwPublicError:
    """Stable safe Gnaww developer error fields."""

    code: str
    message: str
    status: int
    request_id: str | None
    correlation_id: str | None
    retryable: bool


class GnawwApiError(Exception):
    """Raised from the stable safe public developer error envelope."""

    def __init__(self, error: GnawwPublicError) -> None:
        super().__init__(error.message)
        self.error = error


class GnawwClient:
    """Curated helpers over generated interpretation and Recipe APIs."""

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = "https://api.gnaww.io",
        workspace_id: str | None = None,
    ) -> None:
        configuration = Configuration(host=base_url.rstrip("/"))
        configuration.api_key["GnawwApiKey"] = api_key

        self._api_client = ApiClient(configuration)
        self._api_client.set_default_header("X-Gnaww-Source-Channel", "sdk")
        self._api_client.set_default_header("X-Gnaww-Client-Id", "gnaww-python-sdk")
        if workspace_id is not None:
            self._api_client.set_default_header(
                "X-Gnaww-Workspace-Id",
                workspace_id,
            )

        self._interpretation = InterpretationApi(self._api_client)
        self._recipes = RecipesApi(self._api_client)

    def __enter__(self) -> GnawwClient:
        self._api_client.__enter__()
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self._api_client.__exit__(exc_type, exc, traceback)

    def consume(self, requirement: str) -> InterpretationResultV02:
        """Interpret messy print intent into the job-centric public result."""

        return self.consume_detailed(requirement).data

    def consume_detailed(
        self,
        requirement: str,
    ) -> GnawwResponse[InterpretationResultV02]:
        request = InterpretPrintRequirementRequest.from_dict(
            {
                "source": {
                    "type": "natural_language",
                    "raw_text": requirement,
                },
                "gjs_version": "0.4",
            }
        )
        return cast(
            GnawwResponse[InterpretationResultV02],
            self._call(
                lambda: self._interpretation.interpret_print_requirement_with_http_info(
                    request
                )
            ),
        )

    def continue_requirement(
        self,
        requirement: str,
        answers: list[GnawwClarificationAnswer],
    ) -> InterpretationResultV02:
        """Continue using public question IDs and return the same v0.2 result shape."""

        return self.continue_requirement_detailed(requirement, answers).data

    def continue_requirement_detailed(
        self,
        requirement: str,
        answers: list[GnawwClarificationAnswer],
    ) -> GnawwResponse[InterpretationResultV02]:
        """Continue interpretation while preserving public truth and trace state."""

        request = ContinueInterpretationRequestV02.from_dict(
            {
                "source": {
                    "type": "natural_language",
                    "raw_text": requirement,
                },
                "gjs_version": "0.4",
                "answers": answers,
            }
        )
        operation = (
            self._interpretation.continue_print_requirement_interpretation_with_http_info
        )
        return cast(
            GnawwResponse[InterpretationResultV02],
            self._call(lambda: operation(request)),
        )

    def get_recipe(self, recipe_id: str) -> Any:
        """Read one safe retained Recipe resource."""

        return self.get_recipe_detailed(recipe_id).data

    def get_recipe_detailed(self, recipe_id: str) -> GnawwResponse[Any]:
        return self._call(
            lambda: self._recipes.get_recipe_with_http_info(recipe_id)
        )

    def resolve_recipe(self, gjs: dict[str, Any]) -> Any:
        """Resolve an API-returned canonical GJS to Recipe identity."""

        return self.resolve_recipe_detailed(gjs).data

    def resolve_recipe_detailed(
        self,
        gjs: dict[str, Any],
    ) -> GnawwResponse[Any]:
        request = ResolveRecipeRequest.from_dict({"gjs": gjs})
        return self._call(
            lambda: self._recipes.resolve_recipe_with_http_info(request)
        )

    def crunch(
        self,
        recipe_id: str,
        *,
        quantity: int,
        target: dict[str, Any],
    ) -> Any:
        """Run resolved-Recipe SpecMatch against one explicit target."""

        return self.crunch_detailed(
            recipe_id,
            quantity=quantity,
            target=target,
        ).data

    def crunch_detailed(
        self,
        recipe_id: str,
        *,
        quantity: int,
        target: dict[str, Any],
    ) -> GnawwResponse[Any]:
        request = MatchRecipeRequest.from_dict(
            {
                "quantity": quantity,
                "target": target,
            }
        )
        return self._call(
            lambda: self._recipes.match_recipe_with_http_info(
                recipe_id,
                request,
            )
        )

    def _call(self, call: Any) -> GnawwResponse[Any]:
        try:
            response = call()
        except ApiException as exc:
            raise GnawwApiError(_public_error_from_exception(exc)) from exc

        headers = cast(dict[str, Any], response.headers)
        return GnawwResponse(
            data=response.data,
            status=response.status_code,
            request_id=_header(headers, "X-Request-Id"),
            correlation_id=_header(headers, "X-Correlation-Id"),
        )


def _public_error_from_exception(exc: ApiException) -> GnawwPublicError:
    decoded: object = None
    body = getattr(exc, "body", None)
    if isinstance(body, str):
        try:
            decoded = json.loads(body)
        except json.JSONDecodeError:
            decoded = None

    headers = cast(dict[str, Any], getattr(exc, "headers", {}) or {})
    status = getattr(exc, "status", None)
    default_status = status if isinstance(status, int) else 0

    if isinstance(decoded, dict):
        public_error = decoded.get("error")
        if isinstance(public_error, dict):
            return GnawwPublicError(
                code=_string(public_error.get("code"), "api_error"),
                message=_string(
                    public_error.get("message"),
                    "Gnaww rejected the developer API request.",
                ),
                status=_integer(public_error.get("status"), default_status),
                request_id=(
                    _optional_string(public_error.get("request_id"))
                    or _header(headers, "X-Request-Id")
                ),
                correlation_id=(
                    _optional_string(public_error.get("correlation_id"))
                    or _header(headers, "X-Correlation-Id")
                ),
                retryable=_boolean(public_error.get("retryable"), False),
            )

    return GnawwPublicError(
        code="api_error",
        message="Gnaww rejected the developer API request.",
        status=default_status,
        request_id=_header(headers, "X-Request-Id"),
        correlation_id=_header(headers, "X-Correlation-Id"),
        retryable=False,
    )


def _header(headers: dict[str, Any], name: str) -> str | None:
    target = name.casefold()
    for key, value in headers.items():
        if str(key).casefold() != target:
            continue
        if isinstance(value, str):
            return value
        if isinstance(value, list) and value and isinstance(value[0], str):
            return value[0]
    return None


def _string(value: object, fallback: str) -> str:
    return value if isinstance(value, str) else fallback


def _optional_string(value: object) -> str | None:
    return value if isinstance(value, str) else None


def _integer(value: object, fallback: int) -> int:
    return value if isinstance(value, int) else fallback


def _boolean(value: object, fallback: bool) -> bool:
    return value if isinstance(value, bool) else fallback
