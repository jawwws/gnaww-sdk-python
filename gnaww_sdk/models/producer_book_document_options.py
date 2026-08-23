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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProducerBookDocumentOptions(BaseModel):
    """
    Supported book, booklet and document options for a producer product.
    """ # noqa: E501
    binding_methods: Optional[List[StrictStr]] = None
    cover_component_roles: Optional[List[StrictStr]] = None
    maximum_page_count: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    minimum_page_count: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    pagination_multiples: Optional[List[StrictInt]] = None
    text_component_roles: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["binding_methods", "cover_component_roles", "maximum_page_count", "minimum_page_count", "pagination_multiples", "text_component_roles"]

    @field_validator('binding_methods')
    def binding_methods_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['saddle_stitched', 'perfect_bound', 'wire_bound', 'case_bound', 'unknown']):
                raise ValueError("each list item must be one of ('saddle_stitched', 'perfect_bound', 'wire_bound', 'case_bound', 'unknown')")
        return value

    @field_validator('cover_component_roles')
    def cover_component_roles_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown']):
                raise ValueError("each list item must be one of ('main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown')")
        return value

    @field_validator('text_component_roles')
    def text_component_roles_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown']):
                raise ValueError("each list item must be one of ('main', 'flat', 'finished', 'cover', 'text', 'insert', 'garment', 'decoration', 'unknown')")
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
        """Create an instance of ProducerBookDocumentOptions from a JSON string"""
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
        # set to None if maximum_page_count (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_page_count is None and "maximum_page_count" in self.model_fields_set:
            _dict['maximum_page_count'] = None

        # set to None if minimum_page_count (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_page_count is None and "minimum_page_count" in self.model_fields_set:
            _dict['minimum_page_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProducerBookDocumentOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "binding_methods": obj.get("binding_methods"),
            "cover_component_roles": obj.get("cover_component_roles"),
            "maximum_page_count": obj.get("maximum_page_count"),
            "minimum_page_count": obj.get("minimum_page_count"),
            "pagination_multiples": obj.get("pagination_multiples"),
            "text_component_roles": obj.get("text_component_roles")
        })
        return _obj
