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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class BenchmarkQuantityGuidance(BaseModel):
    """
    Non-binding quantity guidance requiring customer confirmation.
    """ # noqa: E501
    basis: Annotated[str, Field(min_length=1, strict=True)]
    lower: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    requires_confirmation: Optional[StrictBool] = True
    typical: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    upper: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    __properties: ClassVar[List[str]] = ["basis", "lower", "requires_confirmation", "typical", "upper"]

    @field_validator('requires_confirmation')
    def requires_confirmation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
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
        """Create an instance of BenchmarkQuantityGuidance from a JSON string"""
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
        # set to None if lower (nullable) is None
        # and model_fields_set contains the field
        if self.lower is None and "lower" in self.model_fields_set:
            _dict['lower'] = None

        # set to None if typical (nullable) is None
        # and model_fields_set contains the field
        if self.typical is None and "typical" in self.model_fields_set:
            _dict['typical'] = None

        # set to None if upper (nullable) is None
        # and model_fields_set contains the field
        if self.upper is None and "upper" in self.model_fields_set:
            _dict['upper'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BenchmarkQuantityGuidance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "basis": obj.get("basis"),
            "lower": obj.get("lower"),
            "requires_confirmation": obj.get("requires_confirmation") if obj.get("requires_confirmation") is not None else True,
            "typical": obj.get("typical"),
            "upper": obj.get("upper")
        })
        return _obj
