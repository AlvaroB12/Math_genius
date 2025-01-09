def solve_linear_equation(equation, variable):
    """Resuelve una ecuación lineal de la forma ax + b = 0."""
    lhs, rhs = equation.split('=')
    lhs_terms = lhs.replace('-', '+-').split('+')
    rhs_terms = rhs.replace('-', '+-').split('+')
    
    lhs_constant = sum(int(term) for term in lhs_terms if variable not in term)
    rhs_constant = sum(int(term) for term in rhs_terms if variable not in term)
    
    lhs_coefficient = sum(int(term.replace(variable, '')) for term in lhs_terms if variable in term)
    rhs_coefficient = sum(int(term.replace(variable, '')) for term in rhs_terms if variable in term)
    
    coefficient = lhs_coefficient - rhs_coefficient
    constant = rhs_constant - lhs_constant
    
    if coefficient == 0:
        return None if constant != 0 else "Infinite solutions"
    return -constant / coefficient

def solve_quadratic_equation(a, b, c):
    """Resuelve una ecuación cuadrática de la forma ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        return [(-b + discriminant**0.5) / (2*a), (-b - discriminant**0.5) / (2*a)]

def simplify_expression(expr):
    """Simplifica una expresión algebraica."""
    terms = expr.replace('-', '+-').split('+')
    result = sum(int(term) for term in terms)
    return result

def expand_expression(expr):
    """Expande una expresión algebraica."""
    if '*' in expr:
        factors = expr.split('*')
        result = 1
        for factor in factors:
            if '^' in factor:
                base, exponent = factor.split('^')
                result *= int(base) ** int(exponent)
            else:
                result *= int(factor)
        return result
    return expr

def factor_expression(expr):
    """Factoriza una expresión algebraica."""
    # Esta es una implementación muy básica y no general
    if '+' in expr:
        terms = expr.split('+')
        common_factors = set()
        for term in terms:
            factors = set(factorize(int(term)))
            if not common_factors:
                common_factors = factors
            else:
                common_factors &= factors
        return '*'.join(map(str, common_factors))
    return expr

def factorize(n):
    """Devuelve los factores primos de un número."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def matrix_determinant(matrix):
    """Calcula el determinante de una matriz cuadrada."""
    # Implementación para matrices de cualquier tamaño
    if len(matrix) != len(matrix[0]):
        raise ValueError("Solo se soportan matrices cuadradas")
    
    # Caso base para matrices 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursión para matrices de mayor tamaño
    determinant = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c+1:] for row in (matrix[:0] + matrix[1:])]
        determinant += ((-1) ** c) * matrix[0][c] * matrix_determinant(sub_matrix)
    return determinant