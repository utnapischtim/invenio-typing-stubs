from typing import Any, Self, overload
from uuid import UUID

from invenio_communities.communities.records.api import Community
from invenio_records.systemfields import SystemField

def is_valid_uuid(value: Any) -> bool: ...

class ParentCommunityField(SystemField):  # type: ignore[misc]
    def __init__(self, key: str = "parent") -> None: ...
    def obj(self, instance: Community) -> Community | None: ...
    def set_obj(
        self, record: Community, obj: Community | UUID | str | None,
    ) -> None: ...
    def post_dump(
        self, record: Community, data: dict[str, Any], dumper: Any | None = None,
    ) -> None: ...
    def post_load(
        self, record: Community, data: dict[str, Any], loader: Any | None = None,
    ) -> None: ...
    @overload  # type: ignore[override]
    def __get__(self, instance: None, owner: type[Community]) -> Self: ...  # type: ignore # keep typing tighter
    @overload
    def __get__(  # type: ignore # keep typing tighter
        self, instance: Community, owner: type[Community],
    ) -> Community | None: ...
    def __set__(self, instance: Community, value: Community | None) -> None: ...  # type: ignore[override]
