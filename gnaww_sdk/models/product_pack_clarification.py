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

class ProductPackClarification(BaseModel):
    """
    One focused question attached to a product pack.
    """ # noqa: E501
    benchmark_id: Optional[StrictStr] = None
    benchmark_version: Optional[StrictStr] = None
    clarification_key: Annotated[str, Field(min_length=1, strict=True)]
    evidence_status: StrictStr
    options: Optional[List[StrictStr]] = None
    question: Annotated[str, Field(min_length=1, strict=True)]
    rationale: Annotated[str, Field(min_length=1, strict=True)]
    required: Optional[StrictBool] = True
    source: StrictStr
    __properties: ClassVar[List[str]] = ["benchmark_id", "benchmark_version", "clarification_key", "evidence_status", "options", "question", "rationale", "required", "source"]

    @field_validator('evidence_status')
    def evidence_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['curated_baseline', 'observed_intent', 'confirmed_outcome', 'empirical', 'general_model_knowledge']):
            raise ValueError("must be one of enum values ('curated_baseline', 'observed_intent', 'confirmed_outcome', 'empirical', 'general_model_knowledge')")
        return value

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['benchmark', 'general_model_knowledge']):
            raise ValueError("must be one of enum values ('benchmark', 'general_model_knowledge')")
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
        """Create an instance of ProductPackClarification from a JSON string"""
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
        # set to None if benchmark_id (nullable) is None
        # and model_fields_set contains the field
        if self.benchmark_id is None and "benchmark_id" in self.model_fields_set:
            _dict['benchmark_id'] = None

        # set to None if benchmark_version (nullable) is None
        # and model_fields_set contains the field
        if self.benchmark_version is None and "benchmark_version" in self.model_fields_set:
            _dict['benchmark_version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductPackClarification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "benchmark_id": obj.get("benchmark_id"),
            "benchmark_version": obj.get("benchmark_version"),
            "clarification_key": obj.get("clarification_key"),
            "evidence_status": obj.get("evidence_status"),
            "options": obj.get("options"),
            "question": obj.get("question"),
            "rationale": obj.get("rationale"),
            "required": obj.get("required") if obj.get("required") is not None else True,
            "source": obj.get("source")
        })
        return _obj
