from collections.abc import Callable
from typing import Any, overload

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField, SystemFieldContext

class RelatedModelFieldContext[R: Record = Record](SystemFieldContext):
    def session_merge(self, record: R) -> None: ...

class RelatedModelField(SystemField):
    _model: type[Any]
    _required: bool
    _load: Callable[..., Any | None]
    _dump: Callable[..., None]
    _context_cls: type[RelatedModelFieldContext]

    def __init__(
        self,
        model: type[Any],
        key: str | None = ...,
        required: bool = ...,
        load: Callable[..., Any | None] | None = ...,
        dump: Callable[..., None] | None = ...,
        context_cls: type[RelatedModelFieldContext] | None = ...,
    ): ...
    def pre_commit(self, record: Record) -> None: ...
    def obj(self, record: Record) -> Any | None: ...
    def set_obj(self, record: Record, obj: Any) -> None: ...
    @overload  # type: ignore[override] # not consistent with systemfield
    def __get__(  # type: ignore[override] # not consistent with systemfield
        self, instance: None, owner: type[Record],
    ) -> RelatedModelFieldContext: ...
    @overload
    def __get__(self, instance: Record, owner: type[Record]) -> Any: ...  # type: ignore[override] # not consistent with systemfield
    def __set__(self, instance: Record, value: Any) -> None: ...  # type: ignore[override]
