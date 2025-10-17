from typing import Any

from invenio_records.api import Record
from invenio_records.systemfields.relations.results import RelationResult

class RelationBase:
    result_cls: type[RelationResult]
    key: str | None
    attrs: list[str]
    keys: list[str]
    _value_key_suffix: str
    _clear_empty: bool
    _cache_key: str | None
    value_check: Any | None
    _cache_ref: dict[str, Any] | None

    def __init__(
        self,
        key: str | None = ...,
        attrs: list[str] | None = ...,
        keys: list[str] | None = ...,
        _value_key_suffix: str = ...,
        _clear_empty: bool = ...,
        cache_key: str | None = ...,
        value_check: Any | None = ...,
    ): ...
    def inject_cache(
        self, cache: dict[str, dict[Any, Any]], default_key: str,
    ) -> None: ...
    @property
    def cache(self) -> dict[str, Any]: ...
    def resolve(self, id_: str) -> Record | None: ...
    @property
    def value_key(self) -> str: ...
    def exists(self, id_: str) -> bool: ...
    def exists_many(self, ids: Any) -> bool: ...
    def get_value(self, record: Record) -> RelationResult: ...
    def parse_value(self, value: Any) -> Any: ...
    def set_value(self, record: Record, value: Any) -> None: ...
    def clear_value(self, record: Record) -> None: ...

class PKRelation(RelationBase):
    record_cls: type[Record]

    def __init__(self, *args: Any, record_cls: type[Record] = ..., **kwargs: Any): ...
    def resolve(self, id_: str) -> Record | None: ...

class ListRelation(RelationBase):
    relation_field: str | None

    def __init__(
        self, *args: Any, relation_field: str | None = ..., **kwargs: Any,
    ): ...
    def _get_parent(self, record: Record, keys: list[str]) -> dict[str, Any]: ...

class PKListRelation(ListRelation, PKRelation):
    """Primary-key list relation."""

class NestedListRelation(ListRelation):
    def exists_many(self, ids: list[list[str]]) -> bool: ...

class PKNestedListRelation(NestedListRelation, PKRelation):
    """Primary-key nested list relation."""
