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
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MatchDifference(BaseModel):
    """
    A customer-safe difference between requested and matched capability.
    """ # noqa: E501
    var_field: StrictStr = Field(alias="field")
    offered: Optional[Any] = None
    reason: StrictStr
    requested: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["field", "offered", "reason", "requested"]

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
        """Create an instance of MatchDifference from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of offered
        if self.offered:
            _dict['offered'] = self.offered.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested
        if self.requested:
            _dict['requested'] = self.requested.to_dict()
        # set to None if offered (nullable) is None
        # and model_fields_set contains the field
        if self.offered is None and "offered" in self.model_fields_set:
            _dict['offered'] = None

        # set to None if requested (nullable) is None
        # and model_fields_set contains the field
        if self.requested is None and "requested" in self.model_fields_set:
            _dict['requested'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchDifference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "field": obj.get("field"),
            "offered": AnyOf.from_dict(obj["offered"]) if obj.get("offered") is not None else None,
            "reason": obj.get("reason"),
            "requested": AnyOf.from_dict(obj["requested"]) if obj.get("requested") is not None else None
        })
        return _obj
