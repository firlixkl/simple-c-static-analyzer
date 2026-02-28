class UnusedVariableRule:
    """
    Detecta variables declaradas pero nunca usadas.
    """

    def analyze(self, ast_root):
        diagnostics = []

        # Recorremos todas las funciones
        for function in ast_root.functions:
            declared_vars = {}
            used_vars = set()

            # 1️⃣ Recoger variables declaradas
            for var in function.variables:
                declared_vars[var.name] = var

            # 2️⃣ Recoger usos de variables
            for usage in function.variable_usages:
                used_vars.add(usage.name)

            # 3️⃣ Detectar no usadas
            for var_name, var_node in declared_vars.items():
                if var_name not in used_vars:
                    diagnostics.append({
                        "rule": "UNUSED_VARIABLE",
                        "message": f"Variable '{var_name}' declarada pero no usada",
                        "line": var_node.line
                    })

        return diagnostics