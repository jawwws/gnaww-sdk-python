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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.custom_dimension_capability import CustomDimensionCapability
from gnaww_sdk.models.dimension_capability import DimensionCapability
from gnaww_sdk.models.material_capability import MaterialCapability
from gnaww_sdk.models.repeat_pattern_capability import RepeatPatternCapability
from gnaww_sdk.models.washability_capability import WashabilityCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FabricHomewaresCapabilityOptions(BaseModel):
    """
    Canonical fabric and homewares production capabilities.
    """ # noqa: E501
    colour_profiles: Optional[List[StrictStr]] = None
    custom_dimensions: Optional[CustomDimensionCapability] = None
    dimensions: Optional[List[DimensionCapability]] = None
    fastening_types: Optional[List[StrictStr]] = None
    hem_styles: Optional[List[StrictStr]] = None
    lining_types: Optional[List[StrictStr]] = None
    materials: Optional[List[MaterialCapability]] = None
    print_methods: Optional[List[StrictStr]] = None
    printed_sides: Optional[List[StrictStr]] = None
    repeat_pattern: Optional[RepeatPatternCapability] = None
    washability: Optional[WashabilityCapability] = None
    __properties: ClassVar[List[str]] = ["colour_profiles", "custom_dimensions", "dimensions", "fastening_types", "hem_styles", "lining_types", "materials", "print_methods", "printed_sides", "repeat_pattern", "washability"]

    @field_validator('colour_profiles')
    def colour_profiles_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['srgb', 'adobe_rgb', 'cmyk', 'icc_managed', 'unknown']):
                raise ValueError("each list item must be one of ('srgb', 'adobe_rgb', 'cmyk', 'icc_managed', 'unknown')")
        return value

    @field_validator('fastening_types')
    def fastening_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['none', 'zip', 'concealed_zip', 'buttons', 'ties', 'eyelets', 'hook_and_loop', 'envelope', 'drawstring', 'unknown']):
                raise ValueError("each list item must be one of ('none', 'zip', 'concealed_zip', 'buttons', 'ties', 'eyelets', 'hook_and_loop', 'envelope', 'drawstring', 'unknown')")
        return value

    @field_validator('hem_styles')
    def hem_styles_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['none', 'overlocked', 'single_turn', 'double_turn', 'rolled', 'blind', 'unknown']):
                raise ValueError("each list item must be one of ('none', 'overlocked', 'single_turn', 'double_turn', 'rolled', 'blind', 'unknown')")
        return value

    @field_validator('lining_types')
    def lining_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['none', 'standard', 'blackout', 'thermal', 'interlining', 'unknown']):
                raise ValueError("each list item must be one of ('none', 'standard', 'blackout', 'thermal', 'interlining', 'unknown')")
        return value

    @field_validator('print_methods')
    def print_methods_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown']):
                raise ValueError("each list item must be one of ('digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown')")
        return value

    @field_validator('printed_sides')
    def printed_sides_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['single_sided', 'double_sided', 'unknown']):
                raise ValueError("each list item must be one of ('single_sided', 'double_sided', 'unknown')")
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
        """Create an instance of FabricHomewaresCapabilityOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_dimensions
        if self.custom_dimensions:
            _dict['custom_dimensions'] = self.custom_dimensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item_dimensions in self.dimensions:
                if _item_dimensions:
                    _items.append(_item_dimensions.to_dict())
            _dict['dimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in materials (list)
        _items = []
        if self.materials:
            for _item_materials in self.materials:
                if _item_materials:
                    _items.append(_item_materials.to_dict())
            _dict['materials'] = _items
        # override the default output from pydantic by calling `to_dict()` of repeat_pattern
        if self.repeat_pattern:
            _dict['repeat_pattern'] = self.repeat_pattern.to_dict()
        # override the default output from pydantic by calling `to_dict()` of washability
        if self.washability:
            _dict['washability'] = self.washability.to_dict()
        # set to None if custom_dimensions (nullable) is None
        # and model_fields_set contains the field
        if self.custom_dimensions is None and "custom_dimensions" in self.model_fields_set:
            _dict['custom_dimensions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FabricHomewaresCapabilityOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "colour_profiles": obj.get("colour_profiles"),
            "custom_dimensions": CustomDimensionCapability.from_dict(obj["custom_dimensions"]) if obj.get("custom_dimensions") is not None else None,
            "dimensions": [DimensionCapability.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "fastening_types": obj.get("fastening_types"),
            "hem_styles": obj.get("hem_styles"),
            "lining_types": obj.get("lining_types"),
            "materials": [MaterialCapability.from_dict(_item) for _item in obj["materials"]] if obj.get("materials") is not None else None,
            "print_methods": obj.get("print_methods"),
            "printed_sides": obj.get("printed_sides"),
            "repeat_pattern": RepeatPatternCapability.from_dict(obj["repeat_pattern"]) if obj.get("repeat_pattern") is not None else None,
            "washability": WashabilityCapability.from_dict(obj["washability"]) if obj.get("washability") is not None else None
        })
        return _obj
