from typing import Any

from invenio_records_resources.references.entity_resolvers.base import EntityResolver
from invenio_requests.customizations import CommentEventType as CommentEventType
from invenio_requests.customizations import LogEventType as LogEventType
from invenio_requests.customizations import ReviewersUpdatedType as ReviewersUpdatedType
from invenio_requests.customizations.event_types import EventType as RequestEventType
from invenio_requests.customizations.request_types import RequestType as RequestType
from invenio_requests.services.permissions import PermissionPolicy as PermissionPolicy
from invenio_requests.services.requests import facets as facets

REQUESTS_PERMISSION_POLICY = PermissionPolicy
REQUESTS_REGISTERED_TYPES: list[RequestType]
REQUESTS_REGISTERED_EVENT_TYPES: list[RequestEventType]
REQUESTS_ENTITY_RESOLVERS: list[type[EntityResolver] | EntityResolver]
REQUESTS_ROUTES: dict[str, str]
REQUESTS_SEARCH: dict[str, list[str]]
REQUESTS_SORT_OPTIONS: dict[str, dict[str, Any]]
REQUESTS_FACETS: dict[str, dict[str, Any]]
REQUESTS_TIMELINE_PAGE_SIZE: int
REQUESTS_MODERATION_ROLE: str
REQUESTS_USER_MODERATION_SEARCH: dict[str, list[str]]
REQUESTS_USER_MODERATION_SORT_OPTIONS: dict[str, dict[str, Any]]
REQUESTS_USER_MODERATION_FACETS: dict[str, dict[str, Any]]
REQUESTS_REVIEWERS_ENABLED: bool
REQUESTS_REVIEWERS_MAX_NUMBER: int
