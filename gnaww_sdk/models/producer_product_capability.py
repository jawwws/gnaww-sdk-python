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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.artwork_requirements import ArtworkRequirements
from gnaww_sdk.models.availability_capability import AvailabilityCapability
from gnaww_sdk.models.dimension_capability import DimensionCapability
from gnaww_sdk.models.material_capability import MaterialCapability
from gnaww_sdk.models.producer_component_capability import ProducerComponentCapability
from gnaww_sdk.models.producer_finishing_capability import ProducerFinishingCapability
from gnaww_sdk.models.producer_process_capability import ProducerProcessCapability
from gnaww_sdk.models.producer_product_option_capability import ProducerProductOptionCapability
from gnaww_sdk.models.quantity_range import QuantityRange
from gnaww_sdk.models.turnaround_capability import TurnaroundCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProducerProductCapability(BaseModel):
    """
    A single producer product and its supported options.
    """ # noqa: E501
    artwork: ArtworkRequirements
    availability: Optional[AvailabilityCapability] = None
    components: Optional[List[ProducerComponentCapability]] = None
    finishings: Optional[List[ProducerFinishingCapability]] = None
    processes: Optional[List[ProducerProcessCapability]] = None
    product_category: Optional[StrictStr] = 'unknown'
    product_family: StrictStr
    product_id: StrictStr
    product_name: StrictStr
    product_options: Optional[ProducerProductOptionCapability] = None
    quantity: QuantityRange
    sides: Optional[List[StrictStr]] = None
    sizes: Optional[List[DimensionCapability]] = None
    substrates: Optional[List[MaterialCapability]] = None
    turnaround: Optional[TurnaroundCapability] = None
    __properties: ClassVar[List[str]] = ["artwork", "availability", "components", "finishings", "processes", "product_category", "product_family", "product_id", "product_name", "product_options", "quantity", "sides", "sizes", "substrates", "turnaround"]

    @field_validator('product_category')
    def product_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown']):
            raise ValueError("must be one of enum values ('commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown')")
        return value

    @field_validator('product_family')
    def product_family_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
            raise ValueError("must be one of enum values ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
        return value

    @field_validator('sides')
    def sides_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
        """Create an instance of ProducerProductCapability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of artwork
        if self.artwork:
            _dict['artwork'] = self.artwork.to_dict()
        # override the default output from pydantic by calling `to_dict()` of availability
        if self.availability:
            _dict['availability'] = self.availability.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in finishings (list)
        _items = []
        if self.finishings:
            for _item_finishings in self.finishings:
                if _item_finishings:
                    _items.append(_item_finishings.to_dict())
            _dict['finishings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in processes (list)
        _items = []
        if self.processes:
            for _item_processes in self.processes:
                if _item_processes:
                    _items.append(_item_processes.to_dict())
            _dict['processes'] = _items
        # override the default output from pydantic by calling `to_dict()` of product_options
        if self.product_options:
            _dict['product_options'] = self.product_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quantity
        if self.quantity:
            _dict['quantity'] = self.quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sizes (list)
        _items = []
        if self.sizes:
            for _item_sizes in self.sizes:
                if _item_sizes:
                    _items.append(_item_sizes.to_dict())
            _dict['sizes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in substrates (list)
        _items = []
        if self.substrates:
            for _item_substrates in self.substrates:
                if _item_substrates:
                    _items.append(_item_substrates.to_dict())
            _dict['substrates'] = _items
        # override the default output from pydantic by calling `to_dict()` of turnaround
        if self.turnaround:
            _dict['turnaround'] = self.turnaround.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProducerProductCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "artwork": ArtworkRequirements.from_dict(obj["artwork"]) if obj.get("artwork") is not None else None,
            "availability": AvailabilityCapability.from_dict(obj["availability"]) if obj.get("availability") is not None else None,
            "components": [ProducerComponentCapability.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "finishings": [ProducerFinishingCapability.from_dict(_item) for _item in obj["finishings"]] if obj.get("finishings") is not None else None,
            "processes": [ProducerProcessCapability.from_dict(_item) for _item in obj["processes"]] if obj.get("processes") is not None else None,
            "product_category": obj.get("product_category") if obj.get("product_category") is not None else 'unknown',
            "product_family": obj.get("product_family"),
            "product_id": obj.get("product_id"),
            "product_name": obj.get("product_name"),
            "product_options": ProducerProductOptionCapability.from_dict(obj["product_options"]) if obj.get("product_options") is not None else None,
            "quantity": QuantityRange.from_dict(obj["quantity"]) if obj.get("quantity") is not None else None,
            "sides": obj.get("sides"),
            "sizes": [DimensionCapability.from_dict(_item) for _item in obj["sizes"]] if obj.get("sizes") is not None else None,
            "substrates": [MaterialCapability.from_dict(_item) for _item in obj["substrates"]] if obj.get("substrates") is not None else None,
            "turnaround": TurnaroundCapability.from_dict(obj["turnaround"]) if obj.get("turnaround") is not None else None
        })
        return _obj
