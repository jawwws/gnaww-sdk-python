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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.gjs import Gjs
from gnaww_sdk.models.specification_external_reference import SpecificationExternalReference
from gnaww_sdk.models.specification_field_provenance import SpecificationFieldProvenance
from gnaww_sdk.models.specification_recipe_reference import SpecificationRecipeReference
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SpecificationResource(BaseModel):
    """
    Safe immutable public representation of retained canonical demand.
    """ # noqa: E501
    content_fingerprint_sha256: Annotated[str, Field(strict=True)]
    created_at: datetime
    external_references: Optional[List[SpecificationExternalReference]] = None
    field_provenance: Optional[List[SpecificationFieldProvenance]] = None
    gjs: Gjs
    gjs_schema_name: Optional[StrictStr] = 'jawwws.print_job_specification'
    gjs_schema_version: StrictStr
    immutable: Optional[StrictBool] = True
    recipe: SpecificationRecipeReference
    resource_version: Optional[Annotated[int, Field(le=1, strict=True, ge=1)]] = 1
    schema_name: Optional[StrictStr] = 'gnaww.specification_resource'
    schema_version: Optional[StrictStr] = '0.1'
    specification_id: Annotated[str, Field(strict=True)]
    __properties: ClassVar[List[str]] = ["content_fingerprint_sha256", "created_at", "external_references", "field_provenance", "gjs", "gjs_schema_name", "gjs_schema_version", "immutable", "recipe", "resource_version", "schema_name", "schema_version", "specification_id"]

    @field_validator('content_fingerprint_sha256')
    def content_fingerprint_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[a-f0-9]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{64}$/")
        return value

    @field_validator('gjs_schema_name')
    def gjs_schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['jawwws.print_job_specification']):
            raise ValueError("must be one of enum values ('jawwws.print_job_specification')")
        return value

    @field_validator('immutable')
    def immutable_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.specification_resource']):
            raise ValueError("must be one of enum values ('gnaww.specification_resource')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.1']):
            raise ValueError("must be one of enum values ('0.1')")
        return value

    @field_validator('specification_id')
    def specification_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^GNS-[a-f0-9]{32}$", value):
            raise ValueError(r"must validate the regular expression /^GNS-[a-f0-9]{32}$/")
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
        """Create an instance of SpecificationResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recipe
        if self.recipe:
            _dict['recipe'] = self.recipe.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpecificationResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content_fingerprint_sha256": obj.get("content_fingerprint_sha256"),
            "created_at": obj.get("created_at"),
            "external_references": [SpecificationExternalReference.from_dict(_item) for _item in obj["external_references"]] if obj.get("external_references") is not None else None,
            "field_provenance": [SpecificationFieldProvenance.from_dict(_item) for _item in obj["field_provenance"]] if obj.get("field_provenance") is not None else None,
            "gjs": Gjs.from_dict(obj["gjs"]) if obj.get("gjs") is not None else None,
            "gjs_schema_name": obj.get("gjs_schema_name") if obj.get("gjs_schema_name") is not None else 'jawwws.print_job_specification',
            "gjs_schema_version": obj.get("gjs_schema_version"),
            "immutable": obj.get("immutable") if obj.get("immutable") is not None else True,
            "recipe": SpecificationRecipeReference.from_dict(obj["recipe"]) if obj.get("recipe") is not None else None,
            "resource_version": obj.get("resource_version") if obj.get("resource_version") is not None else 1,
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.specification_resource',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "specification_id": obj.get("specification_id")
        })
        return _obj
