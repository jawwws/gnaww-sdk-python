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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ColourCapability(BaseModel):
    """
    Supported print colour capability.
    """ # noqa: E501
    maximum_spot_colours: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    modes: Annotated[List[StrictStr], Field(min_length=1)]
    supports_metallic_ink: Optional[StrictBool] = False
    supports_white_ink: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["maximum_spot_colours", "modes", "supports_metallic_ink", "supports_white_ink"]

    @field_validator('modes')
    def modes_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['mono', 'full_colour', 'spot', 'unknown']):
                raise ValueError("each list item must be one of ('mono', 'full_colour', 'spot', 'unknown')")
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
        """Create an instance of ColourCapability from a JSON string"""
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
        # set to None if maximum_spot_colours (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_spot_colours is None and "maximum_spot_colours" in self.model_fields_set:
            _dict['maximum_spot_colours'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ColourCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maximum_spot_colours": obj.get("maximum_spot_colours"),
            "modes": obj.get("modes"),
            "supports_metallic_ink": obj.get("supports_metallic_ink") if obj.get("supports_metallic_ink") is not None else False,
            "supports_white_ink": obj.get("supports_white_ink") if obj.get("supports_white_ink") is not None else False
        })
        return _obj
