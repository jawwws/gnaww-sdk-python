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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PhysicalRequirementDecision(BaseModel):
    """
    Machine-readable physical-demand decision with buyer-safe guidance.
    """ # noqa: E501
    approval_required: Optional[StrictBool] = False
    buyer_message: Annotated[str, Field(min_length=1, strict=True)]
    buyer_question: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    candidates: Optional[List[Dict[str, Any]]] = None
    classification: StrictStr
    field_path: Annotated[str, Field(min_length=1, strict=True)]
    posture: Annotated[str, Field(min_length=1, strict=True)]
    property_type: Annotated[str, Field(min_length=1, strict=True)]
    requested: Optional[Dict[str, Any]] = None
    schema_name: Optional[StrictStr] = 'gnaww.physical_requirement_decision'
    schema_version: Optional[StrictStr] = '0.1'
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["approval_required", "buyer_message", "buyer_question", "candidates", "classification", "field_path", "posture", "property_type", "requested", "schema_name", "schema_version"]

    @field_validator('classification')
    def classification_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['exact', 'acceptable_substitute', 'review_required', 'unacceptable', 'unknown']):
            raise ValueError("must be one of enum values ('exact', 'acceptable_substitute', 'review_required', 'unacceptable', 'unknown')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.physical_requirement_decision']):
            raise ValueError("must be one of enum values ('gnaww.physical_requirement_decision')")
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
        """Create an instance of PhysicalRequirementDecision from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if buyer_question (nullable) is None
        # and model_fields_set contains the field
        if self.buyer_question is None and "buyer_question" in self.model_fields_set:
            _dict['buyer_question'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalRequirementDecision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approval_required": obj.get("approval_required") if obj.get("approval_required") is not None else False,
            "buyer_message": obj.get("buyer_message"),
            "buyer_question": obj.get("buyer_question"),
            "candidates": obj.get("candidates"),
            "classification": obj.get("classification"),
            "field_path": obj.get("field_path"),
            "posture": obj.get("posture"),
            "property_type": obj.get("property_type"),
            "requested": obj.get("requested"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.physical_requirement_decision',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1'
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
