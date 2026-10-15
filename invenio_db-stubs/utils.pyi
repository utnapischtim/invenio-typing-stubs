from collections.abc import Callable
from functools import partial
from typing import Any

from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy
from sqlalchemy.engine import Engine

from .shared import db


def alembic_test_context() -> dict[str, bool | Callable[..., bool]]: ...
def create_alembic_version_table() -> None: ...
def drop_alembic_version_table() -> None: ...
def has_table(engine: Engine, table: str) -> bool: ...
def versioning_models_registered(manager: Any, base: Any) -> bool: ...
def versioning_model_classname(manager: Any, model: Any) -> str: ...
def rebuild_encrypted_properties(
    old_key: str,
    model: Any,
    properties: list[str],
    db: FlaskSQLAlchemy = ...,
) -> None: ...
def update_table_columns_column_type(
    table_name: str,
    column_name: str,
    to_type: db.UTCDateTime | db.DateTime | None = None,
    existing_type: db.UTCDateTime | db.DateTime | None = None,
    existing_nullable: bool | None = None,
) -> None: ...

update_table_columns_column_type_to_utc_datetime = partial(...)

update_table_columns_column_type_to_datetime = partial(...)
