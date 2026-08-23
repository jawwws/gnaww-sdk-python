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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.finished_size import FinishedSize
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FoldedLeafletOptions(BaseModel):
    """
    Folded leaflet production options.
    """ # noqa: E501
    finished_size: Optional[FinishedSize] = None
    flat_size: Optional[FinishedSize] = None
    fold_pattern: Optional[StrictStr] = 'unknown'
    panels: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    __properties: ClassVar[List[str]] = ["finished_size", "flat_size", "fold_pattern", "panels"]

    @field_validator('fold_pattern')
    def fold_pattern_validate_enum(cls, value):
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
        """Create an instance of FoldedLeafletOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of finished_size
        if self.finished_size:
            _dict['finished_size'] = self.finished_size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flat_size
        if self.flat_size:
            _dict['flat_size'] = self.flat_size.to_dict()
        # set to None if panels (nullable) is None
        # and model_fields_set contains the field
        if self.panels is None and "panels" in self.model_fields_set:
            _dict['panels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FoldedLeafletOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "finished_size": FinishedSize.from_dict(obj["finished_size"]) if obj.get("finished_size") is not None else None,
            "flat_size": FinishedSize.from_dict(obj["flat_size"]) if obj.get("flat_size") is not None else None,
            "fold_pattern": obj.get("fold_pattern") if obj.get("fold_pattern") is not None else 'unknown',
            "panels": obj.get("panels")
        })
        return _obj
