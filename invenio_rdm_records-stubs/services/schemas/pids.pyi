
from marshmallow import Schema
from marshmallow import fields as fields

class PIDSchema(Schema):
    identifier: fields.String
    provider: fields.String
    client: fields.String
