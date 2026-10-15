re  # -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2026 CERN.
# Copyright (C)      2022 TU Wien.
# Copyright (C) 2026 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for collecting statistics."""

from collections import namedtuple

from flask import Flask
from invenio_base.utils import load_or_import_from_config, obj_or_import_string
from invenio_queues.proxies import current_queues
from werkzeug.utils import cached_property

from . import config
from .queries import Query
from .receivers import EventEmitter, build_event_emitter, register_receivers

_Event = namedtuple("Event", ["name", "queue", "templates", "cls", "params"])

_Aggregation = namedtuple("Aggregation", ["name", "templates", "cls", "params"])

_Query = namedtuple("Query", ["name", "cls", "permission_factory", "params"])

class _InvenioStatsState:
    """State object for Invenio stats."""

    def __init__(self, app: Flask) -> None: ...
    @property
    def events_config(self) -> dict: ...
    @property
    def aggregations_config(self) -> dict: ...
    @property
    def queries_config(self) -> dict: ...
    def get_event_emitter(self, event_name: str) -> EventEmitter: ...
    def get_query(self, query_name: str) -> Query: ...
    @cached_property
    def events(self) -> dict: ...
    @cached_property
    def aggregations(self) -> dict: ...
    @cached_property
    def queries(self) -> dict: ...
    @cached_property
    def permission_factory(self) -> None: ...
    def publish(self, event_type: str, events: list) -> None: ...
    def consume(self, event_type: str, no_ack: bool = True, payload: bool = True): ...

class InvenioStats(object):
    """Invenio-Stats extension."""

    def __init__(self, app: Flask | None = None, **kwargs: dict) -> None: ...
    def init_app(self, app: Flask) -> _InvenioStatsState: ...
    def init_config(self, app: Flask) -> None: ...
    def __getattr__(self, name: str): ...

def finalize_app(app: Flask) -> None: ...
