from collections.abc import Iterator
from typing import Any, Generic, TypeVar

from flask import Flask
from invenio_records_permissions.policies import BasePermissionPolicy
from invenio_records_resources.services.base.results import (
    ServiceBulkItemResult,
    ServiceBulkListResult,
    ServiceItemResult,
    ServiceListResult,
)

PermissionPolicyT = TypeVar("PermissionPolicyT", bound=BasePermissionPolicy)

class ServiceConfig(Generic[PermissionPolicyT]):
    service_id: str | None
    permission_policy_cls: type[PermissionPolicyT]
    result_item_cls: type[ServiceItemResult]
    result_list_cls: type[ServiceListResult]
    result_bulk_item_cls: type[ServiceBulkItemResult]
    result_bulk_list_cls: type[ServiceBulkListResult]

def _make_cls(cls: type, attrs: dict[str, Any]) -> type: ...

class ConfiguratorMixin:
    """Shared customization for requests service config."""

    @classmethod
    def build(cls, app: Flask) -> ServiceConfig[Any]: ...

class SearchOptionsMixin:
    """Customization of search options."""

    @classmethod
    def customize(cls, opts: Any) -> type: ...

class FromConfig:
    """Data descriptor to connect config with application configuration."""

    config_key: str
    default: Any
    import_string: bool

    def __init__(
        self, config_key: str, default: Any = ..., import_string: bool = ...,
    ) -> None: ...
    def __get__(self, obj: Any, objtype: type = ...) -> Any: ...
    def __set_name__(self, owner: type, name: str) -> None: ...
    def __set__(self, obj: Any, value: Any) -> None: ...

class OptionsSelector:
    """Generic helper to select and validate facet/sort options."""

    iterate_all_options: bool
    available_options: dict[str, Any]
    selected_options: list[str]

    def __init__(
        self, available_options: dict[str, Any], selected_options: list[str],
    ) -> None: ...
    def __iter__(self) -> Iterator[tuple[str, Any]]: ...
    def map_option(self, key: str, option: Any) -> tuple[str, Any]: ...
    def __call__(self) -> OptionsSelector: ...

class SortOptionsSelector(OptionsSelector):
    """Sort options for the search configuration."""

    default: str
    default_no_query: str

    def __init__(
        self,
        available_options: dict[str, Any],
        selected_options: list[str],
        default: str | None = ...,
        default_no_query: str | None = ...,
    ) -> None: ...

class SearchConfig:
    """Search endpoint configuration."""

    _sort: Any
    _facets: Any
    _query_parser_cls: type | None

    def __init__(
        self,
        config: dict[str, Any] | None = ...,
        sort: dict[str, Any] | None = ...,
        facets: dict[str, Any] | None = ...,
    ) -> None: ...
    @property
    def sort_options(self) -> dict[str, Any]: ...
    @property
    def available_sort_options(self) -> dict[str, Any]: ...
    @property
    def sort_default(self) -> str | None: ...
    @property
    def sort_default_no_query(self) -> str | None: ...
    @property
    def facets(self) -> dict[str, Any]: ...
    @property
    def query_parser_cls(self) -> type | None: ...

class FromConfigSearchOptions:
    """Data descriptor for search options configuration."""

    config_key: str
    sort_key: str
    facet_key: str
    default: dict[str, Any]
    search_option_cls: type | None
    search_option_cls_key: str | None

    def __init__(
        self,
        config_key: str,
        sort_key: str,
        facet_key: str,
        default: dict[str, Any] | None = ...,
        search_option_cls: type | None = ...,
        search_option_cls_key: str | None = ...,
    ) -> None: ...
    def __get__(self, obj: Any, objtype: type = ...) -> Any: ...
