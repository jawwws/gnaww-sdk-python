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
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Finishing(BaseModel):
    """
    A requested finishing operation.
    """ # noqa: E501
    category: Optional[StrictStr] = 'unknown'
    name: StrictStr
    notes: Optional[StrictStr] = None
    process: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["category", "name", "notes", "process"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['folding', 'lamination', 'binding', 'cutting', 'drilling', 'perforation', 'creasing', 'stitching', 'foiling', 'spot_uv', 'die_cutting', 'embossing', 'debossing', 'corner_rounding', 'packaging', 'other', 'unknown']):
            raise ValueError("must be one of enum values ('folding', 'lamination', 'binding', 'cutting', 'drilling', 'perforation', 'creasing', 'stitching', 'foiling', 'spot_uv', 'die_cutting', 'embossing', 'debossing', 'corner_rounding', 'packaging', 'other', 'unknown')")
        return value

    @field_validator('process')
    def process_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown']):
            raise ValueError("must be one of enum values ('digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown')")
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
        """Create an instance of Finishing from a JSON string"""
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
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if process (nullable) is None
        # and model_fields_set contains the field
        if self.process is None and "process" in self.model_fields_set:
            _dict['process'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Finishing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category") if obj.get("category") is not None else 'unknown',
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "process": obj.get("process")
        })
        return _obj
