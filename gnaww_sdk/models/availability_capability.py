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
from gnaww_sdk.models.capability_evidence import CapabilityEvidence
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AvailabilityCapability(BaseModel):
    """
    Stable availability mode and optional live current status.
    """ # noqa: E501
    available_quantity: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    evidence: Optional[CapabilityEvidence] = None
    mode: Optional[StrictStr] = 'unknown'
    status: Optional[StrictStr] = 'unknown'
    __properties: ClassVar[List[str]] = ["available_quantity", "evidence", "mode", "status"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['made_to_order', 'stocked', 'mixed', 'unknown']):
            raise ValueError("must be one of enum values ('made_to_order', 'stocked', 'mixed', 'unknown')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['available', 'limited', 'unavailable', 'unknown']):
            raise ValueError("must be one of enum values ('available', 'limited', 'unavailable', 'unknown')")
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
        """Create an instance of AvailabilityCapability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of evidence
        if self.evidence:
            _dict['evidence'] = self.evidence.to_dict()
        # set to None if available_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.available_quantity is None and "available_quantity" in self.model_fields_set:
            _dict['available_quantity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AvailabilityCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available_quantity": obj.get("available_quantity"),
            "evidence": CapabilityEvidence.from_dict(obj["evidence"]) if obj.get("evidence") is not None else None,
            "mode": obj.get("mode") if obj.get("mode") is not None else 'unknown',
            "status": obj.get("status") if obj.get("status") is not None else 'unknown'
        })
        return _obj
