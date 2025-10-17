
from collections.abc import Mapping
from typing import Any

from marshmallow import Schema as Schema
from marshmallow import fields as fields

class GeoJSONSchema(Schema):
    features: fields.Method
    type: fields.Constant
    def get_locations(self, obj: Mapping[str, Any]) -> list[Mapping[str, Any]]: ...
