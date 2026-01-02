"""
Stub file writer for .pyi file generation.

Formats extracted definitions and writes them to .pyi files in the standard stub format.
"""

from parser import ClassDefinition, MethodDefinition, Module
from pathlib import Path


class StubFileWriter:
    """Writes extracted definitions to .pyi stub files."""

    def write_stub_file(self, output_file: Path, module: Module) -> None:
        """
        Write module definitions to a .pyi stub file.

        Args:
            output_file: Path where the .pyi file will be written
            module: Module object containing all definitions
        """
        output_file.parent.mkdir(parents=True, exist_ok=True)

        lines = []

        # Create lookup dictionaries for quick access
        functions_dict = {func.name: func for func in module.functions}
        variables_dict = {var: var for var in module.variables}
        classes_dict = {cls.name: cls for cls in module.classes}

        # Write items in order as they appear in the original file
        for item_type, item_name in module.items:
            if item_type == "variable" and item_name in variables_dict:
                lines.append(f"{item_name}: ...")
            elif item_type == "function" and item_name in functions_dict:
                func = functions_dict[item_name]
                lines.append(func.signature)
            elif item_type == "class" and item_name in classes_dict:
                cls = classes_dict[item_name]
                lines.extend(self._format_class(cls))

            # Add separator between top-level items (except for the last one)
            if (
                (item_type != module.items[-1][0] or module.items[-1][1] != item_name)
                and lines
                and lines[-1] != ""
            ):
                lines.append("")

        # Write to file
        content = "\n".join(lines).rstrip()
        with output_file.open("w", encoding="utf-8") as f:
            f.write(content)
            if content:
                f.write("\n")

    def _format_class(self, cls: ClassDefinition) -> list[str]:
        """
        Format a class definition as stub file content.

        Args:
            cls: ClassDefinition object

        Returns:
            List of formatted lines
        """
        lines = []

        # Class declaration
        base_str = f"({', '.join(cls.base_classes)})" if cls.base_classes else ""
        lines.append(f"class {cls.name}{base_str}:")

        if not cls.variables and not cls.methods:
            lines.append("    ...")
            return lines

        # Class variables
        lines.extend(f"    {var}: ..." for var in cls.variables)

        if cls.variables and cls.methods:
            lines.append("")

        # Methods
        for method in cls.methods:
            formatted_method = self._format_method(method)
            lines.extend(formatted_method)

        return lines

    def _format_method(self, method: MethodDefinition) -> list[str]:
        """
        Format a method definition with proper indentation.

        Args:
            method: MethodDef object

        Returns:
            List of formatted lines
        """
        lines = []
        indent = "    "

        # Add decorators if needed
        if method.is_property:
            lines.append(f"{indent}@property")
        if method.is_static:
            lines.append(f"{indent}@staticmethod")
        if method.is_class_method:
            lines.append(f"{indent}@classmethod")

        # Add method signature with indentation
        signature = method.signature.replace("def ", "def ")
        lines.append(f"{indent}{signature}")

        return lines
