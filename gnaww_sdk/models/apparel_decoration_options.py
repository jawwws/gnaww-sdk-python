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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApparelDecorationOptions(BaseModel):
    """
    Apparel decoration production options.
    """ # noqa: E501
    decoration_method: Optional[StrictStr] = 'unknown'
    garment_colour: Optional[StrictStr] = None
    garment_type: Optional[StrictStr] = None
    position: Optional[StrictStr] = 'unknown'
    printable_height_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    printable_width_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    size_range: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["decoration_method", "garment_colour", "garment_type", "position", "printable_height_mm", "printable_width_mm", "size_range"]

    @field_validator('decoration_method')
    def decoration_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'unknown']):
            raise ValueError("must be one of enum values ('dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'unknown')")
        return value

    @field_validator('position')
    def position_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
        """Create an instance of ApparelDecorationOptions from a JSON string"""
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
        # set to None if garment_colour (nullable) is None
        # and model_fields_set contains the field
        if self.garment_colour is None and "garment_colour" in self.model_fields_set:
            _dict['garment_colour'] = None

        # set to None if garment_type (nullable) is None
        # and model_fields_set contains the field
        if self.garment_type is None and "garment_type" in self.model_fields_set:
            _dict['garment_type'] = None

        # set to None if printable_height_mm (nullable) is None
        # and model_fields_set contains the field
        if self.printable_height_mm is None and "printable_height_mm" in self.model_fields_set:
            _dict['printable_height_mm'] = None

        # set to None if printable_width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.printable_width_mm is None and "printable_width_mm" in self.model_fields_set:
            _dict['printable_width_mm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApparelDecorationOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "decoration_method": obj.get("decoration_method") if obj.get("decoration_method") is not None else 'unknown',
            "garment_colour": obj.get("garment_colour"),
            "garment_type": obj.get("garment_type"),
            "position": obj.get("position") if obj.get("position") is not None else 'unknown',
            "printable_height_mm": obj.get("printable_height_mm"),
            "printable_width_mm": obj.get("printable_width_mm"),
            "size_range": obj.get("size_range")
        })
        return _obj
