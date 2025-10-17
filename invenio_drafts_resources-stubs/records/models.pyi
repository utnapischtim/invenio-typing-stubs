from datetime import datetime
from typing import ClassVar
from uuid import UUID

from invenio_records.models import RecordMetadataBase
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped

class ParentRecordMixin[ParentModel: type]:
    __parent_record_model__: ClassVar[type]
    @declared_attr
    def parent_id(cls) -> Mapped[UUID]: ...
    @declared_attr
    def parent(cls) -> Mapped[ParentModel]: ...
    index: Mapped[int | None]

class ParentRecordStateMixin[ParentModel: type, RecordModel: type, DraftModel: type]:
    __parent_record_model__: ClassVar[type]
    __record_model__: ClassVar[type]
    __draft_model__: ClassVar[type]
    @declared_attr
    def parent_id(cls) -> Mapped[UUID]: ...
    @declared_attr
    def latest_id(cls) -> Mapped[UUID | None]: ...
    latest_index: Mapped[int | None]
    @declared_attr
    def next_draft_id(cls) -> Mapped[UUID | None]: ...

class DraftMetadataBase(RecordMetadataBase):
    fork_version_id: Mapped[int | None]
    expires_at: Mapped[datetime | None]
