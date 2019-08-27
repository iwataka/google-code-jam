#!/usr/bin/env python

import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_solve(self):
        ans = solve(1000000000, [[1, 1]]*100)
        self.assertAlmostEqual(ans, 4 * 100 + math.sqrt(1**2 + 1**2) * 2 * 100, 7)
        ans = solve(670, [[1, 1]]*100)
        self.assertAlmostEqual(ans, 670, 7)

if __name__ == '__main__':
    unittest.main()
