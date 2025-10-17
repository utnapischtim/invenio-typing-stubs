
from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_requests.customizations import actions as actions
from invenio_requests.customizations.actions import (
    AcceptAction,
    DeclineAction,
    RequestAction,
)
from invenio_requests.customizations.request_types import RequestType

class DeclineUserAction(DeclineAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class AcceptUserAction(AcceptAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class UserModerationRequest(RequestType):
    type_id: str
    name: str
    creator_can_be_none: bool
    topic_can_be_none: bool
    allowed_creator_ref_types: list[str]
    allowed_receiver_ref_types: list[str]
    allowed_topic_ref_types: list[str]
    available_actions: dict[str, type[RequestAction]]
