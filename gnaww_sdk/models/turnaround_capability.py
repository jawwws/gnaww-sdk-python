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

class TurnaroundCapability(BaseModel):
    """
    Producer turnaround range with explicit basis and provenance.
    """ # noqa: E501
    basis: Optional[StrictStr] = 'unknown'
    evidence: Optional[CapabilityEvidence] = None
    maximum_working_days: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    minimum_working_days: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    __properties: ClassVar[List[str]] = ["basis", "evidence", "maximum_working_days", "minimum_working_days"]

    @field_validator('basis')
    def basis_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['production_only', 'production_and_dispatch', 'unknown']):
            raise ValueError("must be one of enum values ('production_only', 'production_and_dispatch', 'unknown')")
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
        """Create an instance of TurnaroundCapability from a JSON string"""
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
        # set to None if maximum_working_days (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_working_days is None and "maximum_working_days" in self.model_fields_set:
            _dict['maximum_working_days'] = None

        # set to None if minimum_working_days (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_working_days is None and "minimum_working_days" in self.model_fields_set:
            _dict['minimum_working_days'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TurnaroundCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "basis": obj.get("basis") if obj.get("basis") is not None else 'unknown',
            "evidence": CapabilityEvidence.from_dict(obj["evidence"]) if obj.get("evidence") is not None else None,
            "maximum_working_days": obj.get("maximum_working_days"),
            "minimum_working_days": obj.get("minimum_working_days")
        })
        return _obj
