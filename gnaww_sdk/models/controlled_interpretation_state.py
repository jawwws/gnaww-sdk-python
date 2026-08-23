# coding: utf-8

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1
    Gnaww SDK

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from gnaww_sdk.models.intent_provider_metadata import IntentProviderMetadata
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ControlledInterpretationState(BaseModel):
    """
    Safe public truth about controlled semantic interpretation.
    """ # noqa: E501
    attempted: StrictBool
    error: Optional[StrictStr] = None
    metadata: Optional[IntentProviderMetadata] = None
    provider: Optional[StrictStr] = None
    status: StrictStr
    __properties: ClassVar[List[str]] = ["attempted", "error", "metadata", "provider", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['not_required', 'completed', 'unavailable', 'failed']):
            raise ValueError("must be one of enum values ('not_required', 'completed', 'unavailable', 'failed')")
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
        """Create an instance of ControlledInterpretationState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if provider (nullable) is None
        # and model_fields_set contains the field
        if self.provider is None and "provider" in self.model_fields_set:
            _dict['provider'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ControlledInterpretationState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attempted": obj.get("attempted"),
            "error": obj.get("error"),
            "metadata": IntentProviderMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "provider": obj.get("provider"),
            "status": obj.get("status")
        })
        return _obj
