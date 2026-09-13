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
from gnaww_sdk.models.public_controlled_production_default import PublicControlledProductionDefault
from gnaww_sdk.models.public_understood_finishing import PublicUnderstoodFinishing
from gnaww_sdk.models.public_understood_print import PublicUnderstoodPrint
from gnaww_sdk.models.public_understood_size import PublicUnderstoodSize
from gnaww_sdk.models.public_understood_substrate import PublicUnderstoodSubstrate
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicUnderstoodRequirement(BaseModel):
    """
    Safe non-canonical evidence projection for review-state interpretation.
    """ # noqa: E501
    completion_support_state: Optional[StrictStr] = None
    controlled_defaults: Optional[List[PublicControlledProductionDefault]] = None
    evidence_basis: Optional[StrictStr] = 'gnaww_deterministic_interpretation'
    finishings: Optional[List[PublicUnderstoodFinishing]] = None
    print_spec: Optional[PublicUnderstoodPrint] = None
    product_family: Optional[StrictStr] = None
    product_name: Optional[StrictStr] = None
    quantity_units: Optional[Annotated[int, Field(strict=True, gt=0)]] = None
    schema_name: Optional[StrictStr] = 'gnaww.understood_requirement'
    schema_version: Optional[StrictStr] = '0.1'
    size: Optional[PublicUnderstoodSize] = None
    substrate: Optional[PublicUnderstoodSubstrate] = None
    truth_state: Optional[StrictStr] = 'understood_not_canonical'
    __properties: ClassVar[List[str]] = ["completion_support_state", "controlled_defaults", "evidence_basis", "finishings", "print_spec", "product_family", "product_name", "quantity_units", "schema_name", "schema_version", "size", "substrate", "truth_state"]

    @field_validator('completion_support_state')
    def completion_support_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['fully_supported', 'supported_with_clarification', 'recognised_not_canonicalisable', 'unsupported']):
            raise ValueError("must be one of enum values ('fully_supported', 'supported_with_clarification', 'recognised_not_canonicalisable', 'unsupported')")
        return value

    @field_validator('evidence_basis')
    def evidence_basis_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww_deterministic_interpretation']):
            raise ValueError("must be one of enum values ('gnaww_deterministic_interpretation')")
        return value

    @field_validator('product_family')
    def product_family_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown']):
            raise ValueError("must be one of enum values ('flyer', 'leaflet', 'folded_leaflet', 'apparel', 'business_card', 'loyalty_card', 'postcard', 'poster', 'sticker', 'label', 'booklet', 'book', 'document', 'card', 'certificate', 'race_bib', 'stationery', 'bookmark', 'presentation_folder', 't_shirt', 'hoodie', 'sweatshirt', 'polo_shirt', 'jacket', 'cap', 'beanie', 'workwear', 'textile_accessory', 'cushion', 'cushion_cover', 'bedding', 'curtain', 'tea_towel', 'blanket', 'fabric_by_metre', 'tablecloth', 'homeware', 'pen', 'mug', 'water_bottle', 'golf_ball', 'umbrella', 'bag', 'notebook', 'lanyard', 'keyring', 'promotional_product', 'unknown')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.understood_requirement']):
            raise ValueError("must be one of enum values ('gnaww.understood_requirement')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.1']):
            raise ValueError("must be one of enum values ('0.1')")
        return value

    @field_validator('truth_state')
    def truth_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['understood_not_canonical']):
            raise ValueError("must be one of enum values ('understood_not_canonical')")
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
        """Create an instance of PublicUnderstoodRequirement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in controlled_defaults (list)
        _items = []
        if self.controlled_defaults:
            for _item_controlled_defaults in self.controlled_defaults:
                if _item_controlled_defaults:
                    _items.append(_item_controlled_defaults.to_dict())
            _dict['controlled_defaults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in finishings (list)
        _items = []
        if self.finishings:
            for _item_finishings in self.finishings:
                if _item_finishings:
                    _items.append(_item_finishings.to_dict())
            _dict['finishings'] = _items
        # override the default output from pydantic by calling `to_dict()` of print_spec
        if self.print_spec:
            _dict['print_spec'] = self.print_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of size
        if self.size:
            _dict['size'] = self.size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of substrate
        if self.substrate:
            _dict['substrate'] = self.substrate.to_dict()
        # set to None if completion_support_state (nullable) is None
        # and model_fields_set contains the field
        if self.completion_support_state is None and "completion_support_state" in self.model_fields_set:
            _dict['completion_support_state'] = None

        # set to None if print_spec (nullable) is None
        # and model_fields_set contains the field
        if self.print_spec is None and "print_spec" in self.model_fields_set:
            _dict['print_spec'] = None

        # set to None if product_family (nullable) is None
        # and model_fields_set contains the field
        if self.product_family is None and "product_family" in self.model_fields_set:
            _dict['product_family'] = None

        # set to None if product_name (nullable) is None
        # and model_fields_set contains the field
        if self.product_name is None and "product_name" in self.model_fields_set:
            _dict['product_name'] = None

        # set to None if quantity_units (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_units is None and "quantity_units" in self.model_fields_set:
            _dict['quantity_units'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if substrate (nullable) is None
        # and model_fields_set contains the field
        if self.substrate is None and "substrate" in self.model_fields_set:
            _dict['substrate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicUnderstoodRequirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion_support_state": obj.get("completion_support_state"),
            "controlled_defaults": [PublicControlledProductionDefault.from_dict(_item) for _item in obj["controlled_defaults"]] if obj.get("controlled_defaults") is not None else None,
            "evidence_basis": obj.get("evidence_basis") if obj.get("evidence_basis") is not None else 'gnaww_deterministic_interpretation',
            "finishings": [PublicUnderstoodFinishing.from_dict(_item) for _item in obj["finishings"]] if obj.get("finishings") is not None else None,
            "print_spec": PublicUnderstoodPrint.from_dict(obj["print_spec"]) if obj.get("print_spec") is not None else None,
            "product_family": obj.get("product_family"),
            "product_name": obj.get("product_name"),
            "quantity_units": obj.get("quantity_units"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.understood_requirement',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "size": PublicUnderstoodSize.from_dict(obj["size"]) if obj.get("size") is not None else None,
            "substrate": PublicUnderstoodSubstrate.from_dict(obj["substrate"]) if obj.get("substrate") is not None else None,
            "truth_state": obj.get("truth_state") if obj.get("truth_state") is not None else 'understood_not_canonical'
        })
        return _obj
