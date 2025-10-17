from collections.abc import Callable, Sequence
from typing import Any, NamedTuple

from flask_principal import Identity, Need
from invenio_communities.communities.records.systemfields.deletion_status import (
    CommunityDeletionStatusEnum as CommunityDeletionStatusEnum,
)
from invenio_communities.members.records.api import Member
from invenio_communities.proxies import current_roles as current_roles
from invenio_records_permissions.generators import Generator
from invenio_search.engine import dsl

class _Need(NamedTuple):
    method: str
    value: str
    role: str

CommunityRoleNeed: Callable[[str, str], Need]

class IfRestrictedBase(Generator):
    field_getter: Callable[[Any], Any]
    field_name: str
    then_value: str
    else_value: str
    then_: list[Generator]
    else_: list[Generator]
    def __init__(
        self,
        field_getter: Callable[[Any], Any],
        field_name: str,
        then_value: str,
        else_value: str,
        then_: list[Generator],
        else_: list[Generator],
    ) -> None: ...
    def generators(self, record: Any) -> list[Generator]: ...
    def needs(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...
    def excludes(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...
    def make_query(
        self, generators: list[Generator], **kwargs: Any,
    ) -> dsl.query.Query | None: ...
    def query_filter(
        self, identity: Identity | None = ..., **kwargs: Any,
    ) -> dsl.query.Query | None: ...

class IfRestricted(IfRestrictedBase):
    def __init__(
        self, field: str, then_: list[Generator], else_: list[Generator],
    ) -> None: ...

class ReviewPolicy(Generator):
    closed_: list[Generator]
    open_: list[Generator]
    members_: list[Generator]
    def __init__(
        self,
        closed_: list[Generator],
        open_: list[Generator],
        members_: list[Generator],
    ) -> None: ...
    def needs(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...
    def excludes(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...

class IfRecordSubmissionPolicyClosed(IfRestrictedBase):
    def __init__(self, then_: list[Generator], else_: list[Generator]) -> None: ...

class IfMemberPolicyClosed(IfRestrictedBase):
    def __init__(self, then_: list[Generator], else_: list[Generator]) -> None: ...

class IfCommunityDeleted(Generator):
    then_: list[Generator]
    else_: list[Generator]
    def __init__(self, then_: list[Generator], else_: list[Generator]) -> None: ...
    def generators(self, record: Any) -> list[Generator]: ...
    def needs(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...
    def excludes(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...
    def make_query(
        self, generators: list[Generator], **kwargs: Any,
    ) -> dsl.query.Query | None: ...
    def query_filter(
        self, identity: Identity | None = ..., **kwargs: Any,
    ) -> dsl.query.Query | None: ...

class AuthenticatedButNotCommunityMembers(Generator):
    def needs(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...
    def excludes(self, record: Any = ..., **kwargs: Any) -> Sequence[Need]: ...

class CommunityRoles(Generator):
    def roles(self, **kwargs: Any) -> list[str]: ...
    def communities(self, identity: Identity) -> list[str]: ...
    def needs(
        self, record: Any = ..., community_id: str | None = ..., **kwargs: Any,
    ) -> Sequence[Need]: ...
    def query_filter(
        self, identity: Identity | None = ..., **kwargs: Any,
    ) -> dsl.query.Query | None: ...

class CommunityMembers(CommunityRoles):
    def roles(self, **kwargs: Any) -> list[str]: ...
    def communities(self, identity: Identity) -> list[str]: ...

class CommunityCurators(CommunityRoles):
    def roles(self, **kwargs: Any) -> list[str]: ...

class CommunityManagers(CommunityRoles):
    def roles(self, **kwargs: Any) -> list[str]: ...

class CommunityManagersForRole(CommunityRoles):
    def roles(
        self, role: str | None = ..., member: Member | None = ..., **kwargs: Any,
    ) -> list[str]: ...

class CommunityOwners(CommunityRoles):
    def roles(self, **kwargs: Any) -> list[str]: ...
    def communities(self, identity: Identity) -> list[str]: ...

class CommunitySelfMember(Generator):
    def needs(
        self, member: Member | None = ..., **kwargs: Any,
    ) -> Sequence[Need]: ...
    def query_filter(
        self, identity: Identity | None = ..., **kwargs: Any,
    ) -> dsl.query.Query | None: ...

class AllowedMemberTypes(Generator):
    allowed_member_types: tuple[str, ...]
    def __init__(self, *allowed_member_types: str) -> None: ...
    def needs(self, **kwargs: Any) -> Sequence[Need]: ...
    def excludes(
        self, member_types: list[str] | None = ..., **kwargs: Any,
    ) -> Sequence[Need]: ...
