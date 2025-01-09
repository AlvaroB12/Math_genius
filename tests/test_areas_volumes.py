import unittest
from ..areas_volumes import *

class TestAreasVolumes(unittest.TestCase):

    def test_area_of_circle(self):
        self.assertAlmostEqual(circle_area(5), 78.54, places=2)

    def test_area_parallelogram(self):
        self.assertEqual(parallelogram_area(5, 10), 50)

    def test_area_of_triangle(self):
        self.assertEqual(triangle_area(5, 10), 25)

    def test_volume_of_cuboid(self):
        self.assertEqual(rectangular_prism_volume(5, 10, 15), 750)

    def test_volume_of_cube(self):
        self.assertEqual(cube_volume(5), 125)

    def test_volume_of_cylinder(self):
        self.assertAlmostEqual(cylinder_volume(5, 10), 785.40, places=2)

    def test_volume_of_cone(self):
        self.assertAlmostEqual(cone_volume(5, 10), 261.80, places=2)

    def test_volume_of_sphere(self):
        self.assertAlmostEqual(sphere_volume(5), 523.60, places=2)

if __name__ == '__main__':
    print("Running areas_volumes tests...")
    print("====================================")
    unittest.main()