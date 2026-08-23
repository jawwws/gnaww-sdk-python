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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.material_composition_part import MaterialCompositionPart
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MaterialCapability(BaseModel):
    """
    A canonical material or substrate capability.
    """ # noqa: E501
    category: Optional[StrictStr] = 'unknown'
    certifications: Optional[List[StrictStr]] = None
    composition: Optional[List[MaterialCompositionPart]] = None
    finish: Optional[StrictStr] = None
    maximum_weight_gsm: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    minimum_weight_gsm: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    name: StrictStr
    standard_weights_gsm: Optional[List[StrictInt]] = None
    weight_gsm: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    __properties: ClassVar[List[str]] = ["category", "certifications", "composition", "finish", "maximum_weight_gsm", "minimum_weight_gsm", "name", "standard_weights_gsm", "weight_gsm"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['paper', 'board', 'synthetic', 'textile', 'plastic', 'metal', 'ceramic', 'glass', 'wood', 'other', 'unknown']):
            raise ValueError("must be one of enum values ('paper', 'board', 'synthetic', 'textile', 'plastic', 'metal', 'ceramic', 'glass', 'wood', 'other', 'unknown')")
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
        """Create an instance of MaterialCapability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in composition (list)
        _items = []
        if self.composition:
            for _item_composition in self.composition:
                if _item_composition:
                    _items.append(_item_composition.to_dict())
            _dict['composition'] = _items
        # set to None if finish (nullable) is None
        # and model_fields_set contains the field
        if self.finish is None and "finish" in self.model_fields_set:
            _dict['finish'] = None

        # set to None if maximum_weight_gsm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_weight_gsm is None and "maximum_weight_gsm" in self.model_fields_set:
            _dict['maximum_weight_gsm'] = None

        # set to None if minimum_weight_gsm (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_weight_gsm is None and "minimum_weight_gsm" in self.model_fields_set:
            _dict['minimum_weight_gsm'] = None

        # set to None if weight_gsm (nullable) is None
        # and model_fields_set contains the field
        if self.weight_gsm is None and "weight_gsm" in self.model_fields_set:
            _dict['weight_gsm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MaterialCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category") if obj.get("category") is not None else 'unknown',
            "certifications": obj.get("certifications"),
            "composition": [MaterialCompositionPart.from_dict(_item) for _item in obj["composition"]] if obj.get("composition") is not None else None,
            "finish": obj.get("finish"),
            "maximum_weight_gsm": obj.get("maximum_weight_gsm"),
            "minimum_weight_gsm": obj.get("minimum_weight_gsm"),
            "name": obj.get("name"),
            "standard_weights_gsm": obj.get("standard_weights_gsm"),
            "weight_gsm": obj.get("weight_gsm")
        })
        return _obj
