from math import *

# Geometría Plana
def distance(p1, p2):
    """Calcula la distancia entre dos puntos en un plano."""
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def midpoint(p1, p2):
    """Calcula el punto medio entre dos puntos."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def slope(p1, p2):
    """Calcula la pendiente de una línea que pasa por dos puntos."""
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

def circle_equation(center, radius):
    """Devuelve la ecuación de una circunferencia."""
    h, k = center
    return f"(x - {h})^2 + (y - {k})^2 = {radius**2}"

def polygon_diagonals(n):
    """Calcula el número de diagonales de un polígono regular."""
    return n * (n - 3) // 2

def polygon_internal_angle(n):
    """Calcula el ángulo interno de un polígono regular."""
    return (n - 2) * 180 / n

# Geometría Espacial
def distance_3d(p1, p2):
    """Calcula la distancia entre dos puntos en 3D."""
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def tetrahedron_volume(a):
    """Calcula el volumen de un tetraedro regular de arista 'a'."""
    return (a**3) / (6 * sqrt(2))

# Transformaciones
def rotate_point_2d(point, angle):
    """Rota un punto en el plano 2D alrededor del origen."""
    x, y = point
    angle_rad = radians(angle)
    new_x = x * cos(angle_rad) - y * sin(angle_rad)
    new_y = x * sin(angle_rad) + y * cos(angle_rad)
    return new_x, new_y

def translate_point_2d(point, translation):
    """Traslada un punto en 2D."""
    return point[0] + translation[0], point[1] + translation[1]
