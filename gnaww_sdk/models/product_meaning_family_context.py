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
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProductMeaningFamilyContext(BaseModel):
    """
    One Gnaww-declared family exposed to semantic interpretation.
    """ # noqa: E501
    completion_archetype: Optional[StrictStr] = None
    product_category: StrictStr
    product_family: StrictStr
    support_state: StrictStr
    __properties: ClassVar[List[str]] = ["completion_archetype", "product_category", "product_family", "support_state"]

    @field_validator('completion_archetype')
    def completion_archetype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['flat_commercial_print', 'folded_paper', 'book_document', 'apparel_decoration', 'fabric_homewares', 'promotional_goods']):
            raise ValueError("must be one of enum values ('flat_commercial_print', 'folded_paper', 'book_document', 'apparel_decoration', 'fabric_homewares', 'promotional_goods')")
        return value

    @field_validator('product_category')
    def product_category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown']):
            raise ValueError("must be one of enum values ('commercial_print', 'apparel', 'fabric_homewares', 'promotional_goods', 'unknown')")
        return value

    @field_validator('product_family')
    def product_family_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
            raise ValueError("must be one of enum values ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
        return value

    @field_validator('support_state')
    def support_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['fully_supported', 'supported_with_clarification', 'recognised_not_canonicalisable', 'unsupported']):
            raise ValueError("must be one of enum values ('fully_supported', 'supported_with_clarification', 'recognised_not_canonicalisable', 'unsupported')")
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
        """Create an instance of ProductMeaningFamilyContext from a JSON string"""
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
        # set to None if completion_archetype (nullable) is None
        # and model_fields_set contains the field
        if self.completion_archetype is None and "completion_archetype" in self.model_fields_set:
            _dict['completion_archetype'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductMeaningFamilyContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion_archetype": obj.get("completion_archetype"),
            "product_category": obj.get("product_category"),
            "product_family": obj.get("product_family"),
            "support_state": obj.get("support_state")
        })
        return _obj
