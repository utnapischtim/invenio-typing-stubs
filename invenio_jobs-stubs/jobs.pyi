from abc import ABC
from collections.abc import Callable

from marshmallow import Schema, fields
from marshmallow_utils.fields import TZDateTime


class PredefinedArgsSchema(Schema):
    job_arg_schema: fields.String
    since: TZDateTime


class JobType(ABC):
    id: str | None = None
    title: str | None = None
    description: str | None = None

    task: Callable | None = None

    arguments_schema = PredefinedArgsSchema

    @classmethod
    def create(
        cls,
        job_cls_name: str,
        arguments_schema,
        id_: str,
        task,
        description: str,
        title: str,
        attrs=None,
    ): ...
    @classmethod
    def build_task_arguments(cls, job_obj, since=None, **kwargs): ...
    @classmethod
    def _build_task_arguments(cls, job_obj, since=None, custom_args=None, **kwargs): ...
