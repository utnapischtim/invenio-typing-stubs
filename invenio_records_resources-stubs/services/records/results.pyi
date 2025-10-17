
from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import Any

from invenio_records_resources.pagination import Pagination
from invenio_records_resources.records.api import Record
from invenio_records_resources.services.base import Service
from invenio_records_resources.services.base.links import Link, LinksTemplate
from invenio_records_resources.services.base.results import (
    ServiceBulkItemResult,
    ServiceBulkListResult,
    ServiceItemResult,
    ServiceListResult,
)
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_records_resources.services.records.service import RecordService

class ExpandableField(ABC):
    def __init__(self, field_name: str): ...
    @property
    def field_name(self) -> str: ...
    @abstractmethod
    def get_value_service(self, value: Any) -> Any: ...
    @abstractmethod
    def ghost_record(self, value: Any) -> Any: ...
    @abstractmethod
    def system_record(self) -> Any: ...
    def has(self, service: Service, value: Any) -> bool: ...
    def add_service_value(self, service: Service, value: Any) -> None: ...
    def add_dereferenced_record(
        self, service: Service, value: Any, resolved_rec: Any,
    ) -> None: ...
    def get_dereferenced_record(self, service: Service, value: Any) -> Any: ...
    @abstractmethod
    def pick(self, identity: Any, resolved_rec: Any) -> Any: ...

class FieldsResolver:
    def __init__(self, expandable_fields: list[ExpandableField] | None): ...
    def resolve(
        self,
        identity: Any,
        hits: Iterable[dict[str, Any]],
    ) -> None: ...
    def expand(
        self,
        identity: Any,
        hit: dict[str, Any],
    ) -> dict[str, Any]: ...

class MultiFieldsResolver(FieldsResolver):
    def expand(self, identity: Any, hit: dict[str, Any]) -> dict[str, Any]: ...

class RecordBulkItem(ServiceBulkItemResult):
    def __init__(
        self,
        op_type: str,
        record: Record,
        errors: list[Any] | None,
        exc: BaseException | None,
    ): ...
    @property
    def errors(self) -> list[Any] | None: ...
    @property
    def op_type(self) -> str: ...
    @property
    def record(
        self,
    ) -> Record: ...
    @property
    def exc(self) -> BaseException | None: ...

class RecordBulkList(ServiceBulkListResult):
    def __init__(self, service: Service, identity: Any, results: list[Any]): ...
    @property
    def results(self) -> Iterator[RecordBulkItem]: ...

class RecordItem(ServiceItemResult):
    _service: RecordService  # keep typing
    _identity: Any  # keep typing
    _record: Record  # keep typing
    _errors: list[Any] | None  # keep typing
    _links_tpl: LinksTemplate | None  # keep typing
    _schema: ServiceSchemaWrapper  # keep typing
    _expandable_fields: list[ExpandableField] | None  # keep typing
    _expand: bool  # keep typing
    _nested_links_item: list[Link] | None  # keep typing
    _data: dict[str, Any] | None  # keep typing

    def __getitem__(self, key: str) -> Any: ...
    def __init__(
        self,
        service: Service,
        identity: Any,
        record: Record,
        errors: list[Any] | None = ...,
        links_tpl: LinksTemplate | None = ...,
        schema: ServiceSchemaWrapper | None = ...,
        expandable_fields: list[ExpandableField] | None = ...,
        expand: bool = ...,
        nested_links_item: list[Link] | None = ...,
    ): ...
    @property
    def _obj(self) -> Record: ...
    @property
    def data(self) -> dict[str, Any]: ...
    def has_permissions_to(self, actions: list[str]) -> dict[str, bool]: ...
    @property
    def id(self) -> str: ...
    @property
    def links(self) -> dict[str, Any]: ...
    @property
    def errors(self) -> list[Any] | None: ...
    def to_dict(self) -> dict[str, Any]: ...

class RecordList(ServiceListResult):
    _expand: bool  # keep typing
    _identity: Any  # keep typing
    _fields_resolver: FieldsResolver | None  # keep typing
    _schema: ServiceSchemaWrapper  # keep typing
    _expandable_fields: list[ExpandableField] | None  # keep typing
    _links_tpl: LinksTemplate | None  # keep typing
    _links_item_tpl: LinksTemplate | None  # keep typing
    _nested_links_item: list[Link] | None  # keep typing
    _service: RecordService  # keep typing
    _results: Any  # keep typing
    _params: Optional[dict[str, Any]]  # keep typing

    def __init__(
        self,
        service: RecordService,
        identity: Any,
        results: Any,
        params: dict[str, Any] | None = ...,
        links_tpl: LinksTemplate | None = ...,
        links_item_tpl: LinksTemplate | None = ...,
        nested_links_item: list[Link] | None = ...,
        schema: ServiceSchemaWrapper | None = ...,
        expandable_fields: list[ExpandableField] | None = ...,
        expand: bool = ...,
    ): ...
    def __iter__(self) -> Iterator[dict[str, Any]]: ...
    def __len__(self) -> int: ...
    @property
    def aggregations(self) -> dict[str, Any] | None: ...
    @property
    def hits(self) -> Iterator[dict[str, Any]]: ...
    @property
    def pagination(self) -> Pagination: ...
    def to_dict(self) -> dict[str, Any]: ...
    @property
    def total(self) -> int | None: ...
