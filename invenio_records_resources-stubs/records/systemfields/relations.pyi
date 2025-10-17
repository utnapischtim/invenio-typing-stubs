from typing import Any

from invenio_pidstore.models import PersistentIdentifier  # type: ignore[import-untyped]
from invenio_records.systemfields.relations import (
    ListRelation,
    NestedListRelation,
    RelationBase,
)
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields.pid import PIDFieldContext

class PIDRelation[R: Record = Record](RelationBase):
    def __init__(
        self, *args: Any, pid_field: PIDFieldContext[R] | None = ..., **kwargs: Any,
    ) -> None: ...
    def resolve(self, id_: str) -> R | None: ...
    def parse_value(self, value: str | PersistentIdentifier | R) -> str: ...

class PIDListRelation(ListRelation, PIDRelation):
    """PID list relation type."""

class PIDNestedListRelation(NestedListRelation, PIDRelation):
    """PID nested list relation type."""
