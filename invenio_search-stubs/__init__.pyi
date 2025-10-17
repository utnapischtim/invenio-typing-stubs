from invenio_search.api import (
    RecordsSearch,
    RecordsSearchV2,
    UnPrefixedRecordsSearch,
    UnPrefixedRecordsSearchV2,
)
from invenio_search.ext import InvenioSearch
from invenio_search.proxies import current_search, current_search_client

__version__: str

__all__ = (
    "InvenioSearch",
    "RecordsSearch",
    "RecordsSearchV2",
    "UnPrefixedRecordsSearch",
    "UnPrefixedRecordsSearchV2",
    "__version__",
    "current_search",
    "current_search_client",
)
