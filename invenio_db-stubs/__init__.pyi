from invenio_db.ext import InvenioDB
from invenio_db.shared import db

__version__: str
__all__ = (
    "InvenioDB",
    "__version__",
    "db",
)

# Note: the precise type of ``db`` is defined in invenio_db.shared as SQLAlchemy,
# which exposes ``Model`` as a type usable as a base class.
