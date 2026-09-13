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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from gnaww_sdk.models.contour import Contour
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CutOperationParameters(BaseModel):
    """
    CutOperationParameters
    """ # noqa: E501
    contour: Optional[Contour] = None
    corner_radius_mm: Optional[Union[Annotated[float, Field(strict=True, gt=0.0)], Annotated[int, Field(strict=True, gt=0)]]] = None
    corners: Optional[List[StrictStr]] = None
    kind: Optional[StrictStr] = 'cut'
    method: StrictStr
    __properties: ClassVar[List[str]] = ["contour", "corner_radius_mm", "corners", "kind", "method"]

    @field_validator('corners')
    def corners_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['top_left', 'top_right', 'bottom_left', 'bottom_right']):
                raise ValueError("each list item must be one of ('top_left', 'top_right', 'bottom_left', 'bottom_right')")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['cut']):
            raise ValueError("must be one of enum values ('cut')")
        return value

    @field_validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['trim', 'guillotine', 'corner_round', 'die_cut', 'kiss_cut', 'laser_cut', 'aperture', 'contour', 'custom']):
            raise ValueError("must be one of enum values ('trim', 'guillotine', 'corner_round', 'die_cut', 'kiss_cut', 'laser_cut', 'aperture', 'contour', 'custom')")
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
        """Create an instance of CutOperationParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contour
        if self.contour:
            _dict['contour'] = self.contour.to_dict()
        # set to None if contour (nullable) is None
        # and model_fields_set contains the field
        if self.contour is None and "contour" in self.model_fields_set:
            _dict['contour'] = None

        # set to None if corner_radius_mm (nullable) is None
        # and model_fields_set contains the field
        if self.corner_radius_mm is None and "corner_radius_mm" in self.model_fields_set:
            _dict['corner_radius_mm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CutOperationParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contour": Contour.from_dict(obj["contour"]) if obj.get("contour") is not None else None,
            "corner_radius_mm": obj.get("corner_radius_mm"),
            "corners": obj.get("corners"),
            "kind": obj.get("kind") if obj.get("kind") is not None else 'cut',
            "method": obj.get("method")
        })
        return _obj
