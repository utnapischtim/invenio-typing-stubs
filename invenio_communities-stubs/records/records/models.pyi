from typing import Any, ClassVar

from invenio_communities.communities.records.models import (
    CommunityMetadata as CommunityMetadata,
)
from sqlalchemy.ext.declarative import declared_attr

class CommunityRelationMixin:
    __record_model__: ClassVar[type[Any] | None]
    __request_model__: ClassVar[type[Any] | None]
    @declared_attr
    def community_id(cls): ...
    @declared_attr
    def record_id(cls): ...
    @declared_attr
    def request_id(cls): ...
