import unittest
import solution

class TestGetAreaRectangle(unittest.TestCase):

    def test_solve_simple(self):
        self.assertEqual(solution.solve('small.txt'), 29)

    def test_solve(self):
        self.assertEqual(solution.solve('test.txt'), 281)

unittest.main()