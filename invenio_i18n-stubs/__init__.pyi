from flask_babel import (
    Babel,
    LazyString,
    force_locale,
    get_locale,
    gettext,
    lazy_gettext,
)
from invenio_i181n.ext import InvenioI18N

_ = gettext
__version__: str

__all__ = (
    "Babel",
    "InvenioI18N",
    "LazyString",
    "_",
    "__version__",
    "force_locale",
    "get_locale",
    "gettext",
    "lazy_gettext",
)
