#!/usr/bin/env python

import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_solve(self):
        # TODO: Edit this test freely
        ans = solve()
        self.assertEqual(ans, 0)

    # TODO: Write your own tests here

if __name__ == '__main__':
    unittest.main()
