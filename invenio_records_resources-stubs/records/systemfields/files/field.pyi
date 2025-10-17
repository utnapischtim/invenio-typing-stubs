from collections.abc import Callable
from typing import Any, Self, overload

from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import FileRecord, Record
from invenio_records_resources.records.systemfields.files.manager import FilesManager

class FilesField(SystemField):
    _store: bool
    _dump: bool
    _dump_entries: bool | Callable[[Record], bool]
    _enabled: bool
    _bucket_id_attr: str
    _bucket_attr: str
    _bucket_args: dict[str, Any]
    _create: bool
    _delete: bool
    _file_cls: type[FileRecord] | None
    def __init__(
        self,
        key: str = ...,
        bucket_id_attr: str = ...,
        bucket_attr: str = ...,
        file_cls: type[FileRecord] | None = ...,
        bucket_args: dict[str, Any] | None = ...,
        *,
        dump_entries: bool | Callable[[Record], bool] = ...,
        store: bool = ...,
        dump: bool = ...,
        enabled: bool = ...,
        create: bool = ...,
        delete: bool = ...,
    ) -> None: ...
    @property
    def _manager_options(self) -> dict[str, Any]: ...
    def dump(
        self,
        record: Record,
        files: FilesManager,
        *,
        include_entries: bool = ...,
    ) -> dict[str, Any]: ...
    @property
    def file_cls(self) -> type[FileRecord] | None: ...
    def load(
        self,
        record: Record,
        data: dict[str, Any],
        *,
        from_dump: bool = ...,
    ) -> FilesManager: ...
    def obj(self, record: Record) -> FilesManager | None: ...
    def store(self, record: Record, files: FilesManager) -> None: ...
    @overload
    def __get__(self, instance: None, owner: type[Record]) -> Self: ...
    @overload
    def __get__(self, instance: Record, owner: type[Record]) -> FilesManager: ...
    def __set__(self, instance: Record, value: FilesManager) -> None: ...
