from sca_parser.clang_parser import ClangParser
from Reglas.unused_variable_rule import UnusedVariableRule
#from analysis.rules.empty_function import EmptyFunctionRule

class Analyzer:
    def __init__(self):
        self.parser = ClangParser()
        self.rules = [
            UnusedVariableRule(),
        ]

    def analyze(self, file_path):
        ast = self.parser.parse_file(file_path)

        # Imprime los nodos del código de C
        for node in ast:
            print(node)


        issues = []

        for node in ast:
            for rule in self.rules:
                result = rule.check(node)
                if result:
                    issues.append(result)


        

        return issues