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
from gnaww_sdk.models.manufacturing_region_geometry import ManufacturingRegionGeometry
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ManufacturingRegion(BaseModel):
    """
    Addressable production target within one component.
    """ # noqa: E501
    edge: Optional[StrictStr] = None
    face: Optional[StrictStr] = None
    geometry: Optional[ManufacturingRegionGeometry] = None
    kind: StrictStr
    name: Optional[StrictStr] = None
    region_id: Annotated[str, Field(strict=True)]
    __properties: ClassVar[List[str]] = ["edge", "face", "geometry", "kind", "name", "region_id"]

    @field_validator('face')
    def face_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['front', 'back', 'top', 'bottom', 'left', 'right', 'inside', 'outside']):
            raise ValueError("must be one of enum values ('front', 'back', 'top', 'bottom', 'left', 'right', 'inside', 'outside')")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['face', 'edge', 'area', 'path', 'named']):
            raise ValueError("must be one of enum values ('face', 'edge', 'area', 'path', 'named')")
        return value

    @field_validator('region_id')
    def region_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9][A-Za-z0-9_.:-]*$/")
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
        """Create an instance of ManufacturingRegion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of geometry
        if self.geometry:
            _dict['geometry'] = self.geometry.to_dict()
        # set to None if edge (nullable) is None
        # and model_fields_set contains the field
        if self.edge is None and "edge" in self.model_fields_set:
            _dict['edge'] = None

        # set to None if face (nullable) is None
        # and model_fields_set contains the field
        if self.face is None and "face" in self.model_fields_set:
            _dict['face'] = None

        # set to None if geometry (nullable) is None
        # and model_fields_set contains the field
        if self.geometry is None and "geometry" in self.model_fields_set:
            _dict['geometry'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManufacturingRegion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edge": obj.get("edge"),
            "face": obj.get("face"),
            "geometry": ManufacturingRegionGeometry.from_dict(obj["geometry"]) if obj.get("geometry") is not None else None,
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "region_id": obj.get("region_id")
        })
        return _obj
