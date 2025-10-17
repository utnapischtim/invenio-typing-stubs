from typing import Any

from invenio_vocabularies.datastreams.datastreams import DataStream as DataStream
from invenio_vocabularies.datastreams.errors import FactoryError as FactoryError

class OptionsConfigMixin:
    CONFIG_VAR: str
    @classmethod
    def options(cls) -> dict[str, Any]: ...

class Factory:
    FACTORY_NAME: str
    @classmethod
    def create(cls, config: dict[str, Any]): ...

class WriterFactory(Factory, OptionsConfigMixin):
    FACTORY_NAME: str
    CONFIG_VAR: str

class ReaderFactory(Factory, OptionsConfigMixin):
    FACTORY_NAME: str
    CONFIG_VAR: str

class TransformerFactory(Factory, OptionsConfigMixin):
    FACTORY_NAME: str
    CONFIG_VAR: str

class DataStreamFactory:
    @classmethod
    def create(
        cls,
        readers_config: list[dict[str, Any]],
        writers_config: list[dict[str, Any]],
        transformers_config: list[dict[str, Any]] | None = None,
        **kwargs,
    ) -> DataStream: ...
