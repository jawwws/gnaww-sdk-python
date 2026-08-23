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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DeliveryDestination(BaseModel):
    """
    Destination information relevant to capability-level routing.
    """ # noqa: E501
    address_text: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=500)]] = None
    country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2)]
    locality: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=120)]] = None
    postal_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=32)]] = None
    region: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=120)]] = None
    __properties: ClassVar[List[str]] = ["address_text", "country_code", "locality", "postal_code", "region"]

    @field_validator('country_code')
    def country_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[A-Za-z]{2}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z]{2}$/")
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
        """Create an instance of DeliveryDestination from a JSON string"""
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
        # set to None if address_text (nullable) is None
        # and model_fields_set contains the field
        if self.address_text is None and "address_text" in self.model_fields_set:
            _dict['address_text'] = None

        # set to None if locality (nullable) is None
        # and model_fields_set contains the field
        if self.locality is None and "locality" in self.model_fields_set:
            _dict['locality'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postal_code'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeliveryDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address_text": obj.get("address_text"),
            "country_code": obj.get("country_code"),
            "locality": obj.get("locality"),
            "postal_code": obj.get("postal_code"),
            "region": obj.get("region")
        })
        return _obj
