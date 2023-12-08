import unittest
import solution

class TestGetAreaRectangle(unittest.TestCase):
   
    def test_mapper_on_seed_to_soil(self):
        mapper = solution.get_mapper(50, 98, 2)
        self.assertEqual(mapper(98), 50)
        self.assertEqual(mapper(99), 51)
        self.assertEqual(mapper(97), None)
        self.assertEqual(mapper(11), None)
        self.assertEqual(mapper(100), None)


    # def test_solve(self):
    #     self.assertEqual(solution.solve("test.txt"), 13)
   

    # def test_solve2(self):
    #     self.assertEqual(solution.solve2("test.txt"), 30)

unittest.main()
