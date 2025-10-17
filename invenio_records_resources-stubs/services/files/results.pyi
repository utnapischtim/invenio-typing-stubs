from collections.abc import Iterator, ValuesView
from io import BufferedReader
from typing import (
    Any,
)

from flask.wrappers import Response
from flask_principal import (
    Identity,
)
from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from invenio_records_resources.services.base.links import LinksTemplate
from invenio_records_resources.services.base.results import ServiceListResult
from invenio_records_resources.services.files.service import FileService
from invenio_records_resources.services.records.results import RecordItem

class FileItem(RecordItem):
    _file: FileRecord

    def __init__(
        self,
        service: FileService,
        identity: Identity,
        file_: FileRecord,
        record: Record,
        errors: Any | None = ...,
        links_tpl: LinksTemplate | None = ...,
    ) -> None: ...
    @property
    def _obj(self) -> FileRecord: ...  # type: ignore[override]
    @property
    def file_id(self) -> str: ...
    def get_stream(self, mode: str) -> BufferedReader: ...
    def open_stream(self, mode: str) -> Any: ...
    @property
    def links(self) -> dict[str, Any]: ...
    def send_file(
        self, restricted: bool = ..., as_attachment: bool = ...,
    ) -> Response: ...

class FileList(ServiceListResult):
    _identity: Identity
    _record: Record
    _results: ValuesView[FileRecord]
    _service: FileService
    _links_tpl: LinksTemplate | None
    _links_item_tpl: LinksTemplate | None

    def __init__(
        self,
        service: FileService,
        identity: Identity,
        results: ValuesView[FileRecord],
        record: Record,
        links_tpl: LinksTemplate | None = ...,
        links_item_tpl: LinksTemplate | None = ...,
    ) -> None: ...
    @property
    def entries(self) -> Iterator[dict[str, Any]]: ...
    def to_dict(self) -> dict[str, Any]: ...
