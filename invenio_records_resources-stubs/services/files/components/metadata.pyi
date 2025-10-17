
from flask_principal import (
    AnonymousIdentity,
    Identity,
)
from invenio_records_resources.records.api import Record
from invenio_records_resources.services.files.components.base import (
    FileServiceComponent,
)

class FileMetadataComponent(FileServiceComponent):
    def commit_file(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        record: Record,
    ): ...
    def init_files(
        self,
        identity: Identity,
        id_: str,
        record: Record,
        data: list[
            dict[
                str,
                str | dict[str, str] | int | dict[str, bool] | dict[str, str | int],
            ]
        ],
    ): ...
    def update_file_metadata(
        self,
        identity: AnonymousIdentity,
        id_: str,
        file_key: str,
        record: Record,
        data: dict[str, dict[str, str]],
    ): ...
    def update_transfer_metadata(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        record: Record,
        transfer_metadata: dict[str, str],
    ): ...
