"""
CLI entry point for the Python package structure replicator.

Handles argument parsing and orchestrates the replication process using Click.
"""

from pathlib import Path

import click

from replicator import PackageReplicator


@click.command()
@click.option("--source", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option("--output", type=click.Path(file_okay=False, dir_okay=True))
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def replicate(source: str, output: str, *, verbose: bool) -> None:
    """
    Replicate a Python package structure as .pyi stub files.

    SOURCE: Base directory of the Python package to replicate
    OUTPUT: Directory where the replicated structure will be created
    """
    source_path = Path(source)
    output_path = Path(output)

    if not source_path.is_dir():
        click.echo(f"Error: Source directory '{source}' not found", err=True)
        raise SystemExit(1)

    try:
        replicator = PackageReplicator(source_path, output_path, verbose=verbose)
        replicator.replicate()
        click.secho(
            f"✓ Successfully replicated package structure to {output_path}",
            fg="green",
        )
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1) from e


if __name__ == "__main__":
    replicate()
