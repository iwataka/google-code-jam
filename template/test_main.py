#!/usr/bin/env python

import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_solve(self):
        ans = solve(0, 0)
        self.assertEqual(ans, 0)

if __name__ == '__main__':
    unittest.main()
