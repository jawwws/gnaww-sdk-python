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
from typing import Any, ClassVar, Dict, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class BookDocumentOptions(BaseModel):
    """
    Book, booklet and document production options.
    """ # noqa: E501
    binding_method: Optional[StrictStr] = 'unknown'
    cover_component_id: Optional[StrictStr] = None
    page_count: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    pagination_multiple: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    spine_width_mm: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    text_component_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["binding_method", "cover_component_id", "page_count", "pagination_multiple", "spine_width_mm", "text_component_id"]

    @field_validator('binding_method')
    def binding_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['saddle_stitched', 'perfect_bound', 'wire_bound', 'case_bound', 'unknown']):
            raise ValueError("must be one of enum values ('saddle_stitched', 'perfect_bound', 'wire_bound', 'case_bound', 'unknown')")
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
        """Create an instance of BookDocumentOptions from a JSON string"""
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
        # set to None if cover_component_id (nullable) is None
        # and model_fields_set contains the field
        if self.cover_component_id is None and "cover_component_id" in self.model_fields_set:
            _dict['cover_component_id'] = None

        # set to None if page_count (nullable) is None
        # and model_fields_set contains the field
        if self.page_count is None and "page_count" in self.model_fields_set:
            _dict['page_count'] = None

        # set to None if pagination_multiple (nullable) is None
        # and model_fields_set contains the field
        if self.pagination_multiple is None and "pagination_multiple" in self.model_fields_set:
            _dict['pagination_multiple'] = None

        # set to None if spine_width_mm (nullable) is None
        # and model_fields_set contains the field
        if self.spine_width_mm is None and "spine_width_mm" in self.model_fields_set:
            _dict['spine_width_mm'] = None

        # set to None if text_component_id (nullable) is None
        # and model_fields_set contains the field
        if self.text_component_id is None and "text_component_id" in self.model_fields_set:
            _dict['text_component_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BookDocumentOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "binding_method": obj.get("binding_method") if obj.get("binding_method") is not None else 'unknown',
            "cover_component_id": obj.get("cover_component_id"),
            "page_count": obj.get("page_count"),
            "pagination_multiple": obj.get("pagination_multiple"),
            "spine_width_mm": obj.get("spine_width_mm"),
            "text_component_id": obj.get("text_component_id")
        })
        return _obj
