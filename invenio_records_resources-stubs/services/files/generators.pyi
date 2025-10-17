from collections.abc import Sequence
from typing import Any

from invenio_records_permissions.generators import ConditionalGenerator, Generator

class IfTransferType(ConditionalGenerator):
    _transfer_type: Any

    def __init__(
        self,
        transfer_type: Any,
        then_: Generator | Sequence[Generator],
        else_: Generator | Sequence[Generator] | None = ...,
    ) -> None: ...
    def _condition(self, **kwargs: Any) -> bool: ...
