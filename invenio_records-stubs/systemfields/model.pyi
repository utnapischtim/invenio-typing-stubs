from typing import Any, Self, overload

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField

class ModelField(SystemField):  # type: ignore[misc]
    _model_field_name: str | None
    dump: bool
    _dump_key: str | None
    _dump_type: Any | None

    def __init__(
        self,
        model_field_name: str | None = ...,
        dump: bool = ...,
        dump_key: str | None = ...,
        dump_type: Any | None = ...,
        **kwargs: Any,
    ): ...
    def _set(self, model: Any, value: Any) -> None: ...
    @property
    def dump_key(self) -> str: ...
    @property
    def dump_type(self) -> Any | None: ...
    @property
    def model_field_name(self) -> str: ...
    def post_init(
        self,
        record: Record,
        data: dict[str, Any],
        model: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    @overload  # type: ignore[override]
    def __get__(self, instance: None, owner: type[Record]) -> Self: ...  # type: ignore # keep typing tighter
    @overload
    def __get__(  # type: ignore # keep typing tighter
        self, instance: Record, owner: type[Record],
    ) -> Any: ...
    def __set__(self, instance: Record, value: Any) -> None: ...  # type: ignore[override]
