from flask import Flask
from flask_babel import Locale

current_i18n: InvenioI18N

class InvenioI18N:
    def __init__(
        self,
        app: Flask | None = None,
        date_formats: str | None = None,
        localeselector: str | None = None,
        timezoneselector: str | None = None,
        entry_point_group: str = "invenio_18n.translations",
        translation_bundle_entry_point: str = "invenio_18n.translations_bundle",
    ) -> None: ...
    @property
    def locale(self) -> Locale | None: ...
