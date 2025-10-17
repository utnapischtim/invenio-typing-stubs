from typing import Any, Generic, TypeVar

from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_rdm_records.services.config import RDMCommunityRecordsConfig
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.records.results import RecordList
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper

C = TypeVar("C", bound=RDMCommunityRecordsConfig)

class CommunityRecordsService(RecordService[C], Generic[C]):
    @property
    def community_record_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def community_cls(self): ...
    def search(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str,
        params: dict[str, Any] | None = ...,
        search_preference: str | None = ...,
        extra_filter: Any | None = ...,
        scan: bool = ...,
        scan_params: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def _remove(
        self, community: Any, record: Any, identity: Identity,
    ) -> list[dict[str, Any]]: ...
    def delete(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str,
        data: dict[str, Any],
        revision_id: int | None = ...,
        uow: UnitOfWork | None = None,
    ) -> list[dict[str, Any]]: ...
