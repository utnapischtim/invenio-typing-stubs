from collections.abc import Callable
from typing import Any

from invenio_requests.proxies import current_requests as current_requests
from marshmallow import fields
from marshmallow.schema import Schema

class EventType:
    type_id: str | None
    payload_schema: dict[str, fields.Field] | Callable[[], dict[str, fields.Field]] | None
    payload_required: bool
    payload: dict[str, Any] | None
    def __init__(self, payload: dict[str, Any] | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @classmethod
    def _create_marshmallow_schema(cls) -> type[Schema]: ...
    @classmethod
    def marshmallow_schema(cls) -> type[Schema]: ...

class LogEventType(EventType):
    @staticmethod
    def payload_schema() -> dict[str, fields.Field]: ...

class ReviewersUpdatedType(EventType):
    @staticmethod
    def payload_schema() -> dict[str, fields.Field]: ...

class CommentEventType(EventType):
    @staticmethod
    def payload_schema() -> dict[str, fields.Field]: ...
    payload_required: bool
