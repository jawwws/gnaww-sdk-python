# coding: utf-8

"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1
    Gnaww SDK

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from gnaww_sdk.models.issue_set import IssueSet
from gnaww_sdk.models.print_job_specification import PrintJobSpecification
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransformResponse(BaseModel):
    """
    Response payload for `POST /v1/transform`.
    """ # noqa: E501
    confidence: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = 0.0
    issues: Optional[IssueSet] = None
    job: Optional[PrintJobSpecification] = None
    next_actions: Optional[List[StrictStr]] = None
    schema_name: Optional[StrictStr] = 'jawwws.transform_response'
    schema_version: Optional[StrictStr] = '0.1'
    status: StrictStr
    unresolved_fields: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["confidence", "issues", "job", "next_actions", "schema_name", "schema_version", "status", "unresolved_fields"]

    @field_validator('schema_name')
    def schema_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['jawwws.transform_response']):
            raise ValueError("must be one of enum values ('jawwws.transform_response')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['mapped', 'needs_review', 'blocked', 'failed']):
            raise ValueError("must be one of enum values ('mapped', 'needs_review', 'blocked', 'failed')")
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
        """Create an instance of TransformResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['job'] = self.job.to_dict()
        # set to None if job (nullable) is None
        # and model_fields_set contains the field
        if self.job is None and "job" in self.model_fields_set:
            _dict['job'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransformResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confidence": obj.get("confidence") if obj.get("confidence") is not None else 0.0,
            "issues": IssueSet.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "job": PrintJobSpecification.from_dict(obj["job"]) if obj.get("job") is not None else None,
            "next_actions": obj.get("next_actions"),
            "schema_name": obj.get("schema_name") if obj.get("schema_name") is not None else 'jawwws.transform_response',
            "schema_version": obj.get("schema_version") if obj.get("schema_version") is not None else '0.1',
            "status": obj.get("status"),
            "unresolved_fields": obj.get("unresolved_fields")
        })
        return _obj
