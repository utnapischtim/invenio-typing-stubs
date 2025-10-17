"""Module storing implementations of PID providers.

Type stubs for invenio_pidstore.providers.base.
"""

import uuid
from typing import Any, ClassVar, Self

from invenio_pidstore.models import PersistentIdentifier, PIDStatus

class BaseProvider:
    """Abstract class for persistent identifier provider classes."""

    pid_type: ClassVar[str | None]
    pid_provider: ClassVar[str | None]
    default_status: ClassVar[PIDStatus]
    pid: PersistentIdentifier

    @classmethod
    def create(
        cls,
        pid_type: str | None = None,
        pid_value: str | None = None,
        object_type: str | None = None,
        object_uuid: str | uuid.UUID | None = None,
        status: PIDStatus | None = None,
        **kwargs: Any,
    ) -> Self: ...
    @classmethod
    def get(
        cls,
        pid_value: str,
        pid_type: str | None = None,
        **kwargs: Any,
    ) -> BaseProvider: ...
    def __init__(self, pid: PersistentIdentifier, **kwargs: Any) -> None: ...
    def reserve(self, *args: Any, **kwargs: Any) -> bool: ...
    def register(self, *args: Any, **kwargs: Any) -> bool: ...
    def update(self, *args: Any, **kwargs: Any) -> bool: ...
    def delete(self) -> bool: ...
    def sync_status(self) -> bool: ...
