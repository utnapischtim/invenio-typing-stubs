
from flask_principal import Identity
from invenio_communities.communities.records.api import Community
from invenio_communities.members.records.api import MemberMixin as MemberMixin
from invenio_records_resources.services.records.components import ServiceComponent

from ...proxies import current_identities_cache as current_identities_cache
from ...utils import on_group_membership_change as on_group_membership_change
from ...utils import on_user_membership_change as on_user_membership_change

class CommunityMemberCachingComponent(ServiceComponent):
    def _member_changed(
        self,
        member: MemberMixin | dict[str, str],
        community: Community | None = ...,
    ) -> None: ...
    def accept_invite(
        self,
        identity: Identity,
        record: MemberMixin | None = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
    def members_add(
        self,
        identity: Identity,
        record: dict[str, str] | None = ...,
        community: Community | None = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
    def members_delete(
        self,
        identity: Identity,
        record: MemberMixin | dict[str, str] | None = ...,
        community: Community | None = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
    def members_update(
        self,
        identity: Identity,
        record: MemberMixin | dict[str, str] | None = ...,
        community: Community | None = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
