from typing import Any

from invenio_records_resources.services.custom_fields.base import BaseListCF
from marshmallow.fields import Field

class KeywordCF(BaseListCF):
    def __init__(
        self,
        name: str,
        field_cls: type[Field] = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def mapping(self) -> dict[str, str]: ...

class TextCF(KeywordCF):
    _use_as_filter: bool

    def __init__(
        self,
        name: str,
        field_cls: type[Field] = ...,
        use_as_filter: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def mapping(self) -> dict[str, Any]: ...
