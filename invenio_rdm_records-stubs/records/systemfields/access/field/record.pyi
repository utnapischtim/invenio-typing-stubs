from collections.abc import Mapping
from enum import Enum
from typing import Any

from invenio_rdm_records.records.systemfields.access.embargo import Embargo
from invenio_rdm_records.records.systemfields.access.protection import Protection
from invenio_records.systemfields import SystemField

class AccessStatusEnum(Enum):
    OPEN = "open"
    EMBARGOED = "embargoed"
    RESTRICTED = "restricted"
    METADATA_ONLY = "metadata-only"

class RecordAccess:
    protection_cls: type[Protection]
    embargo_cls: type[Embargo]

    protection: Protection
    embargo: Embargo
    has_files: bool | None
    errors: list[Exception]

    def __init__(
        self,
        protection: Protection | None = ...,
        embargo: Embargo | None = ...,
        protection_cls: type[Protection] | None = ...,
        embargo_cls: type[Embargo] | None = ...,
        has_files: bool | None = ...,
    ) -> None: ...
    @property
    def status(self) -> AccessStatusEnum: ...
    def dump(self) -> dict[str, Any]: ...
    def lift_embargo(self) -> bool: ...
    def refresh_from_dict(self, access_dict: Mapping[str, Any]) -> None: ...
    @classmethod
    def from_dict(
        cls,
        access_dict: Mapping[str, Any] | None,
        protection_cls: type[Protection] | None = ...,
        embargo_cls: type[Embargo] | None = ...,
        has_files: bool | None = ...,
    ) -> RecordAccess: ...
    def __eq__(self, other: object) -> bool: ...

class RecordAccessField(SystemField):
    def __init__(
        self, key: str = ..., access_obj_class: type[RecordAccess] = ...,
    ) -> None: ...
    def obj(self, instance: Any) -> RecordAccess: ...
    def set_obj(self, record: Any, obj: Mapping[str, Any] | RecordAccess) -> None: ...
    def pre_commit(self, record: Any) -> None: ...
    def post_dump(
        self, record: Any, data: Mapping[str, Any], dumper: Any | None = ...,
    ) -> None: ...
    def pre_load(self, data: Mapping[str, Any], loader: Any | None = ...) -> None: ...
