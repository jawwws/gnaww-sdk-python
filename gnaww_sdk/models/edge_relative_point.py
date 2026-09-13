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

class EdgeRelativePoint(BaseModel):
    """
    Point positioned from one horizontal and one vertical component edge.
    """ # noqa: E501
    horizontal_edge: StrictStr
    horizontal_offset_mm: Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]
    vertical_edge: StrictStr
    vertical_offset_mm: Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]
    __properties: ClassVar[List[str]] = ["horizontal_edge", "horizontal_offset_mm", "vertical_edge", "vertical_offset_mm"]

    @field_validator('horizontal_edge')
    def horizontal_edge_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['left', 'right']):
            raise ValueError("must be one of enum values ('left', 'right')")
        return value

    @field_validator('vertical_edge')
    def vertical_edge_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['top', 'bottom']):
            raise ValueError("must be one of enum values ('top', 'bottom')")
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
        """Create an instance of EdgeRelativePoint from a JSON string"""
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
        """Create an instance of EdgeRelativePoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "horizontal_edge": obj.get("horizontal_edge"),
            "horizontal_offset_mm": obj.get("horizontal_offset_mm"),
            "vertical_edge": obj.get("vertical_edge"),
            "vertical_offset_mm": obj.get("vertical_offset_mm")
        })
        return _obj
