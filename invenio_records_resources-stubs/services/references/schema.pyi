from typing import Any

import marshmallow as ma
from marshmallow import Schema, validates_schema

class EntityReferenceBaseSchema(Schema):
    @validates_schema
    def there_can_be_only_one(self, data: dict[str, Any], **kwargs: Any) -> None: ...
    @classmethod
    def create_from_dict(
        cls,
        allowed_types: list[str],
        special_fields: dict[str, ma.fields.Field] | None = ...,
    ) -> type[EntityReferenceBaseSchema]: ...

class MultipleEntityReferenceBaseSchema(EntityReferenceBaseSchema):
    @classmethod
    def create_from_dict(
        cls,
        allowed_types: list[str],
        special_fields: dict[str, ma.fields.Field] | None = ...,
    ) -> type[MultipleEntityReferenceBaseSchema]: ...
