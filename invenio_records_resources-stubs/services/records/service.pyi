from collections.abc import Iterator
from typing import Any, Generic, TypeVar

from flask_principal import (
    Identity,
)
from invenio_db.uow import UnitOfWork
from invenio_indexer.api import RecordIndexer
from invenio_records_resources.records.api import (
    Record,
)
from invenio_records_resources.services.base.links import LinksTemplate
from invenio_records_resources.services.base.service import Service
from invenio_records_resources.services.records.config import (
    RecordServiceConfig,
    SearchOptions,
)
from invenio_records_resources.services.records.results import (
    RecordBulkItem,
    RecordBulkList,
    RecordItem,
    RecordList,
)
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_search import RecordsSearchV2
from opensearch_dsl.response import Response


class RecordIndexerMixin:
    @property
    def indexer(self) -> RecordIndexer: ...
    def record_to_index(self, record: Record) -> str: ...

C = TypeVar("C", bound=RecordServiceConfig)

class RecordService(Service[C], RecordIndexerMixin, Generic[C]):
    def _create(
        self,
        record_cls: type[Record],
        identity: Identity,
        data: dict[str, Any],
        raise_errors: bool = ...,
        uow: UnitOfWork = ...,
        expand: bool = ...,
    ) -> RecordItem: ...
    def _read_many(
        self,
        identity: Identity,
        search_query: Any,
        fields: list[str] | None = ...,
        max_records: int = ...,
        record_cls: None = ...,
        search_opts: None = ...,
        extra_filter: None = ...,
        preference: None = ...,
        sort: None = ...,
        **kwargs,
    ) -> Response: ...
    def _search(
        self,
        action: str,
        identity: Identity,
        params: dict[str, Any],
        search_preference: str | None,
        record_cls: type[RecordItem] | None = ...,
        search_opts: type[SearchOptions] | None = ...,
        extra_filter: Any | None = ...,
        permission_action: str = ...,
        versioning: bool = ...,
        **kwargs,
    ) -> RecordsSearchV2: ...
    def check_revision_id(
        self,
        record: Record,
        expected_revision_id: int | None,
    ): ...
    @property
    def components(self) -> Iterator[Any]: ...
    def create(
        self,
        identity: Identity,
        data: dict[str, Any],
        uow: UnitOfWork = ...,
        expand: bool = ...,
    ) -> RecordItem: ...
    def create_or_update_many(
        self,
        identity: Identity,
        data: list[tuple[str, dict[str, Any]]],
        uow: UnitOfWork = ...,
    ) -> RecordBulkList: ...
    def create_search(
        self,
        identity: Identity,
        record_cls: type[Record],
        search_opts: type[SearchOptions],
        permission_action: str = ...,
        preference: str | None = ...,
        extra_filter: None = ...,
        versioning: bool = ...,
    ) -> RecordsSearchV2: ...
    def delete(
        self,
        identity: Identity,
        id_: str,
        revision_id: int | None = ...,
        uow: UnitOfWork = ...,
    ) -> bool: ...
    @property
    def expandable_fields(self) -> list[Any]: ...
    @property
    def links_item_tpl(self) -> LinksTemplate: ...
    def on_relation_update(
        self,
        identity: Identity,
        record_type: str,
        records_info: list[Any],
        notif_time: str,
        limit: int = ...,
    ): ...
    def read(
        self,
        identity: Identity,
        id_: str,
        expand: bool = ...,
        action: str = ...,
    ) -> RecordItem: ...
    def read_all(
        self,
        identity: Identity,
        fields: list[str],
        max_records: int = ...,
        **kwargs,
    ) -> RecordList: ...
    def read_many(
        self,
        identity: Identity,
        ids: list[str],
        fields: list[str] | None = ...,
        **kwargs,
    ) -> RecordList: ...
    @property
    def record_cls(
        self,
    ) -> type[Record]: ...
    def reindex(
        self,
        identity: Identity,
        params: dict[str, Any] | None = ...,
        search_preference: str | None = ...,
        search_query: Any | None = ...,
        extra_filter: Any | None = ...,
        **kwargs,
    ) -> bool: ...
    def scan(
        self,
        identity: Identity,
        params: dict[str, Any] | None = ...,
        search_preference: None = ...,
        expand: bool = ...,
        **kwargs,
    ) -> RecordList: ...
    @property
    def schema(self) -> ServiceSchemaWrapper: ...
    def search(
        self,
        identity: Identity,
        params: dict[str, Any] | None = ...,
        search_preference: str | None = ...,
        expand: bool = ...,
        **kwargs,
    ) -> RecordList: ...
    def search_request(
        self,
        identity: Identity,
        params: dict[str, Any],
        record_cls: type[Record],
        search_opts: type[SearchOptions],
        preference: str | None = ...,
        extra_filter: None = ...,
        permission_action: str = ...,
        versioning: bool = ...,
    ) -> RecordsSearchV2: ...
    def update(
        self,
        identity: Identity,
        id_: str,
        data: dict[str, Any],
        revision_id: int | None = ...,
        uow: UnitOfWork = ...,
        expand: bool = ...,
    ) -> RecordItem: ...
    def exists(self, identity: Identity, id_: str) -> bool: ...
    def rebuild_index(self, identity: Identity, uow: UnitOfWork = ...) -> bool: ...

    # inherited but with narrowed return types
    def result_bulk_item(self, *args: Any, **kwargs: Any) -> RecordBulkItem: ...
    def result_bulk_list(self, *args: Any, **kwargs: Any) -> RecordBulkList: ...
    def result_item(self, *args: Any, **kwargs: Any) -> RecordItem: ...
    def result_list(self, *args: Any, **kwargs: Any) -> RecordList: ...
