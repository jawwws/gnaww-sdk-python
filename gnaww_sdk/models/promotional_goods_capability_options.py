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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.decoration_area_capability import DecorationAreaCapability
from gnaww_sdk.models.dimension_capability import DimensionCapability
from gnaww_sdk.models.material_capability import MaterialCapability
from gnaww_sdk.models.personalisation_capability import PersonalisationCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PromotionalGoodsCapabilityOptions(BaseModel):
    """
    Canonical promotional-goods product and decoration capabilities.
    """ # noqa: E501
    capacities_ml: Optional[List[StrictInt]] = None
    compliance_claims: Optional[List[StrictStr]] = None
    decoration_areas: Optional[List[DecorationAreaCapability]] = None
    dimensions: Optional[List[DimensionCapability]] = None
    materials: Optional[List[MaterialCapability]] = None
    packaging_types: Optional[List[StrictStr]] = None
    personalisation: Optional[PersonalisationCapability] = None
    product_colours: Optional[List[StrictStr]] = None
    product_types: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["capacities_ml", "compliance_claims", "decoration_areas", "dimensions", "materials", "packaging_types", "personalisation", "product_colours", "product_types"]

    @field_validator('packaging_types')
    def packaging_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['bulk', 'individual_bag', 'gift_box', 'retail_box', 'custom', 'unknown']):
                raise ValueError("each list item must be one of ('bulk', 'individual_bag', 'gift_box', 'retail_box', 'custom', 'unknown')")
        return value

    @field_validator('product_types')
    def product_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
                raise ValueError("each list item must be one of ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
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
        """Create an instance of PromotionalGoodsCapabilityOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in decoration_areas (list)
        _items = []
        if self.decoration_areas:
            for _item_decoration_areas in self.decoration_areas:
                if _item_decoration_areas:
                    _items.append(_item_decoration_areas.to_dict())
            _dict['decoration_areas'] = _items
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PromotionalGoodsCapabilityOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capacities_ml": obj.get("capacities_ml"),
            "compliance_claims": obj.get("compliance_claims"),
            "decoration_areas": [DecorationAreaCapability.from_dict(_item) for _item in obj["decoration_areas"]] if obj.get("decoration_areas") is not None else None,
            "dimensions": [DimensionCapability.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "materials": [MaterialCapability.from_dict(_item) for _item in obj["materials"]] if obj.get("materials") is not None else None,
            "packaging_types": obj.get("packaging_types"),
            "personalisation": PersonalisationCapability.from_dict(obj["personalisation"]) if obj.get("personalisation") is not None else None,
            "product_colours": obj.get("product_colours"),
            "product_types": obj.get("product_types")
        })
        return _obj
