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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gnaww_sdk.models.public_match_target_request import PublicMatchTargetRequest
from gnaww_sdk.models.service_requirements import ServiceRequirements
from gnaww_sdk.models.use_requirement import UseRequirement
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MatchRecipeRequest(BaseModel):
    """
    Run context supplied when matching one persisted Recipe.
    """ # noqa: E501
    quantity: Annotated[int, Field(strict=True, gt=0)]
    schema_name: Optional[StrictStr] = 'gnaww.recipe_specmatch_request'
    schema_version: Optional[StrictStr] = '0.1'
    service_requirements: Optional[ServiceRequirements] = None
    target: PublicMatchTargetRequest
    use_requirements: Optional[List[UseRequirement]] = None
    __properties: ClassVar[List[str]] = ["quantity", "schema_name", "schema_version", "service_requirements", "target", "use_requirements"]

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.recipe_specmatch_request']):
            raise ValueError("must be one of enum values ('gnaww.recipe_specmatch_request')")
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
        """Create an instance of MatchRecipeRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of service_requirements
        if self.service_requirements:
            _dict['service_requirements'] = self.service_requirements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in use_requirements (list)
        _items = []
        if self.use_requirements:
            for _item_use_requirements in self.use_requirements:
                if _item_use_requirements:
                    _items.append(_item_use_requirements.to_dict())
            _dict['use_requirements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchRecipeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.recipe_specmatch_request',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "service_requirements": ServiceRequirements.from_dict(obj["service_requirements"]) if obj.get("service_requirements") is not None else None,
            "target": PublicMatchTargetRequest.from_dict(obj["target"]) if obj.get("target") is not None else None,
            "use_requirements": [UseRequirement.from_dict(_item) for _item in obj["use_requirements"]] if obj.get("use_requirements") is not None else None
        })
        return _obj
