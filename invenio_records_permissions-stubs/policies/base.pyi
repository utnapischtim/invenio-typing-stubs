from typing import Any

from flask_principal import Need
from invenio_access import Permission
from invenio_records_permissions.generators import Generator
from invenio_search.engine import dsl

class BasePermissionPolicy(Permission):
    # NOTE: tuples keep the defaults immutable on the base but subclasses can
    # safely override the attribute with their own tuple of generators.
    can_search: tuple[Generator, ...]
    can_create: tuple[Generator, ...]
    can_read: tuple[Generator, ...]
    can_update: tuple[Generator, ...]
    can_delete: tuple[Generator, ...]
    action: str
    over: dict[str, Any]
    def __init__(self, action: str, **over: Any) -> None: ...
    @property
    def generators(self) -> list[Generator]: ...
    @property
    def needs(self) -> set[Need]: ...
    @property
    def excludes(self) -> set[Need]: ...
    def _query_filters_superuser(
        self, filters: list[dsl.query.Query],
    ) -> list[dsl.query.Query]: ...
    @property
    def query_filters(self) -> list[dsl.query.Query]: ...
