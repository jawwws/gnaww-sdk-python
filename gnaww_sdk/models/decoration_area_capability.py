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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DecorationAreaCapability(BaseModel):
    """
    A reusable decoration position and size capability.
    """ # noqa: E501
    maximum_colours: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    maximum_diameter_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    maximum_height_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    maximum_width_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    methods: Annotated[List[StrictStr], Field(min_length=1)]
    position: StrictStr
    supports_full_colour: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["maximum_colours", "maximum_diameter_mm", "maximum_height_mm", "maximum_width_mm", "methods", "position", "supports_full_colour"]

    @field_validator('methods')
    def methods_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'unknown']):
                raise ValueError("each list item must be one of ('dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'unknown')")
        return value

    @field_validator('position')
    def position_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['front', 'back', 'left_chest', 'right_chest', 'sleeve', 'cap_front', 'left', 'right', 'wrap', 'barrel', 'lid', 'base', 'unknown']):
            raise ValueError("must be one of enum values ('front', 'back', 'left_chest', 'right_chest', 'sleeve', 'cap_front', 'left', 'right', 'wrap', 'barrel', 'lid', 'base', 'unknown')")
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
        """Create an instance of DecorationAreaCapability from a JSON string"""
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
        # set to None if maximum_colours (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_colours is None and "maximum_colours" in self.model_fields_set:
            _dict['maximum_colours'] = None

        # set to None if maximum_diameter_mm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_diameter_mm is None and "maximum_diameter_mm" in self.model_fields_set:
            _dict['maximum_diameter_mm'] = None

        # set to None if maximum_height_mm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_height_mm is None and "maximum_height_mm" in self.model_fields_set:
            _dict['maximum_height_mm'] = None

        # set to None if maximum_width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_width_mm is None and "maximum_width_mm" in self.model_fields_set:
            _dict['maximum_width_mm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DecorationAreaCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maximum_colours": obj.get("maximum_colours"),
            "maximum_diameter_mm": obj.get("maximum_diameter_mm"),
            "maximum_height_mm": obj.get("maximum_height_mm"),
            "maximum_width_mm": obj.get("maximum_width_mm"),
            "methods": obj.get("methods"),
            "position": obj.get("position"),
            "supports_full_colour": obj.get("supports_full_colour") if obj.get("supports_full_colour") is not None else False
        })
        return _obj
