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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.issue_set import IssueSet
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FulfilmentMatchResult(BaseModel):
    """
    Capability-plane fulfilment result for one producer profile.
    """ # noqa: E501
    destination_country_code: StrictStr
    issues: Optional[IssueSet] = None
    match_reasons: Optional[List[StrictStr]] = None
    offered_maximum_delivery_working_days: Optional[StrictInt] = None
    offered_minimum_delivery_working_days: Optional[StrictInt] = None
    offered_service_classes: Optional[List[StrictStr]] = None
    requested_maximum_delivery_working_days: Optional[StrictInt] = None
    requested_service_class: Optional[StrictStr] = None
    service_country_codes: Optional[List[StrictStr]] = None
    status: StrictStr
    __properties: ClassVar[List[str]] = ["destination_country_code", "issues", "match_reasons", "offered_maximum_delivery_working_days", "offered_minimum_delivery_working_days", "offered_service_classes", "requested_maximum_delivery_working_days", "requested_service_class", "service_country_codes", "status"]

    @field_validator('offered_service_classes')
    def offered_service_classes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['standard', 'express', 'freight']):
                raise ValueError("each list item must be one of ('standard', 'express', 'freight')")
        return value

    @field_validator('requested_service_class')
    def requested_service_class_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['standard', 'express', 'freight']):
            raise ValueError("must be one of enum values ('standard', 'express', 'freight')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['matched', 'needs_review', 'blocked']):
            raise ValueError("must be one of enum values ('matched', 'needs_review', 'blocked')")
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
        """Create an instance of FulfilmentMatchResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # set to None if offered_maximum_delivery_working_days (nullable) is None
        # and model_fields_set contains the field
        if self.offered_maximum_delivery_working_days is None and "offered_maximum_delivery_working_days" in self.model_fields_set:
            _dict['offered_maximum_delivery_working_days'] = None

        # set to None if offered_minimum_delivery_working_days (nullable) is None
        # and model_fields_set contains the field
        if self.offered_minimum_delivery_working_days is None and "offered_minimum_delivery_working_days" in self.model_fields_set:
            _dict['offered_minimum_delivery_working_days'] = None

        # set to None if requested_maximum_delivery_working_days (nullable) is None
        # and model_fields_set contains the field
        if self.requested_maximum_delivery_working_days is None and "requested_maximum_delivery_working_days" in self.model_fields_set:
            _dict['requested_maximum_delivery_working_days'] = None

        # set to None if requested_service_class (nullable) is None
        # and model_fields_set contains the field
        if self.requested_service_class is None and "requested_service_class" in self.model_fields_set:
            _dict['requested_service_class'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FulfilmentMatchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_country_code": obj.get("destination_country_code"),
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "match_reasons": obj.get("match_reasons"),
            "offered_maximum_delivery_working_days": obj.get("offered_maximum_delivery_working_days"),
            "offered_minimum_delivery_working_days": obj.get("offered_minimum_delivery_working_days"),
            "offered_service_classes": obj.get("offered_service_classes"),
            "requested_maximum_delivery_working_days": obj.get("requested_maximum_delivery_working_days"),
            "requested_service_class": obj.get("requested_service_class"),
            "service_country_codes": obj.get("service_country_codes"),
            "status": obj.get("status")
        })
        return _obj
