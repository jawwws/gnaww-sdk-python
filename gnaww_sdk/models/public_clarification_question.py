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
from gnaww_sdk.models.public_clarification_option import PublicClarificationOption
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicClarificationQuestion(BaseModel):
    """
    One Gnaww-owned question needed to progress buyer demand.
    """ # noqa: E501
    current_value: Optional[StrictStr] = None
    field_path: Annotated[str, Field(min_length=1, strict=True)]
    input_type: Optional[StrictStr] = 'single_select'
    key: Annotated[str, Field(strict=True)]
    options: Optional[List[PublicClarificationOption]] = None
    question: Annotated[str, Field(min_length=1, strict=True)]
    rationale: Annotated[str, Field(min_length=1, strict=True)]
    required: Optional[StrictBool] = True
    source: StrictStr
    __properties: ClassVar[List[str]] = ["current_value", "field_path", "input_type", "key", "options", "question", "rationale", "required", "source"]

    @field_validator('input_type')
    def input_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['single_select', 'text', 'integer']):
            raise ValueError("must be one of enum values ('single_select', 'text', 'integer')")
        return value

    @field_validator('key')
    def key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[a-z][a-z0-9_.\[\]]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_.\[\]]*$/")
        return value

    @field_validator('required')
    def required_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['use_requirement', 'canonical_field', 'fulfilment_requirement']):
            raise ValueError("must be one of enum values ('use_requirement', 'canonical_field', 'fulfilment_requirement')")
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
        """Create an instance of PublicClarificationQuestion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict['options'] = _items
        # set to None if current_value (nullable) is None
        # and model_fields_set contains the field
        if self.current_value is None and "current_value" in self.model_fields_set:
            _dict['current_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicClarificationQuestion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current_value": obj.get("current_value"),
            "field_path": obj.get("field_path"),
            "input_type": obj.get("input_type") if obj.get("input_type") is not None else 'single_select',
            "key": obj.get("key"),
            "options": [PublicClarificationOption.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None,
            "question": obj.get("question"),
            "rationale": obj.get("rationale"),
            "required": obj.get("required") if obj.get("required") is not None else True,
            "source": obj.get("source")
        })
        return _obj
