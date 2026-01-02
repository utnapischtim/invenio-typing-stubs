"""
Directory structure replicator for Python packages.

Handles the replication of the package directory structure and converts .py files to .pyi files
with extracted definitions.
"""

from parser import PythonFileParser
from pathlib import Path

import click
from writer import StubFileWriter


class PackageReplicator:
    """Replicates a Python package structure as .pyi stub files."""

    def __init__(self, source: Path, output: Path, *, verbose: bool = False) -> None:
        """
        Initialize the replicator.

        Args:
            source: Path to the source Python package
            output: Path to the output directory for .pyi files
            verbose: Whether to print verbose output
        """
        self.source = source
        self.output = output
        self.verbose = verbose
        self.parser = PythonFileParser()
        self.writer = StubFileWriter()

    def replicate(self) -> None:
        """
        Replicate the package structure by walking through all directories and files.

        For each Python file found, extract definitions and write .pyi files.
        """
        self._walk_and_replicate(self.source)

    def _walk_and_replicate(self, current_source: Path) -> None:
        """
        Recursively walk through the source directory structure.

        Args:
            current_source: Current directory being processed
        """
        relative_path = current_source.relative_to(self.source)
        current_output = self.output / relative_path
        current_output.mkdir(parents=True, exist_ok=True)

        for item in sorted(current_source.iterdir()):
            if item.is_dir() and (
                "alembic" in item.name
                or "translations" in item.name
                or "tests" in item.name
                or "docs" in item.name
                or "build" in item.name
                or "egg" in item.name
                or "examples" in item.name
            ):
                continue

            if item.is_dir() and not item.name.startswith("."):
                self._walk_and_replicate(item)
            elif item.is_file() and item.suffix == ".py":
                self._process_python_file(item)

    def _process_python_file(self, py_file: Path) -> None:
        """
        Process a single Python file by extracting definitions and writing .pyi file.

        Args:
            py_file: Path to the Python file to process
        """
        relative_path = py_file.relative_to(self.source)
        output_file = self.output / relative_path.with_suffix(".pyi")

        try:
            definitions = self.parser.extract_definitions(py_file)
            self.writer.write_stub_file(output_file, definitions)

            if self.verbose:
                click.secho(f"✓ Processed: {relative_path} → {output_file.name}")
        except Exception as e:
            if self.verbose:
                click.secho(f"✗ Error processing {relative_path}: {e}")
