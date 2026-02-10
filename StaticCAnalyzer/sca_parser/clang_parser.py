# parser/clang_parser.py

from clang.cindex import Index
from .ast_builder import ASTBuilder


class ClangParser:
    def __init__(self):
        self.index = Index.create()
        self.builder = ASTBuilder()


    def parse_file(self, file_path: str):
        """
        Parsea un archivo C y devuelve un AST propio.
        """
        translation_unit = self.index.parse(file_path)

        ast_nodes = []

        root_cursor = translation_unit.cursor

        for cursor in root_cursor.get_children():
            node = self.builder.build_node(cursor)
            if node:
                ast_nodes.append(node)

        return ast_nodes
