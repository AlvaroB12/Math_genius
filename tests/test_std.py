import unittest
from ..std import *

class TestStatistics(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4, 5]), 1.414, places=3)

    def test_correlation_coefficient(self):
        self.assertAlmostEqual(correlation_coefficient([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 1.0)

    def test_variance(self):
        self.assertAlmostEqual(variance([1, 2, 3, 4, 5]), 2.5)

if __name__ == '__main__':
    print("Running statistics tests...")
    print("====================================")
    unittest.main()
