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
from gnaww_sdk.models.product_meaning_decision_point import ProductMeaningDecisionPoint
from gnaww_sdk.models.product_meaning_family_context import ProductMeaningFamilyContext
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GroundedProductMeaning(BaseModel):
    """
    Review-safe product meaning grounded against Gnaww-controlled truth.
    """ # noqa: E501
    confidence: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]
    coverage_state: StrictStr
    decision_points: Optional[List[ProductMeaningDecisionPoint]] = None
    family_candidates: Optional[List[ProductMeaningFamilyContext]] = None
    family_mapping_state: StrictStr
    meaning_id: Annotated[str, Field(strict=True)]
    rationale: Annotated[str, Field(min_length=1, strict=True)]
    requires_review: Optional[StrictBool] = True
    semantic_concept: Annotated[str, Field(min_length=1, strict=True)]
    source_expression: Annotated[str, Field(min_length=1, strict=True)]
    __properties: ClassVar[List[str]] = ["confidence", "coverage_state", "decision_points", "family_candidates", "family_mapping_state", "meaning_id", "rationale", "requires_review", "semantic_concept", "source_expression"]

    @field_validator('coverage_state')
    def coverage_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['canonical_candidates', 'known_concept_coverage_gap']):
            raise ValueError("must be one of enum values ('canonical_candidates', 'known_concept_coverage_gap')")
        return value

    @field_validator('family_mapping_state')
    def family_mapping_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['direct_equivalence', 'depends_on_decision', 'no_safe_mapping']):
            raise ValueError("must be one of enum values ('direct_equivalence', 'depends_on_decision', 'no_safe_mapping')")
        return value

    @field_validator('meaning_id')
    def meaning_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^meaning-[0-9]{3}$", value):
            raise ValueError(r"must validate the regular expression /^meaning-[0-9]{3}$/")
        return value

    @field_validator('requires_review')
    def requires_review_validate_enum(cls, value):
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
        """Create an instance of GroundedProductMeaning from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in decision_points (list)
        _items = []
        if self.decision_points:
            for _item_decision_points in self.decision_points:
                if _item_decision_points:
                    _items.append(_item_decision_points.to_dict())
            _dict['decision_points'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in family_candidates (list)
        _items = []
        if self.family_candidates:
            for _item_family_candidates in self.family_candidates:
                if _item_family_candidates:
                    _items.append(_item_family_candidates.to_dict())
            _dict['family_candidates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GroundedProductMeaning from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confidence": obj.get("confidence"),
            "coverage_state": obj.get("coverage_state"),
            "decision_points": [ProductMeaningDecisionPoint.from_dict(_item) for _item in obj["decision_points"]] if obj.get("decision_points") is not None else None,
            "family_candidates": [ProductMeaningFamilyContext.from_dict(_item) for _item in obj["family_candidates"]] if obj.get("family_candidates") is not None else None,
            "family_mapping_state": obj.get("family_mapping_state"),
            "meaning_id": obj.get("meaning_id"),
            "rationale": obj.get("rationale"),
            "requires_review": obj.get("requires_review") if obj.get("requires_review") is not None else True,
            "semantic_concept": obj.get("semantic_concept"),
            "source_expression": obj.get("source_expression")
        })
        return _obj
