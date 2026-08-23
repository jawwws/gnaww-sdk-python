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
from gnaww_sdk.models.benchmark_quantity_guidance import BenchmarkQuantityGuidance
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProductPackRecommendation(BaseModel):
    """
    One review-only product recommendation.
    """ # noqa: E501
    benchmark_id: Optional[StrictStr] = None
    benchmark_version: Optional[StrictStr] = None
    clarification_keys: Optional[List[StrictStr]] = None
    evidence_status: StrictStr
    priority: StrictStr
    product_category: StrictStr
    product_family: StrictStr
    purpose: Annotated[str, Field(min_length=1, strict=True)]
    quantity_guidance: Optional[BenchmarkQuantityGuidance] = None
    rationale: Annotated[str, Field(min_length=1, strict=True)]
    recommendation_id: Annotated[str, Field(min_length=1, strict=True)]
    requires_confirmation: StrictBool
    source: StrictStr
    title: Annotated[str, Field(min_length=1, strict=True)]
    __properties: ClassVar[List[str]] = ["benchmark_id", "benchmark_version", "clarification_keys", "evidence_status", "priority", "product_category", "product_family", "purpose", "quantity_guidance", "rationale", "recommendation_id", "requires_confirmation", "source", "title"]

    @field_validator('evidence_status')
    def evidence_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['curated_baseline', 'observed_intent', 'confirmed_outcome', 'empirical', 'general_model_knowledge']):
            raise ValueError("must be one of enum values ('curated_baseline', 'observed_intent', 'confirmed_outcome', 'empirical', 'general_model_knowledge')")
        return value

    @field_validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['core', 'optional', 'avoid']):
            raise ValueError("must be one of enum values ('core', 'optional', 'avoid')")
        return value

    @field_validator('product_category')
    def product_category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown']):
            raise ValueError("must be one of enum values ('commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown')")
        return value

    @field_validator('product_family')
    def product_family_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
            raise ValueError("must be one of enum values ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
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
        """Create an instance of ProductPackRecommendation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quantity_guidance
        if self.quantity_guidance:
            _dict['quantity_guidance'] = self.quantity_guidance.to_dict()
        # set to None if benchmark_id (nullable) is None
        # and model_fields_set contains the field
        if self.benchmark_id is None and "benchmark_id" in self.model_fields_set:
            _dict['benchmark_id'] = None

        # set to None if benchmark_version (nullable) is None
        # and model_fields_set contains the field
        if self.benchmark_version is None and "benchmark_version" in self.model_fields_set:
            _dict['benchmark_version'] = None

        # set to None if quantity_guidance (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_guidance is None and "quantity_guidance" in self.model_fields_set:
            _dict['quantity_guidance'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductPackRecommendation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "benchmark_id": obj.get("benchmark_id"),
            "benchmark_version": obj.get("benchmark_version"),
            "clarification_keys": obj.get("clarification_keys"),
            "evidence_status": obj.get("evidence_status"),
            "priority": obj.get("priority"),
            "product_category": obj.get("product_category"),
            "product_family": obj.get("product_family"),
            "purpose": obj.get("purpose"),
            "quantity_guidance": BenchmarkQuantityGuidance.from_dict(obj["quantity_guidance"]) if obj.get("quantity_guidance") is not None else None,
            "rationale": obj.get("rationale"),
            "recommendation_id": obj.get("recommendation_id"),
            "requires_confirmation": obj.get("requires_confirmation"),
            "source": obj.get("source"),
            "title": obj.get("title")
        })
        return _obj
