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
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from gnaww_sdk.models.fulfilment_match_result import FulfilmentMatchResult
from gnaww_sdk.models.spec_match_result import SpecMatchResult
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicProducerUniverseCandidate(BaseModel):
    """
    Safe ranked producer result with explicit capability truth.
    """ # noqa: E501
    fulfilment: FulfilmentMatchResult
    is_live_supplier: StrictBool
    match: SpecMatchResult
    producer_id: Annotated[str, Field(min_length=1, strict=True)]
    producer_name: Annotated[str, Field(min_length=1, strict=True)]
    producer_profile_id: Annotated[str, Field(min_length=1, strict=True)]
    producer_profile_schema_version: Annotated[str, Field(min_length=1, strict=True)]
    rank: Annotated[int, Field(strict=True, ge=1)]
    source: StrictStr
    status: StrictStr
    truth_state: StrictStr
    __properties: ClassVar[List[str]] = ["fulfilment", "is_live_supplier", "match", "producer_id", "producer_name", "producer_profile_id", "producer_profile_schema_version", "rank", "source", "status", "truth_state"]

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['published_profile', 'demo_fixture']):
            raise ValueError("must be one of enum values ('published_profile', 'demo_fixture')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['capable', 'needs_review', 'blocked']):
            raise ValueError("must be one of enum values ('capable', 'needs_review', 'blocked')")
        return value

    @field_validator('truth_state')
    def truth_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['published_capability', 'fixture_backed']):
            raise ValueError("must be one of enum values ('published_capability', 'fixture_backed')")
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
        """Create an instance of PublicProducerUniverseCandidate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fulfilment
        if self.fulfilment:
            _dict['fulfilment'] = self.fulfilment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of match
        if self.match:
            _dict['match'] = self.match.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicProducerUniverseCandidate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fulfilment": FulfilmentMatchResult.from_dict(obj["fulfilment"]) if obj.get("fulfilment") is not None else None,
            "is_live_supplier": obj.get("is_live_supplier"),
            "match": SpecMatchResult.from_dict(obj["match"]) if obj.get("match") is not None else None,
            "producer_id": obj.get("producer_id"),
            "producer_name": obj.get("producer_name"),
            "producer_profile_id": obj.get("producer_profile_id"),
            "producer_profile_schema_version": obj.get("producer_profile_schema_version"),
            "rank": obj.get("rank"),
            "source": obj.get("source"),
            "status": obj.get("status"),
            "truth_state": obj.get("truth_state")
        })
        return _obj
