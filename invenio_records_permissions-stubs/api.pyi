
from invenio_records_permissions.policies import BasePermissionPolicy
from invenio_search.engine import dsl

def permission_filter(
    permission: BasePermissionPolicy | None,
) -> dsl.query.Query: ...
