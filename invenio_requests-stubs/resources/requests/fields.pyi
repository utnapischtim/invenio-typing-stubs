from collections.abc import Mapping
from typing import Any

from marshmallow import fields

class ReferenceString(fields.Field):
    default_error_messages: dict[str, str]

    def _deserialize(
        self,
        value: str | None,
        attr: str | None,
        data: Mapping[str, Any] | None,
        **kwargs: Any,
    ) -> dict[str, str] | None: ...
    def _serialize(
        self, value: Any, attr: str | None, obj: Any, **kwargs: Any,
    ) -> str: ...
