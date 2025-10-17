from typing import Any

from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_records_resources.services.base.links import (
    EndpointLink,
    Link,
    LinksTemplate,
)

class CommunityLinksTemplate(LinksTemplate):
    def __init__(
        self,
        links: dict[str, CommunityEndpointLink | CommunityUIEndpointLink],
        action_link: CommunityEndpointLink,
        available_actions: list[dict[str, str]],
        context: dict[str, type[CommunityPermissionPolicy]] | None = None,
    ) -> None: ...
    def expand(self, identity: Any, obj: Any) -> dict[str, str]: ...

class CommunityEndpointLink(EndpointLink):
    @staticmethod
    def vars(obj: Any, vars: dict[str, Any]) -> None: ...

class CommunityUIEndpointLink(EndpointLink):
    @staticmethod
    def vars(obj: Any, vars: dict[str, Any]) -> None: ...

class CommunityLink(Link):
    @staticmethod
    def vars(obj: Any, vars: dict[str, Any]) -> None: ...
