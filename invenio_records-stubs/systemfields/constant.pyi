from typing import Any, Self, overload

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField

class ConstantField(SystemField):  # type: ignore[misc]
    value: Any

    def __init__(
        self,
        key: str | None = ...,
        value: Any = ...,
    ): ...
    def pre_init(
        self,
        record: Record,
        data: dict[str, Any] | None,
        model: Any = ...,
        **kwargs: Any,
    ) -> None: ...
    @overload  # type: ignore[override]
    def __get__(self, instance: None, owner: type[Record]) -> Self: ...  # type: ignore # keep typing tighter
    @overload
    def __get__(  # type: ignore # keep typing tighter
        self, instance: Record, owner: type[Record],
    ) -> Any: ...
    def __set__(self, instance: Record, value: Any) -> None: ...  # type: ignore[override]
