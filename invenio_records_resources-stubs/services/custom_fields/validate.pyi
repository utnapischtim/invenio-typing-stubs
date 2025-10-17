
from invenio_records_resources.services.custom_fields.base import BaseCF

def validate_custom_fields(
    available_fields: list[BaseCF],
    namespaces: set[str] | None = ...,
    given_fields: list[str] | None = ...,
) -> None: ...
