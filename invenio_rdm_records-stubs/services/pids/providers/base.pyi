from collections.abc import Sequence
from typing import Any

from flask import Flask
from invenio_pidstore.models import PersistentIdentifier, PIDStatus
from invenio_rdm_records.records.api import RDMDraft, RDMRecord

class PIDProvider:
    """Base class for PID providers."""

    name: str
    label: str
    client: Any | None
    pid_type: str | None
    default_status: PIDStatus
    managed: bool

    def __init__(
        self,
        name: str,
        client: Any | None = ...,
        pid_type: str | None = ...,
        default_status: PIDStatus = ...,
        managed: bool = ...,
        label: str | None = ...,
        *kwargs: Any,
    ) -> None: ...
    def generate_id(
        self, record: RDMRecord | RDMDraft | dict[str, Any], **kwargs: Any,
    ) -> str: ...
    @classmethod
    def is_enabled(cls, app: Flask | None = ...) -> bool: ...
    def is_managed(self) -> bool: ...
    def can_modify(self, pid: PersistentIdentifier, **kwargs: Any) -> bool: ...
    def get(
        self, pid_value: str | int, pid_provider: str | None = ...,
    ) -> PersistentIdentifier: ...
    def create(
        self,
        record: Any,
        pid_value: str | None = ...,
        status: PIDStatus | None = ...,
        **kwargs: Any,
    ) -> PersistentIdentifier: ...
    def reserve(
        self,
        pid: PersistentIdentifier,
        record: RDMRecord | RDMDraft | dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> bool: ...
    def register(
        self,
        pid: PersistentIdentifier,
        record: RDMRecord | RDMDraft | dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> bool: ...
    def update(
        self,
        pid: PersistentIdentifier,
        record: RDMRecord | RDMDraft | dict[str, Any] | None = ...,
        url: str | None = ...,
        **kwargs: Any,
    ) -> bool | None: ...
    def restore(self, pid: PersistentIdentifier, **kwargs: Any) -> None: ...
    def delete(
        self,
        pid: PersistentIdentifier,
        soft_delete: bool = ...,
        **kwargs: Any,
    ) -> bool | None: ...
    def validate(
        self,
        record: RDMRecord | RDMDraft | dict[str, Any],
        identifier: str | None = ...,
        provider: str | None = ...,
        **kwargs: Any,
    ) -> tuple[bool, list[dict[str, Any]]]: ...
    def _insert_pid_type_error_msg(
        self, errors: list[dict[str, Any]], error_msg: str | Sequence[str],
    ) -> None: ...
    def validate_restriction_level(
        self,
        record: RDMRecord | RDMDraft | dict[str, Any],
        identifier: str | None,
        **kwargs: Any,
    ) -> None: ...
    def create_and_reserve(
        self, record: RDMRecord | RDMDraft | dict[str, Any], **kwargs: Any,
    ) -> None: ...
