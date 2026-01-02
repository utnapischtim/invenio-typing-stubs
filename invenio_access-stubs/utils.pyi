from flask_principal import Identity
from invenio_accounts.models import User


def get_identity(user: User) -> Identity: ...
