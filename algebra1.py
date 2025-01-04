from sympy import symbols, Eq, solve, simplify, expand, factor
import numpy as np

def solve_equation(equation, variable):
    """Resuelve una ecuación algebraica."""
    x = symbols(variable)
    return solve(equation, x)

def simplify_expression(expr):
    """Simplifica una expresión algebraica."""
    return simplify(expr)

def expand_expression(expr):
    """Expande una expresión algebraica."""
    return expand(expr)

def factor_expression(expr):
    """Factoriza una expresión algebraica."""
    return factor(expr)

def matrix_determinant(matrix):
    """Calcula el determinante de una matriz."""
    return np.linalg.det(matrix)

def matrix_rank(matrix):
    """Calcula el rango de una matriz."""
    return np.linalg.matrix_rank(matrix)

def matrix_trace(matrix):
    """Calcula la traza de una matriz."""
    return np.trace(matrix)
