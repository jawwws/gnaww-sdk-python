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
from gnaww_sdk.models.manufacturing_assembly import ManufacturingAssembly
from gnaww_sdk.models.manufacturing_component import ManufacturingComponent
from gnaww_sdk.models.manufacturing_operation import ManufacturingOperation
from gnaww_sdk.models.manufacturing_quantity import ManufacturingQuantity
from gnaww_sdk.models.manufacturing_variation import ManufacturingVariation
from gnaww_sdk.models.quality_requirement import QualityRequirement
from gnaww_sdk.models.service_requirements import ServiceRequirements
from gnaww_sdk.models.use_requirement import UseRequirement
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PrintJobSpecificationV05(BaseModel):
    """
    GJS v0.5 compositional manufacturing definition foundation.
    """ # noqa: E501
    assemblies: Optional[List[ManufacturingAssembly]] = None
    components: Annotated[List[ManufacturingComponent], Field(min_length=1)]
    confidence: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = 0.0
    operations: Optional[List[ManufacturingOperation]] = None
    product_category: Optional[StrictStr] = 'unknown'
    product_family: StrictStr
    product_name: Optional[StrictStr] = None
    quality_requirements: Optional[List[QualityRequirement]] = None
    quantity: Optional[ManufacturingQuantity] = None
    schema_name: Optional[StrictStr] = 'jawwws.print_job_specification'
    schema_version: Optional[StrictStr] = '0.5'
    service_requirements: Optional[ServiceRequirements] = None
    status: Optional[StrictStr] = 'mapped'
    unresolved_fields: Optional[List[StrictStr]] = None
    use_requirements: Optional[List[UseRequirement]] = None
    variations: Optional[List[ManufacturingVariation]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["assemblies", "components", "confidence", "operations", "product_category", "product_family", "product_name", "quality_requirements", "quantity", "schema_name", "schema_version", "service_requirements", "status", "unresolved_fields", "use_requirements", "variations"]

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

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['jawwws.print_job_specification']):
            raise ValueError("must be one of enum values ('jawwws.print_job_specification')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.5']):
            raise ValueError("must be one of enum values ('0.5')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['mapped', 'needs_review', 'blocked', 'failed']):
            raise ValueError("must be one of enum values ('mapped', 'needs_review', 'blocked', 'failed')")
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
        """Create an instance of PrintJobSpecificationV05 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in assemblies (list)
        _items = []
        if self.assemblies:
            for _item_assemblies in self.assemblies:
                if _item_assemblies:
                    _items.append(_item_assemblies.to_dict())
            _dict['assemblies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in operations (list)
        _items = []
        if self.operations:
            for _item_operations in self.operations:
                if _item_operations:
                    _items.append(_item_operations.to_dict())
            _dict['operations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in quality_requirements (list)
        _items = []
        if self.quality_requirements:
            for _item_quality_requirements in self.quality_requirements:
                if _item_quality_requirements:
                    _items.append(_item_quality_requirements.to_dict())
            _dict['quality_requirements'] = _items
        # override the default output from pydantic by calling `to_dict()` of quantity
        if self.quantity:
            _dict['quantity'] = self.quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_requirements
        if self.service_requirements:
            _dict['service_requirements'] = self.service_requirements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in use_requirements (list)
        _items = []
        if self.use_requirements:
            for _item_use_requirements in self.use_requirements:
                if _item_use_requirements:
                    _items.append(_item_use_requirements.to_dict())
            _dict['use_requirements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variations (list)
        _items = []
        if self.variations:
            for _item_variations in self.variations:
                if _item_variations:
                    _items.append(_item_variations.to_dict())
            _dict['variations'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if product_name (nullable) is None
        # and model_fields_set contains the field
        if self.product_name is None and "product_name" in self.model_fields_set:
            _dict['product_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrintJobSpecificationV05 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assemblies": [ManufacturingAssembly.from_dict(_item) for _item in obj["assemblies"]] if obj.get("assemblies") is not None else None,
            "components": [ManufacturingComponent.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "confidence": obj.get("confidence") if obj.get("confidence") is not None else 0.0,
            "operations": [ManufacturingOperation.from_dict(_item) for _item in obj["operations"]] if obj.get("operations") is not None else None,
            "product_category": obj.get("product_category") if obj.get("product_category") is not None else 'unknown',
            "product_family": obj.get("product_family"),
            "product_name": obj.get("product_name"),
            "quality_requirements": [QualityRequirement.from_dict(_item) for _item in obj["quality_requirements"]] if obj.get("quality_requirements") is not None else None,
            "quantity": ManufacturingQuantity.from_dict(obj["quantity"]) if obj.get("quantity") is not None else None,
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'jawwws.print_job_specification',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.5',
            "service_requirements": ServiceRequirements.from_dict(obj["service_requirements"]) if obj.get("service_requirements") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else 'mapped',
            "unresolved_fields": obj.get("unresolved_fields"),
            "use_requirements": [UseRequirement.from_dict(_item) for _item in obj["use_requirements"]] if obj.get("use_requirements") is not None else None,
            "variations": [ManufacturingVariation.from_dict(_item) for _item in obj["variations"]] if obj.get("variations") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
