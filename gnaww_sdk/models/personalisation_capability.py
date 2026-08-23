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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PersonalisationCapability(BaseModel):
    """
    Supported per-item or variable-data personalisation.
    """ # noqa: E501
    maximum_variants: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    per_item_artwork: Optional[StrictBool] = False
    sequential_numbering: Optional[StrictBool] = False
    supported: Optional[StrictBool] = False
    variable_images: Optional[StrictBool] = False
    variable_text: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["maximum_variants", "per_item_artwork", "sequential_numbering", "supported", "variable_images", "variable_text"]

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
        """Create an instance of PersonalisationCapability from a JSON string"""
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
        # set to None if maximum_variants (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_variants is None and "maximum_variants" in self.model_fields_set:
            _dict['maximum_variants'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PersonalisationCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maximum_variants": obj.get("maximum_variants"),
            "per_item_artwork": obj.get("per_item_artwork") if obj.get("per_item_artwork") is not None else False,
            "sequential_numbering": obj.get("sequential_numbering") if obj.get("sequential_numbering") is not None else False,
            "supported": obj.get("supported") if obj.get("supported") is not None else False,
            "variable_images": obj.get("variable_images") if obj.get("variable_images") is not None else False,
            "variable_text": obj.get("variable_text") if obj.get("variable_text") is not None else False
        })
        return _obj
