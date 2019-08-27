#!/usr/bin/env python

import unittest
from main import *


class TestMain(unittest.TestCase):

    def test_solve(self):
        y, z = solve(2, 2, [(2, 1), (2, 2)])
        self.assertEqual(y, 1)
        self.assertEqual(z, 1)
        y, z = solve(2, 2, [(1, 1), (1, 2)])
        self.assertEqual(y, 2)
        self.assertEqual(z, 0)
        y, z = solve(2, 2, [(1, 1), (2, 1)])
        self.assertEqual(y, 2)
        self.assertEqual(z, 0)
        y, z = solve(1000, 4, [(3, 2), (2, 1), (3, 3), (3, 1)])
        self.assertEqual(y, 2)
        self.assertEqual(z, 1)
        y, z = solve(3, 5, [(3, 1), (2, 2), (3, 3), (2, 2), (3, 1)])
        self.assertEqual(y, 2)
        self.assertEqual(z, 1)
        y, z = solve(1000, 1000, [(1, 1)] * 1000)
        self.assertEqual(y, 1000)
        self.assertEqual(z, 0)
        y, z = solve(0, 0, [])
        self.assertEqual(y, 0)
        self.assertEqual(z, 0)
        # y, z = solve(2, 6, [(1, 3), (1, 2), (1, 1), (2, 2), (2, 3), (2, 1)])
        # self.assertEqual(y, 3)
        # self.assertEqual(z, 0)


if __name__ == '__main__':
    unittest.main()
