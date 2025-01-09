import unittest

class TestSample(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    print("Running sample tests...")
    print("====================================")
    unittest.main()
