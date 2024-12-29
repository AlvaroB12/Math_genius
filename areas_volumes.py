import math

# Áreas
def rectangle_area(length, width):
    """Calcula el área de un rectángulo."""
    return length * width

def triangle_area(base, height):
    """Calcula el área de un triángulo."""
    return (base * height) / 2

def trapezoid_area(base1, base2, height):
    """Calcula el área de un trapecio."""
    return ((base1 + base2) * height) / 2

def circle_area(radius):
    """Calcula el área de un círculo."""
    return math.pi * radius**2

def polygon_area(n_sides, side_length):
    """Calcula el área de un polígono regular."""
    apothem = side_length / (2 * math.tan(math.pi / n_sides))
    perimeter = n_sides * side_length
    return (apothem * perimeter) / 2

# Volúmenes
def cube_volume(side):
    """Calcula el volumen de un cubo."""
    return side ** 3

def cone_volume(radius, height):
    """Calcula el volumen de un cono."""
    return (1 / 3) * math.pi * radius**2 * height

def cylinder_volume(radius, height):
    """Calcula el volumen de un cilindro."""
    return math.pi * radius**2 * height

def sphere_volume(radius):
    """Calcula el volumen de una esfera."""
    return (4 / 3) * math.pi * radius**3
