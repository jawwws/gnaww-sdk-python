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

class PublicUseConditionReview(BaseModel):
    """
    One controlled product-use question or grounded semantic proposal.
    """ # noqa: E501
    allowed_values: Annotated[List[StrictStr], Field(min_length=1)]
    condition_key: Annotated[str, Field(strict=True)]
    proposed_value: Optional[StrictStr] = None
    question: Annotated[str, Field(min_length=1, strict=True)]
    rationale: Annotated[str, Field(min_length=1, strict=True)]
    requires_confirmation: Optional[StrictBool] = True
    source_expression: Optional[StrictStr] = None
    truth_state: StrictStr
    __properties: ClassVar[List[str]] = ["allowed_values", "condition_key", "proposed_value", "question", "rationale", "requires_confirmation", "source_expression", "truth_state"]

    @field_validator('condition_key')
    def condition_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[a-z][a-z0-9_]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_]*$/")
        return value

    @field_validator('requires_confirmation')
    def requires_confirmation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('truth_state')
    def truth_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['semantically_proposed', 'unresolved']):
            raise ValueError("must be one of enum values ('semantically_proposed', 'unresolved')")
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
        """Create an instance of PublicUseConditionReview from a JSON string"""
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
        # set to None if proposed_value (nullable) is None
        # and model_fields_set contains the field
        if self.proposed_value is None and "proposed_value" in self.model_fields_set:
            _dict['proposed_value'] = None

        # set to None if source_expression (nullable) is None
        # and model_fields_set contains the field
        if self.source_expression is None and "source_expression" in self.model_fields_set:
            _dict['source_expression'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicUseConditionReview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_values": obj.get("allowed_values"),
            "condition_key": obj.get("condition_key"),
            "proposed_value": obj.get("proposed_value"),
            "question": obj.get("question"),
            "rationale": obj.get("rationale"),
            "requires_confirmation": obj.get("requires_confirmation") if obj.get("requires_confirmation") is not None else True,
            "source_expression": obj.get("source_expression"),
            "truth_state": obj.get("truth_state")
        })
        return _obj
