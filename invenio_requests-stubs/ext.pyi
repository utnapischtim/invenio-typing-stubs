from typing import Protocol

from flask.app import Flask
from invenio_requests import config as config
from invenio_requests.registry import TypeRegistry as TypeRegistry
from invenio_requests.resources import (
    RequestCommentsResource as RequestCommentsResource,
)
from invenio_requests.resources import (
    RequestCommentsResourceConfig as RequestCommentsResourceConfig,
)
from invenio_requests.resources import RequestsResource as RequestsResource
from invenio_requests.resources import RequestsResourceConfig as RequestsResourceConfig
from invenio_requests.services import RequestEventsService as RequestEventsService
from invenio_requests.services import (
    RequestEventsServiceConfig as RequestEventsServiceConfig,
)
from invenio_requests.services import RequestsService as RequestsService
from invenio_requests.services import RequestsServiceConfig as RequestsServiceConfig
from invenio_requests.services import (
    UserModerationRequestService as UserModerationRequestService,
)

class _ServiceConfigs(Protocol):
    requests: RequestsServiceConfig
    request_events: RequestEventsServiceConfig

class InvenioRequests:
    requests_service: RequestsService | None
    requests_resource: RequestsResource | None
    request_comments_service: RequestEventsService | None
    _schema_cache: dict[str, object]
    _events_schema_cache: dict[str, object]
    def __init__(self, app: Flask | None = None) -> None: ...
    def init_app(self, app: Flask) -> None: ...
    def init_config(self, app: Flask) -> None: ...
    def service_configs(self, app: Flask) -> _ServiceConfigs: ...
    request_events_service: RequestEventsService | None
    user_moderation_requests_service: UserModerationRequestService | None
    def init_services(self, app: Flask) -> None: ...
    request_events_resource: RequestCommentsResource | None
    def init_resources(self, app: Flask) -> None: ...
    request_type_registry: TypeRegistry | None
    event_type_registry: TypeRegistry | None
    entity_resolvers_registry: TypeRegistry | None
    def init_registry(self, app: Flask) -> None: ...

def register_entry_point(
    registry: TypeRegistry, ep_name: str, app: Flask | None = None,
) -> None: ...
def finalize_app(app: Flask) -> None: ...
def api_finalize_app(app: Flask) -> None: ...
def init(app: Flask) -> None: ...
