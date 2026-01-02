from collections.abc import Callable


def jwt_proccessor() -> dict[str, Callable[..., str]]: ...
