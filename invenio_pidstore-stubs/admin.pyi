"""Admin model views for PersistentIdentifier.

Type stubs for invenio_pidstore.admin.
"""

from typing import Any
from uuid import UUID as UUID

from markupsafe import Markup as Markup

def _(x: str) -> str: ...
def object_formatter(v: Any, c: Any, m: Any, p: Any) -> Markup | str: ...

class FilterUUID:
    """UUID aware filter."""

    def apply(self, query: Any, value: str, alias: Any) -> Any: ...

class PersistentIdentifierModelView:
    """ModelView for the PersistentIdentifier."""

    can_create: bool
    can_edit: bool
    can_delete: bool
    can_view_details: bool
    column_display_all_relations: bool
    column_list: tuple[str, ...]
    column_labels: dict[str, str]
    column_filters: tuple[Any, ...]
    column_searchable_list: tuple[str, ...]
    column_default_sort: tuple[str, bool]
    column_formatters: dict[str, Any]
    page_size: int

pid_adminview: dict[str, Any]
