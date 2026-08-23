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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DimensionCapability(BaseModel):
    """
    An exact standard or named physical dimension capability.
    """ # noqa: E501
    depth_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    diameter_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    height_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    standard_name: Optional[StrictStr] = None
    width_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    __properties: ClassVar[List[str]] = ["depth_mm", "diameter_mm", "height_mm", "standard_name", "width_mm"]

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
        """Create an instance of DimensionCapability from a JSON string"""
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
        # set to None if depth_mm (nullable) is None
        # and model_fields_set contains the field
        if self.depth_mm is None and "depth_mm" in self.model_fields_set:
            _dict['depth_mm'] = None

        # set to None if diameter_mm (nullable) is None
        # and model_fields_set contains the field
        if self.diameter_mm is None and "diameter_mm" in self.model_fields_set:
            _dict['diameter_mm'] = None

        # set to None if height_mm (nullable) is None
        # and model_fields_set contains the field
        if self.height_mm is None and "height_mm" in self.model_fields_set:
            _dict['height_mm'] = None

        # set to None if standard_name (nullable) is None
        # and model_fields_set contains the field
        if self.standard_name is None and "standard_name" in self.model_fields_set:
            _dict['standard_name'] = None

        # set to None if width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.width_mm is None and "width_mm" in self.model_fields_set:
            _dict['width_mm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DimensionCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "depth_mm": obj.get("depth_mm"),
            "diameter_mm": obj.get("diameter_mm"),
            "height_mm": obj.get("height_mm"),
            "standard_name": obj.get("standard_name"),
            "width_mm": obj.get("width_mm")
        })
        return _obj
