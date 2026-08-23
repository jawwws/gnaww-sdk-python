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

class PromotionalGoodsOptions(BaseModel):
    """
    Promotional-goods production and decoration options.
    """ # noqa: E501
    capacity_ml: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    decoration_diameter_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    decoration_height_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    decoration_method: Optional[StrictStr] = 'unknown'
    decoration_position: Optional[StrictStr] = 'unknown'
    decoration_width_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    packaging_type: Optional[StrictStr] = 'unknown'
    personalisation_required: Optional[StrictBool] = False
    product_colour: Optional[StrictStr] = None
    required_compliance_claims: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["capacity_ml", "decoration_diameter_mm", "decoration_height_mm", "decoration_method", "decoration_position", "decoration_width_mm", "packaging_type", "personalisation_required", "product_colour", "required_compliance_claims"]

    @field_validator('decoration_method')
    def decoration_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'unknown']):
            raise ValueError("must be one of enum values ('dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'unknown')")
        return value

    @field_validator('decoration_position')
    def decoration_position_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['front', 'back', 'left_chest', 'right_chest', 'sleeve', 'cap_front', 'left', 'right', 'wrap', 'barrel', 'lid', 'base', 'unknown']):
            raise ValueError("must be one of enum values ('front', 'back', 'left_chest', 'right_chest', 'sleeve', 'cap_front', 'left', 'right', 'wrap', 'barrel', 'lid', 'base', 'unknown')")
        return value

    @field_validator('packaging_type')
    def packaging_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['bulk', 'individual_bag', 'gift_box', 'retail_box', 'custom', 'unknown']):
            raise ValueError("must be one of enum values ('bulk', 'individual_bag', 'gift_box', 'retail_box', 'custom', 'unknown')")
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
        """Create an instance of PromotionalGoodsOptions from a JSON string"""
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
        # set to None if capacity_ml (nullable) is None
        # and model_fields_set contains the field
        if self.capacity_ml is None and "capacity_ml" in self.model_fields_set:
            _dict['capacity_ml'] = None

        # set to None if decoration_diameter_mm (nullable) is None
        # and model_fields_set contains the field
        if self.decoration_diameter_mm is None and "decoration_diameter_mm" in self.model_fields_set:
            _dict['decoration_diameter_mm'] = None

        # set to None if decoration_height_mm (nullable) is None
        # and model_fields_set contains the field
        if self.decoration_height_mm is None and "decoration_height_mm" in self.model_fields_set:
            _dict['decoration_height_mm'] = None

        # set to None if decoration_width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.decoration_width_mm is None and "decoration_width_mm" in self.model_fields_set:
            _dict['decoration_width_mm'] = None

        # set to None if product_colour (nullable) is None
        # and model_fields_set contains the field
        if self.product_colour is None and "product_colour" in self.model_fields_set:
            _dict['product_colour'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PromotionalGoodsOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capacity_ml": obj.get("capacity_ml"),
            "decoration_diameter_mm": obj.get("decoration_diameter_mm"),
            "decoration_height_mm": obj.get("decoration_height_mm"),
            "decoration_method": obj.get("decoration_method") if obj.get("decoration_method") is not None else 'unknown',
            "decoration_position": obj.get("decoration_position") if obj.get("decoration_position") is not None else 'unknown',
            "decoration_width_mm": obj.get("decoration_width_mm"),
            "packaging_type": obj.get("packaging_type") if obj.get("packaging_type") is not None else 'unknown',
            "personalisation_required": obj.get("personalisation_required") if obj.get("personalisation_required") is not None else False,
            "product_colour": obj.get("product_colour"),
            "required_compliance_claims": obj.get("required_compliance_claims")
        })
        return _obj
