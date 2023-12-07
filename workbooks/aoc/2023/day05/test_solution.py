import unittest
import solution

class TestGetAreaRectangle(unittest.TestCase):
   

    def test_solve(self):
        self.assertEqual(solution.solve("test.txt"), 13)
   

    def test_solve2(self):
        self.assertEqual(solution.solve2("test.txt"), 30)

unittest.main()
