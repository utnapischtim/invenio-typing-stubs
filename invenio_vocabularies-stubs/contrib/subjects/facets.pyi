from collections.abc import Iterable

class SubjectsLabels:
    def __call__(self, ids: Iterable[str]) -> dict[str, str]: ...
