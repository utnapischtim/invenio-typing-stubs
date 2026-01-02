"""
Python file parser for extracting class and function definitions.

Uses AST to extract class definitions, methods, functions, and global variables
from Python files for .pyi stub file generation.
"""

from ast import (
    Assign,
    Attribute,
    ClassDef,
    FunctionDef,
    List,
    Name,
    Tuple,
    arguments,
    expr,
    parse,
    unparse,
)
from dataclasses import dataclass
from pathlib import Path


@dataclass
class MethodDefinition:
    """Represents a method or function definition."""

    name: str
    signature: str
    is_property: bool = False
    is_static: bool = False
    is_class_method: bool = False
    decorators: list[str] | None = None


@dataclass
class ClassDefinition:
    """Represents a class definition with its methods and variables."""

    name: str
    methods: list[MethodDefinition]
    variables: list[str]
    base_classes: list[str]
    items: list[tuple[str, str]]


@dataclass
class Module:
    """Represents a Python module with its top-level definitions."""

    classes: list[ClassDefinition]
    functions: list[MethodDefinition]
    variables: list[str]
    items: list[tuple[str, str]]


class PythonFileParser:
    """Parses Python files and extracts definitions using AST."""

    def extract_definitions(self, file_path: Path) -> Module:
        """
        Extract all definitions from a Python file.

        Args:
            file_path: Path to the Python file to parse

        Returns:
            Module object containing all extracted definitions
        """
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read()

        try:
            tree = parse(content)
        except SyntaxError as e:
            msg = f"Invalid Python syntax in {file_path}: {e}"
            raise ValueError(msg) from e

        classes = []
        functions = []
        variables = []
        items = []

        for node in tree.body:
            if isinstance(node, ClassDef):
                cls = self._extract_class(node)
                classes.append(cls)
                items.append(("class", cls.name))
            elif isinstance(node, FunctionDef):
                func = self._extract_function(node)
                functions.append(func)
                items.append(("function", func.name))
            elif isinstance(node, Assign):
                vars_list = self._extract_variables(node)
                variables.extend(vars_list)
                items.extend(("variable", var) for var in vars_list)

        return Module(
            classes=classes,
            functions=functions,
            variables=variables,
            items=items,
        )

    def _extract_class(self, node: ClassDef) -> ClassDefinition:
        """
        Extract class definition from AST node.

        Args:
            node: AST ClassDef node

        Returns:
            ClassDefinition object with methods and variables
        """
        methods = []
        variables = []
        base_classes = [self._get_node_name(base) for base in node.bases]
        items = []

        for item in node.body:
            if isinstance(item, FunctionDef):
                method = self._extract_function(item)
                methods.append(method)
                items.append(("method", method.name))
            elif isinstance(item, Assign):
                vars_list = self._extract_variables(item)
                variables.extend(vars_list)
                items.extend(("variable", var) for var in vars_list)

        return ClassDefinition(
            name=node.name,
            methods=methods,
            variables=variables,
            base_classes=base_classes,
            items=items,
        )

    def _extract_function(self, node: FunctionDef) -> MethodDefinition:
        """
        Extract function or method definition from AST node.

        Args:
            node: AST FunctionDef or AsyncFunctionDef node

        Returns:
            MethodDef object with signature
        """
        is_property = any(
            isinstance(d, Name) and d.id == "property" for d in node.decorator_list
        )
        is_static = any(
            isinstance(d, Name) and d.id == "staticmethod" for d in node.decorator_list
        )
        is_class_method = any(
            isinstance(d, Name) and d.id == "classmethod" for d in node.decorator_list
        )

        decorators = self._extract_decorators(node.decorator_list)
        signature = self._build_signature(node)

        return MethodDefinition(
            name=node.name,
            signature=signature,
            is_property=is_property,
            is_static=is_static,
            is_class_method=is_class_method,
            decorators=decorators if decorators else None,
        )

    def _build_signature(self, node: FunctionDef) -> str:
        """
        Build function signature string from AST node.

        Args:
            node: AST FunctionDef node

        Returns:
            Function signature string
        """
        args_str = self._format_arguments(node.args)

        return_annotation = ""
        if node.returns:
            return_annotation = f" -> {unparse(node.returns)}"

        return f"def {node.name}({args_str}){return_annotation}: ..."

    def _format_arguments(self, args: arguments) -> str:
        """
        Format function arguments into a signature string.

        Args:
            args: AST arguments node

        Returns:
            Formatted arguments string
        """
        params = [arg.arg for arg in args.posonlyargs]

        if args.posonlyargs:
            params.append("/")

        params.extend(arg.arg for arg in args.args)

        if args.vararg:
            params.append(f"*{args.vararg.arg}")
        elif args.kwonlyargs:
            params.append("*")

        params.extend(arg.arg for arg in args.kwonlyargs)

        if args.kwarg:
            params.append(f"**{args.kwarg.arg}")

        return ", ".join(params)

    def _extract_variables(self, node: Assign) -> list[str]:
        """
        Extract variable names from assignment node.

        Args:
            node: AST Assign node

        Returns:
            List of variable names
        """
        variables = []
        for target in node.targets:
            if isinstance(target, Name):
                variables.append(target.id)
            elif isinstance(target, (Tuple, List)):
                variables.extend(elt.id for elt in target.elts if isinstance(elt, Name))
        return variables

    def _get_node_name(self, node: expr) -> str:
        """
        Get name from an AST node (for base classes).

        Args:
            node: AST node

        Returns:
            Name string
        """

        if isinstance(node, Name):
            return node.id
        if isinstance(node, Attribute):
            return unparse(node)
        return ""

    def _extract_decorators(self, decorator_list: list[expr]) -> list[str]:
        """
        Extract decorator names from decorator list.

        Args:
            decorator_list: List of AST decorator nodes

        Returns:
            List of decorator names as strings
        """
        decorators = []
        for decorator in decorator_list:
            decorator_str = unparse(decorator)
            decorators.append(decorator_str)
        return decorators
