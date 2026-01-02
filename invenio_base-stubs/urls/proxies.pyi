from werkzeug.local import LocalProxy
from werkzeug.routing import MapAdapter


def other_bind() -> MapAdapter: ...

other_app_map_adapter: LocalProxy

def current_bind() -> MapAdapter: ...

current_app_map_adapter: LocalProxy
