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

class VariationField(BaseModel):
    """
    VariationField
    """ # noqa: E501
    artwork_or_asset_ref: Optional[StrictStr] = None
    data_type: Optional[StrictStr] = 'unknown'
    field_key: Annotated[str, Field(strict=True)]
    __properties: ClassVar[List[str]] = ["artwork_or_asset_ref", "data_type", "field_key"]

    @field_validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['text', 'number', 'image', 'code', 'artwork', 'unknown']):
            raise ValueError("must be one of enum values ('text', 'number', 'image', 'code', 'artwork', 'unknown')")
        return value

    @field_validator('field_key')
    def field_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9][A-Za-z0-9_.:-]*$/")
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
        """Create an instance of VariationField from a JSON string"""
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
        # set to None if artwork_or_asset_ref (nullable) is None
        # and model_fields_set contains the field
        if self.artwork_or_asset_ref is None and "artwork_or_asset_ref" in self.model_fields_set:
            _dict['artwork_or_asset_ref'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VariationField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "artwork_or_asset_ref": obj.get("artwork_or_asset_ref"),
            "data_type": obj.get("data_type") if obj.get("data_type") is not None else 'unknown',
            "field_key": obj.get("field_key")
        })
        return _obj
