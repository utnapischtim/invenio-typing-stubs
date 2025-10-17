"""Persistent identifier store and registration.

Type stubs for invenio_pidstore.models.
"""

import logging
import uuid
from enum import Enum
from typing import ClassVar

from flask_babel import LazyString
from sqlalchemy import Column, Index
from sqlalchemy_utils.models import Timestamp

PID_STATUS_TITLES: dict[str, LazyString]
logger: logging.Logger

class PIDStatus(Enum):
    """Constants for possible status of any given PID."""

    NEW = "N"
    RESERVED = "K"
    REGISTERED = "R"
    REDIRECTED = "M"
    DELETED = "D"

    def __init__(self, value: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def title(self) -> str: ...

class _Model: ...

class PersistentIdentifier(_Model, Timestamp):
    """Store and register persistent identifiers."""

    __tablename__: ClassVar[str]
    __table_args__: ClassVar[tuple[Index, ...]]

    id: Column[int]
    pid_type: Column[str]
    pid_value: Column[str]
    pid_provider: Column[str | None]
    status: Column[PIDStatus]
    object_type: Column[str | None]
    object_uuid: Column[uuid.UUID | None]

    @classmethod
    def create(
        cls,
        pid_type: str,
        pid_value: str,
        pid_provider: str | None = None,
        status: PIDStatus = ...,
        object_type: str | None = None,
        object_uuid: str | uuid.UUID | None = None,
    ) -> PersistentIdentifier: ...
    @classmethod
    def get(
        cls,
        pid_type: str,
        pid_value: str | int,
        pid_provider: str | None = None,
    ) -> PersistentIdentifier: ...
    @classmethod
    def get_by_object(
        cls,
        pid_type: str,
        object_type: str,
        object_uuid: str | uuid.UUID,
    ) -> PersistentIdentifier: ...
    def has_object(self) -> bool: ...
    def get_assigned_object(
        self, object_type: str | None = None,
    ) -> uuid.UUID | None: ...
    def assign(
        self,
        object_type: str,
        object_uuid: str | uuid.UUID,
        overwrite: bool = False,
    ) -> bool: ...
    def unassign(self) -> bool: ...
    def get_redirect(self) -> PersistentIdentifier: ...
    def redirect(self, pid: PersistentIdentifier) -> bool: ...
    def reserve(self) -> bool: ...
    def register(self) -> bool: ...
    def delete(self) -> bool: ...
    def sync_status(self, status: PIDStatus) -> bool: ...
    def is_redirected(self) -> bool: ...
    def is_registered(self) -> bool: ...
    def is_deleted(self) -> bool: ...
    def is_new(self) -> bool: ...
    def is_reserved(self) -> bool: ...

class Redirect(_Model, Timestamp):
    """Redirect for a persistent identifier."""

    __tablename__: ClassVar[str]

    id: Column[uuid.UUID]
    pid_id: Column[int]
    pid: PersistentIdentifier

class RecordIdentifier(_Model):
    """Sequence generator for integer record identifiers."""

    __tablename__: ClassVar[str]

    recid: Column[int]

    @classmethod
    def next(cls) -> int: ...
    @classmethod
    def max(cls) -> int: ...
    @classmethod
    def _set_sequence(cls, val: int) -> None: ...
    @classmethod
    def insert(cls, val: int) -> None: ...

__all__ = (
    "PIDStatus",
    "PersistentIdentifier",
    "RecordIdentifier",
    "Redirect",
)
