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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from gnaww_sdk.models.producer_product_capability import ProducerProductCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProducerCapabilityResource(BaseModel):
    """
    Safe capability-only projection of one producer profile.
    """ # noqa: E501
    is_live_supplier: StrictBool
    producer_id: Annotated[str, Field(min_length=1, strict=True)]
    producer_name: Annotated[str, Field(min_length=1, strict=True)]
    producer_profile_id: Annotated[str, Field(min_length=1, strict=True)]
    producer_profile_schema_version: Annotated[str, Field(min_length=1, strict=True)]
    products: Annotated[List[ProducerProductCapability], Field(min_length=1)]
    schema_name: StrictStr
    schema_version: StrictStr
    source: StrictStr
    truth_state: StrictStr
    __properties: ClassVar[List[str]] = ["is_live_supplier", "producer_id", "producer_name", "producer_profile_id", "producer_profile_schema_version", "products", "schema_name", "schema_version", "source", "truth_state"]

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['gnaww.producer_capability_resource']):
            raise ValueError("must be one of enum values ('gnaww.producer_capability_resource')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['0.1']):
            raise ValueError("must be one of enum values ('0.1')")
        return value

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['published_profile', 'demo_fixture', 'api_derived_demo']):
            raise ValueError("must be one of enum values ('published_profile', 'demo_fixture', 'api_derived_demo')")
        return value

    @field_validator('truth_state')
    def truth_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['published_capability', 'fixture_backed', 'live_api_derived']):
            raise ValueError("must be one of enum values ('published_capability', 'fixture_backed', 'live_api_derived')")
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
        """Create an instance of ProducerCapabilityResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item_products in self.products:
                if _item_products:
                    _items.append(_item_products.to_dict())
            _dict['products'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProducerCapabilityResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "is_live_supplier": obj.get("is_live_supplier"),
            "producer_id": obj.get("producer_id"),
            "producer_name": obj.get("producer_name"),
            "producer_profile_id": obj.get("producer_profile_id"),
            "producer_profile_schema_version": obj.get("producer_profile_schema_version"),
            "products": [ProducerProductCapability.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "schema_name": obj.get("schema_name"),
            "schema_version": obj.get("schema_version"),
            "source": obj.get("source"),
            "truth_state": obj.get("truth_state")
        })
        return _obj
