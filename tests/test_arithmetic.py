import unittest
from ..arithmetic import *

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(substract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(root(9, 2), 3)

    def test_logarithm(self):
        self.assertEqual(logarithm(100, 10), 2)

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_lcm(self):
        self.assertEqual(lcm(12, 15), 60)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))  
        
    def test_nth_fibonacci(self):
        self.assertEqual(nth_fibonacci(5), 3)

    def test_divisors(self):
        self.assertEqual(divisors(12), [1, 2, 3, 4, 6, 12])

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(12), [2, 2, 3])

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_modular_inverse(self):
        self.assertEqual(modular_inverse(7, 40), 23)

    def test_chinese_remainder_theorem(self):
        self.assertEqual(chinese_remainder_theorem([2, 3, 2], [3, 5, 7]), 23)   

    def test_prod(self):
        self.assertEqual(prod([1, 2, 3, 4]), 24)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(123))

    def test_is_armstrong(self):
        self.assertTrue(is_armstrong(153))
        self.assertFalse(is_armstrong(123))

    def test_is_perfect(self):
        self.assertTrue(is_perfect(28))
        self.assertFalse(is_perfect(123))

    def test_is_abundant(self):
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(123))

    def test_is_deficient(self):
        self.assertTrue(is_deficient(15))
        self.assertFalse(is_deficient(123))

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(123456789))
        self.assertFalse(is_pandigital(12345678))

    def test_is_harshad(self):
        self.assertTrue(is_harshad(18))
        self.assertFalse(is_harshad(123))

    def test_is_pronic(self):
        self.assertTrue(is_pronic(12))
        self.assertFalse(is_pronic(123))

    def test_is_amicable(self):
        self.assertTrue(is_amicable(220, 284))
        self.assertFalse(is_amicable(123, 456))

if __name__ == '__main__':
    print("Running arithmetic tests...")
    print("====================================")
    unittest.main()
