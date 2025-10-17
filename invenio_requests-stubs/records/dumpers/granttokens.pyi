from typing import (
    Any,
)

from invenio_records.api import Record
from invenio_records.dumpers import SearchDumperExt

class GrantTokensDumperExt(SearchDumperExt):
    grants_field: str
    fields: tuple[str, ...]

    def __init__(self, *fields: str) -> None: ...
    def dump(self, record: Record, data: dict[str, Any]) -> None: ...
    def load(self, data: dict[str, Any], record_cls: type[Record]) -> None: ...
