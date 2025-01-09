from scipy import *
import numpy as np
from sympy import *
from matplotlib import *
from math import *

def integrate_trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    return np.trapz(y, x)

def solve_system_of_equations(coefficients, constants):
    return np.linalg.solve(coefficients, constants)

def derivative(f, x):
    return diff(f, x)

def integrate(f, x):
    return integrate(f, x)

def solve_differential_equation(f, x):
    return dsolve(f, x)

def solve_integral_equation(f, x):
    return solve(f, x)

def summation(func, start, end):
    return sum(func(i) for i in range(start, end+1))

def productory(func, start, end):
    return prod(func(i) for i in range(start, end+1))

def limit(f, x, a):
    return limit(f, x, a)

def riemann_sum(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    return np.sum(y)*(b-a)/n

def tangent_line(f, x, a):
    return diff(f, x).subs(x, a)

def riemann_sum_3d(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    return np.sum(y)*(b-a)/n

