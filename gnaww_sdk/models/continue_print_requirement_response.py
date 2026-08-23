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
from gnaww_sdk.models.issue_set import IssueSet
from gnaww_sdk.models.print_job_specification_v04 import PrintJobSpecificationV04
from gnaww_sdk.models.public_clarification_question import PublicClarificationQuestion
from gnaww_sdk.models.public_fulfilment_state import PublicFulfilmentState
from gnaww_sdk.models.public_recipe_state import PublicRecipeState
from gnaww_sdk.models.public_spec_match_readiness import PublicSpecMatchReadiness
from gnaww_sdk.models.source_input import SourceInput
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ContinuePrintRequirementResponse(BaseModel):
    """
    Guided completion state without persistence or matching execution.
    """ # noqa: E501
    fulfilment: Optional[PublicFulfilmentState] = None
    gjs: Optional[PrintJobSpecificationV04] = None
    issues: Optional[IssueSet] = None
    next_actions: Optional[List[StrictStr]] = None
    persistence_performed: Optional[StrictBool] = False
    producer_selection_performed: Optional[StrictBool] = False
    product_family: Optional[StrictStr] = None
    questions: Optional[List[PublicClarificationQuestion]] = None
    recipe: PublicRecipeState
    remaining_question_keys: Optional[List[StrictStr]] = None
    schema_name: Optional[StrictStr] = 'gnaww.interpretation_continuation_result'
    schema_version: Optional[StrictStr] = '0.1'
    source: SourceInput
    specmatch: PublicSpecMatchReadiness
    specmatch_performed: Optional[StrictBool] = False
    status: StrictStr
    universe_match_ready: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["fulfilment", "gjs", "issues", "next_actions", "persistence_performed", "producer_selection_performed", "product_family", "questions", "recipe", "remaining_question_keys", "schema_name", "schema_version", "source", "specmatch", "specmatch_performed", "status", "universe_match_ready"]

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

    @field_validator('product_family')
    def product_family_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
            raise ValueError("must be one of enum values ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.interpretation_continuation_result']):
            raise ValueError("must be one of enum values ('gnaww.interpretation_continuation_result')")
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
        if value not in set(['review_required', 'specmatch_ready', 'failed']):
            raise ValueError("must be one of enum values ('review_required', 'specmatch_ready', 'failed')")
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
        """Create an instance of ContinuePrintRequirementResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gjs
        if self.gjs:
            _dict['gjs'] = self.gjs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specmatch
        if self.specmatch:
            _dict['specmatch'] = self.specmatch.to_dict()
        # set to None if gjs (nullable) is None
        # and model_fields_set contains the field
        if self.gjs is None and "gjs" in self.model_fields_set:
            _dict['gjs'] = None

        # set to None if product_family (nullable) is None
        # and model_fields_set contains the field
        if self.product_family is None and "product_family" in self.model_fields_set:
            _dict['product_family'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContinuePrintRequirementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fulfilment": PublicFulfilmentState.from_dict(obj["fulfilment"]) if obj.get("fulfilment") is not None else None,
            "gjs": PrintJobSpecificationV04.from_dict(obj["gjs"]) if obj.get("gjs") is not None else None,
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "next_actions": obj.get("next_actions"),
            "persistence_performed": obj.get("persistence_performed") if obj.get("persistence_performed") is not None else False,
            "producer_selection_performed": obj.get("producer_selection_performed") if obj.get("producer_selection_performed") is not None else False,
            "product_family": obj.get("product_family"),
            "questions": [PublicClarificationQuestion.from_dict(_item) for _item in obj["questions"]] if obj.get("questions") is not None else None,
            "recipe": PublicRecipeState.from_dict(obj["recipe"]) if obj.get("recipe") is not None else None,
            "remaining_question_keys": obj.get("remaining_question_keys"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.interpretation_continuation_result',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "source": SourceInput.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "specmatch": PublicSpecMatchReadiness.from_dict(obj["specmatch"]) if obj.get("specmatch") is not None else None,
            "specmatch_performed": obj.get("specmatch_performed") if obj.get("specmatch_performed") is not None else False,
            "status": obj.get("status"),
            "universe_match_ready": obj.get("universe_match_ready") if obj.get("universe_match_ready") is not None else False
        })
        return _obj
