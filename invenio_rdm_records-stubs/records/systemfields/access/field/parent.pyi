from collections.abc import Mapping
from typing import Any, ClassVar

from invenio_rdm_records.records.systemfields.access.access_settings import (
    AccessSettings,
)
from invenio_rdm_records.records.systemfields.access.grants import Grants
from invenio_rdm_records.records.systemfields.access.links import Links
from invenio_rdm_records.records.systemfields.access.owners import Owner
from invenio_records.systemfields import SystemField

class ParentRecordAccess:
    grant_cls: ClassVar[type[Grants]]
    links_cls: ClassVar[type[Links]]
    owner_cls: ClassVar[type[Owner]]
    settings_cls: ClassVar[type[AccessSettings]]

    _owned_by: Owner
    grants: Grants
    links: Links
    _settings: AccessSettings
    errors: list[Exception]

    def __init__(
        self,
        owned_by: Owner | None = ...,
        grants: Grants | None = ...,
        links: Links | None = ...,
        owner_cls: type[Owner] | None = ...,
        settings: AccessSettings | None = ...,
        grants_cls: type[Grants] | None = ...,
        links_cls: type[Links] | None = ...,
        settings_cls: type[AccessSettings] | None = ...,
    ) -> None: ...
    @property
    def owned_by(self) -> Owner: ...
    @owned_by.setter
    def owned_by(self, value: Mapping[str, Any] | Owner) -> None: ...
    @property
    def owner(self) -> Owner: ...
    @owner.setter
    def owner(self, value: Mapping[str, Any] | Owner) -> None: ...
    @property
    def settings(self) -> AccessSettings: ...
    @settings.setter
    def settings(self, value: Mapping[str, Any] | AccessSettings) -> None: ...
    def dump(self) -> dict[str, Any]: ...
    def refresh_from_dict(self, access_dict: Mapping[str, Any]) -> None: ...
    @classmethod
    def from_dict(
        cls,
        access_dict: Mapping[str, Any] | None,
        owner_cls: type[Owner] | None = ...,
        grants_cls: type[Grants] | None = ...,
        links_cls: type[Links] | None = ...,
        settings_cls: type[AccessSettings] | None = ...,
    ) -> ParentRecordAccess: ...

class ParentRecordAccessField(SystemField):
    def __init__(
        self, key: str = ..., access_obj_class: type[ParentRecordAccess] = ...,
    ) -> None: ...
    def obj(self, instance: Any) -> ParentRecordAccess: ...
    def set_obj(
        self, record: Any, obj: Mapping[str, Any] | ParentRecordAccess,
    ) -> None: ...
    def pre_commit(self, record: Any) -> None: ...
