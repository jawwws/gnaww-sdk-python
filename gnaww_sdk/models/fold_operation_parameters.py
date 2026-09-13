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
from gnaww_sdk.models.fold_line import FoldLine
from gnaww_sdk.models.fold_panel import FoldPanel
from gnaww_sdk.models.manufacturing_geometry import ManufacturingGeometry
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FoldOperationParameters(BaseModel):
    """
    FoldOperationParameters
    """ # noqa: E501
    basis: StrictStr
    fold_lines: Optional[List[FoldLine]] = None
    input_geometry: Optional[ManufacturingGeometry] = None
    kind: Optional[StrictStr] = 'fold'
    named_pattern: Optional[StrictStr] = None
    physical_panels: Optional[List[FoldPanel]] = None
    resulting_geometry: Optional[ManufacturingGeometry] = None
    __properties: ClassVar[List[str]] = ["basis", "fold_lines", "input_geometry", "kind", "named_pattern", "physical_panels", "resulting_geometry"]

    @field_validator('basis')
    def basis_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['unresolved', 'explicit_lines', 'named_pattern', 'legacy_input_output']):
            raise ValueError("must be one of enum values ('unresolved', 'explicit_lines', 'named_pattern', 'legacy_input_output')")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['fold']):
            raise ValueError("must be one of enum values ('fold')")
        return value

    @field_validator('named_pattern')
    def named_pattern_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['half_fold', 'tri_fold', 'z_fold', 'gate_fold', 'roll_fold', 'cross_fold', 'unknown']):
            raise ValueError("must be one of enum values ('half_fold', 'tri_fold', 'z_fold', 'gate_fold', 'roll_fold', 'cross_fold', 'unknown')")
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
        """Create an instance of FoldOperationParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fold_lines (list)
        _items = []
        if self.fold_lines:
            for _item_fold_lines in self.fold_lines:
                if _item_fold_lines:
                    _items.append(_item_fold_lines.to_dict())
            _dict['fold_lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of input_geometry
        if self.input_geometry:
            _dict['input_geometry'] = self.input_geometry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in physical_panels (list)
        _items = []
        if self.physical_panels:
            for _item_physical_panels in self.physical_panels:
                if _item_physical_panels:
                    _items.append(_item_physical_panels.to_dict())
            _dict['physical_panels'] = _items
        # override the default output from pydantic by calling `to_dict()` of resulting_geometry
        if self.resulting_geometry:
            _dict['resulting_geometry'] = self.resulting_geometry.to_dict()
        # set to None if input_geometry (nullable) is None
        # and model_fields_set contains the field
        if self.input_geometry is None and "input_geometry" in self.model_fields_set:
            _dict['input_geometry'] = None

        # set to None if named_pattern (nullable) is None
        # and model_fields_set contains the field
        if self.named_pattern is None and "named_pattern" in self.model_fields_set:
            _dict['named_pattern'] = None

        # set to None if resulting_geometry (nullable) is None
        # and model_fields_set contains the field
        if self.resulting_geometry is None and "resulting_geometry" in self.model_fields_set:
            _dict['resulting_geometry'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FoldOperationParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "basis": obj.get("basis"),
            "fold_lines": [FoldLine.from_dict(_item) for _item in obj["fold_lines"]] if obj.get("fold_lines") is not None else None,
            "input_geometry": ManufacturingGeometry.from_dict(obj["input_geometry"]) if obj.get("input_geometry") is not None else None,
            "kind": obj.get("kind") if obj.get("kind") is not None else 'fold',
            "named_pattern": obj.get("named_pattern"),
            "physical_panels": [FoldPanel.from_dict(_item) for _item in obj["physical_panels"]] if obj.get("physical_panels") is not None else None,
            "resulting_geometry": ManufacturingGeometry.from_dict(obj["resulting_geometry"]) if obj.get("resulting_geometry") is not None else None
        })
        return _obj
