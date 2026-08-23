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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class RecipeResource(BaseModel):
    """
    Safe developer-facing representation of one canonical Recipe.
    """ # noqa: E501
    canonical_payload: Dict[str, Any]
    canonicalisation_version: StrictStr
    created_at: datetime
    recipe_id: StrictStr
    recipe_schema_name: StrictStr
    recipe_schema_version: StrictStr
    schema_name: Optional[StrictStr] = 'gnaww.recipe_resource'
    schema_version: Optional[StrictStr] = '0.1'
    status: StrictStr
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["canonical_payload", "canonicalisation_version", "created_at", "recipe_id", "recipe_schema_name", "recipe_schema_version", "schema_name", "schema_version", "status"]

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.recipe_resource']):
            raise ValueError("must be one of enum values ('gnaww.recipe_resource')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['active']):
            raise ValueError("must be one of enum values ('active')")
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
        """Create an instance of RecipeResource from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecipeResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canonical_payload": obj.get("canonical_payload"),
            "canonicalisation_version": obj.get("canonicalisation_version"),
            "created_at": obj.get("created_at"),
            "recipe_id": obj.get("recipe_id"),
            "recipe_schema_name": obj.get("recipe_schema_name"),
            "recipe_schema_version": obj.get("recipe_schema_version"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.recipe_resource',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
