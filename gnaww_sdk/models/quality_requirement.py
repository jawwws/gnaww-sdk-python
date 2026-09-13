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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.numeric_tolerance import NumericTolerance
from gnaww_sdk.models.operation_target import OperationTarget
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class QualityRequirement(BaseModel):
    """
    QualityRequirement
    """ # noqa: E501
    category: StrictStr
    description: Annotated[str, Field(min_length=1, strict=True)]
    requirement_id: Annotated[str, Field(strict=True)]
    target: Optional[OperationTarget] = None
    tolerance: Optional[NumericTolerance] = None
    __properties: ClassVar[List[str]] = ["category", "description", "requirement_id", "target", "tolerance"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['colour', 'dimension', 'weight', 'registration', 'code_readability', 'surface', 'batch_consistency', 'other']):
            raise ValueError("must be one of enum values ('colour', 'dimension', 'weight', 'registration', 'code_readability', 'surface', 'batch_consistency', 'other')")
        return value

    @field_validator('requirement_id')
    def requirement_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9][A-Za-z0-9_.:-]*$/")
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
        """Create an instance of QualityRequirement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tolerance
        if self.tolerance:
            _dict['tolerance'] = self.tolerance.to_dict()
        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if tolerance (nullable) is None
        # and model_fields_set contains the field
        if self.tolerance is None and "tolerance" in self.model_fields_set:
            _dict['tolerance'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QualityRequirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "description": obj.get("description"),
            "requirement_id": obj.get("requirement_id"),
            "target": OperationTarget.from_dict(obj["target"]) if obj.get("target") is not None else None,
            "tolerance": NumericTolerance.from_dict(obj["tolerance"]) if obj.get("tolerance") is not None else None
        })
        return _obj
