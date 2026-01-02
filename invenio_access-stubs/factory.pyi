from flask_principal import Need


def action_factory(
    name: str,
    *,
    parameter: bool = False,
) -> Need: ...
