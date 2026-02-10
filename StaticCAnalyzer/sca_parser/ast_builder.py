# parser/ast_builder.py

from clang.cindex import CursorKind
from .ast_nodes import FunctionNode, VariableNode


class ASTBuilder:
    def build_node(self, cursor):
        """
        Traduce un cursor de Clang a un nodo propio.
        """
        if cursor.kind == CursorKind.FUNCTION_DECL:
            return self._build_function(cursor)

        if cursor.kind == CursorKind.VAR_DECL:
            return self._build_variable(cursor)

        return None


    def _build_function(self, cursor):
        parameters = [
            arg.spelling for arg in cursor.get_arguments()
        ]

        return FunctionNode(
            name=cursor.spelling,
            return_type=cursor.result_type.spelling,
            parameters=parameters,
            body_nodes=[],
            file=cursor.location.file.name,
            line=cursor.location.line,
            column=cursor.location.column,
        )


    def _build_variable(self, cursor):
        is_initialized = any(
            c.kind.name.endswith("EXPR") for c in cursor.get_children()
        )

        return VariableNode(
            name=cursor.spelling,
            var_type=cursor.type.spelling,
            is_initialized=is_initialized,
            file=cursor.location.file.name,
            line=cursor.location.line,
            column=cursor.location.column,
        )
