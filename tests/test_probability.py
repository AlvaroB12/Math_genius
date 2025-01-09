import unittest
from ..probability import *

class TestProbability(unittest.TestCase):

    def test_probability(self):
        event = {1, 2, 3}
        space = {1, 2, 3, 4, 5, 6}
        self.assertEqual(probability(event, space), 0.5)

    def test_conditional_probability(self):
        event = {1, 2, 3}
        condition = {1, 2, 3, 4, 5, 6}
        self.assertEqual(conditional_probability(event, condition), 0.5)

    def test_binomial_distribution(self):
        self.assertAlmostEqual(binomial_distribution(5, 0.5, 2), 0.3125)

    def test_poisson_distribution(self):
        self.assertAlmostEqual(poisson_distribution(2, 3), 0.18044704431548356)

    def test_normal_distribution(self):
        self.assertAlmostEqual(normal_distribution(0, 0, 1), 0.3989422804014327)

    def test_monte_carlo_simulation(self):
        def func():
            return 1
        self.assertEqual(monte_carlo_simulation(func, 10000), 1)

if __name__ == '__main__':
    print("Running probability tests...")
    print("====================================")
    unittest.main()
