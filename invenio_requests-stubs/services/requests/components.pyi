from typing import TYPE_CHECKING, Any

from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_records_resources.records.api import Record as BaseRecord
from invenio_records_resources.services.records.components import (
    DataComponent,
    ServiceComponent,
)
from invenio_requests.customizations.event_types import (
    ReviewersUpdatedType as ReviewersUpdatedType,
)
from invenio_requests.proxies import current_events_service as current_events_service

if TYPE_CHECKING:
    from invenio_requests.records.api import Request

class RequestNumberComponent(ServiceComponent):
    def create(
        self,
        identity: Identity,
        data: dict[str, Any] | None = None,
        record: Request | None = None,
        **kwargs: Any,
    ) -> None: ...

class EntityReferencesComponent(ServiceComponent):
    def create(
        self,
        identity: Identity,
        data: dict[str, Any] | None = None,
        record: Request | None = None,
        **kwargs: Any,
    ) -> None: ...

class RequestDataComponent(DataComponent):
    def update(
        self,
        identity: Identity,
        data: dict[str, Any] | None = None,
        record: BaseRecord | None = None,
        **kwargs: Any,
    ) -> None: ...

class RequestReviewersComponent(ServiceComponent):
    def _ensure_no_duplicates(self, reviewers: list[Any]) -> list[Any]: ...
    def _reviewers_updated(
        self, previous_reviewers: list[Any], new_reviewers: list[Any],
    ) -> bool: ...
    def _validate_reviewers(self, reviewers: list[Any]) -> None: ...
    def update(
        self,
        identity: Identity,
        data: dict[str, Any] | None = None,
        record: BaseRecord | None = None,
        uow: UnitOfWork = ...,
        **kwargs: Any,
    ) -> None: ...

class RequestPayloadComponent(DataComponent):
    def update(
        self,
        identity: Identity,
        data: dict[str, Any] | None = None,
        record: BaseRecord | None = None,
        **kwargs: Any,
    ) -> None: ...
