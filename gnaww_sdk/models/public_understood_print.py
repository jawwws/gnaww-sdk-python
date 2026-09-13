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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicUnderstoodPrint(BaseModel):
    """
    Deterministically understood print-process evidence before canonical completion.
    """ # noqa: E501
    colour: Optional[StrictStr] = None
    processes: Optional[List[StrictStr]] = None
    sides: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["colour", "processes", "sides"]

    @field_validator('colour')
    def colour_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['mono', 'full_colour', 'spot', 'unknown']):
            raise ValueError("must be one of enum values ('mono', 'full_colour', 'spot', 'unknown')")
        return value

    @field_validator('processes')
    def processes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown']):
                raise ValueError("each list item must be one of ('digital_print', 'offset_litho', 'large_format', 'dtg', 'dtf', 'htv', 'embroidery', 'screen_print', 'sublimation', 'digital_textile_print', 'reactive_dye_print', 'pigment_print', 'sewing', 'hemming', 'pad_print', 'uv_print', 'engraving', 'laser_engraving', 'cutting', 'folding', 'binding', 'lamination', 'foiling', 'spot_uv', 'unknown')")
        return value

    @field_validator('sides')
    def sides_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['single_sided', 'double_sided', 'unknown']):
            raise ValueError("must be one of enum values ('single_sided', 'double_sided', 'unknown')")
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
        """Create an instance of PublicUnderstoodPrint from a JSON string"""
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
        # set to None if colour (nullable) is None
        # and model_fields_set contains the field
        if self.colour is None and "colour" in self.model_fields_set:
            _dict['colour'] = None

        # set to None if sides (nullable) is None
        # and model_fields_set contains the field
        if self.sides is None and "sides" in self.model_fields_set:
            _dict['sides'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicUnderstoodPrint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "colour": obj.get("colour"),
            "processes": obj.get("processes"),
            "sides": obj.get("sides")
        })
        return _obj
