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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SourceInput(BaseModel):
    """
    Original requirement data submitted to Gnaww.
    """ # noqa: E501
    data: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    raw_text: Optional[StrictStr] = None
    reference: Optional[StrictStr] = None
    source_system: Optional[StrictStr] = None
    type: StrictStr
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["data", "metadata", "raw_text", "reference", "source_system", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['natural_language', 'structured_json', 'email', 'csv_row', 'storefront_product']):
            raise ValueError("must be one of enum values ('natural_language', 'structured_json', 'email', 'csv_row', 'storefront_product')")
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
        """Create an instance of SourceInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if raw_text (nullable) is None
        # and model_fields_set contains the field
        if self.raw_text is None and "raw_text" in self.model_fields_set:
            _dict['raw_text'] = None

        # set to None if reference (nullable) is None
        # and model_fields_set contains the field
        if self.reference is None and "reference" in self.model_fields_set:
            _dict['reference'] = None

        # set to None if source_system (nullable) is None
        # and model_fields_set contains the field
        if self.source_system is None and "source_system" in self.model_fields_set:
            _dict['source_system'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": obj.get("data"),
            "metadata": obj.get("metadata"),
            "raw_text": obj.get("raw_text"),
            "reference": obj.get("reference"),
            "source_system": obj.get("source_system"),
            "type": obj.get("type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
