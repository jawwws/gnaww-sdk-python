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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class IntentProviderMetadata(BaseModel):
    """
    Audit-safe provider metadata without credentials or raw secrets.
    """ # noqa: E501
    input_tokens: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    mode: StrictStr
    model: Optional[StrictStr] = None
    output_tokens: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    provider: Annotated[str, Field(min_length=1, strict=True)]
    request_id: Optional[StrictStr] = None
    total_tokens: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    __properties: ClassVar[List[str]] = ["input_tokens", "mode", "model", "output_tokens", "provider", "request_id", "total_tokens"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['none', 'fixture', 'live']):
            raise ValueError("must be one of enum values ('none', 'fixture', 'live')")
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
        """Create an instance of IntentProviderMetadata from a JSON string"""
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
        # set to None if input_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.input_tokens is None and "input_tokens" in self.model_fields_set:
            _dict['input_tokens'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if output_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.output_tokens is None and "output_tokens" in self.model_fields_set:
            _dict['output_tokens'] = None

        # set to None if request_id (nullable) is None
        # and model_fields_set contains the field
        if self.request_id is None and "request_id" in self.model_fields_set:
            _dict['request_id'] = None

        # set to None if total_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.total_tokens is None and "total_tokens" in self.model_fields_set:
            _dict['total_tokens'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntentProviderMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input_tokens": obj.get("input_tokens"),
            "mode": obj.get("mode"),
            "model": obj.get("model"),
            "output_tokens": obj.get("output_tokens"),
            "provider": obj.get("provider"),
            "request_id": obj.get("request_id"),
            "total_tokens": obj.get("total_tokens")
        })
        return _obj
