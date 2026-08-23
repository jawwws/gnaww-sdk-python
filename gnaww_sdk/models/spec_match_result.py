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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from gnaww_sdk.models.issue_set import IssueSet
from gnaww_sdk.models.match_difference import MatchDifference
from gnaww_sdk.models.physical_requirement_decision import PhysicalRequirementDecision
from gnaww_sdk.models.producer_product_reference import ProducerProductReference
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SpecMatchResult(BaseModel):
    """
    Result of matching a canonical job against producer capabilities.
    """ # noqa: E501
    confidence: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = 0.0
    differences: Optional[List[MatchDifference]] = None
    issues: Optional[IssueSet] = None
    match_reasons: Optional[List[StrictStr]] = None
    match_score: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = 0.0
    physical_requirements: Optional[List[PhysicalRequirementDecision]] = None
    product: Optional[ProducerProductReference] = None
    status: StrictStr
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["confidence", "differences", "issues", "match_reasons", "match_score", "physical_requirements", "product", "status"]

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
        """Create an instance of SpecMatchResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in differences (list)
        _items = []
        if self.differences:
            for _item_differences in self.differences:
                if _item_differences:
                    _items.append(_item_differences.to_dict())
            _dict['differences'] = _items
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in physical_requirements (list)
        _items = []
        if self.physical_requirements:
            for _item_physical_requirements in self.physical_requirements:
                if _item_physical_requirements:
                    _items.append(_item_physical_requirements.to_dict())
            _dict['physical_requirements'] = _items
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if product (nullable) is None
        # and model_fields_set contains the field
        if self.product is None and "product" in self.model_fields_set:
            _dict['product'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpecMatchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confidence": obj.get("confidence") if obj.get("confidence") is not None else 0.0,
            "differences": [MatchDifference.from_dict(_item) for _item in obj["differences"]] if obj.get("differences") is not None else None,
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "match_reasons": obj.get("match_reasons"),
            "match_score": obj.get("match_score") if obj.get("match_score") is not None else 0.0,
            "physical_requirements": [PhysicalRequirementDecision.from_dict(_item) for _item in obj["physical_requirements"]] if obj.get("physical_requirements") is not None else None,
            "product": ProducerProductReference.from_dict(obj["product"]) if obj.get("product") is not None else None,
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
