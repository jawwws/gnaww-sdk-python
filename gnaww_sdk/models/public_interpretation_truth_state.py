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

from pydantic import BaseModel, ConfigDict, StrictBool, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicInterpretationTruthState(BaseModel):
    """
    Side-effect and live-truth flags for interpretation only.
    """ # noqa: E501
    availability_checked: Optional[StrictBool] = False
    live_pricing_performed: Optional[StrictBool] = False
    order_created: Optional[StrictBool] = False
    persistence_performed: Optional[StrictBool] = False
    producer_acceptance_performed: Optional[StrictBool] = False
    producer_selection_performed: Optional[StrictBool] = False
    specmatch_performed: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["availability_checked", "live_pricing_performed", "order_created", "persistence_performed", "producer_acceptance_performed", "producer_selection_performed", "specmatch_performed"]

    @field_validator('availability_checked')
    def availability_checked_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('live_pricing_performed')
    def live_pricing_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('order_created')
    def order_created_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('persistence_performed')
    def persistence_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('producer_acceptance_performed')
    def producer_acceptance_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('producer_selection_performed')
    def producer_selection_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
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
        """Create an instance of PublicInterpretationTruthState from a JSON string"""
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
        """Create an instance of PublicInterpretationTruthState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability_checked": obj.get("availability_checked") if obj.get("availability_checked") is not None else False,
            "live_pricing_performed": obj.get("live_pricing_performed") if obj.get("live_pricing_performed") is not None else False,
            "order_created": obj.get("order_created") if obj.get("order_created") is not None else False,
            "persistence_performed": obj.get("persistence_performed") if obj.get("persistence_performed") is not None else False,
            "producer_acceptance_performed": obj.get("producer_acceptance_performed") if obj.get("producer_acceptance_performed") is not None else False,
            "producer_selection_performed": obj.get("producer_selection_performed") if obj.get("producer_selection_performed") is not None else False,
            "specmatch_performed": obj.get("specmatch_performed") if obj.get("specmatch_performed") is not None else False
        })
        return _obj
