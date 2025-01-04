from math  import *

# Áreas
def parallelogram_area(length, width):
    """Calcula el área de un paralelogramo."""
    return length * width

def triangle_area(base, height):
    """Calcula el área de un triángulo."""
    return (base * height) / 2

def trapezoid_area(base1, base2, height):
    """Calcula el área de un trapecio."""
    return ((base1 + base2) * height) / 2

def circle_area(radius):
    """Calcula el área de un círculo."""
    return pi * radius**2

def regular_polygon_area(n_sides, side_length):
    """Calcula el área de un polígono regular."""
    apothem = side_length / (2 * tan(pi / n_sides))
    perimeter = n_sides * side_length
    return (apothem * perimeter) / 2

# Volúmenes
def cube_volume(side):
    """Calcula el volumen de un cubo."""
    return side ** 3

def cone_volume(radius, height):
    """Calcula el volumen de un cono."""
    return (1 / 3) * pi * radius**2 * height

def cylinder_volume(radius, height):
    """Calcula el volumen de un cilindro."""
    return pi * radius**2 * height

def sphere_volume(radius):
    """Calcula el volumen de una esfera."""
    return (4 / 3) * pi * radius**3

def rectangular_prism_volume(length, width, height):
    return length * width * height

def triangular_prism_volume(base, height, length):
    return (1 / 2) * base * height * length

def regular_polygon_prism_volume(n_sides, side_length, height):
    apothem = side_length / (2 * tan(pi / n_sides))
    perimeter = n_sides * side_length
    base_area = (apothem * perimeter) / 2
    return base_area * height

def triangular_pyramid_volume(base, height, length):
    base_area = (1 / 2) * base * height
    return (1 / 3) * base_area * length

def rectangular_pyramid_volume(length, width, height):
    base_area = length * width
    return (1 / 3) * base_area * height

def regular_polygon_pyramid_volume(n_sides, side_length, height):
    apothem = side_length / (2 * tan(pi / n_sides))
    perimeter = n_sides * side_length
    base_area = (apothem * perimeter) / 2
    return (1 / 3) * base_area * height

def ellipsoid_volume(a, b, c):
    return (4 / 3) * pi * a * b * c

def torus_volume(R, r):
    return 2 * pi**2 * R * r**2

def frustum_volume(R, r, height):
    return (1 / 3) * pi * height * (R**2 + r**2 + R * r)

def cylinder_sector_volume(radius, height, angle):
    return (1 / 2) * pi * radius**2 * height * (angle / 360)

def sphere_sector_volume(radius, angle):
    return (2 / 3) * pi * radius**3 * (angle / 360)

def spherical_cap_volume(radius, height):
    return (1 / 3) * pi * height**2 * (3 * radius - height)

def spherical_wedge_volume(radius, height):
    return (1 / 6) * pi * height**2 * (3 * radius - height)

def spherical_segment_volume(radius, height):
    return (1 / 6) * pi * height * (3 * radius**2 + height**2)

def spherical_sector_volume(radius, angle):
    return (2 / 3) * pi * radius**3 * (angle / 360)

def spherical_cone_volume(radius, height):
    return (1 / 3) * pi * height * radius**2

def ellipsoid_sector_volume(a, b, c, angle):
    return (1 / 6) * pi * a * b * c * (angle / 360)

def ellipsoid_segment_volume(a, b, c, height):
    return (1 / 6) * pi * height * (3 * a * b + height**2)

def ellipsoid_wedge_volume(a, b, c, height):
    return (1 / 6) * pi * height**2 * (3 * a * b + height)

def ellipsoid_cap_volume(a, b, c, height):
    return (1 / 6) * pi * height**2 * (3 * a * b - height)

def ellipsoid_cone_volume(a, b, c, height):
    return (1 / 6) * pi * height * a * b

def torus_sector_volume(R, r, angle):
    return pi**2 * R * r**2 * (angle / 360)

def torus_segment_volume(R, r, height):
    return pi**2 * R * r * height

def torus_wedge_volume(R, r, height):
    return pi**2 * R * r * height

def torus_cap_volume(R, r, height):
    return pi**2 * R * r * height

def torus_cone_volume(R, r, height):
    return (1 / 3) * pi**2 * R * r * height

def frustum_sector_volume(R, r, height, angle):
    return (1 / 6) * pi * height * (R**2 + r**2 + R * r) * (angle / 360)

def frustum_segment_volume(R, r, height):
    return (1 / 6) * pi * height * (R**2 + r**2 + R * r)

def frustum_wedge_volume(R, r, height):
    return (1 / 6) * pi * height * (R**2 + r**2 + R * r)

def frustum_cap_volume(R, r, height):
    return (1 / 6) * pi * height * (R**2 + r**2 + R * r)    

def frustum_cone_volume(R, r, height):
    return (1 / 6) * pi * height * (R**2 + r**2 + R * r)

def cylinder_sector_area(radius, height, angle):
    return 2 * pi * radius * height * (angle / 360)

def sphere_sector_area(radius, angle):
    return 2 * pi * radius**2 * (angle / 360)

def spherical_cap_area(radius, height):
    return 2 * pi * radius * height

def spherical_wedge_area(radius, height):
    return 2 * pi * radius * height

def spherical_segment_area(radius, height):
    return 2 * pi * radius * height

def spherical_sector_area(radius, angle):
    return 2 * pi * radius**2 * (angle / 360)

def spherical_cone_area(radius, height):
    return 2 * pi * radius * height

def ellipsoid_sector_area(a, b, angle):
    return 2 * pi * a * b * (angle / 360)

def ellipsoid_segment_area(a, b):
    return 2 * pi * a * b

def ellipsoid_wedge_area(a, b):
    return 2 * pi * a * b

def ellipsoid_cap_area(a, b):
    return 2 * pi * a * b

def ellipsoid_cone_area(a, b):
    return 2 * pi * a * b

def torus_sector_area(R, r, angle):
    return 2 * pi**2 * R * r * (angle / 360)

def torus_segment_area(R, r):
    return 2 * pi**2 * R * r

def torus_wedge_area(R, r):
    return 2 * pi**2 * R * r

def torus_cap_area(R, r):
    return 2 * pi**2 * R * r

def torus_cone_area(R, r):
    return 2 * pi**2 * R * r

def frustum_sector_area(R, r, angle):
    return 2 * pi * (R + r) * (R - r) * (angle / 360)

def frustum_segment_area(R, r):
    return 2 * pi * (R + r) * (R - r)

def frustum_wedge_area(R, r):
    return 2 * pi * (R + r) * (R - r)

def frustum_cap_area(R, r):
    return 2 * pi * (R + r) * (R - r)

def frustum_cone_area(R, r):
    return 2 * pi * (R + r) * (R - r)

def parallelogram_perimeter(length, width):
    """Calcula el perímetro de un paralelogramo."""
    return 2 * (length + width)

def triangle_perimeter(side1, side2, side3):
    """Calcula el perímetro de un triángulo."""
    return side1 + side2 + side3

def trapezoid_perimeter(base1, base2, side1, side2):
    """Calcula el perímetro de un trapecio."""
    return base1 + base2 + side1 + side2

def circle_circumference(radius):
    """Calcula la circunferencia de un círculo."""
    return 2 * pi * radius

def regular_polygon_perimeter(n_sides, side_length):
    """Calcula el perímetro de un polígono regular."""
    return n_sides * side_length

def cube_surface_area(side):
    """Calcula el área superficial de un cubo."""
    return 6 * side**2

def cone_surface_area(radius, height):
    """Calcula el área superficial de un cono."""
    lateral_area = pi * radius * sqrt(radius**2 + height**2)
    base_area = pi * radius**2
    return lateral_area + base_area

def cylinder_surface_area(radius, height):
    """Calcula el área superficial de un cilindro."""
    lateral_area = 2 * pi * radius * height
    base_area = pi * radius**2
    return 2 * base_area + lateral_area

def sphere_surface_area(radius):
    """Calcula el área superficial de una esfera."""
    return 4 * pi * radius**2

def rectangular_prism_surface_area(length, width, height):
    """Calcula el área superficial de un prisma rectangular."""
    lateral_area = 2 * (length + width) * height
    base_area = length * width
    return 2 * base_area + lateral_area

def triangular_prism_surface_area(base, height, length):
    """Calcula el área superficial de un prisma triangular."""
    lateral_area = 3 * base * height
    base_area = (1 / 2) * base * length
    return base_area + lateral_area

def regular_polygon_prism_surface_area(n_sides, side_length, height):
    """Calcula el área superficial de un prisma de polígono regular."""
    apothem = side_length / (2 * tan(pi / n_sides))
    perimeter = n_sides * side_length
    base_area = (apothem * perimeter) / 2
    lateral_area = perimeter * height
    return 2 * base_area + lateral_area

def triangular_pyramid_surface_area(base, height, length):
    """Calcula el área superficial de una pirámide triangular."""
    base_area = (1 / 2) * base * height
    lateral_area = 3 * base * length
    return base_area + lateral_area

def rectangular_pyramid_surface_area(length, width, height):
    """Calcula el área superficial de una pirámide rectangular."""
    base_area = length * width
    lateral_area = 2 * length * sqrt((width / 2)**2 + height**2)
    return base_area + lateral_area

def regular_polygon_pyramid_surface_area(n_sides, side_length, height):
    """Calcula el área superficial de una pirámide de polígono regular."""
    apothem = side_length / (2 * tan(pi / n_sides))
    perimeter = n_sides * side_length
    base_area = (apothem * perimeter) / 2
    lateral_area = perimeter * height
    return base_area + lateral_area

def ellipsoid_surface_area(a, b, c):
    """Calcula el área superficial de un elipsoide."""
    p = (a + b + c) / 2
    area = 4 * pi * ((a * b * c) / 3)**(1 / 3) * (0.5, 1.5, 2, -p**2 / a**2) + 4 * pi * (a * b * c)**(1 / 3) * (0.5, 1.5, 2, -p**2 / c**2)
    return area

def torus_surface_area(R, r):
    """Calcula el área superficial de un toro."""
    return 4 * pi**2 * R * r

def frustum_surface_area(R, r, height):
    """Calcula el área superficial de un tronco de cono."""
    lateral_area = pi * (R + r) * sqrt((R - r)**2 + height**2)
    base_area = pi * (R**2 + r**2)
    return lateral_area + base_area

def cylinder_sector_surface_area(radius, height, angle):
    """Calcula el área superficial de un sector cilíndrico."""
    lateral_area = pi * radius * height * (angle / 360)
    base_area = pi * radius**2
    return lateral_area + base_area

def sphere_sector_surface_area(radius, angle):
    """Calcula el área superficial de un sector esférico."""
    return 2 * pi * radius**2 * (angle / 360)

def spherical_cap_surface_area(radius, height):
    """Calcula el área superficial de una casquete esférico."""
    base_area = pi * radius**2
    lateral_area = pi * radius * height
    return base_area + lateral_area

def spherical_wedge_surface_area(radius, height):
    """Calcula el área superficial de una cuña esférica."""
    base_area = pi * radius**2
    lateral_area = pi * radius * height
    return base_area + lateral_area

def spherical_segment_surface_area(radius, height):
    """Calcula el área superficial de un segmento esférico."""
    base_area = pi * radius**2
    lateral_area = pi * radius * height
    return base_area + lateral_area

def spherical_sector_surface_area(radius, angle):
    """Calcula el área superficial de un sector esférico."""
    return 2 * pi * radius**2 * (angle / 360)

