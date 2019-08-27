#!/usr/bin/env python

import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_solve1(self):
        ans = solve(3, [[1,2,3], [1,2,3], [1,2,3]])
        self.assertEqual(ans, 6)

    def test_solve2(self):
        ans = solve(3, [[1,1,3], [1,1,-3], [-1,2,-2]])
        self.assertEqual(ans, 2)

if __name__ == '__main__':
    unittest.main()
