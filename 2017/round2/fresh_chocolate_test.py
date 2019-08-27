#!/usr/bin/env python

import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_solve(self):
        ans = solve([4, 5, 6, 4], 3)
        self.assertEqual(ans, 3)
        ans = solve([4, 5, 6, 4], 2)
        self.assertEqual(ans, 4)
        ans = solve([1, 1, 1], 3)
        self.assertEqual(ans, 1)

        ans = solve([2, 2, 4, 4], 4)
        self.assertEqual(ans, 3)

        ans = solve([100] * 100, 4)
        self.assertEqual(ans, 100)

if __name__ == '__main__':
    unittest.main()
