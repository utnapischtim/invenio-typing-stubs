from typing import Any, Self, overload

from invenio_communities.records.records.systemfields.communities.context import (
    CommunitiesFieldContext as CommunitiesFieldContext,
)
from invenio_communities.records.records.systemfields.communities.manager import (
    CommunitiesRelationManager as CommunitiesRelationManager,
)
from invenio_records.api import Record
from invenio_records.systemfields import SystemField

class CommunitiesField(SystemField):  # type: ignore[misc]
    def __init__(
        self,
        m2m_model_cls: type[Any],
        key: str = "communities",
        context_cls: type[Any] | None = None,
        manager_cls: type[Any] | None = None,
    ) -> None: ...
    def pre_commit(self, record: Record) -> None: ...
    def obj(self, record: Record) -> CommunitiesRelationManager: ...
    def post_dump(
        self, record: Record, data: Any, dumper: Any | None = None,
    ) -> None: ...
    def post_load(
        self, record: Record, data: Any, loader: Any | None = None,
    ) -> None: ...
    @overload  # type: ignore[override]
    def __get__(self, instance: None, owner: type[Record]) -> Self: ...  # type: ignore # keep typing tighter
    @overload
    def __get__(  # type: ignore # keep typing tighter
        self, instance: Record, owner: type[Record],
    ) -> CommunitiesRelationManager: ...
    def __set__(self, instance: Record, value: CommunitiesRelationManager) -> None: ...  # type: ignore[override]
