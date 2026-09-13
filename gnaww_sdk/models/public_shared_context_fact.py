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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.public_interpretation_scope import PublicInterpretationScope
from gnaww_sdk.models.value import Value
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicSharedContextFact(BaseModel):
    """
    One provenance-aware fact that applies across the parent intent.
    """ # noqa: E501
    context_id: Annotated[str, Field(strict=True)]
    key: Annotated[str, Field(strict=True)]
    posture: Optional[StrictStr] = 'exact'
    provenance: StrictStr
    requires_confirmation: Optional[StrictBool] = False
    scope: Optional[PublicInterpretationScope] = None
    source_expression: Optional[StrictStr] = None
    value: Optional[Value] = None
    __properties: ClassVar[List[str]] = ["context_id", "key", "posture", "provenance", "requires_confirmation", "scope", "source_expression", "value"]

    @field_validator('context_id')
    def context_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^context_[a-z0-9][a-z0-9_.-]*$", value):
            raise ValueError(r"must validate the regular expression /^context_[a-z0-9][a-z0-9_.-]*$/")
        return value

    @field_validator('key')
    def key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[a-z][a-z0-9_.-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_.-]*$/")
        return value

    @field_validator('posture')
    def posture_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['exact', 'preference', 'tolerance', 'ambiguous']):
            raise ValueError("must be one of enum values ('exact', 'preference', 'tolerance', 'ambiguous')")
        return value

    @field_validator('provenance')
    def provenance_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['supplied', 'derived', 'confirmed', 'controlled']):
            raise ValueError("must be one of enum values ('supplied', 'derived', 'confirmed', 'controlled')")
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
        """Create an instance of PublicSharedContextFact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # set to None if source_expression (nullable) is None
        # and model_fields_set contains the field
        if self.source_expression is None and "source_expression" in self.model_fields_set:
            _dict['source_expression'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicSharedContextFact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "context_id": obj.get("context_id"),
            "key": obj.get("key"),
            "posture": obj.get("posture") if obj.get("posture") is not None else 'exact',
            "provenance": obj.get("provenance"),
            "requires_confirmation": obj.get("requires_confirmation") if obj.get("requires_confirmation") is not None else False,
            "scope": PublicInterpretationScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "source_expression": obj.get("source_expression"),
            "value": Value.from_dict(obj["value"]) if obj.get("value") is not None else None
        })
        return _obj
