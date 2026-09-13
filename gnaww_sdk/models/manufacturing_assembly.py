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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ManufacturingAssembly(BaseModel):
    """
    ManufacturingAssembly
    """ # noqa: E501
    assembly_id: Annotated[str, Field(strict=True)]
    input_component_ids: Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)]
    operation_ids: Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)]
    output_component_id: Optional[Annotated[str, Field(strict=True)]] = None
    __properties: ClassVar[List[str]] = ["assembly_id", "input_component_ids", "operation_ids", "output_component_id"]

    @field_validator('assembly_id')
    def assembly_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9][A-Za-z0-9_.:-]*$/")
        return value

    @field_validator('output_component_id')
    def output_component_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not isinstance(value, str):
            value = str(value)

        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9][A-Za-z0-9_.:-]*$/")
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
        """Create an instance of ManufacturingAssembly from a JSON string"""
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
        # set to None if output_component_id (nullable) is None
        # and model_fields_set contains the field
        if self.output_component_id is None and "output_component_id" in self.model_fields_set:
            _dict['output_component_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManufacturingAssembly from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assembly_id": obj.get("assembly_id"),
            "input_component_ids": obj.get("input_component_ids"),
            "operation_ids": obj.get("operation_ids"),
            "output_component_id": obj.get("output_component_id")
        })
        return _obj
