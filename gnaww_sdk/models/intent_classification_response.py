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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from gnaww_sdk.models.intent_plan_evidence import IntentPlanEvidence
from gnaww_sdk.models.issue_set import IssueSet
from gnaww_sdk.models.source_input import SourceInput
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class IntentClassificationResponse(BaseModel):
    """
    Deterministic classification of product-led versus outcome-led input.
    """ # noqa: E501
    candidate_product_families: Optional[List[StrictStr]] = None
    confidence: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]
    detected_product_categories: Optional[List[StrictStr]] = None
    detected_product_families: Optional[List[StrictStr]] = None
    deterministic: Optional[StrictBool] = True
    evidence: Optional[List[IntentPlanEvidence]] = None
    input_kind: StrictStr
    issues: Optional[IssueSet] = None
    requires_intent_planner: StrictBool
    schema_name: Optional[StrictStr] = 'jawwws.intent_classification_response'
    schema_version: Optional[StrictStr] = '0.1'
    source: SourceInput
    status: StrictStr
    __properties: ClassVar[List[str]] = ["candidate_product_families", "confidence", "detected_product_categories", "detected_product_families", "deterministic", "evidence", "input_kind", "issues", "requires_intent_planner", "schema_name", "schema_version", "source", "status"]

    @field_validator('candidate_product_families')
    def candidate_product_families_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
                raise ValueError("each list item must be one of ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
        return value

    @field_validator('detected_product_categories')
    def detected_product_categories_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown']):
                raise ValueError("each list item must be one of ('commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown')")
        return value

    @field_validator('detected_product_families')
    def detected_product_families_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
                raise ValueError("each list item must be one of ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
        return value

    @field_validator('deterministic')
    def deterministic_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('input_kind')
    def input_kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['product_led', 'outcome_led', 'mixed', 'needs_review']):
            raise ValueError("must be one of enum values ('product_led', 'outcome_led', 'mixed', 'needs_review')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['jawwws.intent_classification_response']):
            raise ValueError("must be one of enum values ('jawwws.intent_classification_response')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['classified', 'needs_review', 'failed']):
            raise ValueError("must be one of enum values ('classified', 'needs_review', 'failed')")
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
        """Create an instance of IntentClassificationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in evidence (list)
        _items = []
        if self.evidence:
            for _item_evidence in self.evidence:
                if _item_evidence:
                    _items.append(_item_evidence.to_dict())
            _dict['evidence'] = _items
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntentClassificationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "candidate_product_families": obj.get("candidate_product_families"),
            "confidence": obj.get("confidence"),
            "detected_product_categories": obj.get("detected_product_categories"),
            "detected_product_families": obj.get("detected_product_families"),
            "deterministic": obj.get("deterministic") if obj.get("deterministic") is not None else True,
            "evidence": [IntentPlanEvidence.from_dict(_item) for _item in obj["evidence"]] if obj.get("evidence") is not None else None,
            "input_kind": obj.get("input_kind"),
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "requires_intent_planner": obj.get("requires_intent_planner"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'jawwws.intent_classification_response',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "source": SourceInput.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "status": obj.get("status")
        })
        return _obj
