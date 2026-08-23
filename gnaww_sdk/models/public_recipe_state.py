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
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicRecipeState(BaseModel):
    """
    Safe Recipe eligibility view without persistence internals.
    """ # noqa: E501
    persisted: Optional[StrictBool] = False
    reasons: Optional[List[StrictStr]] = None
    recipe_id: Optional[StrictStr] = None
    status: StrictStr
    __properties: ClassVar[List[str]] = ["persisted", "reasons", "recipe_id", "status"]

    @field_validator('persisted')
    def persisted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['eligible', 'ineligible', 'not_available']):
            raise ValueError("must be one of enum values ('eligible', 'ineligible', 'not_available')")
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
        """Create an instance of PublicRecipeState from a JSON string"""
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
        # set to None if recipe_id (nullable) is None
        # and model_fields_set contains the field
        if self.recipe_id is None and "recipe_id" in self.model_fields_set:
            _dict['recipe_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicRecipeState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "persisted": obj.get("persisted") if obj.get("persisted") is not None else False,
            "reasons": obj.get("reasons"),
            "recipe_id": obj.get("recipe_id"),
            "status": obj.get("status")
        })
        return _obj
