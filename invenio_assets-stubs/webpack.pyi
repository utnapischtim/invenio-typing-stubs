class WebpackThemeBundle:
    def __init__(
        self,
        import_name: str,
        folder: str,
        default: str | None = None,
        themes: dict[str, dict[str, dict[str, str]]] | None = None,
    ) -> None: ...
