import unittest
from ..graphics import *

class TestGraphics(unittest.TestCase):

    def test_plot_2d_function(self):
        plot_2d_function('x'**2)

    def test_plot_3d_function(self):
        plot_3d_function('x'**2 + 'y'**2)

if __name__ == '__main__':
    print("Running graphics tests...")
    print("================================")
    unittest.main()
    