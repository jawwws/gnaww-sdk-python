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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class WashabilityCapability(BaseModel):
    """
    Supported fabric wash-care methods and limits.
    """ # noqa: E501
    maximum_temperature_c: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = None
    methods: Optional[List[StrictStr]] = None
    tumble_dry_supported: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["maximum_temperature_c", "methods", "tumble_dry_supported"]

    @field_validator('methods')
    def methods_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['machine_wash', 'hand_wash', 'dry_clean', 'not_washable', 'unknown']):
                raise ValueError("each list item must be one of ('machine_wash', 'hand_wash', 'dry_clean', 'not_washable', 'unknown')")
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
        """Create an instance of WashabilityCapability from a JSON string"""
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
        # set to None if maximum_temperature_c (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_temperature_c is None and "maximum_temperature_c" in self.model_fields_set:
            _dict['maximum_temperature_c'] = None

        # set to None if tumble_dry_supported (nullable) is None
        # and model_fields_set contains the field
        if self.tumble_dry_supported is None and "tumble_dry_supported" in self.model_fields_set:
            _dict['tumble_dry_supported'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WashabilityCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maximum_temperature_c": obj.get("maximum_temperature_c"),
            "methods": obj.get("methods"),
            "tumble_dry_supported": obj.get("tumble_dry_supported")
        })
        return _obj
