# test_parser.py

from sca_parser.clang_parser import ClangParser

parser = ClangParser()
ast = parser.parse_file("CLI/test.c")

for node in ast:
    print(node)
