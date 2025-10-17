from typing import Any

from flask_principal import Identity
from invenio_records_resources.pagination import Pagination
from invenio_records_resources.records.api import FileRecord, Record
from invenio_records_resources.services.base.links import Link, LinksTemplate
from invenio_requests.records.api import Request

class RequestLinksTemplate(LinksTemplate):
    def __init__(
        self,
        links: dict[str, RequestLink],
        action_link: RequestLink,
        context: dict[str, Any] | None = None,
    ) -> None: ...
    def expand(
        self, identity: Identity, obj: Record | FileRecord | Pagination | Any,
    ) -> dict[str, str]: ...

class RequestLink(Link):
    @staticmethod
    def vars(record: Request, vars: dict[str, Any]) -> None: ...
