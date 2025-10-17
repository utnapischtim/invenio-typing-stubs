import abc
from collections.abc import Collection, Sequence
from typing import Any, ClassVar, Iterator

from flask_principal import ActionNeed as ActionNeed
from flask_principal import Identity, Need
from invenio_records.api import Record
from invenio_search.engine import dsl

# keep typing: using record: Record here instead of dict to be consistent with the usage
# in invenio_records_resources and elsewhere.

class Generator:
    def needs(self, **kwargs: Any) -> Collection[Need]: ...
    def excludes(self, **kwargs: Any) -> Collection[Need]: ...
    def query_filter(
        self,
        **kwargs: Any,
    ) -> dsl.query.Query | list[dsl.query.Query] | None: ...

class AnyUser(Generator):
    def needs(self, **kwargs: Any) -> Sequence[Need]: ...
    def query_filter(self, **kwargs: Any) -> dsl.query.Query: ...

class SystemProcess(Generator):
    def needs(self, **kwargs: Any) -> Sequence[Need]: ...
    def query_filter(
        self,
        identity: Identity | None = ...,
        **kwargs: Any,
    ) -> dsl.query.Query | list[dsl.query.Query] | None: ...

class SystemProcessWithoutSuperUser(SystemProcess):
    @staticmethod
    def _expand_superuser_access_action() -> Iterator[Any]: ...
    def excludes(self, **kwargs: Any) -> Collection[Need]: ...

class Disable(Generator):
    def excludes(self, **kwargs: Any) -> Collection[Need]: ...
    def query_filter(self, **kwargs: Any) -> dsl.query.Query: ...

class RecordOwners(Generator):
    def needs(
        self,
        record: Record | None = ...,
        **kwargs: Any,
    ) -> Collection[Need]: ...
    def query_filter(
        self,
        identity: Identity | None = ...,
        **kwargs: Any,
    ) -> dsl.query.Query | list[dsl.query.Query] | None: ...

class AnyUserIfPublic(Generator):
    def needs(
        self,
        record: Record | None = ...,
        **kwargs: Any,
    ) -> Collection[Need]: ...
    def excludes(
        self,
        record: Record | None = ...,
        **kwargs: Any,
    ) -> Collection[Need]: ...
    def query_filter(self, **kwargs: Any) -> dsl.query.Query: ...

class AuthenticatedUser(Generator):
    def needs(self, **kwargs: Any) -> Collection[Need]: ...
    def query_filter(self, **kwargs: Any) -> dsl.query.Query: ...

class AllowedByAccessLevel(Generator):
    ACTION_TO_ACCESS_LEVELS: ClassVar[dict[str, list[str]]]
    action: str
    def __init__(self, action: str = "read") -> None: ...
    def needs(
        self,
        record: Record | None = ...,
        **kwargs: Any,
    ) -> Collection[Need]: ...
    def query_filter(
        self,
        identity: Identity | None = ...,
        **kwargs: Any,
    ) -> dsl.query.Query | list[dsl.query.Query] | None: ...

class AdminAction(Generator):
    action: Need
    def __init__(self, action: Need) -> None: ...
    def needs(self, **kwargs: Any) -> Sequence[Need]: ...
    def query_filter(
        self,
        identity: Identity | None = ...,
        **kwargs: Any,
    ) -> dsl.query.Query | list[dsl.query.Query] | None: ...

class ConditionalGenerator(Generator, metaclass=abc.ABCMeta):
    then_: Sequence[Generator]
    else_: Sequence[Generator]
    def __init__(
        self,
        then_: Sequence[Generator],
        else_: Sequence[Generator],
    ) -> None: ...
    @abc.abstractmethod
    def _condition(self, **kwargs: Any) -> bool: ...
    def _generators(
        self,
        record: Record | None = ...,
        **kwargs: Any,
    ) -> Sequence[Generator]: ...
    def needs(
        self,
        record: Record | None = ...,
        **kwargs: Any,
    ) -> Collection[Need]: ...
    def excludes(
        self,
        record: Record | None = ...,
        **kwargs: Any,
    ) -> Collection[Need]: ...
    @staticmethod
    def _make_query(
        generators: Sequence[Generator],
        **kwargs: Any,
    ) -> dsl.query.Query | None: ...

class CompositeGenerator(Generator, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _generators(self, **context: Any) -> Sequence[Generator]: ...
    def needs(self, **context: Any) -> list[Need]: ...
    def excludes(self, **context: Any) -> list[Need]: ...
    def query_filter(self, **context: Any) -> dsl.query.Query | None: ...

class SameAs(CompositeGenerator):
    def __init__(self, permission_name: str) -> None: ...
    def _generators(self, **context: Any) -> list[Generator]: ...
    def __add__(self, other: Sequence[Generator] | Generator) -> list[Generator]: ...
    def __iter__(self) -> Iterator[SameAs]: ...

class IfConfig(ConditionalGenerator):
    accept_values: Sequence[Any]
    config_key: str
    def __init__(
        self,
        config_key: str,
        accept_values: Sequence[Any] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def _condition(self, **kwargs: Any) -> bool: ...
