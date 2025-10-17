
from collections.abc import Mapping
from typing import Any

from marshmallow import Schema as Schema
from marshmallow import fields as fields
from marshmallow import missing as missing

PROFILE_URL: str

class DataPackageSchema(Schema):
    profile: fields.Constant
    id: fields.Str
    name: fields.Str
    title: fields.Str
    description: fields.Str
    version: fields.Str
    created: fields.Str
    homepage: fields.Str
    keywords: fields.Method
    resources: fields.Method
    licenses: fields.Method
    contributors: fields.Method

    def get_keywords(self, obj: Mapping[str, Any]) -> list[str] | None: ...
    def get_resources(self, obj: Mapping[str, Any]) -> list[Mapping[str, Any]]: ...
    def get_licenses(
        self, obj: Mapping[str, Any],
    ) -> list[Mapping[str, Any]] | None: ...
    def get_contributors(
        self, obj: Mapping[str, Any],
    ) -> list[Mapping[str, Any]] | None: ...
