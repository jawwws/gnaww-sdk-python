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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.colour_capability import ColourCapability
from gnaww_sdk.models.custom_dimension_capability import CustomDimensionCapability
from gnaww_sdk.models.dimension_capability import DimensionCapability
from gnaww_sdk.models.material_capability import MaterialCapability
from gnaww_sdk.models.personalisation_capability import PersonalisationCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CommercialPrintOptions(BaseModel):
    """
    Shared commercial print capability fields.
    """ # noqa: E501
    colour: ColourCapability
    custom_dimensions: Optional[CustomDimensionCapability] = None
    dimensions: Annotated[List[DimensionCapability], Field(min_length=1)]
    materials: Annotated[List[MaterialCapability], Field(min_length=1)]
    personalisation: Optional[PersonalisationCapability] = None
    printed_sides: Annotated[List[StrictStr], Field(min_length=1)]
    __properties: ClassVar[List[str]] = ["colour", "custom_dimensions", "dimensions", "materials", "personalisation", "printed_sides"]

    @field_validator('printed_sides')
    def printed_sides_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['single_sided', 'double_sided', 'unknown']):
                raise ValueError("each list item must be one of ('single_sided', 'double_sided', 'unknown')")
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
        """Create an instance of CommercialPrintOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of colour
        if self.colour:
            _dict['colour'] = self.colour.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_dimensions
        if self.custom_dimensions:
            _dict['custom_dimensions'] = self.custom_dimensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item_dimensions in self.dimensions:
                if _item_dimensions:
                    _items.append(_item_dimensions.to_dict())
            _dict['dimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in materials (list)
        _items = []
        if self.materials:
            for _item_materials in self.materials:
                if _item_materials:
                    _items.append(_item_materials.to_dict())
            _dict['materials'] = _items
        # override the default output from pydantic by calling `to_dict()` of personalisation
        if self.personalisation:
            _dict['personalisation'] = self.personalisation.to_dict()
        # set to None if custom_dimensions (nullable) is None
        # and model_fields_set contains the field
        if self.custom_dimensions is None and "custom_dimensions" in self.model_fields_set:
            _dict['custom_dimensions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommercialPrintOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "colour": ColourCapability.from_dict(obj["colour"]) if obj.get("colour") is not None else None,
            "custom_dimensions": CustomDimensionCapability.from_dict(obj["custom_dimensions"]) if obj.get("custom_dimensions") is not None else None,
            "dimensions": [DimensionCapability.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "materials": [MaterialCapability.from_dict(_item) for _item in obj["materials"]] if obj.get("materials") is not None else None,
            "personalisation": PersonalisationCapability.from_dict(obj["personalisation"]) if obj.get("personalisation") is not None else None,
            "printed_sides": obj.get("printed_sides")
        })
        return _obj
