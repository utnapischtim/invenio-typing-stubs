from typing import (
    Any,
)

from invenio_records.api import Record
from invenio_records.dumpers import SearchDumperExt

class CalculatedFieldDumperExt(SearchDumperExt):
    field: str
    property: str

    def __init__(self, field: str, prop: str | None = None) -> None: ...
    def dump(self, record: Record, data: dict[str, Any]) -> None: ...
    def load(self, data: dict[str, Any], record_cls: type[Record]) -> None: ...
