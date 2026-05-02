"""Servicios del motor de análisis.

Proporciona `analyze_java_code` que parsea Java con javalang,
cuenta LOC, calcula una métrica básica de complejidad y detecta
code smells sencillos como métodos muy largos.
"""
from __future__ import annotations

import re
from typing import Any, Dict, List

import javalang


def analyze_java_code(code_string: str) -> Dict[str, Any]:
    """Analiza código Java y devuelve métricas básicas.

    Retorna un dict con las claves: `loc`, `complexity`, `code_smells`.
    - `loc`: líneas de código no vacías.
    - `complexity`: conteo simple de estructuras de control (if/for/while/switch/catch).
    - `code_smells`: lista de descripciones (p. ej. métodos > 50 líneas).
    """
    # Contar LOC (líneas no vacías)
    loc = sum(1 for line in code_string.splitlines() if line.strip())

    complexity = 0
    code_smells: List[str] = []
    method_count = 0

    # Intentamos parsear con javalang y contar nodos AST relevantes
    try:
        cu = javalang.parse.parse(code_string)

        # contar estructuras de control
        for _, node in cu.filter(javalang.tree.IfStatement):
            complexity += 1
        for _, node in cu.filter(javalang.tree.ForStatement):
            complexity += 1
        for _, node in cu.filter(javalang.tree.WhileStatement):
            complexity += 1
        for _, node in cu.filter(javalang.tree.SwitchStatement):
            complexity += 1
        for _, node in cu.filter(javalang.tree.CatchClause):
            complexity += 1
        # contar declaraciones de método y detectar parámetros largos
        for _, node in cu.filter(javalang.tree.MethodDeclaration):
            method_count += 1
            params = getattr(node, "parameters", []) or []
            if len(params) > 5:
                name = getattr(node, "name", "<anonymous>")
                code_smells.append(f"Long Parameter List en método: {name}")
    except javalang.parser.JavaSyntaxError:
        # Si falla el parse, usar conteo simple por palabras clave como fallback
        lowered = code_string
        complexity = (
            lowered.count(" if ")
            + lowered.count(" for ")
            + lowered.count(" while ")
            + lowered.count(" switch ")
            + lowered.count(" catch ")
        )
        method_count = 0

    # Detectar métodos largos (>50 LOC) mediante regex y balanceo de llaves
    method_pattern = re.compile(
        r'(?:(?:public|protected|private|static|final|synchronized|abstract|native|strictfp)\s+)*'
        r'(?:[\w\<\>\[\]]+\s+)?'  # tipo de retorno opcional (constructor permitido)
        r'(?P<name>[A-Za-z_][\w]*)\s*\([^)]*\)\s*\{',
        re.MULTILINE,
    )

    for m in method_pattern.finditer(code_string):
        name = m.group("name")
        # empezar justo después de la llave de apertura
        idx = m.end()
        brace_count = 1
        i = idx
        length = len(code_string)
        while i < length and brace_count > 0:
            ch = code_string[i]
            if ch == "{":
                brace_count += 1
            elif ch == "}":
                brace_count -= 1
            i += 1

        method_body = code_string[m.start():i]
        method_loc = sum(1 for line in method_body.splitlines() if line.strip())
        if method_loc > 50:
            code_smells.append(f"Long method: {name} ({method_loc} LOC)")

    return {
        "loc": loc,
        "complexity": complexity,
        "method_count": method_count,
        "code_smells": code_smells,
    }
