from typing import Any

from flask_principal import Identity
from invenio_records_resources.services.records.params import SuggestQueryParser
from invenio_search.engine import dsl

class FilteredSuggestQueryParser(SuggestQueryParser):
    filter_field: str | None
    def __init__(
        self,
        identity: Identity | None = None,
        filter_field: str | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> None: ...
    def parse(self, query_str: str) -> dsl.query.Query: ...
    def extract_subtype_s(self, query_str: str) -> tuple[list[str], str]: ...
