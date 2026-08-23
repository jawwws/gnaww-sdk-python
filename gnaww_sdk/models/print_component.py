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
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.finished_size import FinishedSize
from gnaww_sdk.models.finishing import Finishing
from gnaww_sdk.models.print_spec import PrintSpec
from gnaww_sdk.models.substrate import Substrate
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PrintComponent(BaseModel):
    """
    Single printable component of a canonical job.
    """ # noqa: E501
    component_id: Optional[StrictStr] = 'main'
    finishings: Optional[List[Finishing]] = None
    print_spec: Optional[PrintSpec] = None
    role: Optional[StrictStr] = 'main'
    size: Optional[FinishedSize] = None
    substrate: Optional[Substrate] = None
    __properties: ClassVar[List[str]] = ["component_id", "finishings", "print_spec", "role", "size", "substrate"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown']):
            raise ValueError("must be one of enum values ('main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown')")
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
        """Create an instance of PrintComponent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in finishings (list)
        _items = []
        if self.finishings:
            for _item_finishings in self.finishings:
                if _item_finishings:
                    _items.append(_item_finishings.to_dict())
            _dict['finishings'] = _items
        # override the default output from pydantic by calling `to_dict()` of print_spec
        if self.print_spec:
            _dict['print_spec'] = self.print_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of size
        if self.size:
            _dict['size'] = self.size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of substrate
        if self.substrate:
            _dict['substrate'] = self.substrate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrintComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "component_id": obj.get("component_id") if obj.get("component_id") is not None else 'main',
            "finishings": [Finishing.from_dict(_item) for _item in obj["finishings"]] if obj.get("finishings") is not None else None,
            "print_spec": PrintSpec.from_dict(obj["print_spec"]) if obj.get("print_spec") is not None else None,
            "role": obj.get("role") if obj.get("role") is not None else 'main',
            "size": FinishedSize.from_dict(obj["size"]) if obj.get("size") is not None else None,
            "substrate": Substrate.from_dict(obj["substrate"]) if obj.get("substrate") is not None else None
        })
        return _obj
