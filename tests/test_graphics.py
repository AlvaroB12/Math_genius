import unittest
from ..graphics import *

class TestGraphics(unittest.TestCase):

    def test_distance(self):
        self.assertAlmostEqual(distance((0, 0), (3, 4)), 5.0)

    def test_midpoint(self):
        self.assertEqual(midpoint((0, 0), (3, 4)), (1.5, 2.0))

    def test_slope(self):
        self.assertEqual(slope((0, 0), (3, 4)), 4/3)

    def test_line(self):
        self.assertEqual(line((0, 0), (3, 4)), (4/3, 0))

    def test_parallel(self):
        self.assertTrue(parallel((0, 0), (3, 4), (1, 1), (4, 5)))

    def test_perpendicular(self):
        self.assertTrue(perpendicular((0, 0), (3, 4), (4, 5), (-4, 3)))

    def test_midpoint_circle(self):
        self.assertEqual(midpoint_circle((0, 0), (3, 4)), (1.5, 2.0))

    def test_distance_circle(self):
        self.assertAlmostEqual(distance_circle((0, 0), (3, 4)), 5.0)

    def test_slope_circle(self):
        self.assertEqual(slope_circle((0, 0), (3, 4)), 4/3)

    def test_line_circle(self):
        self.assertEqual(line_circle((0, 0), (3, 4)), (4/3, 0))

    def test_parallel_circle(self):
        self.assertTrue(parallel_circle((0, 0), (3, 4), (1, 1), (4, 5)))

    def test_perpendicular_circle(self):
        self.assertTrue(perpendicular_circle((0, 0), (3, 4), (4, 5), (-4, 3)))

    def test_midpoint_ellipse(self):
        self.assertEqual(midpoint_ellipse((0, 0), (3, 4)), (1.5, 2.0))

    def test_distance_ellipse(self):
        self.assertAlmostEqual(distance_ellipse((0, 0), (3, 4)), 5.0)

    def test_slope_ellipse(self):
        self.assertEqual(slope_ellipse((0, 0), (3, 4)), 4/3)

    def test_plot_2d_function(self):
        plot_2d_function(x**2)

    def test_plot_3d_function(self):
        plot_3d_function(x**2 + y**2)

if __name__ == '__main__':
    print("Running graphics tests...")
    print("================================")
    unittest.main()
    