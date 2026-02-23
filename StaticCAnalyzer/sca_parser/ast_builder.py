# parser/ast_builder.py

from clang.cindex import CursorKind
from .ast_nodes import FunctionNode, VariableNode


class ASTBuilder:
    """
    Traduce cursores de Clang a nodos de nuestro AST interno.
    Actúa como capa de adaptación entre Clang y el modelo propio.
    """

    def build_node(self, cursor):
        """
        Punto de entrada: decide qué tipo de nodo construir
        según el tipo del cursor.
        """

        if cursor.kind == CursorKind.FUNCTION_DECL:
            return self._build_function(cursor)

        if cursor.kind == CursorKind.VAR_DECL:
            return self._build_variable(cursor)

        # Si el tipo no está soportado, se ignora.
        return None


    def _build_function(self, cursor):
        """
        Construye un nodo de función a partir de FUNCTION_DECL.
        """

        # Extrae los nombres de los parámetros.
        parameters = [arg.spelling for arg in cursor.get_arguments()]

        return FunctionNode(
            name=cursor.spelling,                     # Nombre de la función
            return_type=cursor.result_type.spelling,  # Tipo de retorno
            parameters=parameters,                    # Parámetros
            body_nodes=[],                            # Cuerpo aún no construido
            file=cursor.location.file.name,           # Archivo fuente
            line=cursor.location.line,                # Línea
            column=cursor.location.column,            # Columna
        )


    def _build_variable(self, cursor):
        """
        Construye un nodo de variable a partir de VAR_DECL.
        """

        # Detecta si la variable tiene inicialización
        # comprobando si algún hijo es una expresión.
        is_initialized = any(
            c.kind.name.endswith("EXPR") for c in cursor.get_children()
        )

        return VariableNode(
            name=cursor.spelling,          # Nombre de la variable
            var_type=cursor.type.spelling, # Tipo declarado
            is_initialized=is_initialized, # ¿Tiene inicialización?
            file=cursor.location.file.name,
            line=cursor.location.line,
            column=cursor.location.column,
        )