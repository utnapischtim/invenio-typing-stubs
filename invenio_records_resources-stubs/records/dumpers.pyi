from typing import Any

from invenio_records.api import Record as BaseRecord
from invenio_records.dumpers import Dumper, SearchDumperExt
from invenio_records_resources.records.api import FileRecord

class CustomFieldsDumperExt(SearchDumperExt):
    _fields_var: str
    key: str

    def __init__(self, fields_var: str, key: str = ...) -> None: ...
    def dump(self, record: BaseRecord, data: dict[str, Any]) -> None: ...
    def load(self, data: dict[str, Any], record_cls: type[BaseRecord]) -> None: ...

class PartialFileDumper(Dumper):
    def dump(self, record: BaseRecord, data: dict[Any, Any]) -> dict[
        str,
        dict[str, str] | str | dict[str, str | dict[str, dict[str, str]] | list[str]] | dict[str, dict[str, str]] | list[str],
    ]: ...
    def load(
        self,
        data: dict[str, Any],
        record_cls: type[FileRecord],
    ) -> FileRecord: ...
