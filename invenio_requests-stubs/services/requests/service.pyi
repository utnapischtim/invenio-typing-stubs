from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

import marshmallow as ma
from _typeshed import Incomplete
from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_requests.customizations import RequestActions as RequestActions
from invenio_requests.customizations.event_types import (
    CommentEventType as CommentEventType,
)
from invenio_requests.errors import CannotExecuteActionError as CannotExecuteActionError
from invenio_requests.proxies import current_events_service as current_events_service
from invenio_requests.proxies import (
    current_request_type_registry as current_request_type_registry,
)
from invenio_requests.records.api import Request
from invenio_requests.resolvers.registry import ResolverRegistry as ResolverRegistry
from invenio_requests.services.requests.config import RequestsServiceConfig
from invenio_requests.services.requests.links import RequestLinksTemplate
from invenio_requests.services.requests.results import RequestItem, RequestList
from invenio_requests.services.results import (
    EntityResolverExpandableField as EntityResolverExpandableField,
)
from invenio_requests.services.results import (
    MultiEntityResolverExpandableField as MultiEntityResolverExpandableField,
)

C = TypeVar("C", bound=RequestsServiceConfig)

class RequestsService(RecordService[C], Generic[C]):
    @property
    def links_item_tpl(self) -> RequestLinksTemplate: ...
    @property
    def request_type_registry(self) -> Any: ...
    @property
    def expandable_fields(
        self,
    ) -> list[EntityResolverExpandableField | MultiEntityResolverExpandableField]: ...
    def _execute(
        self,
        identity: Identity,
        request: Request,
        action: str,
        uow: UnitOfWork,
    ) -> None: ...
    def create(  # type: ignore[override]
        self,
        identity: Identity,
        data: dict[str, Any],
        request_type: Incomplete,
        receiver: dict[str, Any],
        creator: dict[str, Any] | None = None,
        topic: dict[str, Any] | None = None,
        expires_at: str | None = None,
        uow: UnitOfWork = ...,
        expand: bool = False,
    ) -> RequestItem: ...
    def execute_action(
        self,
        identity: Identity,
        id_: str | int,
        action: str,
        data: dict[str, Any] | None = None,
        uow: UnitOfWork = ...,
        expand: bool = False,
        **kwargs: Any,
    ) -> RequestItem: ...
    def search_user_requests(
        self,
        identity: Identity,
        params: dict[str, Any] | None = None,
        search_preference: str | None = None,
        expand: bool = False,
        **kwargs: Any,
    ) -> RequestList: ...
    def _wrap_schema(self, schema: type[ma.Schema]) -> ServiceSchemaWrapper: ...
