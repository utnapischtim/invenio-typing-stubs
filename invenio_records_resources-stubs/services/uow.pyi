from typing import Any

from invenio_db.uow import ModelCommitOp as ModelCommitOp
from invenio_db.uow import ModelDeleteOp as ModelDeleteOp
from invenio_db.uow import Operation, UnitOfWork
from invenio_db.uow import unit_of_work as unit_of_work
from invenio_indexer.api import RecordIndexer  # type: ignore[import-untyped]
from invenio_records_resources.records.api import FileRecord, Record

class ChangeNotificationOp(Operation):
    def __init__(self, record_type: str, records: list[Record]): ...
    def on_post_commit(self, uow: UnitOfWork): ...

class RecordBulkCommitOp(Operation):
    def __init__(
        self,
        records: list[Record],
        indexer: RecordIndexer | None = ...,
        index_refresh: bool = ...,
    ): ...
    def on_commit(self, uow: UnitOfWork): ...
    def on_register(self, uow: UnitOfWork): ...

class RecordCommitOp(Operation):
    def __init__(
        self,
        record: FileRecord | Record,
        indexer: RecordIndexer | None = ...,
        index_refresh: bool = ...,
    ): ...
    def on_commit(self, uow: UnitOfWork): ...
    def on_register(self, uow: UnitOfWork): ...

class RecordIndexOp(RecordCommitOp):
    def on_register(self, uow: UnitOfWork): ...

class RecordDeleteOp(Operation):
    def __init__(
        self,
        record: Record,
        indexer: RecordIndexer | None = ...,
        force: bool = ...,
        index_refresh: bool = ...,
    ): ...
    def on_commit(self, uow: UnitOfWork): ...
    def on_register(self, uow: UnitOfWork): ...

class RecordIndexDeleteOp(RecordDeleteOp):
    def on_register(self, uow: UnitOfWork): ...

class RecordBulkIndexOp(Operation):
    def __init__(self, records_iter: Any, indexer: RecordIndexer | None = ...): ...
    def on_post_commit(self, uow: UnitOfWork): ...

class IndexRefreshOp(Operation):
    def __init__(self, indexer: Any, index: str | None = ..., **kwargs: Any): ...
    def on_post_commit(self, uow: UnitOfWork): ...

class TaskOp(Operation):
    def __init__(self, celery_task: Any, *args, **kwargs): ...
    def on_post_commit(self, uow: UnitOfWork): ...
    celery_kwargs: dict[str, Any]
    @classmethod
    def for_async_apply(
        cls,
        celery_task: Any,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        **celery_kwargs: Any,
    ) -> TaskOp: ...

class TaskRevokeOp(Operation):
    def __init__(self, task_id: str) -> None: ...
    def on_post_commit(self, uow: UnitOfWork) -> None: ...
