#!/usr/bin/env python

import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_solve1(self):
        ans = solve(2, 0)
        self.assertEqual(ans, 1)

    def test_solve2(self):
        ans = solve(4, 5)
        self.assertEqual(ans, 5)

    def test_solve3(self):
        ans = solve(9, 3)
        self.assertEqual(ans, 6)

    def test_solve4(self):
        ans = solve(9, 0)
        self.assertEqual(ans, 3)

    def test_solve5(self):
        ans = solve(0, 0)
        self.assertEqual(ans, 0)

    def test_solve6(self):
        ans = solve(3, 9)
        self.assertEqual(ans, 6)

if __name__ == '__main__':
    unittest.main()
