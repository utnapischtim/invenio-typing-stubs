from typing import Any

from marshmallow import Schema, fields, post_load, pre_load

class MinimalCommunitySchema(Schema):
    slug: fields.String
    title: fields.String
    @post_load
    def load_default(self, data: dict[str, str], **kwargs) -> dict[str, Any]: ...

class SubcommunityRequestSchema(Schema):
    community_id: fields.String
    community: fields.Nested
    @pre_load
    def validate(self, data: dict[str, Any], **kwargs) -> dict[str, Any]: ...
