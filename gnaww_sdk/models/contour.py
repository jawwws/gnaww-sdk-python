# coding: utf-8

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1

"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from gnaww_sdk.models.circle2_d import Circle2D
from gnaww_sdk.models.line2_d import Line2D
from gnaww_sdk.models.path_reference import PathReference
from gnaww_sdk.models.rectangle2_d import Rectangle2D
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

CONTOUR_ANY_OF_SCHEMAS = ["Circle2D", "Line2D", "PathReference", "Rectangle2D"]

class Contour(BaseModel):
    """
    Contour
    """

    # data type: Line2D
    anyof_schema_1_validator: Optional[Line2D] = None
    # data type: Rectangle2D
    anyof_schema_2_validator: Optional[Rectangle2D] = None
    # data type: Circle2D
    anyof_schema_3_validator: Optional[Circle2D] = None
    # data type: PathReference
    anyof_schema_4_validator: Optional[PathReference] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[Circle2D, Line2D, PathReference, Rectangle2D]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "Circle2D", "Line2D", "PathReference", "Rectangle2D" }

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
        if v is None:
            return v

        instance = Contour.model_construct()
        error_messages = []
        # validate data type: Line2D
        if not isinstance(v, Line2D):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Line2D`")
        else:
            return v

        # validate data type: Rectangle2D
        if not isinstance(v, Rectangle2D):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Rectangle2D`")
        else:
            return v

        # validate data type: Circle2D
        if not isinstance(v, Circle2D):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Circle2D`")
        else:
            return v

        # validate data type: PathReference
        if not isinstance(v, PathReference):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PathReference`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Contour with anyOf schemas: Circle2D, Line2D, PathReference, Rectangle2D. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        # anyof_schema_1_validator: Optional[Line2D] = None
        try:
            instance.actual_instance = Line2D.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[Rectangle2D] = None
        try:
            instance.actual_instance = Rectangle2D.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[Circle2D] = None
        try:
            instance.actual_instance = Circle2D.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[PathReference] = None
        try:
            instance.actual_instance = PathReference.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Contour with anyOf schemas: Circle2D, Line2D, PathReference, Rectangle2D. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], Circle2D, Line2D, PathReference, Rectangle2D]]:
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
