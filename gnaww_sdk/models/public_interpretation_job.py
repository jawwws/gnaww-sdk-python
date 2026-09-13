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
from gnaww_sdk.models.gjs1 import Gjs1
from gnaww_sdk.models.grounded_product_meaning import GroundedProductMeaning
from gnaww_sdk.models.issue_set import IssueSet
from gnaww_sdk.models.public_controlled_production_default import PublicControlledProductionDefault
from gnaww_sdk.models.public_interpretation_fulfilment_state import PublicInterpretationFulfilmentState
from gnaww_sdk.models.public_interpretation_question import PublicInterpretationQuestion
from gnaww_sdk.models.public_job_context_fact import PublicJobContextFact
from gnaww_sdk.models.public_job_structure import PublicJobStructure
from gnaww_sdk.models.public_recipe_state import PublicRecipeState
from gnaww_sdk.models.public_spec_match_readiness import PublicSpecMatchReadiness
from gnaww_sdk.models.public_understood_requirement import PublicUnderstoodRequirement
from gnaww_sdk.models.public_use_condition_review import PublicUseConditionReview
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicInterpretationJob(BaseModel):
    """
    One independently producible Job Proposal or canonical Job state.
    """ # noqa: E501
    context: Optional[List[PublicJobContextFact]] = None
    controlled_defaults: Optional[List[PublicControlledProductionDefault]] = None
    fulfilment: Optional[PublicInterpretationFulfilmentState] = None
    gjs: Optional[Gjs1] = None
    grounded_product_summary: Optional[StrictStr] = None
    issues: Optional[IssueSet] = None
    job_id: Annotated[str, Field(strict=True)]
    next_actions: Optional[List[StrictStr]] = None
    product_family: Optional[StrictStr] = None
    product_meaning_review: Optional[List[GroundedProductMeaning]] = None
    questions: Optional[List[PublicInterpretationQuestion]] = None
    recipe: Optional[PublicRecipeState] = None
    specmatch: Optional[PublicSpecMatchReadiness] = None
    status: StrictStr
    structure: Optional[List[PublicJobStructure]] = None
    understood_requirement: Optional[PublicUnderstoodRequirement] = None
    universe_match_ready: Optional[StrictBool] = False
    unresolved_fields: Optional[List[StrictStr]] = None
    use_condition_review: Optional[List[PublicUseConditionReview]] = None
    __properties: ClassVar[List[str]] = ["context", "controlled_defaults", "fulfilment", "gjs", "grounded_product_summary", "issues", "job_id", "next_actions", "product_family", "product_meaning_review", "questions", "recipe", "specmatch", "status", "structure", "understood_requirement", "universe_match_ready", "unresolved_fields", "use_condition_review"]

    @field_validator('job_id')
    def job_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^job_[a-z0-9][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^job_[a-z0-9][a-z0-9_-]*$/")
        return value

    @field_validator('product_family')
    def product_family_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
            raise ValueError("must be one of enum values ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
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
        """Create an instance of PublicInterpretationJob from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in context (list)
        _items = []
        if self.context:
            for _item_context in self.context:
                if _item_context:
                    _items.append(_item_context.to_dict())
            _dict['context'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in controlled_defaults (list)
        _items = []
        if self.controlled_defaults:
            for _item_controlled_defaults in self.controlled_defaults:
                if _item_controlled_defaults:
                    _items.append(_item_controlled_defaults.to_dict())
            _dict['controlled_defaults'] = _items
        # override the default output from pydantic by calling `to_dict()` of fulfilment
        if self.fulfilment:
            _dict['fulfilment'] = self.fulfilment.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of each item in questions (list)
        _items = []
        if self.questions:
            for _item_questions in self.questions:
                if _item_questions:
                    _items.append(_item_questions.to_dict())
            _dict['questions'] = _items
        # override the default output from pydantic by calling `to_dict()` of recipe
        if self.recipe:
            _dict['recipe'] = self.recipe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specmatch
        if self.specmatch:
            _dict['specmatch'] = self.specmatch.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in structure (list)
        _items = []
        if self.structure:
            for _item_structure in self.structure:
                if _item_structure:
                    _items.append(_item_structure.to_dict())
            _dict['structure'] = _items
        # override the default output from pydantic by calling `to_dict()` of understood_requirement
        if self.understood_requirement:
            _dict['understood_requirement'] = self.understood_requirement.to_dict()
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

        # set to None if grounded_product_summary (nullable) is None
        # and model_fields_set contains the field
        if self.grounded_product_summary is None and "grounded_product_summary" in self.model_fields_set:
            _dict['grounded_product_summary'] = None

        # set to None if product_family (nullable) is None
        # and model_fields_set contains the field
        if self.product_family is None and "product_family" in self.model_fields_set:
            _dict['product_family'] = None

        # set to None if understood_requirement (nullable) is None
        # and model_fields_set contains the field
        if self.understood_requirement is None and "understood_requirement" in self.model_fields_set:
            _dict['understood_requirement'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicInterpretationJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "context": [PublicJobContextFact.from_dict(_item) for _item in obj["context"]] if obj.get("context") is not None else None,
            "controlled_defaults": [PublicControlledProductionDefault.from_dict(_item) for _item in obj["controlled_defaults"]] if obj.get("controlled_defaults") is not None else None,
            "fulfilment": PublicInterpretationFulfilmentState.from_dict(obj["fulfilment"]) if obj.get("fulfilment") is not None else None,
            "gjs": Gjs1.from_dict(obj["gjs"]) if obj.get("gjs") is not None else None,
            "grounded_product_summary": obj.get("grounded_product_summary"),
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "job_id": obj.get("job_id"),
            "next_actions": obj.get("next_actions"),
            "product_family": obj.get("product_family"),
            "product_meaning_review": [GroundedProductMeaning.from_dict(_item) for _item in obj["product_meaning_review"]] if obj.get("product_meaning_review") is not None else None,
            "questions": [PublicInterpretationQuestion.from_dict(_item) for _item in obj["questions"]] if obj.get("questions") is not None else None,
            "recipe": PublicRecipeState.from_dict(obj["recipe"]) if obj.get("recipe") is not None else None,
            "specmatch": PublicSpecMatchReadiness.from_dict(obj["specmatch"]) if obj.get("specmatch") is not None else None,
            "status": obj.get("status"),
            "structure": [PublicJobStructure.from_dict(_item) for _item in obj["structure"]] if obj.get("structure") is not None else None,
            "understood_requirement": PublicUnderstoodRequirement.from_dict(obj["understood_requirement"]) if obj.get("understood_requirement") is not None else None,
            "universe_match_ready": obj.get("universe_match_ready") if obj.get("universe_match_ready") is not None else False,
            "unresolved_fields": obj.get("unresolved_fields"),
            "use_condition_review": [PublicUseConditionReview.from_dict(_item) for _item in obj["use_condition_review"]] if obj.get("use_condition_review") is not None else None
        })
        return _obj
