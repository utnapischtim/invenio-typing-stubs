from io import (
    BufferedReader,
    BytesIO,
)
from typing import (
    ClassVar,
)

from invenio_records_resources.services.files.transfer.base import Transfer
from werkzeug.wsgi import LimitedStream

class LocalTransfer(Transfer):
    transfer_type: ClassVar[str]

    def set_file_content(
        self,
        stream: BytesIO | BufferedReader | LimitedStream,
        content_length: int | None,
    ) -> None: ...
