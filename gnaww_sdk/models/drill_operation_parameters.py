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
from gnaww_sdk.models.drill_hole import DrillHole
from gnaww_sdk.models.repeated_drill_pattern import RepeatedDrillPattern
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DrillOperationParameters(BaseModel):
    """
    DrillOperationParameters
    """ # noqa: E501
    holes: Optional[List[DrillHole]] = None
    kind: Optional[StrictStr] = 'drill'
    patterns: Optional[List[RepeatedDrillPattern]] = None
    __properties: ClassVar[List[str]] = ["holes", "kind", "patterns"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['drill']):
            raise ValueError("must be one of enum values ('drill')")
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
        """Create an instance of DrillOperationParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in holes (list)
        _items = []
        if self.holes:
            for _item_holes in self.holes:
                if _item_holes:
                    _items.append(_item_holes.to_dict())
            _dict['holes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in patterns (list)
        _items = []
        if self.patterns:
            for _item_patterns in self.patterns:
                if _item_patterns:
                    _items.append(_item_patterns.to_dict())
            _dict['patterns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DrillOperationParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "holes": [DrillHole.from_dict(_item) for _item in obj["holes"]] if obj.get("holes") is not None else None,
            "kind": obj.get("kind") if obj.get("kind") is not None else 'drill',
            "patterns": [RepeatedDrillPattern.from_dict(_item) for _item in obj["patterns"]] if obj.get("patterns") is not None else None
        })
        return _obj
