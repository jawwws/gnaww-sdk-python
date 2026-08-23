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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CustomDimensionCapability(BaseModel):
    """
    Supported limits for custom-sized production.
    """ # noqa: E501
    increments_mm: Optional[List[Union[StrictFloat, StrictInt]]] = None
    maximum_depth_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    maximum_diameter_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    maximum_height_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    maximum_width_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    minimum_depth_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    minimum_diameter_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    minimum_height_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    minimum_width_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    __properties: ClassVar[List[str]] = ["increments_mm", "maximum_depth_mm", "maximum_diameter_mm", "maximum_height_mm", "maximum_width_mm", "minimum_depth_mm", "minimum_diameter_mm", "minimum_height_mm", "minimum_width_mm"]

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
        """Create an instance of CustomDimensionCapability from a JSON string"""
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
        # set to None if maximum_depth_mm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_depth_mm is None and "maximum_depth_mm" in self.model_fields_set:
            _dict['maximum_depth_mm'] = None

        # set to None if maximum_diameter_mm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_diameter_mm is None and "maximum_diameter_mm" in self.model_fields_set:
            _dict['maximum_diameter_mm'] = None

        # set to None if maximum_height_mm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_height_mm is None and "maximum_height_mm" in self.model_fields_set:
            _dict['maximum_height_mm'] = None

        # set to None if maximum_width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_width_mm is None and "maximum_width_mm" in self.model_fields_set:
            _dict['maximum_width_mm'] = None

        # set to None if minimum_depth_mm (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_depth_mm is None and "minimum_depth_mm" in self.model_fields_set:
            _dict['minimum_depth_mm'] = None

        # set to None if minimum_diameter_mm (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_diameter_mm is None and "minimum_diameter_mm" in self.model_fields_set:
            _dict['minimum_diameter_mm'] = None

        # set to None if minimum_height_mm (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_height_mm is None and "minimum_height_mm" in self.model_fields_set:
            _dict['minimum_height_mm'] = None

        # set to None if minimum_width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_width_mm is None and "minimum_width_mm" in self.model_fields_set:
            _dict['minimum_width_mm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomDimensionCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "increments_mm": obj.get("increments_mm"),
            "maximum_depth_mm": obj.get("maximum_depth_mm"),
            "maximum_diameter_mm": obj.get("maximum_diameter_mm"),
            "maximum_height_mm": obj.get("maximum_height_mm"),
            "maximum_width_mm": obj.get("maximum_width_mm"),
            "minimum_depth_mm": obj.get("minimum_depth_mm"),
            "minimum_diameter_mm": obj.get("minimum_diameter_mm"),
            "minimum_height_mm": obj.get("minimum_height_mm"),
            "minimum_width_mm": obj.get("minimum_width_mm")
        })
        return _obj
