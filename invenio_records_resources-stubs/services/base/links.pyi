from collections.abc import Callable, Mapping
from typing import Any

from flask_principal import (
    Identity,
)
from invenio_records_resources.pagination import Pagination
from invenio_records_resources.records.api import FileRecord, Record
from invenio_records_resources.services.files.links import FileEndpointLink
from invenio_records_resources.services.records.links import (
    RecordEndpointLink,
    RecordLink,
)

def preprocess_vars(vars: dict[str, Any]) -> dict[str, Any]: ...

class EndpointLink:
    def __init__(
        self,
        endpoint: str,
        when: Callable | None = ...,
        vars: Callable | None = ...,
        params: list[str] | None = ...,
    ): ...
    def expand(
        self,
        obj: Record | FileRecord | Pagination | Any,
        context: dict[str, Any],
    ) -> str: ...
    def should_render(
        self,
        obj: Record | FileRecord | Pagination | Any,
        context: dict[str, Any],
    ) -> bool: ...
    @staticmethod
    def vars(obj: Any, vars: dict[str, Any]) -> None: ...

class ExternalLink:
    def __init__(
        self,
        uritemplate: str,
        when: Callable | None = ...,
        vars: Callable | None = ...,
    ): ...

class Link:
    def __init__(self, *args, **kwargs): ...

class LinksTemplate:
    def __init__(
        self,
        links: (
            Mapping[
                str,
                RecordLink
                | Link
                | RecordEndpointLink
                | FileEndpointLink
                | EndpointLink,
            ]
            | None
        ) = ...,
        context: Any = ...,
    ): ...
    @property
    def context(
        self,
    ) -> dict[str, Any]: ...
    def expand(
        self,
        identity: Identity,
        obj: Record | FileRecord | Pagination | Any,
    ) -> dict[str, str]: ...

class ConditionalLink:
    def __init__(
        self,
        cond: Callable | None = None,
        if_: Link | EndpointLink | None = None,  # keep typing as there are two different link classes
        else_: Link | EndpointLink | None = None,
    ): ...
    def should_render(
        self, obj: Record | FileRecord | Pagination | Any, ctx: dict[str, Any],
    ) -> bool: ...
    def expand(
        self, obj: Record | FileRecord | Pagination | Any, ctx: dict[str, Any],
    ) -> str: ...

class NestedLinks:
    def __init__(
        self,
        links: dict[
            str,
            RecordLink | Link | RecordEndpointLink | FileEndpointLink | EndpointLink,
        ],
        key: str | None = None,
        load_key: str | None = None,
        dump_key: str | None = None,
        context_func: Any | None = None,
    ): ...
    def context(
        self, identity: Identity, record: Record, key: str, value: Any,
    ) -> dict[str, Any]: ...
    def expand(
        self, identity: Identity, record: Record, data: dict[str, Any],
    ) -> Any: ...
