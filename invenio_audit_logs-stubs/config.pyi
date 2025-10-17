from typing import Any

from invenio_records_resources.services.records.facets import TermsFacet as TermsFacet

# NOTE: Facets config follows the common pattern used across Invenio packages.

AUDIT_LOGS_SEARCH: dict[str, list[str]]
AUDIT_LOGS_FACETS: dict[
    str, dict[str, Any],
]  # {"facet": TermsFacet, "ui": {"field": str}}
AUDIT_LOGS_SORT_OPTIONS: dict[
    str, dict[str, Any],
]  # {"title": str, "fields": List[str]}
AUDIT_LOGS_ENABLED: bool
AUDIT_LOGS_METADATA_FIELDS: dict[str, bool]
