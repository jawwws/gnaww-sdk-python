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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gnaww_sdk.models.public_interpretation_continuation_answer import PublicInterpretationContinuationAnswer
from gnaww_sdk.models.source_input import SourceInput
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ContinueInterpretationRequestV02(BaseModel):
    """
    Stateless continuation request keyed by public question identities.
    """ # noqa: E501
    answers: Optional[List[PublicInterpretationContinuationAnswer]] = None
    gjs_version: Optional[StrictStr] = '0.4'
    matching_mode: Optional[StrictStr] = 'single_target'
    schema_name: Optional[StrictStr] = 'gnaww.interpretation_continuation_request'
    schema_version: Optional[StrictStr] = '0.2'
    source: SourceInput
    __properties: ClassVar[List[str]] = ["answers", "gjs_version", "matching_mode", "schema_name", "schema_version", "source"]

    @field_validator('gjs_version')
    def gjs_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.4']):
            raise ValueError("must be one of enum values ('0.4')")
        return value

    @field_validator('matching_mode')
    def matching_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['single_target', 'producer_universe']):
            raise ValueError("must be one of enum values ('single_target', 'producer_universe')")
        return value

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gnaww.interpretation_continuation_request']):
            raise ValueError("must be one of enum values ('gnaww.interpretation_continuation_request')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0.2']):
            raise ValueError("must be one of enum values ('0.2')")
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
        """Create an instance of ContinueInterpretationRequestV02 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in answers (list)
        _items = []
        if self.answers:
            for _item_answers in self.answers:
                if _item_answers:
                    _items.append(_item_answers.to_dict())
            _dict['answers'] = _items
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContinueInterpretationRequestV02 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "answers": [PublicInterpretationContinuationAnswer.from_dict(_item) for _item in obj["answers"]] if obj.get("answers") is not None else None,
            "gjs_version": obj.get("gjs_version") if obj.get("gjs_version") is not None else '0.4',
            "matching_mode": obj.get("matching_mode") if obj.get("matching_mode") is not None else 'single_target',
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'gnaww.interpretation_continuation_request',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.2',
            "source": SourceInput.from_dict(obj["source"]) if obj.get("source") is not None else None
        })
        return _obj
