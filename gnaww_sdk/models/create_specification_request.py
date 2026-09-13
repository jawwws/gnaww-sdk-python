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
from gnaww_sdk.models.gjs import Gjs
from gnaww_sdk.models.specification_external_reference import SpecificationExternalReference
from gnaww_sdk.models.specification_field_provenance import SpecificationFieldProvenance
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CreateSpecificationRequest(BaseModel):
    """
    Explicitly retain one completed canonical Gnaww Job Specification.
    """ # noqa: E501
    external_references: Optional[Annotated[List[SpecificationExternalReference], Field(max_length=20)]] = None
    field_provenance: Optional[Annotated[List[SpecificationFieldProvenance], Field(max_length=200)]] = None
    gjs: Gjs
    idempotency_key: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = None
    schema_name: Optional[StrictStr] = 'gnaww.specification_create_request'
    schema_version: Optional[StrictStr] = '0.1'
    __properties: ClassVar[List[str]] = ["external_references", "field_provenance", "gjs", "idempotency_key", "schema_name", "schema_version"]

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.specification_create_request']):
            raise ValueError("must be one of enum values ('gnaww.specification_create_request')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.1']):
            raise ValueError("must be one of enum values ('0.1')")
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
        """Create an instance of CreateSpecificationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in external_references (list)
        _items = []
        if self.external_references:
            for _item_external_references in self.external_references:
                if _item_external_references:
                    _items.append(_item_external_references.to_dict())
            _dict['external_references'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in field_provenance (list)
        _items = []
        if self.field_provenance:
            for _item_field_provenance in self.field_provenance:
                if _item_field_provenance:
                    _items.append(_item_field_provenance.to_dict())
            _dict['field_provenance'] = _items
        # override the default output from pydantic by calling `to_dict()` of gjs
        if self.gjs:
            _dict['gjs'] = self.gjs.to_dict()
        # set to None if idempotency_key (nullable) is None
        # and model_fields_set contains the field
        if self.idempotency_key is None and "idempotency_key" in self.model_fields_set:
            _dict['idempotency_key'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSpecificationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "external_references": [SpecificationExternalReference.from_dict(_item) for _item in obj["external_references"]] if obj.get("external_references") is not None else None,
            "field_provenance": [SpecificationFieldProvenance.from_dict(_item) for _item in obj["field_provenance"]] if obj.get("field_provenance") is not None else None,
            "gjs": Gjs.from_dict(obj["gjs"]) if obj.get("gjs") is not None else None,
            "idempotency_key": obj.get("idempotency_key"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.specification_create_request',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1'
        })
        return _obj
