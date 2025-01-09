import unittest
from ..geometry import *

class TestGeometry(unittest.TestCase):

    def test_distance_between_points(self):
        self.assertAlmostEqual(distance_between_points((0, 0), (3, 4)), 5.0)

    def test_midpoint(self):
        self.assertEqual(midpoint((0, 0), (3, 4)), (1.5, 2.0))

    def test_slope(self):
        self.assertEqual(slope((0, 0), (3, 4)), 4/3)

    def test_circle_equation(self):
        self.assertEqual(circle_equation((0, 0), 5), "(x - 0)^2 + (y - 0)^2 = 25")

    def test_polygon_diagonals(self):
        self.assertEqual(polygon_diagonals(5), 5)

    def test_polygon_internal_angle(self):
        self.assertEqual(polygon_internal_angle(5), 108.0)

    def test_distance_3d(self):
        self.assertAlmostEqual(distance_3d((0, 0, 0), (3, 4, 5)), 7.0710678118654755)

    def test_tetrahedron_volume(self):
        self.assertAlmostEqual(tetrahedron_volume(3), 3.0)

    def test_rotate_point_2d(self):
        self.assertAlmostEqual(rotate_point_2d((1, 0), 90), (0.0, 1.0))

    def test_translate_point_2d(self):
        self.assertEqual(translate_point_2d((1, 1), (2, 3)), (3, 4))

if __name__ == '__main__':
    print("Running geometry tests...")
    print("====================================")
    unittest.main()
