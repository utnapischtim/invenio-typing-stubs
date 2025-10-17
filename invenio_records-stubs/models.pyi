from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy.engine.base import Connection
from sqlalchemy.orm import Mapped
from sqlalchemy.orm.mapper import Mapper

class Timestamp:
    created: Mapped[datetime]
    updated: Mapped[datetime]

def timestamp_before_update(
    mapper: Mapper, connection: Connection, target: Any,
) -> None: ...

class _Model: ...

class RecordMetadataBase(_Model, Timestamp):
    encoder: Any | None
    id: Mapped[UUID]
    json: Mapped[dict[str, Any] | None]
    version_id: Mapped[int]
    __mapper_args__: dict[str, Any]

    def __init__(self, data: dict[str, Any] | None = ..., **kwargs: Any) -> None: ...
    @property
    def is_deleted(self) -> Any: ...
    @is_deleted.setter
    def is_deleted(self, value: bool) -> None: ...
    @property
    def data(self) -> dict[str, Any]: ...
    @data.setter
    def data(self, value: dict[str, Any]) -> None: ...
    @classmethod
    def encode(cls, value: dict[str, Any]) -> dict[str, Any]: ...
    @classmethod
    def decode(cls, json: Any) -> Any: ...

class RecordMetadata(RecordMetadataBase):
    __tablename__: str
    __versioned__: dict[str, Any]
