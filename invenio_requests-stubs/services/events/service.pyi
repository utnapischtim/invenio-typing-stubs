from typing import Any, Generic, TypeVar
from uuid import UUID

from _typeshed import Incomplete
from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.records.results import RecordItem, RecordList
from invenio_requests.customizations import CommentEventType as CommentEventType
from invenio_requests.customizations.event_types import LogEventType as LogEventType
from invenio_requests.records.api import Request, RequestEvent
from invenio_requests.records.api import RequestEventFormat as RequestEventFormat
from invenio_requests.resolvers.registry import ResolverRegistry as ResolverRegistry
from invenio_requests.services.events.config import RequestEventsServiceConfig
from invenio_requests.services.results import (
    EntityResolverExpandableField as EntityResolverExpandableField,
)

C = TypeVar("C", bound=RequestEventsServiceConfig)

class RequestEventsService(RecordService[C], Generic[C]):
    @property
    def expandable_fields(self) -> list[EntityResolverExpandableField]: ...
    def _get_creator(
        self,
        identity: Identity,
        request: Request | None = ...,
    ) -> dict[str, Any]: ...
    def _get_event(
        self,
        event_id: str | int,
        with_deleted: bool = ...,
    ) -> RequestEvent: ...
    def _get_request(self, request_id: str | int) -> Request: ...
    def create(  # type: ignore[override]
        self,
        identity: Identity,
        request_id: str | int | UUID,
        data: dict[str, Any],
        event_type: Incomplete,
        uow: UnitOfWork = ...,
        expand: bool = False,
        notify: bool = True,
    ) -> RecordItem: ...
    def search(  # type: ignore[override]
        self,
        identity: Identity,
        request_id: str | int,
        params: dict[str, Any] | None = None,
        search_preference: str | None = None,
        **kwargs: Any,
    ) -> RecordList: ...
    @property
    def request_cls(self) -> type[Request]: ...
