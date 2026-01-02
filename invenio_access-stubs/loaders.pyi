from flask_principal import Identity


def load_permissions_on_identity_loaded(sender: object, identity: Identity) -> None: ...
