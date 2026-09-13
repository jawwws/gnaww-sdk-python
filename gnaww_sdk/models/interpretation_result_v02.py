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
from gnaww_sdk.models.issue_set import IssueSet
from gnaww_sdk.models.product_pack_response import ProductPackResponse
from gnaww_sdk.models.public_capability_question import PublicCapabilityQuestion
from gnaww_sdk.models.public_controlled_interpretation_state import PublicControlledInterpretationState
from gnaww_sdk.models.public_interpretation_intent import PublicInterpretationIntent
from gnaww_sdk.models.public_interpretation_job import PublicInterpretationJob
from gnaww_sdk.models.public_interpretation_question import PublicInterpretationQuestion
from gnaww_sdk.models.public_interpretation_truth_state import PublicInterpretationTruthState
from gnaww_sdk.models.public_shared_context_fact import PublicSharedContextFact
from gnaww_sdk.models.source_input import SourceInput
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class InterpretationResultV02(BaseModel):
    """
    Job-centric public messy-intent interpretation result.
    """ # noqa: E501
    capability_questions: Optional[List[PublicCapabilityQuestion]] = None
    controlled_interpretation: PublicControlledInterpretationState
    intent: PublicInterpretationIntent
    issues: Optional[IssueSet] = None
    jobs: Optional[List[PublicInterpretationJob]] = None
    next_actions: Optional[List[StrictStr]] = None
    questions: Optional[List[PublicInterpretationQuestion]] = None
    recommendations: Optional[List[ProductPackResponse]] = None
    requested_gjs_version: StrictStr
    schema_name: Optional[StrictStr] = 'gnaww.interpretation_result'
    schema_version: Optional[StrictStr] = '0.2'
    shared_context: Optional[List[PublicSharedContextFact]] = None
    source: SourceInput
    status: StrictStr
    truth: Optional[PublicInterpretationTruthState] = None
    __properties: ClassVar[List[str]] = ["capability_questions", "controlled_interpretation", "intent", "issues", "jobs", "next_actions", "questions", "recommendations", "requested_gjs_version", "schema_name", "schema_version", "shared_context", "source", "status", "truth"]

    @field_validator('requested_gjs_version')
    def requested_gjs_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['0.3', '0.4']):
            raise ValueError("must be one of enum values ('0.3', '0.4')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.interpretation_result']):
            raise ValueError("must be one of enum values ('gnaww.interpretation_result')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.2']):
            raise ValueError("must be one of enum values ('0.2')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['canonical_ready', 'review_required', 'needs_review', 'failed']):
            raise ValueError("must be one of enum values ('canonical_ready', 'review_required', 'needs_review', 'failed')")
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
        """Create an instance of InterpretationResultV02 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in capability_questions (list)
        _items = []
        if self.capability_questions:
            for _item_capability_questions in self.capability_questions:
                if _item_capability_questions:
                    _items.append(_item_capability_questions.to_dict())
            _dict['capability_questions'] = _items
        # override the default output from pydantic by calling `to_dict()` of controlled_interpretation
        if self.controlled_interpretation:
            _dict['controlled_interpretation'] = self.controlled_interpretation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of intent
        if self.intent:
            _dict['intent'] = self.intent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item_jobs in self.jobs:
                if _item_jobs:
                    _items.append(_item_jobs.to_dict())
            _dict['jobs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in questions (list)
        _items = []
        if self.questions:
            for _item_questions in self.questions:
                if _item_questions:
                    _items.append(_item_questions.to_dict())
            _dict['questions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recommendations (list)
        _items = []
        if self.recommendations:
            for _item_recommendations in self.recommendations:
                if _item_recommendations:
                    _items.append(_item_recommendations.to_dict())
            _dict['recommendations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shared_context (list)
        _items = []
        if self.shared_context:
            for _item_shared_context in self.shared_context:
                if _item_shared_context:
                    _items.append(_item_shared_context.to_dict())
            _dict['shared_context'] = _items
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of truth
        if self.truth:
            _dict['truth'] = self.truth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InterpretationResultV02 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capability_questions": [PublicCapabilityQuestion.from_dict(_item) for _item in obj["capability_questions"]] if obj.get("capability_questions") is not None else None,
            "controlled_interpretation": PublicControlledInterpretationState.from_dict(obj["controlled_interpretation"]) if obj.get("controlled_interpretation") is not None else None,
            "intent": PublicInterpretationIntent.from_dict(obj["intent"]) if obj.get("intent") is not None else None,
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "jobs": [PublicInterpretationJob.from_dict(_item) for _item in obj["jobs"]] if obj.get("jobs") is not None else None,
            "next_actions": obj.get("next_actions"),
            "questions": [PublicInterpretationQuestion.from_dict(_item) for _item in obj["questions"]] if obj.get("questions") is not None else None,
            "recommendations": [ProductPackResponse.from_dict(_item) for _item in obj["recommendations"]] if obj.get("recommendations") is not None else None,
            "requested_gjs_version": obj.get("requested_gjs_version"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.interpretation_result',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.2',
            "shared_context": [PublicSharedContextFact.from_dict(_item) for _item in obj["shared_context"]] if obj.get("shared_context") is not None else None,
            "source": SourceInput.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "status": obj.get("status"),
            "truth": PublicInterpretationTruthState.from_dict(obj["truth"]) if obj.get("truth") is not None else None
        })
        return _obj
