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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SpecificationFieldProvenance(BaseModel):
    """
    Safe provenance for one canonical demand field.
    """ # noqa: E501
    path: Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    provenance: StrictStr
    source_reference: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    __properties: ClassVar[List[str]] = ["path", "provenance", "source_reference"]

    @field_validator('provenance')
    def provenance_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['supplied', 'confirmed_review', 'user_input', 'user_override', 'catalogue_guidance', 'deterministic_taxonomy']):
            raise ValueError("must be one of enum values ('supplied', 'confirmed_review', 'user_input', 'user_override', 'catalogue_guidance', 'deterministic_taxonomy')")
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
        """Create an instance of SpecificationFieldProvenance from a JSON string"""
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
        # set to None if source_reference (nullable) is None
        # and model_fields_set contains the field
        if self.source_reference is None and "source_reference" in self.model_fields_set:
            _dict['source_reference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpecificationFieldProvenance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "path": obj.get("path"),
            "provenance": obj.get("provenance"),
            "source_reference": obj.get("source_reference")
        })
        return _obj
