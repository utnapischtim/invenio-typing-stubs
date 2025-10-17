"""Invenio module that stores and registers persistent identifiers.

Type stubs for invenio_pidstore.ext.
"""

import uuid
from collections.abc import Callable
from typing import Any

from flask import Flask
from invenio_pidstore.fetchers import FetchedPID as FetchedPID
from invenio_pidstore.models import PersistentIdentifier as PersistentIdentifier

def pid_exists(value: str, pidtype: str | None = None) -> bool: ...

class _PIDStoreState:
    """Persistent identifier store state."""

    app: Flask
    minters: dict[str, Callable[[uuid.UUID, dict[str, Any]], PersistentIdentifier]]
    fetchers: dict[str, Callable[[uuid.UUID, dict[str, Any]], FetchedPID]]

    def __init__(
        self,
        app: Flask,
        minters_entry_point_group: str | None = None,
        fetchers_entry_point_group: str | None = None,
    ) -> None: ...
    def register_minter(
        self,
        name: str,
        minter: Callable[[uuid.UUID, dict[str, Any]], PersistentIdentifier],
    ) -> None: ...
    def register_fetcher(
        self, name: str, fetcher: Callable[[uuid.UUID, dict[str, Any]], FetchedPID],
    ) -> None: ...
    def load_minters_entry_point_group(self, entry_point_group: str) -> None: ...
    def load_fetchers_entry_point_group(self, entry_point_group: str) -> None: ...

class InvenioPIDStore:
    """Invenio-PIDStore extension."""

    _state: _PIDStoreState

    def __init__(
        self,
        app: Flask | None = None,
        minters_entry_point_group: str = "invenio_pidstore.minters",
        fetchers_entry_point_group: str = "invenio_pidstore.fetchers",
    ) -> None: ...
    def init_app(
        self,
        app: Flask,
        minters_entry_point_group: str | None = None,
        fetchers_entry_point_group: str | None = None,
    ) -> _PIDStoreState: ...
    def init_config(self, app: Flask) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
