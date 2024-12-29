import math

# Geometría Plana
def distance_between_points(p1, p2):
    """Calcula la distancia entre dos puntos en un plano."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def midpoint(p1, p2):
    """Calcula el punto medio entre dos puntos."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def slope(p1, p2):
    """Calcula la pendiente de una línea que pasa por dos puntos."""
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

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

def polygon_area(n_sides, side_length):
    """Calcula el área de un polígono regular."""
    apothem = side_length / (2 * math.tan(math.pi / n_sides))
    perimeter = n_sides * side_length
    return (apothem * perimeter) / 2

# Geometría Espacial
def distance_3d(p1, p2):
    """Calcula la distancia entre dos puntos en 3D."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def tetrahedron_volume(a):
    """Calcula el volumen de un tetraedro regular de arista 'a'."""
    return (a**3) / (6 * math.sqrt(2))

def prism_volume(base_area, height):
    """Calcula el volumen de un prisma."""
    return base_area * height

def pyramid_volume(base_area, height):
    """Calcula el volumen de una pirámide."""
    return (1 / 3) * base_area * height

# Transformaciones
def rotate_point_2d(point, angle):
    """Rota un punto en el plano 2D alrededor del origen."""
    x, y = point
    angle_rad = math.radians(angle)
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return new_x, new_y

def translate_point_2d(point, translation):
    """Traslada un punto en 2D."""
    return point[0] + translation[0], point[1] + translation[1]
