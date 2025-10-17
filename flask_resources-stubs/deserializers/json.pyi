

from flask_resources.deserializers.base import DeserializerMixin

type JSONValue = (
    str | int | float | bool | None | dict[str, JSONValue] | list[JSONValue]
)

class JSONDeserializer(DeserializerMixin):
    def deserialize(
        self, data: str | bytes | bytearray | memoryview | None,
    ) -> JSONValue | None: ...
