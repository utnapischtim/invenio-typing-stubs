from collections.abc import Callable
from typing import Any

from flask_principal import Need

LinkNeed: Callable[[Any], Need]
