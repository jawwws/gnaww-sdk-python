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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, Optional
from gnaww_sdk.models.apparel_options import ApparelOptions
from gnaww_sdk.models.commercial_print_options import CommercialPrintOptions
from gnaww_sdk.models.fabric_homewares_capability_options import FabricHomewaresCapabilityOptions
from gnaww_sdk.models.producer_book_document_options import ProducerBookDocumentOptions
from gnaww_sdk.models.producer_folded_leaflet_options import ProducerFoldedLeafletOptions
from gnaww_sdk.models.promotional_goods_capability_options import PromotionalGoodsCapabilityOptions
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProducerProductOptionCapability(BaseModel):
    """
    Family-specific producer options without supplier-specific payloads.
    """ # noqa: E501
    apparel: Optional[ApparelOptions] = None
    book_document: Optional[ProducerBookDocumentOptions] = None
    commercial_print: Optional[CommercialPrintOptions] = None
    fabric_homewares: Optional[FabricHomewaresCapabilityOptions] = None
    folded_leaflet: Optional[ProducerFoldedLeafletOptions] = None
    promotional_goods: Optional[PromotionalGoodsCapabilityOptions] = None
    __properties: ClassVar[List[str]] = ["apparel", "book_document", "commercial_print", "fabric_homewares", "folded_leaflet", "promotional_goods"]

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
        """Create an instance of ProducerProductOptionCapability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of apparel
        if self.apparel:
            _dict['apparel'] = self.apparel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of book_document
        if self.book_document:
            _dict['book_document'] = self.book_document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of commercial_print
        if self.commercial_print:
            _dict['commercial_print'] = self.commercial_print.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fabric_homewares
        if self.fabric_homewares:
            _dict['fabric_homewares'] = self.fabric_homewares.to_dict()
        # override the default output from pydantic by calling `to_dict()` of folded_leaflet
        if self.folded_leaflet:
            _dict['folded_leaflet'] = self.folded_leaflet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotional_goods
        if self.promotional_goods:
            _dict['promotional_goods'] = self.promotional_goods.to_dict()
        # set to None if apparel (nullable) is None
        # and model_fields_set contains the field
        if self.apparel is None and "apparel" in self.model_fields_set:
            _dict['apparel'] = None

        # set to None if book_document (nullable) is None
        # and model_fields_set contains the field
        if self.book_document is None and "book_document" in self.model_fields_set:
            _dict['book_document'] = None

        # set to None if commercial_print (nullable) is None
        # and model_fields_set contains the field
        if self.commercial_print is None and "commercial_print" in self.model_fields_set:
            _dict['commercial_print'] = None

        # set to None if fabric_homewares (nullable) is None
        # and model_fields_set contains the field
        if self.fabric_homewares is None and "fabric_homewares" in self.model_fields_set:
            _dict['fabric_homewares'] = None

        # set to None if folded_leaflet (nullable) is None
        # and model_fields_set contains the field
        if self.folded_leaflet is None and "folded_leaflet" in self.model_fields_set:
            _dict['folded_leaflet'] = None

        # set to None if promotional_goods (nullable) is None
        # and model_fields_set contains the field
        if self.promotional_goods is None and "promotional_goods" in self.model_fields_set:
            _dict['promotional_goods'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProducerProductOptionCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apparel": ApparelOptions.from_dict(obj["apparel"]) if obj.get("apparel") is not None else None,
            "book_document": ProducerBookDocumentOptions.from_dict(obj["book_document"]) if obj.get("book_document") is not None else None,
            "commercial_print": CommercialPrintOptions.from_dict(obj["commercial_print"]) if obj.get("commercial_print") is not None else None,
            "fabric_homewares": FabricHomewaresCapabilityOptions.from_dict(obj["fabric_homewares"]) if obj.get("fabric_homewares") is not None else None,
            "folded_leaflet": ProducerFoldedLeafletOptions.from_dict(obj["folded_leaflet"]) if obj.get("folded_leaflet") is not None else None,
            "promotional_goods": PromotionalGoodsCapabilityOptions.from_dict(obj["promotional_goods"]) if obj.get("promotional_goods") is not None else None
        })
        return _obj
