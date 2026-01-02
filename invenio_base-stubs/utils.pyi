from importlib.metadata import EntryPoint

from flask import Flask


def entry_points(group: str) -> list[EntryPoint]: ...
def obj_or_import_string[T](
    value: str | T | None,
    default: T | None = None,
) -> T | None: ...
def load_or_import_from_config[T](
    key: str,
    app: Flask | None = None,
    default: T | None = None,
) -> T | None: ...
