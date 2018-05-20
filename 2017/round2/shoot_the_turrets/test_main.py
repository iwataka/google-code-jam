#!/usr/bin/env python

import unittest
from main import *


class TestMain(unittest.TestCase):

    field_case6_small = [
        ['S', '.', '.', 'S', '.', 'S', 'S'],
        ['#', '#', '.', '#', '.', '.', '#'],
        ['S', '#', '.', 'T', '#', '.', 'T'],
        ['.', '#', '.', 'T', '#', '.', '.'],
        ['.', '.', 'T', '.', '#', '.', 'T'],
        ['#', '#', '#', '#', 'S', '#', '#'],
        ['.', 'T', 'T', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'S', '.']
    ]

    test_graph = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1]
    ]

    def test_solve(self):
        M = 0
        C = 2
        R = 2
        field = [['T', 'T'], ['T', 'S']]
        ans, _ = solve(C, R, M, field)
        self.assertEqual(ans, 1)

        M = 4
        C = len(self.field_case6_small[0])
        R = len(self.field_case6_small)
        ans, _ = solve(C, R, M, self.field_case6_small)
        self.assertEqual(ans, 7)

    def test_get_shootable_turrets(self):
        x = 1
        y = 1
        M = 0
        C = 2
        R = 2
        field = [['T', 'T'], ['T', 'S']]
        ts = get_shootable_turrets(x, y, M, C, R, field)
        self.assertEqual(len(ts[0]), 2)

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

        x = 0
        y = 6
        M = 4
        C = len(self.field_case6_small[0])
        R = len(self.field_case6_small)
        ts = get_shootable_turrets(x, y, M, C, R, self.field_case6_small)
        self.assertEqual(len(ts[0]), 0)
        self.assertEqual(len(ts[1]), 0)
        self.assertEqual(len(ts[2]), 0)
        self.assertEqual(len(ts[3]), 1)
        self.assertEqual(len(ts[4]), 2)

    def test_find_alternating_path(self):
        count = 0
        graph = []
        connections = []
        path = find_alternating_path(graph, connections)
        self.assertIsNone(path)

        connections = [0, 3, -1, 2, 1]
        path = find_alternating_path(self.test_graph, connections)
        self.assertIsNotNone(path)

    def test_calc_maxbpm(self):
        maxbpm = calc_maxbpm(self.test_graph)
        for row in maxbpm:
            self.assertEqual(sum(row), 1, "Not expected Max BPM: %s" % maxbpm)

    def test_correct(self):
        maxbpm = [[0, 0, 1]]
        shootable_turrets_list = [[set(), set(), {(1, 2)}, {(2, 3)}]]
        turrets = [(1, 2), (3, 2), (2, 3)]
        bpm, corrected = correct(maxbpm, shootable_turrets_list, turrets)
        self.assertTrue(corrected)
        self.assertEqual(bpm, [[1, 0, 0]])

        maxbpm = [[0, 0, 1], [1, 0, 0]]
        shootable_turrets_list = [[set(), set(), {(1, 2)}, {(2, 3)}], [
            {(1, 2)}, set(), set(), set()]]
        turrets = [(1, 2), (3, 2), (2, 3)]
        bpm, corrected = correct(maxbpm, shootable_turrets_list, turrets)
        self.assertFalse(corrected)
        self.assertEqual(bpm, maxbpm)


if __name__ == '__main__':
    unittest.main()
