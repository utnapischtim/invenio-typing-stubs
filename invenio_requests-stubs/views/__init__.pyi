from flask import Blueprint
from invenio_requests.views.api import (
    create_request_events_bp as create_request_events_bp,
)
from invenio_requests.views.api import create_requests_bp as create_requests_bp
from invenio_requests.views.ui import create_ui_blueprint as create_ui_blueprint

__all__ = [
    "blueprint",
    "create_request_events_bp",
    "create_requests_bp",
    "create_ui_blueprint",
]

blueprint: Blueprint
