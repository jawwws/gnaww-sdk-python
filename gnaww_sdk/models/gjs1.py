# coding: utf-8

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1
    Gnaww SDK

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from gnaww_sdk.models.print_job_specification import PrintJobSpecification
from gnaww_sdk.models.print_job_specification_v04 import PrintJobSpecificationV04
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

GJS1_ANY_OF_SCHEMAS = ["PrintJobSpecification", "PrintJobSpecificationV04"]

class Gjs1(BaseModel):
    """
    Gjs1
    """

    # data type: PrintJobSpecificationV04
    anyof_schema_1_validator: Optional[PrintJobSpecificationV04] = None
    # data type: PrintJobSpecification
    anyof_schema_2_validator: Optional[PrintJobSpecification] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[PrintJobSpecification, PrintJobSpecificationV04]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "PrintJobSpecification", "PrintJobSpecificationV04" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = Gjs1.model_construct()
        error_messages = []
        # validate data type: PrintJobSpecificationV04
        if not isinstance(v, PrintJobSpecificationV04):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PrintJobSpecificationV04`")
        else:
            return v

        # validate data type: PrintJobSpecification
        if not isinstance(v, PrintJobSpecification):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PrintJobSpecification`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Gjs1 with anyOf schemas: PrintJobSpecification, PrintJobSpecificationV04. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[PrintJobSpecificationV04] = None
        try:
            instance.actual_instance = PrintJobSpecificationV04.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[PrintJobSpecification] = None
        try:
            instance.actual_instance = PrintJobSpecification.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Gjs1 with anyOf schemas: PrintJobSpecification, PrintJobSpecificationV04. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], PrintJobSpecification, PrintJobSpecificationV04]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
