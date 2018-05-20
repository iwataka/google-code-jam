#!/usr/bin/env python

import unittest
from main import *


class TestMain(unittest.TestCase):

    def test_solve(self):
        M = 0
        C = 2
        R = 2
        field = [['T', 'T'], ['T', 'S']]
        ans, _ = solve(C, R, M, field)
        self.assertEqual(ans, 1)

    def test_get_shootable_turrets1(self):
        x = 1
        y = 1
        M = 0
        C = 2
        R = 2
        field = [['T', 'T'], ['T', 'S']]
        ts = get_shootable_turrets(x, y, M, C, R, field)
        self.assertEqual(len(ts[0]), 2)

    def test_get_shootable_turrets2(self):
        x = 1
        y = 2
        M = 2
        C = 3
        R = 3
        field = [['T', 'T', 'T'], ['T', '#', 'S'], ['T', 'T', 'T']]
        ts = get_shootable_turrets(x, y, M, C, R, field)
        self.assertEqual(len(ts[0]), 2)
        self.assertEqual(len(ts[1]), 4)
        self.assertEqual(len(ts[2]), 0)

    def test_get_shootable_turrets3(self):
        x = 0
        y = 6
        M = 4
        field = [['S', '.', '.', 'S', '.', 'S', 'S'], ['#', '#', '.', '#', '.', '.', '#'], ['S', '#', '.', 'T', '#', '.', 'T'], ['.', '#', '.', 'T', '#', '.', '.'], [
            '.', '.', 'T', '.', '#', '.', 'T'], ['#', '#', '#', '#', 'S', '#', '#'], ['.', 'T', 'T', '#', '.', '.', '.'], ['.', '.', '.', '.', '.', 'S', '.']]
        C = len(field[0])
        R = len(field)
        ts = get_shootable_turrets(x, y, M, C, R, field)
        self.assertEqual(len(ts[0]), 0)

    def test_find_alternating_path(self):
        count = 0
        for _ in find_alternating_path([], [[1, -1], [-1, -1]]):
            count += 1
        self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()
