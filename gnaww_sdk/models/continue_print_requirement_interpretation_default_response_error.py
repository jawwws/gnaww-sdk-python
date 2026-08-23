# coding: utf-8

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ContinuePrintRequirementInterpretationDefaultResponseError(BaseModel):
    """
    ContinuePrintRequirementInterpretationDefaultResponseError
    """ # noqa: E501
    code: Annotated[str, Field(min_length=1, strict=True)]
    correlation_id: Annotated[str, Field(strict=True)]
    details: Dict[str, Any]
    message: Annotated[str, Field(min_length=1, strict=True)]
    request_id: Annotated[str, Field(strict=True)]
    retryable: StrictBool
    status: Annotated[int, Field(le=599, strict=True, ge=400)]
    __properties: ClassVar[List[str]] = ["code", "correlation_id", "details", "message", "request_id", "retryable", "status"]

    @field_validator('correlation_id')
    def correlation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^cor_[0-9A-HJKMNP-TV-Z]{26}$", value):
            raise ValueError(r"must validate the regular expression /^cor_[0-9A-HJKMNP-TV-Z]{26}$/")
        return value

    @field_validator('request_id')
    def request_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^req_[0-9A-HJKMNP-TV-Z]{26}$", value):
            raise ValueError(r"must validate the regular expression /^req_[0-9A-HJKMNP-TV-Z]{26}$/")
        return value

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ContinuePrintRequirementInterpretationDefaultResponseError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContinuePrintRequirementInterpretationDefaultResponseError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "correlation_id": obj.get("correlation_id"),
            "details": obj.get("details"),
            "message": obj.get("message"),
            "request_id": obj.get("request_id"),
            "retryable": obj.get("retryable"),
            "status": obj.get("status")
        })
        return _obj
