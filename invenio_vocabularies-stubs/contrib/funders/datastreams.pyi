from typing import Any

from invenio_vocabularies.contrib.common.ror.datastreams import (
    RORTransformer as RORTransformer,
)
from invenio_vocabularies.datastreams.writers import ServiceWriter as ServiceWriter

class FundersServiceWriter(ServiceWriter):
    def __init__(self, *args, **kwargs) -> None: ...
    def _entry_id(self, entry): ...

class FundersRORTransformer(RORTransformer):
    def __init__(
        self, *args, vocab_schemes=None, funder_fundref_doi_prefix=None, **kwargs,
    ) -> None: ...

VOCABULARIES_DATASTREAM_READERS: dict[str, type[Any]]
VOCABULARIES_DATASTREAM_WRITERS: dict[str, type[FundersServiceWriter]]
VOCABULARIES_DATASTREAM_TRANSFORMERS: dict[str, type[FundersRORTransformer]]
DATASTREAM_CONFIG: dict[str, Any]
