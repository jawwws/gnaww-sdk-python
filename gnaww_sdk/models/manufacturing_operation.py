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
from gnaww_sdk.models.manufacturing_operation_parameters import ManufacturingOperationParameters
from gnaww_sdk.models.operation_target import OperationTarget
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ManufacturingOperation(BaseModel):
    """
    ManufacturingOperation
    """ # noqa: E501
    category: StrictStr
    depends_on: Optional[List[Annotated[str, Field(strict=True)]]] = None
    method: Optional[StrictStr] = None
    operation_id: Annotated[str, Field(strict=True)]
    parameters: Optional[ManufacturingOperationParameters] = None
    targets: Annotated[List[OperationTarget], Field(min_length=1)]
    __properties: ClassVar[List[str]] = ["category", "depends_on", "method", "operation_id", "parameters", "targets"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['print', 'decorate', 'coat', 'laminate', 'emboss', 'deboss', 'foil', 'spot_finish', 'cut', 'die_cut', 'laser_cut', 'drill', 'perforate', 'crease', 'fold', 'stitch', 'sew', 'bind', 'glue', 'attach', 'assemble', 'cure', 'dry', 'inspect', 'pack', 'other']):
            raise ValueError("must be one of enum values ('print', 'decorate', 'coat', 'laminate', 'emboss', 'deboss', 'foil', 'spot_finish', 'cut', 'die_cut', 'laser_cut', 'drill', 'perforate', 'crease', 'fold', 'stitch', 'sew', 'bind', 'glue', 'attach', 'assemble', 'cure', 'dry', 'inspect', 'pack', 'other')")
        return value

    @field_validator('operation_id')
    def operation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of ManufacturingOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item_targets in self.targets:
                if _item_targets:
                    _items.append(_item_targets.to_dict())
            _dict['targets'] = _items
        # set to None if method (nullable) is None
        # and model_fields_set contains the field
        if self.method is None and "method" in self.model_fields_set:
            _dict['method'] = None

        # set to None if parameters (nullable) is None
        # and model_fields_set contains the field
        if self.parameters is None and "parameters" in self.model_fields_set:
            _dict['parameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManufacturingOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "depends_on": obj.get("depends_on"),
            "method": obj.get("method"),
            "operation_id": obj.get("operation_id"),
            "parameters": ManufacturingOperationParameters.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
            "targets": [OperationTarget.from_dict(_item) for _item in obj["targets"]] if obj.get("targets") is not None else None
        })
        return _obj
