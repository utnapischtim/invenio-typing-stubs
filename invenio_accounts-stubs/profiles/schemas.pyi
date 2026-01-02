from marshmallow import Schema
from marshmallow.fields import String


def validate_visibility(value: str) -> None: ...
def validate_locale(value: str) -> None: ...
def validate_timezone(value: str) -> None: ...

class UserProfileSchema(Schema):
    full_name: String
    affiliations: String

class UserPreferencesSchema(Schema):
    visibility: String
    email_visibility: String
    locale: String
    timezone: String
