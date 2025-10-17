
from collections.abc import Generator, Iterable
from typing import Any

def get_user_records(
    user_id: str | int, from_db: bool = ..., status: Iterable[Any] | None = ...,
) -> Generator[str]: ...
