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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GrammageRequirement(BaseModel):
    """
    Demand-side grammage target, range and substitution posture.
    """ # noqa: E501
    maximum_gsm: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    minimum_gsm: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    outcome: Optional[StrictStr] = None
    posture: Optional[StrictStr] = 'unspecified'
    source_expression: Optional[StrictStr] = None
    substitute_approval_required: Optional[StrictBool] = False
    target_gsm: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    __properties: ClassVar[List[str]] = ["maximum_gsm", "minimum_gsm", "outcome", "posture", "source_expression", "substitute_approval_required", "target_gsm"]

    @field_validator('posture')
    def posture_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['exact_required', 'preferred_target', 'acceptable_range', 'close_substitute_acceptable', 'producer_recommendation_acceptable', 'unspecified']):
            raise ValueError("must be one of enum values ('exact_required', 'preferred_target', 'acceptable_range', 'close_substitute_acceptable', 'producer_recommendation_acceptable', 'unspecified')")
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
        """Create an instance of GrammageRequirement from a JSON string"""
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
        # set to None if maximum_gsm (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_gsm is None and "maximum_gsm" in self.model_fields_set:
            _dict['maximum_gsm'] = None

        # set to None if minimum_gsm (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_gsm is None and "minimum_gsm" in self.model_fields_set:
            _dict['minimum_gsm'] = None

        # set to None if outcome (nullable) is None
        # and model_fields_set contains the field
        if self.outcome is None and "outcome" in self.model_fields_set:
            _dict['outcome'] = None

        # set to None if source_expression (nullable) is None
        # and model_fields_set contains the field
        if self.source_expression is None and "source_expression" in self.model_fields_set:
            _dict['source_expression'] = None

        # set to None if target_gsm (nullable) is None
        # and model_fields_set contains the field
        if self.target_gsm is None and "target_gsm" in self.model_fields_set:
            _dict['target_gsm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GrammageRequirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maximum_gsm": obj.get("maximum_gsm"),
            "minimum_gsm": obj.get("minimum_gsm"),
            "outcome": obj.get("outcome"),
            "posture": obj.get("posture") if obj.get("posture") is not None else 'unspecified',
            "source_expression": obj.get("source_expression"),
            "substitute_approval_required": obj.get("substitute_approval_required") if obj.get("substitute_approval_required") is not None else False,
            "target_gsm": obj.get("target_gsm")
        })
        return _obj
