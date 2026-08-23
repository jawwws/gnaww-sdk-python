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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.issue import Issue
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class IssueSet(BaseModel):
    """
    Grouped issues returned by Gnaww responses.
    """ # noqa: E501
    blockers: Optional[List[Issue]] = None
    info: Optional[List[Issue]] = None
    warnings: Optional[List[Issue]] = None
    __properties: ClassVar[List[str]] = ["blockers", "info", "warnings"]

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
        """Create an instance of IssueSet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in blockers (list)
        _items = []
        if self.blockers:
            for _item_blockers in self.blockers:
                if _item_blockers:
                    _items.append(_item_blockers.to_dict())
            _dict['blockers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in info (list)
        _items = []
        if self.info:
            for _item_info in self.info:
                if _item_info:
                    _items.append(_item_info.to_dict())
            _dict['info'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssueSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blockers": [Issue.from_dict(_item) for _item in obj["blockers"]] if obj.get("blockers") is not None else None,
            "info": [Issue.from_dict(_item) for _item in obj["info"]] if obj.get("info") is not None else None,
            "warnings": [Issue.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None
        })
        return _obj
