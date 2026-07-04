from typing import Any, ClassVar

from flask import Flask
from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy
from flask_sqlalchemy.model import Model
from sqlalchemy import MetaData
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session
from sqlalchemy.types import DateTime, TypeDecorator

NAMING_CONVENTION: dict[str, str]
metadata: MetaData

class UTCDateTime(TypeDecorator):
    """Custom UTC datetime type."""

    impl: type = DateTime

    # todo: should be discussed, but has to be set explicitly to remove warning
    cache_ok: bool = False

class Timestamp:
    created: UTCDateTime
    updated: UTCDateTime

class SQLAlchemy(FlaskSQLAlchemy):
    Model: ClassVar[Model]
    UTCDateTime: ClassVar[UTCDateTime]
    Timestamp: ClassVar[Timestamp]

    def apply_driver_hacks(
        self,
        app: Flask,
        sa_url: URL,
        options: dict[str, Any],
    ) -> tuple[URL, dict[str, Any]]: ...
    @property
    def session(self) -> Session: ...  # type: ignore[override]

def do_sqlite_connect(dbapi_connection: Any, connection_record: Any) -> None: ...
def do_sqlite_begin(dbapi_connection: Any) -> None: ...

db: SQLAlchemy
