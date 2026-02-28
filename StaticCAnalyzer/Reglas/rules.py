class BaseRule:
    def analyze(self, ast_root):
        """
        Ejecuta la regla sobre el AST completo.
        Devuelve una lista de diagnósticos.
        """
        raise NotImplementedError