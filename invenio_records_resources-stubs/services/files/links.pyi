from typing import Any

from invenio_records_resources.services.base import EndpointLink, Link

class FileLink(Link):
    @staticmethod
    def vars(obj: Any, vars: dict[str, Any]) -> None: ...

class FileEndpointLink(EndpointLink):
    @staticmethod
    def vars(obj: Any, vars: dict[str, Any]) -> None: ...
