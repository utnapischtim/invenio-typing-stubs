"""Persistent identifier fetchers.

Type stubs for invenio_pidstore.fetchers.
"""

import uuid
from typing import Any, NamedTuple

class FetchedPID(NamedTuple):
    """A pid fetcher."""

    provider: type[Any]
    pid_type: str
    pid_value: str

def recid_fetcher_v2(record_uuid: uuid.UUID, data: dict[str, Any]) -> FetchedPID: ...
def recid_fetcher(record_uuid: uuid.UUID, data: dict[str, Any]) -> FetchedPID: ...
