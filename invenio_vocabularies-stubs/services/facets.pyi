
from invenio_cache.decorators import cached_with_expiration
from invenio_vocabularies.proxies import current_service as current_service

def get_service(service_id): ...
def get_vocabs(service_id, type, fields, ids): ...
@cached_with_expiration
def get_cached_vocab(service_id, type, fields, id_): ...
def lazy_get_label(vocab_item): ...

class VocabularyLabels:
    vocabulary: str
    cache: bool
    cache_ttl: int
    fields: list[str]
    service_id: str | None
    id_field: str
    def __init__(
        self,
        vocabulary: str,
        cache: bool = True,
        cache_ttl: int = 3600,
        service_id: str | None = None,
        id_field: str = "id",
    ) -> None: ...
    def __call__(self, ids): ...
