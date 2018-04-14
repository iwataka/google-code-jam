import unittest
import math
from main import *

def get_area_for_single_rotation(ps):
    p1 = ps[0]
    p2 = ps[1]
    p3 = ps[2]
    return (abs(p1[0]) + abs(p2[0])) * 2 * 1

def get_area_for_double_rotation(ps):
    p1 = ps[0]
    p2 = ps[1]
    p3 = ps[2]
    return (abs(p1[2]) * 2 - abs(p3[2])) * 2 * math.sqrt(2) + abs(p3[2]) * 2 * math.sqrt(2) / 2 

class TestMain(unittest.TestCase):

    def test_solve(self):
        desired_area = 1.414213
        ps = solve(desired_area)
        area = get_area_for_single_rotation(ps)
        self.assertAlmostEqual(area, desired_area - math.pow(10, -6), 5)

        desired_area = 1.2
        ps = solve(desired_area)
        area = get_area_for_single_rotation(ps)
        self.assertAlmostEqual(area, desired_area - math.pow(10, -6), 5)

        desired_area = 1.0
        ps = solve(desired_area)
        area = get_area_for_single_rotation(ps)
        self.assertAlmostEqual(area, desired_area - math.pow(10, -6), 5)

        desired_area = 1.732050
        ps = solve(desired_area)
        area = get_area_for_double_rotation(ps)
        self.assertAlmostEqual(area, desired_area - math.pow(10, -6), 5)

if __name__ == '__main__':
    unittest.main()
