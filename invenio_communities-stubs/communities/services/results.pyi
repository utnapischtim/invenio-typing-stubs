from collections.abc import Generator
from typing import Any

from flask_principal import Identity
from flask_sqlalchemy.pagination import QueryPagination
from invenio_communities.communities.services.links import CommunityLinksTemplate
from invenio_communities.communities.services.service import CommunityService
from invenio_records_resources.services.base.links import LinksTemplate
from invenio_records_resources.services.records.results import RecordItem, RecordList
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_requests.services.results import EntityResolverExpandableField

class CommunityListResult(RecordList):
    def __init__(
        self,
        service: CommunityService,
        identity: Identity,
        results: QueryPagination,
        params: dict[str, str | int] | None = None,
        links_tpl: LinksTemplate | None = None,
        links_item_tpl: CommunityLinksTemplate | None = None,
        schema: ServiceSchemaWrapper | None = None,
        expandable_fields: list[EntityResolverExpandableField] | None = None,
        expand: bool = False,
    ) -> None: ...
    @property
    def hits(self) -> Generator[dict[str, Any]]: ...

class CommunityFeaturedList(CommunityListResult):
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def total(self) -> int: ...
    @property
    def hits(self) -> Generator[dict[str, Any]]: ...

class CommunityItem(RecordItem):
    @property
    def links(self) -> dict[str, str]: ...
    def to_dict(self) -> dict[str, Any]: ...

class FeaturedCommunityItem(CommunityItem): ...
