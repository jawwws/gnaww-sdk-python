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
from gnaww_sdk.models.operation_target import OperationTarget
from gnaww_sdk.models.variation_field import VariationField
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ManufacturingVariation(BaseModel):
    """
    ManufacturingVariation
    """ # noqa: E501
    data_asset_ref: Optional[StrictStr] = None
    fields: Optional[List[VariationField]] = None
    scope: StrictStr
    source_basis: Optional[StrictStr] = 'explicit'
    targets: Annotated[List[OperationTarget], Field(min_length=1)]
    variation_id: Annotated[str, Field(strict=True)]
    __properties: ClassVar[List[str]] = ["data_asset_ref", "fields", "scope", "source_basis", "targets", "variation_id"]

    @field_validator('scope')
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['per_unit', 'grouped', 'batch']):
            raise ValueError("must be one of enum values ('per_unit', 'grouped', 'batch')")
        return value

    @field_validator('source_basis')
    def source_basis_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['explicit', 'legacy_variable_data']):
            raise ValueError("must be one of enum values ('explicit', 'legacy_variable_data')")
        return value

    @field_validator('variation_id')
    def variation_id_validate_regular_expression(cls, value):
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
        """Create an instance of ManufacturingVariation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item_targets in self.targets:
                if _item_targets:
                    _items.append(_item_targets.to_dict())
            _dict['targets'] = _items
        # set to None if data_asset_ref (nullable) is None
        # and model_fields_set contains the field
        if self.data_asset_ref is None and "data_asset_ref" in self.model_fields_set:
            _dict['data_asset_ref'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManufacturingVariation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data_asset_ref": obj.get("data_asset_ref"),
            "fields": [VariationField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "scope": obj.get("scope"),
            "source_basis": obj.get("source_basis") if obj.get("source_basis") is not None else 'explicit',
            "targets": [OperationTarget.from_dict(_item) for _item in obj["targets"]] if obj.get("targets") is not None else None,
            "variation_id": obj.get("variation_id")
        })
        return _obj
