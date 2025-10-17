from abc import abstractmethod

class CustomFieldsException(Exception):
    @property
    @abstractmethod
    def description(self) -> str: ...

class CustomFieldsInvalidArgument(CustomFieldsException):
    arg_name: str
    def __init__(self, arg_name: str): ...
    @property
    def description(self) -> str: ...

class CustomFieldsNotConfigured(CustomFieldsException):
    field_names: set[str]
    def __init__(self, field_names: set[str]): ...
    @property
    def description(self) -> str: ...

class InvalidCustomFieldsNamespace(CustomFieldsException):
    field_name: str
    given_namespace: str
    def __init__(self, field_name: str, given_namespace: str): ...
    @property
    def description(self) -> str: ...
