
from typing import Any

import marshmallow as ma  # type: ignore[import-untyped]
from flask_principal import Identity  # type: ignore[import-untyped]
from invenio_db.uow import UnitOfWork  # type: ignore[import-untyped]
from invenio_requests.customizations import actions
from invenio_requests.customizations.request_types import RequestType
from marshmallow import fields  # type: ignore[import-untyped]

class UserSubmitAction(actions.SubmitAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class UserCancelAction(actions.CancelAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class UserDeclineAction(actions.DeclineAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class GuestCancelAction(actions.CancelAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class GuestDeclineAction(actions.DeclineAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class GuestSubmitAction(actions.SubmitAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class GuestAcceptAction(actions.AcceptAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class UserAcceptAction(actions.AcceptAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class UserAccessRequest(RequestType):
    type_id: str
    name: str
    creator_can_be_none: bool
    topic_can_be_none: bool
    allowed_creator_ref_types: list[str]
    allowed_receiver_ref_types: list[str]
    allowed_topic_ref_types: list[str]
    available_actions: dict[str, type[actions.RequestAction]]
    payload_schema: dict[str, fields.Field] | None
    def _update_link_config(self, **context_vars: Any) -> dict[str, Any]: ...

class GuestAccessRequest(RequestType):
    type_id: str
    name: str
    creator_can_be_none: bool
    topic_can_be_none: bool
    allowed_creator_ref_types: list[str]
    allowed_receiver_ref_types: list[str]
    allowed_topic_ref_types: list[str]
    available_actions: dict[str, type[actions.RequestAction]]
    payload_schema: dict[str, fields.Field] | None
    payload_schema_cls: type[ma.Schema] | None
    @classmethod
    def _create_payload_cls(cls) -> None: ...
    def _update_link_config(self, **context_vars: Any) -> dict[str, Any]: ...
    def _validate_days(self, value: str) -> None: ...
