import unittest
from ..calculus import *

class TestCalculus(unittest.TestCase):

    def test_derivative(self):
        self.assertEqual(derivative("3x^2 + 2x + 1"), "6x + 2")

    def test_integrate(self):
        self.assertEqual(integrate("6x + 2"), "3x^2 + 2x + C")

    def test_limit(self):
        self.assertEqual(limit("1/x", "inf"), 0)

    def test_riemann_sum(self):
        self.assertAlmostEqual(riemann_sum("x^2", 0, 1, 4), 0.46875)

    def test_tangent_line(self):
        self.assertEqual(tangent_line("x^2", 2), "4x - 4")

    def test_riemann_sum_3d(self):
        self.assertAlmostEqual(riemann_sum_3d("x^2", 0, 1, 4), 0.46875)

if __name__ == '__main__':
    print("Running calculus tests...")
    print("====================================")
    unittest.main()