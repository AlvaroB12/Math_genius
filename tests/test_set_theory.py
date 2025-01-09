import unittest
from ..set_theory import *

class TestSetTheory(unittest.TestCase):
    
    def test_union(self):
        self.assertEqual(union({1, 2, 3}, {3, 4, 5}), {1, 2, 3, 4, 5})

    def test_intersection(self):
        self.assertEqual(intersection({1, 2, 3}, {3, 4, 5}), {3})

    def test_difference(self):
        self.assertEqual(difference({1, 2, 3}, {3, 4, 5}), {1, 2})

    def test_symmetric_difference(self):
        self.assertEqual(symmetric_difference({1, 2, 3}, {3, 4, 5}), {1, 2, 4, 5})

    def test_is_subset(self):
        self.assertTrue(is_subset({1, 2}, {1, 2, 3}))

    def test_is_superset(self):
        self.assertTrue(is_superset({1, 2, 3}, {1, 2}))

    def test_is_disjoint(self):
        self.assertTrue(is_disjoint({1, 2}, {3, 4}))

    def test_cartesian_product(self):
        self.assertEqual(cartesian_product({1, 2}, {3, 4}), {(1, 3), (1, 4), (2, 3), (2, 4)})

    def test_power_set(self):
        self.assertEqual(power_set({1, 2}), {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})})

    def test_set_partition(self):
        self.assertEqual(set_partition({1, 2}), {frozenset({1, 2}), frozenset({1}, {2})})

    def test_set_cardinality(self):
        self.assertEqual(set_cardinality({1, 2, 3}), 3)

    def test_set_complement(self):
        self.assertEqual(set_complement({1, 2, 3, 4, 5}, {1, 3, 5}), {2, 4})

if __name__ == '__main__':
    print("Running set_theory tests...")
    print("====================================")
    unittest.main()
