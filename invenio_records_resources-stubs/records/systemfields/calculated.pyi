from typing import Any

from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import Record

class CalculatedField(SystemField):  # type: ignore[misc]
    _use_cache: bool
    def __init__(self, key: str | None = ..., use_cache: bool = ...) -> None: ...
    def obj(self, instance: Record) -> Any: ...
    def calculate(self, record: Record) -> Any: ...

class CalculatedIndexedField(CalculatedField):
    _index: bool
    def __init__(
        self, key: str | None = ..., use_cache: bool = ..., index: bool = ...,
    ) -> None: ...
    def pre_dump(
        self, record: Record, data: Any, dumper: Any | None = ...,
    ) -> None: ...
    def post_load(
        self, record: Record, data: Any, loader: Any | None = ...,
    ) -> None: ...
