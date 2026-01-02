from typing import Any, Protocol

from flask_principal import Need
from flask_sqlalchemy.model import Model
from invenio_db import db
from sqlalchemy import UniqueConstraint
from sqlalchemy.engine.base import Connection
from sqlalchemy.orm.mapper import Mapper
from sqlalchemy.orm.relationships import Relationship
from sqlalchemy.sql.schema import Column


class Stringable(Protocol):
    def __str__(self) -> str: ...

class ActionNeedMixin:
    id: Column
    action: Column
    exclude: Column
    argument: Column

    @classmethod
    def create(cls, action: Need, **kwargs: dict) -> ActionNeedMixin: ...
    @classmethod
    def allow(cls, action: Need, **kwargs: dict) -> ActionNeedMixin: ...
    @classmethod
    def deny(cls, action: Need, **kwargs: dict) -> ActionNeedMixin: ...
    @classmethod
    def query_by_action(cls, action: Need, argument: Stringable) -> Any: ...
    @property
    def need(self) -> Need: ...

class ActionUsers(ActionNeedMixin, Model):
    __tablename__: str
    __table_args__: tuple[UniqueConstraint]
    user_id: Column
    user: Relationship

    @property
    def need(self) -> Need: ...

class ActionRoles(ActionNeedMixin, Model):
    __tablename__: str
    __table_args__: tuple[UniqueConstraint]
    role_id: Column
    role: Relationship

    @property
    def need(self) -> Need: ...

class ActionSystemRoles(ActionNeedMixin, Model):
    __tablename__: str
    __table_args__: tuple[UniqueConstraint]
    role_name: Column

    @classmethod
    def create(cls, action: Need, **kwargs: dict) -> ActionNeedMixin: ...
    def validate_role_name(self, key: str, role_name: str) -> str: ...
    @property
    def need(self) -> Need: ...

def get_action_cache_key(name: Stringable, argument: Stringable) -> None: ...
def removed_or_inserted_action(
    mapper: Mapper,
    connection: Connection,
    target: ActionRoles,
) -> None: ...
def changed_action(
    mapper: Mapper,
    connection: Connection,
    target: ActionRoles,
) -> None: ...
