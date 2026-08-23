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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Issue(BaseModel):
    """
    A customer-safe issue raised during transformation or matching.
    """ # noqa: E501
    code: StrictStr
    var_field: Optional[StrictStr] = Field(default=None, alias="field")
    message: StrictStr
    severity: StrictStr
    source: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["code", "field", "message", "severity", "source"]

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['blocker', 'warning', 'info']):
            raise ValueError("must be one of enum values ('blocker', 'warning', 'info')")
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
        """Create an instance of Issue from a JSON string"""
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
        # set to None if var_field (nullable) is None
        # and model_fields_set contains the field
        if self.var_field is None and "var_field" in self.model_fields_set:
            _dict['field'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Issue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "field": obj.get("field"),
            "message": obj.get("message"),
            "severity": obj.get("severity"),
            "source": obj.get("source")
        })
        return _obj
