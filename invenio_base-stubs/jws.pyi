from datetime import datetime
from typing import Any, Iterable, overload

from itsdangerous.serializer import Serializer, _PDataSerializer
from itsdangerous.signer import Signer, SigningAlgorithm


class JSONWebSignatureSerializer(Serializer):
    # jws_algorithms: ...
    # default_algorithm: ...
    # default_serializer: ...

    def __init__(
        self,
        secret_key: str | bytes | Iterable[str] | Iterable[bytes],
        salt: str | bytes | None = None,
        serializer: Any | None = None,
        serializer_kwargs: dict[str, Any] | None = None,
        signer: type[Signer] | None = None,
        signer_kwargs: dict[str, Any] | None = None,
        algorithm_name: Any = None,
    ) -> None: ...
    def load_payload(
        self,
        payload: str | bytes,
        serializer: _PDataSerializer | None = None,
        *,
        return_header: bool = False,
    ) -> Any: ...
    @overload
    def dump_payload(self, header: dict[str, Any], obj: Any) -> bytes: ...
    @overload
    def dump_payload(self, obj: Any) -> bytes: ...
    def make_algorithm(self, algorithm_name: str) -> SigningAlgorithm: ...
    def make_signer(
        self, salt: str | bytes | None = None, algorithm: SigningAlgorithm | None = None
    ) -> Signer: ...
    def make_header(self, header_fields: dict[str, Any] | None) -> dict[str, Any]: ...
    def dumps(
        self,
        obj: Any,
        salt: str | bytes | None = None,
        header_fields: dict[str, Any] | None = None,
    ) -> bytes: ...
    @overload
    def loads(
        self,
        s: str | bytes,
        salt: str | bytes | None = None,
        *,
        return_header: bool = False,
    ) -> Any: ...
    @overload
    def loads(
        self,
        s: str | bytes,
        salt: str | bytes | None = None,
        **kwargs: Any,
    ) -> Any: ...
    def loads_unsafe(
        self,
        s: str | bytes,
        salt: str | bytes | None = None,
        *,
        return_header: bool = False,
    ) -> tuple[bool, Any]: ...

class TimedJSONWebSignatureSerializer(JSONWebSignatureSerializer):
    # DEFAULT_EXPIRES_IN: ...

    def __init__(
        self,
        secret_key: str | bytes | Iterable[str] | Iterable[bytes],
        expires_in: int | None = None,
        **kwargs: dict,
    ) -> None: ...
    def make_header(self, header_fields: dict[str, Any] | None) -> dict[str, Any]: ...
    @overload
    def loads(
        self,
        s: str | bytes,
        salt: str | bytes | None = None,
        *,
        return_header: bool = False,
    ) -> Any: ...
    @overload
    def loads(
        self,
        s: str | bytes,
        salt: str | bytes | None = None,
        **kwargs: Any,
    ) -> Any: ...
    def get_issue_date(self, header: dict[str, Any]) -> datetime | None: ...
    def now(self) -> int: ...
