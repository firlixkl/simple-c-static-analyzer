from sca_parser.clang_parser import ClangParser
#from analysis.rules.empty_function import EmptyFunctionRule

class Analyzer:
    def __init__(self):
        self.parser = ClangParser()
        self.rules = [
            #EmptyFunctionRule(),
        ]

    def analyze(self, file_path):
        ast = self.parser.parse_file(file_path)

        # Imprime los nodos del código de C
        for node in ast:
            print(node)


        issues = []

        # Da error   File "C:\Users\Felipe\Documents\GitHub\simple-c-static-analyzer\StaticCAnalyzer\Analyzer\analyzer.py", line 21, in analyze for function in ast.functions: AttributeError: 'list' object has no attribute 'functions'
        '''for function in ast.functions:
            for rule in self.rules:
                result = rule.check(function)
                if result:
                    issues.append(result)'''

        

        return issues