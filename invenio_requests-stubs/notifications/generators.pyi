from typing import Any

from invenio_notifications.models import Notification, Recipient
from invenio_requests.proxies import current_events_service as current_events_service

class RequestParticipantsRecipient:
    key: str
    def __init__(self, key: str) -> None: ...
    def _get_user_id(self, request_field: dict[str, Any]) -> str | None: ...
    def __call__(
        self, notification: Notification, recipients: dict[str, Recipient],
    ) -> dict[str, Recipient]: ...
