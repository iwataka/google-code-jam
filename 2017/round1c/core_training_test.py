import unittest
from main import solve, calc_total_possibility


class TestMain(unittest.TestCase):

    def test_calc_total_possibility(self):
        possib = calc_total_possibility([1.0, 1.0, 1.0], 3)
        self.assertAlmostEqual(possib, 1.0, 7)
        possib = calc_total_possibility([1.0, 0.9, 0.8], 3)
        self.assertAlmostEqual(possib, 0.72, 7)
        possib = calc_total_possibility([0.0, 0.0, 0.0], 3)
        self.assertAlmostEqual(possib, 0.0, 7)
        possib = calc_total_possibility([1.0, 0.0, 0.0], 1)
        self.assertAlmostEqual(possib, 1.0, 7)

    def test_solve(self):
        # tests for sample cases
        possib = solve([0.5, 0.7, 0.8, 0.6], 4, 1.4)
        self.assertAlmostEqual(possib, 1.0, 7)
        possib = solve([0.0, 0.0], 2, 1.0)
        self.assertAlmostEqual(possib, 0.25, 7)
        possib = solve([0.9, 0.8], 1, 0.0)
        self.assertAlmostEqual(possib, 0.98, 7)
        possib = solve([0.4, 0.5], 1, 0.1)
        self.assertAlmostEqual(possib, 0.76, 7)

        # tests for performance
        possib = solve([0.0] * 50, 25, 0.0)
        self.assertAlmostEqual(possib, 0.0, 7)

        possib = solve([0.0, 0.5, 1.0], 2, 0.5)
        self.assertAlmostEqual(possib, 1.0, 7)
        possib = solve([0.0, 0.5, 1.0], 2, 1)
        self.assertAlmostEqual(possib, 1.0, 7)

        possib = solve([0.0, 0.00005, 0.00001], 2, 0)
        self.assertAlmostEqual(possib, 0.0, 7)

        possib = solve([0.1] * 50, 25, 0.9 * 25)
        self.assertAlmostEqual(possib, 1.0, 7)


if __name__ == '__main__':
    unittest.main()
