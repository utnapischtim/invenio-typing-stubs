from io import BufferedReader, BytesIO
from typing import Any, ClassVar

from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from invenio_records_resources.services.files.transfer.providers.remote import (
    RemoteTransferBase,
)
from werkzeug.wsgi import LimitedStream

class FetchTransfer(RemoteTransferBase):
    transfer_type: ClassVar[str]
    def commit_file(self) -> None: ...
    def init_file(
        self, record: Record, file_metadata: dict[str, Any], **kwargs,
    ) -> FileRecord: ...
    def set_file_content(
        self,
        stream: BytesIO | BufferedReader | LimitedStream,
        content_length: int | None,
    ) -> None: ...
    @property
    def status(self) -> str: ...

    class Schema(RemoteTransferBase.Schema):
        def validate_names(self, value: str) -> None: ...
