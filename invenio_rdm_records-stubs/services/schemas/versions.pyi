
from marshmallow import Schema

class VersionsSchema(Schema):
    field_dump_permissions: dict[str, str]
