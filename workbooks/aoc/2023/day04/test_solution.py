import unittest
import solution

def load_engine(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

class TestGetAreaRectangle(unittest.TestCase):
   

    def test_solve(self):
        self.assertEqual(solution.solve("test.txt"), 13)
   

    def test_solve2(self):
        self.assertEqual(solution.solve2("test.txt"), 30)

unittest.main()
