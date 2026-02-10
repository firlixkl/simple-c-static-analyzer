# parser/ast_nodes.py

from dataclasses import dataclass
from typing import List


@dataclass
class ASTNode:
    file: str
    line: int
    column: int


@dataclass
class FunctionNode(ASTNode):
    name: str
    return_type: str
    parameters: List[str]
    body_nodes: List[ASTNode]


@dataclass
class VariableNode(ASTNode):
    name: str
    var_type: str
    is_initialized: bool
