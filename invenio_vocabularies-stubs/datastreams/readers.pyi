import abc
from abc import ABC
from collections.abc import Generator
from pathlib import Path
from typing import Any

from invenio_vocabularies.datastreams.errors import ReaderError as ReaderError
from invenio_vocabularies.datastreams.xml import etree_to_dict as etree_to_dict
from lxml import etree

class BaseReader(ABC, metaclass=abc.ABCMeta):
    def __init__(
        self,
        origin: Path | str | None = None,
        mode: str = "r",
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def read(self, item=None, *args, **kwargs) -> Generator[Any]: ...

class YamlReader(BaseReader): ...

class TarReader(BaseReader):
    def __init__(
        self, *args, mode: str = "r|gz", regex: str | None = None, **kwargs: Any,
    ) -> None: ...

class SimpleHTTPReader(BaseReader):
    content_type: str | None
    def __init__(
        self,
        origin: Path | str | None = None,
        id: str | None = None,
        ids: list[str] | None = None,
        content_type: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def read(self, item=None, *args, **kwargs) -> Generator[bytes]: ...

class ZipReader(BaseReader):
    def __init__(
        self,
        *args: Any,
        options: dict[str, Any] | None = None,
        regex: str | None = None,
        **kwargs: Any,
    ) -> None: ...

class JsonReader(BaseReader): ...
class JsonLinesReader(BaseReader): ...
class GzipReader(BaseReader): ...

class CSVReader(BaseReader):
    csv_options: dict[str, Any]
    as_dict: bool
    def __init__(
        self,
        *args: Any,
        csv_options: dict[str, Any] | None = None,
        as_dict: bool = True,
        **kwargs: Any,
    ) -> None: ...

class XMLReader(BaseReader):
    root_element: str | None
    def __init__(
        self, root_element: etree._Element | None = None, *args: Any, **kwargs: Any,
    ) -> None: ...

class OAIPMHReader(BaseReader):
    def __init__(
        self,
        *args: Any,
        base_url: str | None = None,
        metadata_prefix: str | None = None,
        set: str | None = None,
        from_date=None,
        until_date=None,
        verb: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def read(
        self, item=None, *args, **kwargs,
    ) -> Generator[dict[str, Any]]: ...

def xml_to_dict(tree: etree._Element) -> dict[str, Any]: ...

class RDFReader(BaseReader):
    @property
    def skos_core(self): ...
    def read(
        self, item: Any = None, *args: Any, **kwargs: Any,
    ) -> Generator[dict[str, Any]]: ...

class SPARQLReader(BaseReader):
    def __init__(
        self,
        origin: Path | str | None,
        query: str,
        mode: str = "r",
        client_params: dict[str, Any] | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def read(
        self, item: Any = None, *args: Any, **kwargs: Any,
    ) -> Generator[dict[str, Any]]: ...
