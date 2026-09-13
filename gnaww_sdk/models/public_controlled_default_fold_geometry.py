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
from typing import Any, ClassVar, Dict, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicControlledDefaultFoldGeometry(BaseModel):
    """
    Customer-safe geometry for one controlled folding assumption.
    """ # noqa: E501
    fold_axis: StrictStr
    fold_position_mm: Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]
    input_height_mm: Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]
    input_orientation: StrictStr
    input_standard_name: StrictStr
    input_width_mm: Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]
    resulting_height_mm: Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]
    resulting_orientation: StrictStr
    resulting_standard_name: StrictStr
    resulting_width_mm: Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]
    __properties: ClassVar[List[str]] = ["fold_axis", "fold_position_mm", "input_height_mm", "input_orientation", "input_standard_name", "input_width_mm", "resulting_height_mm", "resulting_orientation", "resulting_standard_name", "resulting_width_mm"]

    @field_validator('fold_axis')
    def fold_axis_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['vertical', 'horizontal', 'custom']):
            raise ValueError("must be one of enum values ('vertical', 'horizontal', 'custom')")
        return value

    @field_validator('input_orientation')
    def input_orientation_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['portrait', 'landscape']):
            raise ValueError("must be one of enum values ('portrait', 'landscape')")
        return value

    @field_validator('resulting_orientation')
    def resulting_orientation_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['portrait', 'landscape']):
            raise ValueError("must be one of enum values ('portrait', 'landscape')")
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
        """Create an instance of PublicControlledDefaultFoldGeometry from a JSON string"""
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
        """Create an instance of PublicControlledDefaultFoldGeometry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fold_axis": obj.get("fold_axis"),
            "fold_position_mm": obj.get("fold_position_mm"),
            "input_height_mm": obj.get("input_height_mm"),
            "input_orientation": obj.get("input_orientation"),
            "input_standard_name": obj.get("input_standard_name"),
            "input_width_mm": obj.get("input_width_mm"),
            "resulting_height_mm": obj.get("resulting_height_mm"),
            "resulting_orientation": obj.get("resulting_orientation"),
            "resulting_standard_name": obj.get("resulting_standard_name"),
            "resulting_width_mm": obj.get("resulting_width_mm")
        })
        return _obj
