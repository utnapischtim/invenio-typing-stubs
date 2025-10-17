from typing import Any, Generic, TypeVar

from flask.blueprints import Blueprint
from invenio_records_resources.resources import RecordResource
from invenio_records_resources.resources.records.resource import (
    request_data,
    request_extra_args,
    request_headers,
    request_search_args,
    request_view_args,
)
from invenio_requests.resources.requests.config import RequestsResourceConfig
from invenio_requests.services.requests.service import RequestsService

C = TypeVar("C", bound=RequestsResourceConfig)
S = TypeVar("S", bound=RequestsService)

class RequestsResource(RecordResource[C, S], Generic[C, S]):
    def create_blueprint(self, **options: Any) -> Blueprint: ...
    def create_url_rules(self): ...
    @request_extra_args
    @request_search_args
    @request_view_args
    def search(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_search_args
    @request_view_args
    def search_user_requests(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_view_args
    def read(self) -> tuple[dict[str, Any], int]: ...
    @request_extra_args
    @request_headers
    @request_view_args
    @request_data
    def update(self) -> tuple[dict[str, Any], int]: ...
    @request_headers
    @request_view_args
    def delete(self) -> tuple[str, int]: ...
    @request_extra_args
    @request_view_args
    @request_headers
    @request_data
    def execute_action(self) -> tuple[dict[str, Any], int]: ...
