
from collections.abc import Callable
from typing import Any

from flask_admin.contrib.sqla import (
    ModelView,  # type: ignore[reportMissingTypeStubs,import-not-found]
)
from invenio_admin.filters import (
    FilterConverter,  # type: ignore[reportMissingTypeStubs,import-not-found]
)
from invenio_records.models import RecordMetadata

class RecordMetadataModelView(ModelView):
    filter_converter: FilterConverter
    can_create: bool
    can_edit: bool
    can_delete: bool
    can_view_details: bool
    column_list: tuple[str, ...]
    column_details_list: tuple[str, ...]
    column_labels: dict[str, Any]
    column_formatters: dict[str, Callable[..., Any]]
    column_filters: tuple[str, ...]
    column_default_sort: tuple[str, bool]
    page_size: int

    def delete_model(self, model: RecordMetadata) -> bool: ...

record_adminview: dict[str, Any]
