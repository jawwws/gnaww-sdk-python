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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ArtworkRequirements(BaseModel):
    """
    Artwork rules that a producer expects for a product.
    """ # noqa: E501
    accepted_file_types: Annotated[List[StrictStr], Field(min_length=1)]
    bleed_mm: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    colour_space: Optional[StrictStr] = None
    recommended_dpi: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    safe_zone_mm: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    __properties: ClassVar[List[str]] = ["accepted_file_types", "bleed_mm", "colour_space", "recommended_dpi", "safe_zone_mm"]

    @field_validator('accepted_file_types')
    def accepted_file_types_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['pdf', 'jpg', 'jpeg', 'png']):
                raise ValueError("each list item must be one of ('pdf', 'jpg', 'jpeg', 'png')")
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
        """Create an instance of ArtworkRequirements from a JSON string"""
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
        # set to None if bleed_mm (nullable) is None
        # and model_fields_set contains the field
        if self.bleed_mm is None and "bleed_mm" in self.model_fields_set:
            _dict['bleed_mm'] = None

        # set to None if colour_space (nullable) is None
        # and model_fields_set contains the field
        if self.colour_space is None and "colour_space" in self.model_fields_set:
            _dict['colour_space'] = None

        # set to None if recommended_dpi (nullable) is None
        # and model_fields_set contains the field
        if self.recommended_dpi is None and "recommended_dpi" in self.model_fields_set:
            _dict['recommended_dpi'] = None

        # set to None if safe_zone_mm (nullable) is None
        # and model_fields_set contains the field
        if self.safe_zone_mm is None and "safe_zone_mm" in self.model_fields_set:
            _dict['safe_zone_mm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArtworkRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accepted_file_types": obj.get("accepted_file_types"),
            "bleed_mm": obj.get("bleed_mm"),
            "colour_space": obj.get("colour_space"),
            "recommended_dpi": obj.get("recommended_dpi"),
            "safe_zone_mm": obj.get("safe_zone_mm")
        })
        return _obj
