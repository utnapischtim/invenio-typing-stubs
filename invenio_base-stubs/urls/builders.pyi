from abc import ABC, abstractmethod
from typing import Callable

from flask import Flask
from werkzeug.routing import BaseConverter


class InvenioUrlsBuilder(ABC):
    @abstractmethod
    def build(self, endpoint: str, values: dict, method: str | None = None) -> str: ...

class NoOpInvenioUrlsBuilder(InvenioUrlsBuilder):
    @abstractmethod
    def build(self, endpoint: str, values: dict, method: str | None = None) -> str: ...

class InvenioAppsUrlsBuilder(InvenioUrlsBuilder):
    def __init__(
        self,
        cfg_of_app_prefix: str,
        cfg_of_other_app_prefix: str,
        groups_of_other_app_entrypoints: dict[str, list] | list,
    ) -> None: ...
    def _load_converters(
        self,
        app_tmp: Flask,
        defaults: dict[str, type[BaseConverter]] | None = None,
    ) -> None: ...
    def _load_blueprints(self, app_tmp: Flask) -> None: ...
    def setup(self, app: Flask, **kwargs: dict) -> None: ...
    def prefix(self, site_cfg: str) -> str: ...
    def build(self, endpoint: str, values: dict, method: str | None = None) -> str: ...

def create_invenio_apps_urls_builder_factory(
    cfg_of_app_prefix: str,
    cfg_of_other_app_prefix: str,
    groups_of_other_app_entrypoints: dict[str, list] | list[str],
) -> Callable[..., InvenioAppsUrlsBuilder]: ...
