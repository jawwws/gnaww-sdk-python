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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.grammage_requirement import GrammageRequirement
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Substrate(BaseModel):
    """
    Requested substrate or material.
    """ # noqa: E501
    category: Optional[StrictStr] = 'unknown'
    finish: Optional[StrictStr] = 'unknown'
    grammage_requirement: Optional[GrammageRequirement] = None
    material: Optional[StrictStr] = None
    texture: Optional[StrictStr] = None
    weight_gsm: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    __properties: ClassVar[List[str]] = ["category", "finish", "grammage_requirement", "material", "texture", "weight_gsm"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['paper', 'board', 'synthetic', 'textile', 'plastic', 'metal', 'ceramic', 'glass', 'wood', 'other', 'unknown']):
            raise ValueError("must be one of enum values ('paper', 'board', 'synthetic', 'textile', 'plastic', 'metal', 'ceramic', 'glass', 'wood', 'other', 'unknown')")
        return value

    @field_validator('finish')
    def finish_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['silk', 'gloss', 'uncoated', 'linen', 'synthetic', 'textile', 'other', 'unknown']):
            raise ValueError("must be one of enum values ('silk', 'gloss', 'uncoated', 'linen', 'synthetic', 'textile', 'other', 'unknown')")
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
        """Create an instance of Substrate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of grammage_requirement
        if self.grammage_requirement:
            _dict['grammage_requirement'] = self.grammage_requirement.to_dict()
        # set to None if grammage_requirement (nullable) is None
        # and model_fields_set contains the field
        if self.grammage_requirement is None and "grammage_requirement" in self.model_fields_set:
            _dict['grammage_requirement'] = None

        # set to None if material (nullable) is None
        # and model_fields_set contains the field
        if self.material is None and "material" in self.model_fields_set:
            _dict['material'] = None

        # set to None if texture (nullable) is None
        # and model_fields_set contains the field
        if self.texture is None and "texture" in self.model_fields_set:
            _dict['texture'] = None

        # set to None if weight_gsm (nullable) is None
        # and model_fields_set contains the field
        if self.weight_gsm is None and "weight_gsm" in self.model_fields_set:
            _dict['weight_gsm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Substrate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category") if obj.get("category") is not None else 'unknown',
            "finish": obj.get("finish") if obj.get("finish") is not None else 'unknown',
            "grammage_requirement": GrammageRequirement.from_dict(obj["grammage_requirement"]) if obj.get("grammage_requirement") is not None else None,
            "material": obj.get("material"),
            "texture": obj.get("texture"),
            "weight_gsm": obj.get("weight_gsm")
        })
        return _obj
