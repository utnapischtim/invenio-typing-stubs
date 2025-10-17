from typing import Any

from celery import shared_task

from ..proxies import current_communities as current_communities

@shared_task
def create_demo_community(
    data: dict[str, Any], logo_path: str | None = None, feature: bool = False,
) -> None: ...
@shared_task
def reindex_featured_entries() -> None: ...
