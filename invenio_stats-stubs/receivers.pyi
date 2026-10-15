from typing import TypedDict, Unpack

from flask import Flask
from invenio_records_resources.records.api import Record


class EventEmitterKwargs(TypedDict):
    record: Record
    via_api: bool

class EventEmitter:
    def __init__(self, name: str, builders) -> None: ...
    def __call__(
        self,
        *args: *tuple[Flask],
        **kwargs: Unpack[EventEmitterKwargs],
    ) -> None: ...

def build_event_emitter(
    event_name: str,
    events_config: dict | None = None,
) -> EventEmitter: ...
def register_receivers(app: Flask, config: dict) -> None: ...

# for backwards compatibility
EventEmmiter = EventEmitter
