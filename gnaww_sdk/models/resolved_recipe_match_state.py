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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ResolvedRecipeMatchState(BaseModel):
    """
    Safe persisted Recipe identity carried by a resolved-Recipe match.
    """ # noqa: E501
    canonicalisation_version: Annotated[str, Field(min_length=1, strict=True)]
    persisted: Optional[StrictBool] = True
    recipe_id: Annotated[str, Field(strict=True)]
    recipe_schema_name: Annotated[str, Field(min_length=1, strict=True)]
    recipe_schema_version: Annotated[str, Field(min_length=1, strict=True)]
    __properties: ClassVar[List[str]] = ["canonicalisation_version", "persisted", "recipe_id", "recipe_schema_name", "recipe_schema_version"]

    @field_validator('persisted')
    def persisted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('recipe_id')
    def recipe_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^GNR-[0-9A-HJKMNP-TV-Z]{26}$", value):
            raise ValueError(r"must validate the regular expression /^GNR-[0-9A-HJKMNP-TV-Z]{26}$/")
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
        """Create an instance of ResolvedRecipeMatchState from a JSON string"""
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
        """Create an instance of ResolvedRecipeMatchState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canonicalisation_version": obj.get("canonicalisation_version"),
            "persisted": obj.get("persisted") if obj.get("persisted") is not None else True,
            "recipe_id": obj.get("recipe_id"),
            "recipe_schema_name": obj.get("recipe_schema_name"),
            "recipe_schema_version": obj.get("recipe_schema_version")
        })
        return _obj
