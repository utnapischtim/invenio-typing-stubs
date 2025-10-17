
from invenio_notifications.models import Notification
from invenio_notifications.services.builders import NotificationBuilder
from invenio_notifications.services.filters import RecipientFilter
from invenio_notifications.services.generators import (
    ContextGenerator,
    RecipientBackendGenerator,
    RecipientGenerator,
)

class CommentRequestEventCreateNotificationBuilder(NotificationBuilder):
    type: str
    context: list[ContextGenerator]
    recipients: list[RecipientGenerator]
    recipient_filters: list[RecipientFilter]
    recipient_backends: list[RecipientBackendGenerator]

    @classmethod
    def build(cls, **kwargs: object) -> Notification: ...
