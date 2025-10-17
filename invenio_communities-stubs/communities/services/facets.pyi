from typing import Any

from invenio_records_resources.services.records.facets.facets import (
    LabelledFacetMixin as LabelledFacetMixin,
)
from invenio_records_resources.services.records.facets.facets import (
    TermsFacet as BaseTermsFacet,
)
from opensearch_dsl.response.aggs import FieldBucket

class TypeFacet(BaseTermsFacet): ...

class VisibilityFacet(BaseTermsFacet):
    def __init__(
        self,
        label: str | None = None,
        value_labels: dict[str, str] | None = None,
        **kwargs: Any,
    ): ...
    def get_label_mapping(self, buckets: list[FieldBucket]) -> dict[str, str]: ...

class RoleFacet(BaseTermsFacet): ...

# exported facet instances used by search options
type: TypeFacet
visibility: VisibilityFacet
role: RoleFacet
visible: BaseTermsFacet
