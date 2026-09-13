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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PublicJobStructure(BaseModel):
    """
    A semantic Variant, Component or Operation kept within one Job.
    """ # noqa: E501
    kind: StrictStr
    label: Annotated[str, Field(min_length=1, strict=True)]
    provenance: Optional[StrictStr] = 'supplied'
    source_expression: Optional[StrictStr] = None
    structure_id: Annotated[str, Field(strict=True)]
    values: Optional[Annotated[List[StrictStr], Field(max_length=20)]] = None
    __properties: ClassVar[List[str]] = ["kind", "label", "provenance", "source_expression", "structure_id", "values"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['variant', 'component', 'operation']):
            raise ValueError("must be one of enum values ('variant', 'component', 'operation')")
        return value

    @field_validator('provenance')
    def provenance_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['supplied', 'derived', 'confirmed', 'controlled']):
            raise ValueError("must be one of enum values ('supplied', 'derived', 'confirmed', 'controlled')")
        return value

    @field_validator('structure_id')
    def structure_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[a-z][a-z0-9_.-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_.-]*$/")
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
        """Create an instance of PublicJobStructure from a JSON string"""
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
        # set to None if source_expression (nullable) is None
        # and model_fields_set contains the field
        if self.source_expression is None and "source_expression" in self.model_fields_set:
            _dict['source_expression'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicJobStructure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kind": obj.get("kind"),
            "label": obj.get("label"),
            "provenance": obj.get("provenance") if obj.get("provenance") is not None else 'supplied',
            "source_expression": obj.get("source_expression"),
            "structure_id": obj.get("structure_id"),
            "values": obj.get("values")
        })
        return _obj
