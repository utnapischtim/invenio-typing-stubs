
from invenio_notifications.models import Notification, Recipient

class UserRecipientFilter:
    def __init__(self, key: str) -> None: ...
    def __call__(
        self, notification: Notification, recipients: dict[str, Recipient],
    ) -> dict[str, Recipient]: ...
