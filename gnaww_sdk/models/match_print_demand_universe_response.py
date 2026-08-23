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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.public_producer_universe_candidate import PublicProducerUniverseCandidate
from gnaww_sdk.models.public_recipe_state import PublicRecipeState
from gnaww_sdk.models.public_spec_match_readiness import PublicSpecMatchReadiness
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MatchPrintDemandUniverseResponse(BaseModel):
    """
    Ranked capability result across an authorised producer universe.
    """ # noqa: E501
    availability_checked: Optional[StrictBool] = False
    best_capable_candidate: Optional[PublicProducerUniverseCandidate] = None
    blocked_count: Annotated[int, Field(strict=True, ge=0)]
    candidates: Optional[List[PublicProducerUniverseCandidate]] = None
    confirmed_capable_count: Annotated[int, Field(strict=True, ge=0)]
    demand_basis: StrictStr
    leading_candidate: Optional[PublicProducerUniverseCandidate] = None
    live_pricing_performed: Optional[StrictBool] = False
    next_actions: Optional[List[StrictStr]] = None
    order_created: Optional[StrictBool] = False
    outcome: StrictStr
    persistence_performed: Optional[StrictBool] = False
    producer_acceptance_performed: Optional[StrictBool] = False
    producer_selection_performed: Optional[StrictBool] = False
    producer_universe_evaluated: Optional[StrictBool] = True
    producer_universe_size: Annotated[int, Field(strict=True, ge=0)]
    ranking_performed: Optional[StrictBool] = True
    readiness: PublicSpecMatchReadiness
    recipe: PublicRecipeState
    review_required_count: Annotated[int, Field(strict=True, ge=0)]
    schema_name: Optional[StrictStr] = 'gnaww.specmatch_universe_result'
    schema_version: Optional[StrictStr] = '0.1'
    specmatch_performed: Optional[StrictBool] = True
    __properties: ClassVar[List[str]] = ["availability_checked", "best_capable_candidate", "blocked_count", "candidates", "confirmed_capable_count", "demand_basis", "leading_candidate", "live_pricing_performed", "next_actions", "order_created", "outcome", "persistence_performed", "producer_acceptance_performed", "producer_selection_performed", "producer_universe_evaluated", "producer_universe_size", "ranking_performed", "readiness", "recipe", "review_required_count", "schema_name", "schema_version", "specmatch_performed"]

    @field_validator('availability_checked')
    def availability_checked_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('demand_basis')
    def demand_basis_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['recipe', 'gjs']):
            raise ValueError("must be one of enum values ('recipe', 'gjs')")
        return value

    @field_validator('live_pricing_performed')
    def live_pricing_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('order_created')
    def order_created_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('outcome')
    def outcome_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['capable_producer_found', 'review_required', 'no_capable_producer']):
            raise ValueError("must be one of enum values ('capable_producer_found', 'review_required', 'no_capable_producer')")
        return value

    @field_validator('persistence_performed')
    def persistence_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('producer_acceptance_performed')
    def producer_acceptance_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('producer_selection_performed')
    def producer_selection_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('producer_universe_evaluated')
    def producer_universe_evaluated_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('ranking_performed')
    def ranking_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.specmatch_universe_result']):
            raise ValueError("must be one of enum values ('gnaww.specmatch_universe_result')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.1']):
            raise ValueError("must be one of enum values ('0.1')")
        return value

    @field_validator('specmatch_performed')
    def specmatch_performed_validate_enum(cls, value):
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
        """Create an instance of MatchPrintDemandUniverseResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of best_capable_candidate
        if self.best_capable_candidate:
            _dict['best_capable_candidate'] = self.best_capable_candidate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in candidates (list)
        _items = []
        if self.candidates:
            for _item_candidates in self.candidates:
                if _item_candidates:
                    _items.append(_item_candidates.to_dict())
            _dict['candidates'] = _items
        # override the default output from pydantic by calling `to_dict()` of leading_candidate
        if self.leading_candidate:
            _dict['leading_candidate'] = self.leading_candidate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of readiness
        if self.readiness:
            _dict['readiness'] = self.readiness.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipe
        if self.recipe:
            _dict['recipe'] = self.recipe.to_dict()
        # set to None if best_capable_candidate (nullable) is None
        # and model_fields_set contains the field
        if self.best_capable_candidate is None and "best_capable_candidate" in self.model_fields_set:
            _dict['best_capable_candidate'] = None

        # set to None if leading_candidate (nullable) is None
        # and model_fields_set contains the field
        if self.leading_candidate is None and "leading_candidate" in self.model_fields_set:
            _dict['leading_candidate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchPrintDemandUniverseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability_checked": obj.get("availability_checked") if obj.get("availability_checked") is not None else False,
            "best_capable_candidate": PublicProducerUniverseCandidate.from_dict(obj["best_capable_candidate"]) if obj.get("best_capable_candidate") is not None else None,
            "blocked_count": obj.get("blocked_count"),
            "candidates": [PublicProducerUniverseCandidate.from_dict(_item) for _item in obj["candidates"]] if obj.get("candidates") is not None else None,
            "confirmed_capable_count": obj.get("confirmed_capable_count"),
            "demand_basis": obj.get("demand_basis"),
            "leading_candidate": PublicProducerUniverseCandidate.from_dict(obj["leading_candidate"]) if obj.get("leading_candidate") is not None else None,
            "live_pricing_performed": obj.get("live_pricing_performed") if obj.get("live_pricing_performed") is not None else False,
            "next_actions": obj.get("next_actions"),
            "order_created": obj.get("order_created") if obj.get("order_created") is not None else False,
            "outcome": obj.get("outcome"),
            "persistence_performed": obj.get("persistence_performed") if obj.get("persistence_performed") is not None else False,
            "producer_acceptance_performed": obj.get("producer_acceptance_performed") if obj.get("producer_acceptance_performed") is not None else False,
            "producer_selection_performed": obj.get("producer_selection_performed") if obj.get("producer_selection_performed") is not None else False,
            "producer_universe_evaluated": obj.get("producer_universe_evaluated") if obj.get("producer_universe_evaluated") is not None else True,
            "producer_universe_size": obj.get("producer_universe_size"),
            "ranking_performed": obj.get("ranking_performed") if obj.get("ranking_performed") is not None else True,
            "readiness": PublicSpecMatchReadiness.from_dict(obj["readiness"]) if obj.get("readiness") is not None else None,
            "recipe": PublicRecipeState.from_dict(obj["recipe"]) if obj.get("recipe") is not None else None,
            "review_required_count": obj.get("review_required_count"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.specmatch_universe_result',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "specmatch_performed": obj.get("specmatch_performed") if obj.get("specmatch_performed") is not None else True
        })
        return _obj
