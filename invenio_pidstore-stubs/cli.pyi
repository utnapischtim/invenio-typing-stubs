"""Click command-line interface for PIDStore management.

Type stubs for invenio_pidstore.cli.
"""


import click
from invenio_pidstore.models import PIDStatus as PIDStatus

def process_status(
    ctx: click.Context, param: click.Parameter, value: str | None,
) -> PIDStatus | None: ...
@click.group()
def pid() -> None: ...
@pid.command()
@click.argument("pid_type")
@click.argument("pid_value")
@click.option("-s", "--status", default="NEW", callback=process_status)
@click.option("-t", "--type", "object_type", default=None)
@click.option("-i", "--uuid", "object_uuid", default=None)
def create(
    pid_type: str,
    pid_value: str,
    status: PIDStatus,
    object_type: str | None,
    object_uuid: str | None,
) -> None: ...
@pid.command()
@click.argument("pid_type")
@click.argument("pid_value")
@click.option("-s", "--status", default=None, callback=process_status)
@click.option("-t", "--type", "object_type", required=True)
@click.option("-i", "--uuid", "object_uuid", required=True)
@click.option("--overwrite", is_flag=True, default=False)
def assign(
    pid_type: str,
    pid_value: str,
    status: PIDStatus | None,
    object_type: str,
    object_uuid: str,
    overwrite: bool,
) -> None: ...
@pid.command()
@click.argument("pid_type")
@click.argument("pid_value")
def unassign(pid_type: str, pid_value: str) -> None: ...
@pid.command("get")
@click.argument("pid_type")
@click.argument("pid_value")
def get_object(pid_type: str, pid_value: str) -> None: ...
@pid.command("dereference")
@click.argument("object_type")
@click.argument("object_uuid")
@click.option("-s", "--status", default=None, callback=process_status)
def dereference_object(
    object_type: str,
    object_uuid: str,
    status: PIDStatus | None,
) -> None: ...
