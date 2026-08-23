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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.public_match_target_state import PublicMatchTargetState
from gnaww_sdk.models.public_spec_match_readiness import PublicSpecMatchReadiness
from gnaww_sdk.models.resolved_recipe_match_state import ResolvedRecipeMatchState
from gnaww_sdk.models.spec_match_result import SpecMatchResult
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MatchRecipeResponse(BaseModel):
    """
    Public deterministic capability-fit result for one persisted Recipe.
    """ # noqa: E501
    availability_checked: Optional[StrictBool] = False
    demand_basis: Optional[StrictStr] = 'recipe'
    live_pricing_performed: Optional[StrictBool] = False
    match: SpecMatchResult
    next_actions: Optional[List[StrictStr]] = None
    order_created: Optional[StrictBool] = False
    persistence_performed: Optional[StrictBool] = False
    producer_acceptance_performed: Optional[StrictBool] = False
    producer_selection_performed: Optional[StrictBool] = False
    readiness: PublicSpecMatchReadiness
    recipe: ResolvedRecipeMatchState
    schema_name: Optional[StrictStr] = 'gnaww.recipe_specmatch_result'
    schema_version: Optional[StrictStr] = '0.1'
    specmatch_performed: Optional[StrictBool] = True
    status: StrictStr
    target: PublicMatchTargetState
    __properties: ClassVar[List[str]] = ["availability_checked", "demand_basis", "live_pricing_performed", "match", "next_actions", "order_created", "persistence_performed", "producer_acceptance_performed", "producer_selection_performed", "readiness", "recipe", "schema_name", "schema_version", "specmatch_performed", "status", "target"]

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
        if value is None:
            return value

        if value not in set(['recipe']):
            raise ValueError("must be one of enum values ('recipe')")
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

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.recipe_specmatch_result']):
            raise ValueError("must be one of enum values ('gnaww.recipe_specmatch_result')")
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

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['matched', 'matched_with_warnings', 'needs_review', 'blocked', 'failed']):
            raise ValueError("must be one of enum values ('matched', 'matched_with_warnings', 'needs_review', 'blocked', 'failed')")
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
        """Create an instance of MatchRecipeResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of match
        if self.match:
            _dict['match'] = self.match.to_dict()
        # override the default output from pydantic by calling `to_dict()` of readiness
        if self.readiness:
            _dict['readiness'] = self.readiness.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipe
        if self.recipe:
            _dict['recipe'] = self.recipe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchRecipeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability_checked": obj.get("availability_checked") if obj.get("availability_checked") is not None else False,
            "demand_basis": obj.get("demand_basis") if obj.get("demand_basis") is not None else 'recipe',
            "live_pricing_performed": obj.get("live_pricing_performed") if obj.get("live_pricing_performed") is not None else False,
            "match": SpecMatchResult.from_dict(obj["match"]) if obj.get("match") is not None else None,
            "next_actions": obj.get("next_actions"),
            "order_created": obj.get("order_created") if obj.get("order_created") is not None else False,
            "persistence_performed": obj.get("persistence_performed") if obj.get("persistence_performed") is not None else False,
            "producer_acceptance_performed": obj.get("producer_acceptance_performed") if obj.get("producer_acceptance_performed") is not None else False,
            "producer_selection_performed": obj.get("producer_selection_performed") if obj.get("producer_selection_performed") is not None else False,
            "readiness": PublicSpecMatchReadiness.from_dict(obj["readiness"]) if obj.get("readiness") is not None else None,
            "recipe": ResolvedRecipeMatchState.from_dict(obj["recipe"]) if obj.get("recipe") is not None else None,
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.recipe_specmatch_result',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "specmatch_performed": obj.get("specmatch_performed") if obj.get("specmatch_performed") is not None else True,
            "status": obj.get("status"),
            "target": PublicMatchTargetState.from_dict(obj["target"]) if obj.get("target") is not None else None
        })
        return _obj
