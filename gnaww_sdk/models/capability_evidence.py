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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CapabilityEvidence(BaseModel):
    """
    Provenance and freshness for operational capability data.
    """ # noqa: E501
    expires_at: Optional[datetime] = None
    observed_at: Optional[datetime] = None
    source: Optional[StrictStr] = 'unknown'
    status: Optional[StrictStr] = 'unknown'
    __properties: ClassVar[List[str]] = ["expires_at", "observed_at", "source", "status"]

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['fixture', 'imported', 'producer_declared', 'live', 'unknown']):
            raise ValueError("must be one of enum values ('fixture', 'imported', 'producer_declared', 'live', 'unknown')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['synthetic', 'unverified', 'verified', 'live', 'unknown']):
            raise ValueError("must be one of enum values ('synthetic', 'unverified', 'verified', 'live', 'unknown')")
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
        """Create an instance of CapabilityEvidence from a JSON string"""
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
        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        # set to None if observed_at (nullable) is None
        # and model_fields_set contains the field
        if self.observed_at is None and "observed_at" in self.model_fields_set:
            _dict['observed_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CapabilityEvidence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expires_at": obj.get("expires_at"),
            "observed_at": obj.get("observed_at"),
            "source": obj.get("source") if obj.get("source") is not None else 'unknown',
            "status": obj.get("status") if obj.get("status") is not None else 'unknown'
        })
        return _obj
