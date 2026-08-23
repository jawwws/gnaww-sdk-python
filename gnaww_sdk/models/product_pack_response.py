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
from gnaww_sdk.models.intent_classification_response import IntentClassificationResponse
from gnaww_sdk.models.intent_provider_metadata import IntentProviderMetadata
from gnaww_sdk.models.product_pack_benchmark_reference import ProductPackBenchmarkReference
from gnaww_sdk.models.product_pack_clarification import ProductPackClarification
from gnaww_sdk.models.product_pack_recommendation import ProductPackRecommendation
from gnaww_sdk.models.source_input import SourceInput
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProductPackResponse(BaseModel):
    """
    Review-only product pack before canonical specification.
    """ # noqa: E501
    benchmark_references: Optional[List[ProductPackBenchmarkReference]] = None
    canonical_specifications_created: Optional[StrictBool] = False
    clarifications: Optional[List[ProductPackClarification]] = None
    classification: IntentClassificationResponse
    confirmed_availability: Optional[StrictBool] = False
    core_recommendations: Optional[List[ProductPackRecommendation]] = None
    deterministic_grounding: Optional[StrictBool] = True
    excluded_recommendations: Optional[List[ProductPackRecommendation]] = None
    grounding_status: StrictStr
    live_pricing_available: Optional[StrictBool] = False
    no_benchmark_reason: Optional[StrictStr] = None
    optional_recommendations: Optional[List[ProductPackRecommendation]] = None
    producer_selection_performed: Optional[StrictBool] = False
    provider_metadata: IntentProviderMetadata
    schema_name: Optional[StrictStr] = 'jawwws.product_pack_response'
    schema_version: Optional[StrictStr] = '0.1'
    source: SourceInput
    specmatch_performed: Optional[StrictBool] = False
    status: Optional[StrictStr] = 'needs_review'
    summary: Annotated[str, Field(min_length=1, strict=True)]
    __properties: ClassVar[List[str]] = ["benchmark_references", "canonical_specifications_created", "clarifications", "classification", "confirmed_availability", "core_recommendations", "deterministic_grounding", "excluded_recommendations", "grounding_status", "live_pricing_available", "no_benchmark_reason", "optional_recommendations", "producer_selection_performed", "provider_metadata", "schema_name", "schema_version", "source", "specmatch_performed", "status", "summary"]

    @field_validator('canonical_specifications_created')
    def canonical_specifications_created_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('confirmed_availability')
    def confirmed_availability_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('deterministic_grounding')
    def deterministic_grounding_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('grounding_status')
    def grounding_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['grounded', 'partially_grounded', 'ungrounded']):
            raise ValueError("must be one of enum values ('grounded', 'partially_grounded', 'ungrounded')")
        return value

    @field_validator('live_pricing_available')
    def live_pricing_available_validate_enum(cls, value):
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

        if value not in set(['jawwws.product_pack_response']):
            raise ValueError("must be one of enum values ('jawwws.product_pack_response')")
        return value

    @field_validator('specmatch_performed')
    def specmatch_performed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false']):
            raise ValueError("must be one of enum values ('false')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['needs_review']):
            raise ValueError("must be one of enum values ('needs_review')")
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
        """Create an instance of ProductPackResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in benchmark_references (list)
        _items = []
        if self.benchmark_references:
            for _item_benchmark_references in self.benchmark_references:
                if _item_benchmark_references:
                    _items.append(_item_benchmark_references.to_dict())
            _dict['benchmark_references'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in clarifications (list)
        _items = []
        if self.clarifications:
            for _item_clarifications in self.clarifications:
                if _item_clarifications:
                    _items.append(_item_clarifications.to_dict())
            _dict['clarifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in core_recommendations (list)
        _items = []
        if self.core_recommendations:
            for _item_core_recommendations in self.core_recommendations:
                if _item_core_recommendations:
                    _items.append(_item_core_recommendations.to_dict())
            _dict['core_recommendations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in excluded_recommendations (list)
        _items = []
        if self.excluded_recommendations:
            for _item_excluded_recommendations in self.excluded_recommendations:
                if _item_excluded_recommendations:
                    _items.append(_item_excluded_recommendations.to_dict())
            _dict['excluded_recommendations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in optional_recommendations (list)
        _items = []
        if self.optional_recommendations:
            for _item_optional_recommendations in self.optional_recommendations:
                if _item_optional_recommendations:
                    _items.append(_item_optional_recommendations.to_dict())
            _dict['optional_recommendations'] = _items
        # override the default output from pydantic by calling `to_dict()` of provider_metadata
        if self.provider_metadata:
            _dict['provider_metadata'] = self.provider_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # set to None if no_benchmark_reason (nullable) is None
        # and model_fields_set contains the field
        if self.no_benchmark_reason is None and "no_benchmark_reason" in self.model_fields_set:
            _dict['no_benchmark_reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductPackResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "benchmark_references": [ProductPackBenchmarkReference.from_dict(_item) for _item in obj["benchmark_references"]] if obj.get("benchmark_references") is not None else None,
            "canonical_specifications_created": obj.get("canonical_specifications_created") if obj.get("canonical_specifications_created") is not None else False,
            "clarifications": [ProductPackClarification.from_dict(_item) for _item in obj["clarifications"]] if obj.get("clarifications") is not None else None,
            "classification": IntentClassificationResponse.from_dict(obj["classification"]) if obj.get("classification") is not None else None,
            "confirmed_availability": obj.get("confirmed_availability") if obj.get("confirmed_availability") is not None else False,
            "core_recommendations": [ProductPackRecommendation.from_dict(_item) for _item in obj["core_recommendations"]] if obj.get("core_recommendations") is not None else None,
            "deterministic_grounding": obj.get("deterministic_grounding") if obj.get("deterministic_grounding") is not None else True,
            "excluded_recommendations": [ProductPackRecommendation.from_dict(_item) for _item in obj["excluded_recommendations"]] if obj.get("excluded_recommendations") is not None else None,
            "grounding_status": obj.get("grounding_status"),
            "live_pricing_available": obj.get("live_pricing_available") if obj.get("live_pricing_available") is not None else False,
            "no_benchmark_reason": obj.get("no_benchmark_reason"),
            "optional_recommendations": [ProductPackRecommendation.from_dict(_item) for _item in obj["optional_recommendations"]] if obj.get("optional_recommendations") is not None else None,
            "producer_selection_performed": obj.get("producer_selection_performed") if obj.get("producer_selection_performed") is not None else False,
            "provider_metadata": IntentProviderMetadata.from_dict(obj["provider_metadata"]) if obj.get("provider_metadata") is not None else None,
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'jawwws.product_pack_response',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "source": SourceInput.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "specmatch_performed": obj.get("specmatch_performed") if obj.get("specmatch_performed") is not None else False,
            "status": obj.get("status") if obj.get("status") is not None else 'needs_review',
            "summary": obj.get("summary")
        })
        return _obj
