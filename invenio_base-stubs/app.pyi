from collections.abc import Callable
from os import PathLike
from typing import Any

from flask import Flask

from .urls.builders import InvenioUrlsBuilder


def create_app_factory(
    app_name: str,
    config_loader: Callable[..., None] | None = None,
    extension_entry_points: list[str] | None = None,
    extensions: list[object] | None = None,
    blueprint_entry_points: list[str] | None = None,
    blueprints: list[object] | None = None,
    converter_entry_points: list[str] | None = None,
    converters: dict[str, Any] | None = None,
    finalize_app_entry_points: list[str] | None = None,
    wsgi_factory: Callable[..., Any] | None = None,
    urls_builder_factory: Callable[..., InvenioUrlsBuilder] | None = None,
    **app_kwargs: dict,
) -> Callable[..., Flask]: ...
def create_cli(
    create_app: Callable[..., Flask] | None = None,
) -> Callable[..., None]: ...
def finalize_app_loader(app: Flask, entry_points: list[str] | None = None) -> None: ...
def app_loader(
    app: Flask,
    entry_points: list[str] | None = None,
    modules: list[object] | None = None,
) -> None: ...
def blueprint_loader(
    app: Flask,
    entry_points: list[str] | None = None,
    modules: list[object] | None = None,
) -> None: ...
def urls_builder_loader(
    app: Flask,
    factory: Callable[..., InvenioUrlsBuilder] | None,
    **kwargs: dict,
) -> None: ...
def converter_loader(
    app: Flask,
    entry_points: list[str] | None = None,
    modules: list[object] | None = None,
) -> None: ...
def _loader(
    app: Flask,
    init_func: Callable[[Any], None],
    entry_points: list[str] | None = None,
    modules: list[object] | None = None,
) -> None: ...
def base_app(
    import_name: str,
    instance_path: str | None = None,
    static_folder: str | PathLike[str] | None = None,
    static_url_path: str | None = "/static",
    template_folder: str | PathLike[str] | None = "templates",
    root_path: str | None = None,
    app_class: type[Flask] = Flask,
    *,
    instance_relative_config: bool = True,
) -> Flask: ...
def configure_warnings() -> None: ...
