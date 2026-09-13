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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.public_controlled_default_fold_geometry import PublicControlledDefaultFoldGeometry
from gnaww_sdk.models.public_controlled_default_user_evidence import PublicControlledDefaultUserEvidence
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicControlledProductionDefault(BaseModel):
    """
    Approved production convention shown separately from explicit source evidence.
    """ # noqa: E501
    evidence_ids: Annotated[List[StrictStr], Field(min_length=1)]
    fold_geometry: PublicControlledDefaultFoldGeometry
    label: Annotated[str, Field(min_length=1, strict=True)]
    rule_id: StrictStr
    rule_version: StrictStr
    summary: Annotated[str, Field(min_length=1, strict=True)]
    target_path: StrictStr
    truth_state: StrictStr
    user_evidence: Optional[PublicControlledDefaultUserEvidence] = None
    verification_key: StrictStr
    __properties: ClassVar[List[str]] = ["evidence_ids", "fold_geometry", "label", "rule_id", "rule_version", "summary", "target_path", "truth_state", "user_evidence", "verification_key"]

    @field_validator('truth_state')
    def truth_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['defaulted', 'confirmed', 'changed']):
            raise ValueError("must be one of enum values ('defaulted', 'confirmed', 'changed')")
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
        """Create an instance of PublicControlledProductionDefault from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fold_geometry
        if self.fold_geometry:
            _dict['fold_geometry'] = self.fold_geometry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_evidence
        if self.user_evidence:
            _dict['user_evidence'] = self.user_evidence.to_dict()
        # set to None if user_evidence (nullable) is None
        # and model_fields_set contains the field
        if self.user_evidence is None and "user_evidence" in self.model_fields_set:
            _dict['user_evidence'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicControlledProductionDefault from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "evidence_ids": obj.get("evidence_ids"),
            "fold_geometry": PublicControlledDefaultFoldGeometry.from_dict(obj["fold_geometry"]) if obj.get("fold_geometry") is not None else None,
            "label": obj.get("label"),
            "rule_id": obj.get("rule_id"),
            "rule_version": obj.get("rule_version"),
            "summary": obj.get("summary"),
            "target_path": obj.get("target_path"),
            "truth_state": obj.get("truth_state"),
            "user_evidence": PublicControlledDefaultUserEvidence.from_dict(obj["user_evidence"]) if obj.get("user_evidence") is not None else None,
            "verification_key": obj.get("verification_key")
        })
        return _obj
