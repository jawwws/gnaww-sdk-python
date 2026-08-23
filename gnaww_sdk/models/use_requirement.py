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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UseRequirement(BaseModel):
    """
    Confirmed production-relevant use intent carried by GJS v0.4.
    """ # noqa: E501
    provenance: StrictStr
    requirement_key: Annotated[str, Field(strict=True)]
    source_expression: Optional[StrictStr] = None
    value: Annotated[str, Field(min_length=1, strict=True)]
    __properties: ClassVar[List[str]] = ["provenance", "requirement_key", "source_expression", "value"]

    @field_validator('provenance')
    def provenance_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['supplied', 'confirmed_review']):
            raise ValueError("must be one of enum values ('supplied', 'confirmed_review')")
        return value

    @field_validator('requirement_key')
    def requirement_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[a-z][a-z0-9_]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_]*$/")
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
        """Create an instance of UseRequirement from a JSON string"""
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
        # set to None if source_expression (nullable) is None
        # and model_fields_set contains the field
        if self.source_expression is None and "source_expression" in self.model_fields_set:
            _dict['source_expression'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UseRequirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "provenance": obj.get("provenance"),
            "requirement_key": obj.get("requirement_key"),
            "source_expression": obj.get("source_expression"),
            "value": obj.get("value")
        })
        return _obj
