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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.controlled_interpretation_state import ControlledInterpretationState
from gnaww_sdk.models.gjs import Gjs
from gnaww_sdk.models.grounded_product_meaning import GroundedProductMeaning
from gnaww_sdk.models.intent_classification_response import IntentClassificationResponse
from gnaww_sdk.models.issue_set import IssueSet
from gnaww_sdk.models.product_pack_response import ProductPackResponse
from gnaww_sdk.models.public_recipe_state import PublicRecipeState
from gnaww_sdk.models.public_spec_match_readiness import PublicSpecMatchReadiness
from gnaww_sdk.models.public_use_condition_review import PublicUseConditionReview
from gnaww_sdk.models.source_input import SourceInput
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class InterpretPrintRequirementResponse(BaseModel):
    """
    Public ordinary-language orchestration result.
    """ # noqa: E501
    classification: IntentClassificationResponse
    controlled_interpretation: ControlledInterpretationState
    gjs: Optional[Gjs] = None
    issues: Optional[IssueSet] = None
    known_product_families: Optional[List[StrictStr]] = None
    next_actions: Optional[List[StrictStr]] = None
    persistence_performed: Optional[StrictBool] = False
    producer_selection_performed: Optional[StrictBool] = False
    product_meaning_review: Optional[List[GroundedProductMeaning]] = None
    reason: StrictStr
    recipe: PublicRecipeState
    recommendation_review: Optional[ProductPackResponse] = None
    requested_gjs_version: StrictStr
    route: StrictStr
    schema_name: Optional[StrictStr] = 'gnaww.interpretation_result'
    schema_version: Optional[StrictStr] = '0.1'
    source: SourceInput
    specmatch: PublicSpecMatchReadiness
    specmatch_performed: Optional[StrictBool] = False
    status: StrictStr
    unresolved_fields: Optional[List[StrictStr]] = None
    use_condition_review: Optional[List[PublicUseConditionReview]] = None
    __properties: ClassVar[List[str]] = ["classification", "controlled_interpretation", "gjs", "issues", "known_product_families", "next_actions", "persistence_performed", "producer_selection_performed", "product_meaning_review", "reason", "recipe", "recommendation_review", "requested_gjs_version", "route", "schema_name", "schema_version", "source", "specmatch", "specmatch_performed", "status", "unresolved_fields", "use_condition_review"]

    @field_validator('known_product_families')
    def known_product_families_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
                raise ValueError("each list item must be one of ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
        return value

    @field_validator('persistence_performed')
    def persistence_performed_validate_enum(cls, value):
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

    @field_validator('reason')
    def reason_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['deterministic_transform_sufficient', 'known_family_not_canonicalised', 'multiple_product_families_need_orchestration', 'deterministic_transform_failed', 'intent_planner_required', 'classification_needs_review', 'classification_failed']):
            raise ValueError("must be one of enum values ('deterministic_transform_sufficient', 'known_family_not_canonicalised', 'multiple_product_families_need_orchestration', 'deterministic_transform_failed', 'intent_planner_required', 'classification_needs_review', 'classification_failed')")
        return value

    @field_validator('requested_gjs_version')
    def requested_gjs_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['0.3', '0.4']):
            raise ValueError("must be one of enum values ('0.3', '0.4')")
        return value

    @field_validator('route')
    def route_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['deterministic_ready', 'canonicalisation_gap', 'recommendation_review_required', 'needs_review', 'failed']):
            raise ValueError("must be one of enum values ('deterministic_ready', 'canonicalisation_gap', 'recommendation_review_required', 'needs_review', 'failed')")
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

        if value not in set(['0.1']):
            raise ValueError("must be one of enum values ('0.1')")
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
        """Create an instance of InterpretPrintRequirementResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of controlled_interpretation
        if self.controlled_interpretation:
            _dict['controlled_interpretation'] = self.controlled_interpretation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gjs
        if self.gjs:
            _dict['gjs'] = self.gjs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in product_meaning_review (list)
        _items = []
        if self.product_meaning_review:
            for _item_product_meaning_review in self.product_meaning_review:
                if _item_product_meaning_review:
                    _items.append(_item_product_meaning_review.to_dict())
            _dict['product_meaning_review'] = _items
        # override the default output from pydantic by calling `to_dict()` of recipe
        if self.recipe:
            _dict['recipe'] = self.recipe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recommendation_review
        if self.recommendation_review:
            _dict['recommendation_review'] = self.recommendation_review.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specmatch
        if self.specmatch:
            _dict['specmatch'] = self.specmatch.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in use_condition_review (list)
        _items = []
        if self.use_condition_review:
            for _item_use_condition_review in self.use_condition_review:
                if _item_use_condition_review:
                    _items.append(_item_use_condition_review.to_dict())
            _dict['use_condition_review'] = _items
        # set to None if gjs (nullable) is None
        # and model_fields_set contains the field
        if self.gjs is None and "gjs" in self.model_fields_set:
            _dict['gjs'] = None

        # set to None if recommendation_review (nullable) is None
        # and model_fields_set contains the field
        if self.recommendation_review is None and "recommendation_review" in self.model_fields_set:
            _dict['recommendation_review'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InterpretPrintRequirementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "classification": IntentClassificationResponse.from_dict(obj["classification"]) if obj.get("classification") is not None else None,
            "controlled_interpretation": ControlledInterpretationState.from_dict(obj["controlled_interpretation"]) if obj.get("controlled_interpretation") is not None else None,
            "gjs": Gjs.from_dict(obj["gjs"]) if obj.get("gjs") is not None else None,
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "known_product_families": obj.get("known_product_families"),
            "next_actions": obj.get("next_actions"),
            "persistence_performed": obj.get("persistence_performed") if obj.get("persistence_performed") is not None else False,
            "producer_selection_performed": obj.get("producer_selection_performed") if obj.get("producer_selection_performed") is not None else False,
            "product_meaning_review": [GroundedProductMeaning.from_dict(_item) for _item in obj["product_meaning_review"]] if obj.get("product_meaning_review") is not None else None,
            "reason": obj.get("reason"),
            "recipe": PublicRecipeState.from_dict(obj["recipe"]) if obj.get("recipe") is not None else None,
            "recommendation_review": ProductPackResponse.from_dict(obj["recommendation_review"]) if obj.get("recommendation_review") is not None else None,
            "requested_gjs_version": obj.get("requested_gjs_version"),
            "route": obj.get("route"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.interpretation_result',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "source": SourceInput.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "specmatch": PublicSpecMatchReadiness.from_dict(obj["specmatch"]) if obj.get("specmatch") is not None else None,
            "specmatch_performed": obj.get("specmatch_performed") if obj.get("specmatch_performed") is not None else False,
            "status": obj.get("status"),
            "unresolved_fields": obj.get("unresolved_fields"),
            "use_condition_review": [PublicUseConditionReview.from_dict(_item) for _item in obj["use_condition_review"]] if obj.get("use_condition_review") is not None else None
        })
        return _obj
