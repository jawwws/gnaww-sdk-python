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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.dimension_capability import DimensionCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProducerFoldedLeafletOptions(BaseModel):
    """
    Supported folded leaflet options for a producer product.
    """ # noqa: E501
    finished_sizes: Optional[List[DimensionCapability]] = None
    flat_sizes: Optional[List[DimensionCapability]] = None
    fold_patterns: Optional[List[StrictStr]] = None
    panel_counts: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["finished_sizes", "flat_sizes", "fold_patterns", "panel_counts"]

    @field_validator('fold_patterns')
    def fold_patterns_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['half_fold', 'tri_fold', 'z_fold', 'gate_fold', 'roll_fold', 'cross_fold', 'unknown']):
                raise ValueError("each list item must be one of ('half_fold', 'tri_fold', 'z_fold', 'gate_fold', 'roll_fold', 'cross_fold', 'unknown')")
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
        """Create an instance of ProducerFoldedLeafletOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in finished_sizes (list)
        _items = []
        if self.finished_sizes:
            for _item_finished_sizes in self.finished_sizes:
                if _item_finished_sizes:
                    _items.append(_item_finished_sizes.to_dict())
            _dict['finished_sizes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in flat_sizes (list)
        _items = []
        if self.flat_sizes:
            for _item_flat_sizes in self.flat_sizes:
                if _item_flat_sizes:
                    _items.append(_item_flat_sizes.to_dict())
            _dict['flat_sizes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProducerFoldedLeafletOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "finished_sizes": [DimensionCapability.from_dict(_item) for _item in obj["finished_sizes"]] if obj.get("finished_sizes") is not None else None,
            "flat_sizes": [DimensionCapability.from_dict(_item) for _item in obj["flat_sizes"]] if obj.get("flat_sizes") is not None else None,
            "fold_patterns": obj.get("fold_patterns"),
            "panel_counts": obj.get("panel_counts")
        })
        return _obj
