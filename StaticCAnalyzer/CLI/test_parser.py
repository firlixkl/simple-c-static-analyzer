# test_parser.py


from Analyzer.analyzer import Analyzer


analyzer = Analyzer()
issues = analyzer.analyze("CLI/test.c")


for issue in issues:
    print(issue)
