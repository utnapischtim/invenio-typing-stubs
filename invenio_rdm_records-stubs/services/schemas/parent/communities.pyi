from collections.abc import Mapping
from typing import Any

from marshmallow import Schema, fields

class CommunitiesSchema(Schema):
    ids: fields.List
    default: fields.String
    entries: fields.List

    def clear_none_values(self, data: Mapping[str, Any], **kwargs: Any) -> Mapping[str, Any]: ...
