import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from sympy import lambdify, symbols
import math

import math
import matplotlib.pyplot as plt

import math
import matplotlib.pyplot as plt

def midpoint(p1, p2):
    """Calcula el punto medio entre dos puntos."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def distance(p1, p2):
    """Calcula la distancia entre dos puntos."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def slope(p1, p2):
    """Calcula la pendiente de la línea que pasa por dos puntos."""
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def line(p1, p2):
    """Calcula la ecuación de la línea que pasa por dos puntos."""
    m = slope(p1, p2)
    b = p1[1] - m * p1[0]
    return (m, b)

def parallel(p1, p2, p3, p4):
    """Determina si dos líneas son paralelas."""
    return slope(p1, p2) == slope(p3, p4)

def perpendicular(p1, p2, p3, p4):
    """Determina si dos líneas son perpendiculares."""
    return slope(p1, p2) * slope(p3, p4) == -1

def plot_points(p1, p2, title):
    """Genera un gráfico de dos puntos."""
    plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='red')
    plt.text(p1[0], p1[1], f'P1{p1}', fontsize=12, ha='right')
    plt.text(p2[0], p2[1], f'P2{p2}', fontsize=12, ha='right')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def plot_line(p1, p2, title):
    """Genera un gráfico de una línea que pasa por dos puntos."""
    m, b = line(p1, p2)
    x = [p1[0], p2[0]]
    y = [m * xi + b for xi in x]
    plt.plot(x, y, label=f'y = {m:.2f}x + {b:.2f}')
    plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='red')
    plt.text(p1[0], p1[1], f'P1{p1}', fontsize=12, ha='right')
    plt.text(p2[0], p2[1], f'P2{p2}', fontsize=12, ha='right')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Funciones específicas para círculos y elipses
def midpoint_circle(p1, p2):
    """Calcula el punto medio entre dos puntos en un círculo."""
    return midpoint(p1, p2)

def distance_circle(p1, p2):
    """Calcula la distancia entre dos puntos en un círculo."""
    return distance(p1, p2)

def slope_circle(p1, p2):
    """Calcula la pendiente de la línea que pasa por dos puntos en un círculo."""
    return slope(p1, p2)

def line_circle(p1, p2):
    """Calcula la ecuación de la línea que pasa por dos puntos en un círculo."""
    return line(p1, p2)

def parallel_circle(p1, p2, p3, p4):
    """Determina si dos líneas en un círculo son paralelas."""
    return parallel(p1, p2, p3, p4)

def perpendicular_circle(p1, p2, p3, p4):
    """Determina si dos líneas en un círculo son perpendiculares."""
    return perpendicular(p1, p2, p3, p4)

def midpoint_ellipse(p1, p2):
    """Calcula el punto medio entre dos puntos en una elipse."""
    return midpoint(p1, p2)

def distance_ellipse(p1, p2):
    """Calcula la distancia entre dos puntos en una elipse."""
    return distance(p1, p2)

def slope_ellipse(p1, p2):
    """Calcula la pendiente de la línea que pasa por dos puntos en una elipse."""
    return slope(p1, p2)

def plot_2d_function(expr, var='x', start=-10, end=10, num_points=1000, color='blue', linestyle='-', label=None):
    x = symbols(var)
    func = lambdify(x, expr, modules=['numpy'])
    x_vals = np.linspace(start, end, num_points)
    y_vals = func(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, color=color, linestyle=linestyle, label=label or f"y = {expr}")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title(f"Gráfico de {expr}")
    plt.xlabel(var)
    plt.ylabel("y")
    plt.grid(alpha=0.4)
    plt.legend()
    plt.show()

def plot_3d_function(expr, vars=('x', 'y'), ranges=(-10, 10, -10, 10), num_points=100):
    x, y = symbols(vars)
    func = lambdify((x, y), expr, modules=['numpy'])

    x_vals = np.linspace(ranges[0], ranges[1], num_points)
    y_vals = np.linspace(ranges[2], ranges[3], num_points)
    x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)
    z_vals = func(x_mesh, y_mesh)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x_mesh, y_mesh, z_vals, cmap='viridis', alpha=0.8)
    ax.set_title(f"Gráfico 3D de {expr}")
    ax.set_xlabel(vars[0])
    ax.set_ylabel(vars[1])
    ax.set_zlabel("z")
    plt.show()

def plot_parametric(x_func, y_func, t_range=(0, 2*np.pi), num_points=1000):
    t_vals = np.linspace(t_range[0], t_range[1], num_points)
    x_vals = x_func(t_vals)
    y_vals = y_func(t_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label="Curva paramétrica")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title("Gráfico Paramétrico")
    plt.xlabel("x(t)")
    plt.ylabel("y(t)")
    plt.grid(alpha=0.4)
    plt.legend()
    plt.show()

def animate_function(expr, var='x', start=-10, end=10, num_points=1000, interval=50):
    x = symbols(var)
    func = lambdify(x, expr, modules=['numpy'])
    x_vals = np.linspace(start, end, num_points)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(start, end)
    ax.set_ylim(-2, 2)
    ax.grid()
    line, = ax.plot([], [], color="blue", lw=2)

    def update(frame):
        y_vals = func(x_vals + frame / 10)
        line.set_data(x_vals, y_vals)
        return line,

    ani = FuncAnimation(fig, update, frames=100, interval=interval, blit=True)
    plt.show()
