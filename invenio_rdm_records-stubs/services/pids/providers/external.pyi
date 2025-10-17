from collections.abc import Sequence
from typing import Any

from flask import Flask
from invenio_pidstore.models import PersistentIdentifier
from invenio_rdm_records.records.api import RDMDraft, RDMRecord

from .base import PIDProvider

class BlockedPrefixes:
    def __init__(
        self,
        prefixes: Sequence[str] | None = ...,
        config_names: Sequence[str] | None = ...,
    ) -> None: ...
    @property
    def prefixes(self) -> list[str]: ...
    def __call__(
        self, record: Any, identifier: str, provider: str, errors: list[str],
    ) -> None: ...

class ExternalPIDProvider(PIDProvider):
    def __init__(
        self,
        name: str,
        pid_type: str,
        validators: Sequence[BlockedPrefixes] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def is_enabled(cls, app: Flask | None = ...) -> bool: ...
    def validate(
        self,
        record: RDMRecord | RDMDraft | dict[str, Any],
        identifier: str | None = ...,
        provider: str | None = ...,
        client: Any | None = ...,
        **kwargs: Any,
    ) -> tuple[bool, list[dict[str, Any]]]: ...
    def delete(
        self, pid: PersistentIdentifier, soft_delete: bool = ..., **kwargs: Any,
    ) -> bool: ...
