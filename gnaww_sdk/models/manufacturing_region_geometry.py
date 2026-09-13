# coding: utf-8

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1

"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from gnaww_sdk.models.circle2_d import Circle2D
from gnaww_sdk.models.line2_d import Line2D
from gnaww_sdk.models.path_reference import PathReference
from gnaww_sdk.models.point2_d import Point2D
from gnaww_sdk.models.rectangle2_d import Rectangle2D
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

MANUFACTURINGREGIONGEOMETRY_ONE_OF_SCHEMAS = ["Circle2D", "Line2D", "PathReference", "Point2D", "Rectangle2D"]

class ManufacturingRegionGeometry(BaseModel):
    """
    ManufacturingRegionGeometry
    """
    # data type: Point2D
    oneof_schema_1_validator: Optional[Point2D] = None
    # data type: Line2D
    oneof_schema_2_validator: Optional[Line2D] = None
    # data type: Rectangle2D
    oneof_schema_3_validator: Optional[Rectangle2D] = None
    # data type: Circle2D
    oneof_schema_4_validator: Optional[Circle2D] = None
    # data type: PathReference
    oneof_schema_5_validator: Optional[PathReference] = None
    actual_instance: Optional[Union[Circle2D, Line2D, PathReference, Point2D, Rectangle2D]] = None
    one_of_schemas: Set[str] = { "Circle2D", "Line2D", "PathReference", "Point2D", "Rectangle2D" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
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
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = ManufacturingRegionGeometry.model_construct()
        error_messages = []
        match = 0
        # validate data type: Point2D
        if not isinstance(v, Point2D):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Point2D`")
        else:
            match += 1
        # validate data type: Line2D
        if not isinstance(v, Line2D):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Line2D`")
        else:
            match += 1
        # validate data type: Rectangle2D
        if not isinstance(v, Rectangle2D):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Rectangle2D`")
        else:
            match += 1
        # validate data type: Circle2D
        if not isinstance(v, Circle2D):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Circle2D`")
        else:
            match += 1
        # validate data type: PathReference
        if not isinstance(v, PathReference):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PathReference`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ManufacturingRegionGeometry with oneOf schemas: Circle2D, Line2D, PathReference, Point2D, Rectangle2D. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ManufacturingRegionGeometry with oneOf schemas: Circle2D, Line2D, PathReference, Point2D, Rectangle2D. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: Optional[str]) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into Point2D
        try:
            instance.actual_instance = Point2D.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Line2D
        try:
            instance.actual_instance = Line2D.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Rectangle2D
        try:
            instance.actual_instance = Rectangle2D.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Circle2D
        try:
            instance.actual_instance = Circle2D.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PathReference
        try:
            instance.actual_instance = PathReference.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ManufacturingRegionGeometry with oneOf schemas: Circle2D, Line2D, PathReference, Point2D, Rectangle2D. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ManufacturingRegionGeometry with oneOf schemas: Circle2D, Line2D, PathReference, Point2D, Rectangle2D. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], Circle2D, Line2D, PathReference, Point2D, Rectangle2D]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
