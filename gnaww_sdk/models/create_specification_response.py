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
from gnaww_sdk.models.specification_resource import SpecificationResource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CreateSpecificationResponse(BaseModel):
    """
    Result of explicit canonical-demand retention.
    """ # noqa: E501
    schema_name: Optional[StrictStr] = 'gnaww.specification_create_result'
    schema_version: Optional[StrictStr] = '0.1'
    specification: SpecificationResource
    status: StrictStr
    __properties: ClassVar[List[str]] = ["schema_name", "schema_version", "specification", "status"]

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.specification_create_result']):
            raise ValueError("must be one of enum values ('gnaww.specification_create_result')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.1']):
            raise ValueError("must be one of enum values ('0.1')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['created', 'existing']):
            raise ValueError("must be one of enum values ('created', 'existing')")
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
        """Create an instance of CreateSpecificationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of specification
        if self.specification:
            _dict['specification'] = self.specification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSpecificationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.specification_create_result',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "specification": SpecificationResource.from_dict(obj["specification"]) if obj.get("specification") is not None else None,
            "status": obj.get("status")
        })
        return _obj
