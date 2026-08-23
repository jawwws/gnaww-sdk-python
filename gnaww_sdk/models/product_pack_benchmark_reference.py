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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProductPackBenchmarkReference(BaseModel):
    """
    Validated benchmark evidence attached by Gnaww.
    """ # noqa: E501
    benchmark_id: Annotated[str, Field(strict=True)]
    benchmark_version: Annotated[str, Field(strict=True)]
    evidence_notes: Annotated[List[StrictStr], Field(min_length=1)]
    evidence_status: StrictStr
    matched_signals: Optional[List[StrictStr]] = None
    score: Annotated[int, Field(strict=True, ge=0)]
    summary: Annotated[str, Field(min_length=1, strict=True)]
    title: Annotated[str, Field(min_length=1, strict=True)]
    __properties: ClassVar[List[str]] = ["benchmark_id", "benchmark_version", "evidence_notes", "evidence_status", "matched_signals", "score", "summary", "title"]

    @field_validator('benchmark_id')
    def benchmark_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^benchmark-[a-z0-9-]+$", value):
            raise ValueError(r"must validate the regular expression /^benchmark-[a-z0-9-]+$/")
        return value

    @field_validator('benchmark_version')
    def benchmark_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[0-9]+\.[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]+\.[0-9]+$/")
        return value

    @field_validator('evidence_status')
    def evidence_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['curated_baseline', 'observed_intent', 'confirmed_outcome', 'empirical']):
            raise ValueError("must be one of enum values ('curated_baseline', 'observed_intent', 'confirmed_outcome', 'empirical')")
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
        """Create an instance of ProductPackBenchmarkReference from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductPackBenchmarkReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "benchmark_id": obj.get("benchmark_id"),
            "benchmark_version": obj.get("benchmark_version"),
            "evidence_notes": obj.get("evidence_notes"),
            "evidence_status": obj.get("evidence_status"),
            "matched_signals": obj.get("matched_signals"),
            "score": obj.get("score"),
            "summary": obj.get("summary"),
            "title": obj.get("title")
        })
        return _obj
