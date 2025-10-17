from typing import Any

from invenio_records_resources.services.custom_fields import KeywordCF
from invenio_vocabularies.services.custom_fields import VocabularyCF

CODEMETA_NAMESPACE: dict[str, str]

CODEMETA_CUSTOM_FIELDS: list[KeywordCF | VocabularyCF]

CODEMETA_CUSTOM_FIELDS_UI: dict[str, Any]

CODEMETA_FACETS: dict[str, dict[str, Any]]
