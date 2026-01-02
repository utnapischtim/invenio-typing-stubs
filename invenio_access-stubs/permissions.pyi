from typing import NamedTuple

from flask_principal import Identity, ItemNeed, Need
from flask_principal import Permission as _Permission

_Need: NamedTuple

type ParameterizedActionNeed = Need
type SystemRoleNeed = Need
type ActionNeed = Need

superuser_access: ActionNeed

any_user: SystemRoleNeed

authenticated_user: SystemRoleNeed

system_process: SystemRoleNeed

system_user_id: str

system_identity: Identity

class _P:
    def update(self, permission: Permission) -> None: ...

class Permission(_Permission):
    allow_by_default: bool

    def __init__(self, *needs: tuple) -> None: ...
    @staticmethod
    def _cache_key(action_need: ParameterizedActionNeed) -> None: ...
    @staticmethod
    def _split_actionsneeds(needs: list[Need]) -> tuple[set[Need], set[Need]]: ...
    def _load_permissions(self) -> None: ...
    def _expand_action(self, explicit_action: ActionNeed) -> ActionNeed: ...

system_permission: Permission
