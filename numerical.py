import numpy as np

def integrate_trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    return np.trapz(y, x)

def solve_system_of_equations(coefficients, constants):
    return np.linalg.solve(coefficients, constants)
