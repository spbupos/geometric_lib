import os
import sys
import unittest

sys.path.extend([os.path.abspath('tests'), os.path.abspath('bin')])
import test_circle
import test_rectangle
import test_triangle
import test_square

if __name__ == '__main__':
    circle_suite = unittest.TestLoader().loadTestsFromModule(test_circle)
    rectangle_suite = unittest.TestLoader().loadTestsFromModule(test_rectangle)
    triangle_suite = unittest.TestLoader().loadTestsFromModule(test_triangle)
    square_suite = unittest.TestLoader().loadTestsFromModule(test_square)

    successful = 1
    successful &= unittest.TextTestRunner(verbosity=3).run(circle_suite).wasSuccessful()
    successful &= unittest.TextTestRunner(verbosity=3).run(rectangle_suite).wasSuccessful()
    successful &= unittest.TextTestRunner(verbosity=3).run(triangle_suite).wasSuccessful()
    successful &= unittest.TextTestRunner(verbosity=3).run(square_suite).wasSuccessful()
    sys.exit(not successful)
