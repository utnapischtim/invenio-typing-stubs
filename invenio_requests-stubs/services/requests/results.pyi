from collections.abc import Generator, Iterator
from typing import Any

from flask_principal import Identity
from invenio_records_resources.services.records.results import RecordItem, RecordList
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_requests.records.api import Request
from invenio_requests.services.requests.links import RequestLinksTemplate
from invenio_requests.services.requests.service import RequestsService

class RequestItem(RecordItem):
    def __init__(
        self,
        service: RequestsService,
        identity: Identity,
        request: Request,
        errors: list[dict[str, Any]] | None = None,
        links_tpl: RequestLinksTemplate | None = None,
        schema: ServiceSchemaWrapper | None = None,
        expandable_fields: list[Any] | None = None,
        expand: bool = False,
    ) -> None: ...
    @property
    def _obj(self) -> Request: ...
    @property
    def id(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...
    @property
    def links(self) -> dict[str, Any]: ...
    @property
    def links_tpl(self) -> RequestLinksTemplate: ...
    @links_tpl.setter
    def links_tpl(self, links_tpl: RequestLinksTemplate) -> None: ...
    @property
    def data(self) -> dict[str, Any]: ...
    @property
    def errors(self) -> list[dict[str, Any]]: ...
    def to_dict(self) -> dict[str, Any]: ...
    def has_permissions_to(self, actions: list[str]) -> dict[str, bool]: ...

class RequestList(RecordList):
    def __init__(
        self,
        service: RequestsService,
        identity: Identity,
        results: Iterator[Any],
        params: dict[str, Any] | None = None,
        links_tpl: Any | None = None,
        links_item_tpl: RequestLinksTemplate | None = None,
        expandable_fields: list[Any] | None = None,
        expand: bool = False,
    ) -> None: ...
    @property
    def hits(self) -> Generator[dict[str, Any]]: ...
    def to_dict(self) -> dict[str, Any]: ...
