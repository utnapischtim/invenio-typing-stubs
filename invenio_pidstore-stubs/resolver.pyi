"""Internal resolver for persistent identifiers.

Type stubs for invenio_pidstore.resolver.
"""

import uuid
from collections.abc import Callable
from typing import Any

from invenio_pidstore.models import PersistentIdentifier

class Resolver:
    """Persistent identifier resolver."""

    pid_type: str | None
    object_type: str | None
    object_getter: Callable[[uuid.UUID], Any] | None
    registered_only: bool

    def __init__(
        self,
        pid_type: str | None = None,
        object_type: str | None = None,
        getter: Callable[[uuid.UUID], Any] | None = None,
        registered_only: bool = True,
    ) -> None: ...
    def resolve(
        self, pid_value: str | int,
    ) -> tuple[PersistentIdentifier, Any]: ...
