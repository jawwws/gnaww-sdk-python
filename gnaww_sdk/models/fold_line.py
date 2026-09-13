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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.line2_d import Line2D
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FoldLine(BaseModel):
    """
    One fold line in the input component coordinate system.
    """ # noqa: E501
    axis: Optional[StrictStr] = None
    direction: Optional[StrictStr] = 'unknown'
    line: Line2D
    sequence: Annotated[int, Field(strict=True, gt=0)]
    __properties: ClassVar[List[str]] = ["axis", "direction", "line", "sequence"]

    @field_validator('axis')
    def axis_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['vertical', 'horizontal', 'custom']):
            raise ValueError("must be one of enum values ('vertical', 'horizontal', 'custom')")
        return value

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['valley', 'mountain', 'unknown']):
            raise ValueError("must be one of enum values ('valley', 'mountain', 'unknown')")
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
        """Create an instance of FoldLine from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of line
        if self.line:
            _dict['line'] = self.line.to_dict()
        # set to None if axis (nullable) is None
        # and model_fields_set contains the field
        if self.axis is None and "axis" in self.model_fields_set:
            _dict['axis'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FoldLine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "axis": obj.get("axis"),
            "direction": obj.get("direction") if obj.get("direction") is not None else 'unknown',
            "line": Line2D.from_dict(obj["line"]) if obj.get("line") is not None else None,
            "sequence": obj.get("sequence")
        })
        return _obj
