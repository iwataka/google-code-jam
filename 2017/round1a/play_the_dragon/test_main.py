import unittest
from main import *

class TestMain(unittest.TestCase):

    # def test_optimize_attacks_and_buffs_with_one_buff(self):
    #     n_turns = optimize_attacks_and_buffs(1, 4, 3)
    #     self.assertEqual(n_turns, 2)

    # def test_optimize_attacks_and_buffs_with_no_buff(self):
    #     n_turns = optimize_attacks_and_buffs(2, 2, 1)
    #     self.assertEqual(n_turns, 1)

    # def test_optimize_attacks_and_buffs_without_buff_ability(self):
    #     n_turns = optimize_attacks_and_buffs(2, 2, 0)
    #     self.assertEqual(n_turns, 1)

    # def test_optimize_attacks_and_buffs_for_specific_testcase1(self):
    #     n_turns = optimize_attacks_and_buffs(7, 19, 1)
    #     self.assertEqual(n_turns, 3)

    # def test_optimize_for_specific_testcase1(self):
    #     n_turns = optimize(65, 41, 27, 3)
    #     self.assertEqual(n_turns, 4)

    def test_solve_for_specific_testcase1(self):
        n_turns = solve(65, 7, 19, 41, 1, 27)
        self.assertEqual(n_turns, 4)

    def test_optimize_attacks_and_buffs_for_specific_testcase2(self):
        n_turns = optimize_attacks_and_buffs(41, 85, 28)
        self.assertEqual(n_turns, 3)

    # def test_optimize_for_specific_testcase2(self):
    #     n_turns = optimize(36, 76, 49, 3)
    #     self.assertEqual(n_turns, 5)

    def test_solve_for_specific_testcase2(self):
        n_turns = solve(36, 41, 85, 76, 28, 49)
        self.assertEqual(n_turns, 5)

    # def test_optimize_attacks_and_buffs_for_sample_testcase1(self):
    #     n_turns = optimize_attacks_and_buffs(5, 16, 0)
    #     self.assertEqual(n_turns, 4)

    def test_solve_for_sample_testcase1(self):
        n_turns = solve(11, 5, 16, 5, 0, 0)
        self.assertEqual(n_turns, 5)

    # # 17 1 77 4 3 1
    # def test_optimize_attacks_and_buffs_for_specific_testcase3(self):
    #     n_turns = optimize_attacks_and_buffs(1, 77, 3)
    #     self.assertEqual(n_turns, 10)

    # def test_optimize_for_specific_testcase3(self):
    #     n_turns = optimize(17, 4, 1, 10)
    #     self.assertEqual(n_turns, 13)

    # def test_optimize_cures_for_specific_testcase3(self):
    #     n_turns = optimize_cures(14, 17, 3, 10)
    #     self.assertEqual(n_turns, 11)

    # def test_solve_for_specific_testcase3(self):
    #     n_turns = solve(17, 1, 77, 4, 3, 1)
    #     self.assertEqual(n_turns, 13)

    # 92 1 19 23 0 0 -> 27
    def test_optimize_attacks_and_buffs_for_specific_testcase4(self):
        n_turns = optimize_attacks_and_buffs(1, 19, 0)
        self.assertEqual(n_turns, 19)

    def test_optimize_cures_for_specific_testcase4(self):
        n_turns = optimize_cures(92, 92, 23, 19)
        self.assertEqual(n_turns, 27)

    # 93 1 95 47 0 1 -> 164
    def test_optimize_attacks_and_buffs_for_specific_testcase5(self):
        n_turns = optimize_attacks_and_buffs(1, 95, 0)
        self.assertEqual(n_turns, 95)

    def test_solve_for_specific_testcase5(self):
        n_turns = solve(93, 1, 95, 47, 0, 1)
        self.assertEqual(n_turns, 164)

    # def test_optimize_cures_for_specific_testcase5(self):
    #     n_turns = optimize_cures(93, 93, 46, 95)
    #     self.assertEqual(n_turns, 164)

if __name__ == '__main__':
    unittest.main()
