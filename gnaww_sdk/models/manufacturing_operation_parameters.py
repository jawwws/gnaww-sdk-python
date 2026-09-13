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
from gnaww_sdk.models.assembly_operation_parameters import AssemblyOperationParameters
from gnaww_sdk.models.cut_operation_parameters import CutOperationParameters
from gnaww_sdk.models.decoration_operation_parameters import DecorationOperationParameters
from gnaww_sdk.models.drill_operation_parameters import DrillOperationParameters
from gnaww_sdk.models.fold_operation_parameters import FoldOperationParameters
from gnaww_sdk.models.inspect_operation_parameters import InspectOperationParameters
from gnaww_sdk.models.legacy_operation_parameters import LegacyOperationParameters
from gnaww_sdk.models.print_operation_parameters import PrintOperationParameters
from gnaww_sdk.models.surface_operation_parameters import SurfaceOperationParameters
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

MANUFACTURINGOPERATIONPARAMETERS_ONE_OF_SCHEMAS = ["AssemblyOperationParameters", "CutOperationParameters", "DecorationOperationParameters", "DrillOperationParameters", "FoldOperationParameters", "InspectOperationParameters", "LegacyOperationParameters", "PrintOperationParameters", "SurfaceOperationParameters"]

class ManufacturingOperationParameters(BaseModel):
    """
    ManufacturingOperationParameters
    """
    # data type: PrintOperationParameters
    oneof_schema_1_validator: Optional[PrintOperationParameters] = None
    # data type: FoldOperationParameters
    oneof_schema_2_validator: Optional[FoldOperationParameters] = None
    # data type: DrillOperationParameters
    oneof_schema_3_validator: Optional[DrillOperationParameters] = None
    # data type: CutOperationParameters
    oneof_schema_4_validator: Optional[CutOperationParameters] = None
    # data type: SurfaceOperationParameters
    oneof_schema_5_validator: Optional[SurfaceOperationParameters] = None
    # data type: DecorationOperationParameters
    oneof_schema_6_validator: Optional[DecorationOperationParameters] = None
    # data type: AssemblyOperationParameters
    oneof_schema_7_validator: Optional[AssemblyOperationParameters] = None
    # data type: InspectOperationParameters
    oneof_schema_8_validator: Optional[InspectOperationParameters] = None
    # data type: LegacyOperationParameters
    oneof_schema_9_validator: Optional[LegacyOperationParameters] = None
    actual_instance: Optional[Union[AssemblyOperationParameters, CutOperationParameters, DecorationOperationParameters, DrillOperationParameters, FoldOperationParameters, InspectOperationParameters, LegacyOperationParameters, PrintOperationParameters, SurfaceOperationParameters]] = None
    one_of_schemas: Set[str] = { "AssemblyOperationParameters", "CutOperationParameters", "DecorationOperationParameters", "DrillOperationParameters", "FoldOperationParameters", "InspectOperationParameters", "LegacyOperationParameters", "PrintOperationParameters", "SurfaceOperationParameters" }

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

        instance = ManufacturingOperationParameters.model_construct()
        error_messages = []
        match = 0
        # validate data type: PrintOperationParameters
        if not isinstance(v, PrintOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PrintOperationParameters`")
        else:
            match += 1
        # validate data type: FoldOperationParameters
        if not isinstance(v, FoldOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoldOperationParameters`")
        else:
            match += 1
        # validate data type: DrillOperationParameters
        if not isinstance(v, DrillOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DrillOperationParameters`")
        else:
            match += 1
        # validate data type: CutOperationParameters
        if not isinstance(v, CutOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CutOperationParameters`")
        else:
            match += 1
        # validate data type: SurfaceOperationParameters
        if not isinstance(v, SurfaceOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SurfaceOperationParameters`")
        else:
            match += 1
        # validate data type: DecorationOperationParameters
        if not isinstance(v, DecorationOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DecorationOperationParameters`")
        else:
            match += 1
        # validate data type: AssemblyOperationParameters
        if not isinstance(v, AssemblyOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AssemblyOperationParameters`")
        else:
            match += 1
        # validate data type: InspectOperationParameters
        if not isinstance(v, InspectOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InspectOperationParameters`")
        else:
            match += 1
        # validate data type: LegacyOperationParameters
        if not isinstance(v, LegacyOperationParameters):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LegacyOperationParameters`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ManufacturingOperationParameters with oneOf schemas: AssemblyOperationParameters, CutOperationParameters, DecorationOperationParameters, DrillOperationParameters, FoldOperationParameters, InspectOperationParameters, LegacyOperationParameters, PrintOperationParameters, SurfaceOperationParameters. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ManufacturingOperationParameters with oneOf schemas: AssemblyOperationParameters, CutOperationParameters, DecorationOperationParameters, DrillOperationParameters, FoldOperationParameters, InspectOperationParameters, LegacyOperationParameters, PrintOperationParameters, SurfaceOperationParameters. Details: " + ", ".join(error_messages))
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

        # deserialize data into PrintOperationParameters
        try:
            instance.actual_instance = PrintOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FoldOperationParameters
        try:
            instance.actual_instance = FoldOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DrillOperationParameters
        try:
            instance.actual_instance = DrillOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CutOperationParameters
        try:
            instance.actual_instance = CutOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SurfaceOperationParameters
        try:
            instance.actual_instance = SurfaceOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DecorationOperationParameters
        try:
            instance.actual_instance = DecorationOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AssemblyOperationParameters
        try:
            instance.actual_instance = AssemblyOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InspectOperationParameters
        try:
            instance.actual_instance = InspectOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LegacyOperationParameters
        try:
            instance.actual_instance = LegacyOperationParameters.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ManufacturingOperationParameters with oneOf schemas: AssemblyOperationParameters, CutOperationParameters, DecorationOperationParameters, DrillOperationParameters, FoldOperationParameters, InspectOperationParameters, LegacyOperationParameters, PrintOperationParameters, SurfaceOperationParameters. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ManufacturingOperationParameters with oneOf schemas: AssemblyOperationParameters, CutOperationParameters, DecorationOperationParameters, DrillOperationParameters, FoldOperationParameters, InspectOperationParameters, LegacyOperationParameters, PrintOperationParameters, SurfaceOperationParameters. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], AssemblyOperationParameters, CutOperationParameters, DecorationOperationParameters, DrillOperationParameters, FoldOperationParameters, InspectOperationParameters, LegacyOperationParameters, PrintOperationParameters, SurfaceOperationParameters]]:
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
