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
from gnaww_sdk.models.dimension_capability import DimensionCapability
from gnaww_sdk.models.material_capability import MaterialCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProducerComponentCapability(BaseModel):
    """
    Optional component-level capability for multi-component products.
    """ # noqa: E501
    role: StrictStr
    sides: Optional[List[StrictStr]] = None
    sizes: Optional[List[DimensionCapability]] = None
    substrates: Optional[List[MaterialCapability]] = None
    __properties: ClassVar[List[str]] = ["role", "sides", "sizes", "substrates"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown']):
            raise ValueError("must be one of enum values ('main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown')")
        return value

    @field_validator('sides')
    def sides_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['single_sided', 'double_sided', 'unknown']):
                raise ValueError("each list item must be one of ('single_sided', 'double_sided', 'unknown')")
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
        """Create an instance of ProducerComponentCapability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sizes (list)
        _items = []
        if self.sizes:
            for _item_sizes in self.sizes:
                if _item_sizes:
                    _items.append(_item_sizes.to_dict())
            _dict['sizes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in substrates (list)
        _items = []
        if self.substrates:
            for _item_substrates in self.substrates:
                if _item_substrates:
                    _items.append(_item_substrates.to_dict())
            _dict['substrates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProducerComponentCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "role": obj.get("role"),
            "sides": obj.get("sides"),
            "sizes": [DimensionCapability.from_dict(_item) for _item in obj["sizes"]] if obj.get("sizes") is not None else None,
            "substrates": [MaterialCapability.from_dict(_item) for _item in obj["substrates"]] if obj.get("substrates") is not None else None
        })
        return _obj
