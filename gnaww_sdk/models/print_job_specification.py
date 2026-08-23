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
from gnaww_sdk.models.print_component import PrintComponent
from gnaww_sdk.models.product_options import ProductOptions
from gnaww_sdk.models.quantity import Quantity
from gnaww_sdk.models.service_requirements import ServiceRequirements
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PrintJobSpecification(BaseModel):
    """
    Canonical Jawwws print job specification returned by Gnaww.
    """ # noqa: E501
    components: Optional[List[PrintComponent]] = None
    confidence: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = 0.0
    options: Optional[ProductOptions] = None
    product_category: Optional[StrictStr] = 'unknown'
    product_family: StrictStr
    product_name: Optional[StrictStr] = None
    quantity: Optional[Quantity] = None
    schema_name: Optional[StrictStr] = 'jawwws.print_job_specification'
    schema_version: Optional[StrictStr] = '0.3'
    service_requirements: Optional[ServiceRequirements] = None
    status: Optional[StrictStr] = 'mapped'
    unresolved_fields: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["components", "confidence", "options", "product_category", "product_family", "product_name", "quantity", "schema_name", "schema_version", "service_requirements", "status", "unresolved_fields"]

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
        """Create an instance of PrintJobSpecification from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quantity
        if self.quantity:
            _dict['quantity'] = self.quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_requirements
        if self.service_requirements:
            _dict['service_requirements'] = self.service_requirements.to_dict()
        # set to None if product_name (nullable) is None
        # and model_fields_set contains the field
        if self.product_name is None and "product_name" in self.model_fields_set:
            _dict['product_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrintJobSpecification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "components": [PrintComponent.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "confidence": obj.get("confidence") if obj.get("confidence") is not None else 0.0,
            "options": ProductOptions.from_dict(obj["options"]) if obj.get("options") is not None else None,
            "product_category": obj.get("product_category") if obj.get("product_category") is not None else 'unknown',
            "product_family": obj.get("product_family"),
            "product_name": obj.get("product_name"),
            "quantity": Quantity.from_dict(obj["quantity"]) if obj.get("quantity") is not None else None,
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'jawwws.print_job_specification',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.3',
            "service_requirements": ServiceRequirements.from_dict(obj["service_requirements"]) if obj.get("service_requirements") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else 'mapped',
            "unresolved_fields": obj.get("unresolved_fields")
        })
        return _obj
