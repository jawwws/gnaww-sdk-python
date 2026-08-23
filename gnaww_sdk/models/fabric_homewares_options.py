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
from typing import Any, ClassVar, Dict, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FabricHomewaresOptions(BaseModel):
    """
    Fabric and homewares production options.
    """ # noqa: E501
    colour_profile: Optional[StrictStr] = 'unknown'
    fastening_type: Optional[StrictStr] = 'unknown'
    hem_style: Optional[StrictStr] = 'unknown'
    lining_type: Optional[StrictStr] = 'unknown'
    maximum_wash_temperature_c: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = None
    print_method: Optional[StrictStr] = 'unknown'
    repeat_height_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    repeat_type: Optional[StrictStr] = 'unknown'
    repeat_width_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    wash_care: Optional[StrictStr] = 'unknown'
    __properties: ClassVar[List[str]] = ["colour_profile", "fastening_type", "hem_style", "lining_type", "maximum_wash_temperature_c", "print_method", "repeat_height_mm", "repeat_type", "repeat_width_mm", "wash_care"]

    @field_validator('colour_profile')
    def colour_profile_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['srgb', 'adobe_rgb', 'cmyk', 'icc_managed', 'unknown']):
            raise ValueError("must be one of enum values ('srgb', 'adobe_rgb', 'cmyk', 'icc_managed', 'unknown')")
        return value

    @field_validator('fastening_type')
    def fastening_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'zip', 'concealed_zip', 'buttons', 'ties', 'eyelets', 'hook_and_loop', 'envelope', 'drawstring', 'unknown']):
            raise ValueError("must be one of enum values ('none', 'zip', 'concealed_zip', 'buttons', 'ties', 'eyelets', 'hook_and_loop', 'envelope', 'drawstring', 'unknown')")
        return value

    @field_validator('hem_style')
    def hem_style_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'overlocked', 'single_turn', 'double_turn', 'rolled', 'blind', 'unknown']):
            raise ValueError("must be one of enum values ('none', 'overlocked', 'single_turn', 'double_turn', 'rolled', 'blind', 'unknown')")
        return value

    @field_validator('lining_type')
    def lining_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'standard', 'blackout', 'thermal', 'interlining', 'unknown']):
            raise ValueError("must be one of enum values ('none', 'standard', 'blackout', 'thermal', 'interlining', 'unknown')")
        return value

    @field_validator('print_method')
    def print_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown']):
            raise ValueError("must be one of enum values ('digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown')")
        return value

    @field_validator('repeat_type')
    def repeat_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'straight', 'half_drop', 'mirror', 'seamless', 'engineered', 'unknown']):
            raise ValueError("must be one of enum values ('none', 'straight', 'half_drop', 'mirror', 'seamless', 'engineered', 'unknown')")
        return value

    @field_validator('wash_care')
    def wash_care_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['machine_wash', 'hand_wash', 'dry_clean', 'not_washable', 'unknown']):
            raise ValueError("must be one of enum values ('machine_wash', 'hand_wash', 'dry_clean', 'not_washable', 'unknown')")
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
        """Create an instance of FabricHomewaresOptions from a JSON string"""
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
        # set to None if maximum_wash_temperature_c (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_wash_temperature_c is None and "maximum_wash_temperature_c" in self.model_fields_set:
            _dict['maximum_wash_temperature_c'] = None

        # set to None if repeat_height_mm (nullable) is None
        # and model_fields_set contains the field
        if self.repeat_height_mm is None and "repeat_height_mm" in self.model_fields_set:
            _dict['repeat_height_mm'] = None

        # set to None if repeat_width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.repeat_width_mm is None and "repeat_width_mm" in self.model_fields_set:
            _dict['repeat_width_mm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FabricHomewaresOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "colour_profile": obj.get("colour_profile") if obj.get("colour_profile") is not None else 'unknown',
            "fastening_type": obj.get("fastening_type") if obj.get("fastening_type") is not None else 'unknown',
            "hem_style": obj.get("hem_style") if obj.get("hem_style") is not None else 'unknown',
            "lining_type": obj.get("lining_type") if obj.get("lining_type") is not None else 'unknown',
            "maximum_wash_temperature_c": obj.get("maximum_wash_temperature_c"),
            "print_method": obj.get("print_method") if obj.get("print_method") is not None else 'unknown',
            "repeat_height_mm": obj.get("repeat_height_mm"),
            "repeat_type": obj.get("repeat_type") if obj.get("repeat_type") is not None else 'unknown',
            "repeat_width_mm": obj.get("repeat_width_mm"),
            "wash_care": obj.get("wash_care") if obj.get("wash_care") is not None else 'unknown'
        })
        return _obj
