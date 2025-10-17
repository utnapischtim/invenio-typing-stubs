from collections.abc import Callable
from typing import Any

from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import Record
from invenio_records_resources.references.entity_resolvers import EntityProxy

class ReferencedEntityField(SystemField):
    _ref_check: Callable[[Record, dict[str, str] | None], bool] | None
    _registry: Any

    def __init__(
        self,
        key: str | None = ...,
        reference_check_func: Callable[[Record, dict[str, str] | None], bool] | None = ...,
        resolver_registry: Any = ...,
    ) -> None: ...
    def _check_reference(
        self, instance: Record, ref_dict: dict[str, str] | None,
    ) -> bool: ...
    def set_obj(
        self,
        instance: Record,
        obj: dict[str, str] | EntityProxy | Any | None,
    ) -> None: ...
    def obj(self, instance: Record) -> EntityProxy | None: ...

class MultiReferenceEntityField(ReferencedEntityField):
    def set_obj(self, instance: Record, obj: Any) -> None: ...
    def obj(self, instance: Record) -> list[EntityProxy]: ...  # type: ignore[override]

def check_allowed_references(
    get_allows_none: Callable[[Record], bool],
    get_allowed_types: Callable[[Record], list[str]],
    request: Record,
    ref_dict: dict[str, str] | None,
) -> bool: ...
