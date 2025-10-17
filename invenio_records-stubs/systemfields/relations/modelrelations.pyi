from typing import Any

from invenio_records.api import Record
from invenio_records.systemfields.relations.relations import RelationBase
from invenio_records.systemfields.relations.results import RelationResult

class ModelRelationResult(RelationResult):
    def _lookup_id(self, *args: Any) -> Any: ...
    def validate(self) -> None: ...
    def dereference(
        self, keys: list[str] | None = ..., attrs: list[str] | None = ...,
    ) -> Any: ...
    def clean(
        self, keys: list[str] | None = ..., attrs: list[str] | None = ...,
    ) -> Any: ...

class ModelRelation(RelationBase):
    result_cls: type[RelationResult]
    _record_cls: type[Record]
    _model_field_name: str

    def __init__(
        self,
        record_cls: type[Record],
        model_field_name: str,
        key: str,
        keys: list[str] | None = ...,
        attrs: list[str] | None = ...,
    ): ...
    def resolve(self, id_: str) -> Any | None: ...
    def parse_value(self, value: Any) -> Any: ...
    def set_value(self, record: Any, value: Any) -> None: ...
    def get_value(self, record: Any) -> ModelRelationResult: ...
    def clear_value(self, record: Any) -> None: ...
