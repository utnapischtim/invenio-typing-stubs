from collections.abc import Callable, Iterable
from typing import Any, Protocol

# Define basic WSGI types
type Environ = dict[str, Any]
type Headers = list[tuple[str, str]]
type ExcInfo = list[Any]
type StartResponse = Callable[[str, Headers, ExcInfo], Iterable[bytes]]
type WSGICallable = Callable[[Environ, StartResponse], Iterable[bytes]]

class WSGIApplication(Protocol):
    """Protocol for WSGI applications."""

    def __call__(
        self, environ: Environ, start_response: StartResponse
    ) -> Iterable[bytes]:
        """Handle WSGI call."""
        ...
    wsgi_app: WSGICallable
    config: dict[str, Any]

def create_wsgi_factory(
    mounts_factories: dict[str, Callable[..., WSGIApplication]],
) -> Callable[[WSGIApplication], WSGICallable]: ...
def wsgi_proxyfix[T: WSGIApplication](
    factory: Callable[..., T] | None = None,
) -> Callable[[T], WSGICallable]: ...
