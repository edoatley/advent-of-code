import unittest
import solution

class TestDay05(unittest.TestCase):
   
    # def test_process_map_line(self):
    #     self.assertEqual(solution.process_map_line('50 98 2'), (98 ,100, -48))
    #     self.assertEqual(solution.process_map_line('52 50 48'), (50 ,98, 2))


    # def test_map_seed_simple(self):
    #     mappings = [[(98 ,100, -48), (50 ,98, 2)]]
    #     self.assertEqual(solution.map_seed(98, mappings), 50)
    #     self.assertEqual(solution.map_seed(99, mappings), 51)
    #     self.assertEqual(solution.map_seed(97, mappings), 99)
    #     self.assertEqual(solution.map_seed(11, mappings), 11)
    #     self.assertEqual(solution.map_seed(100, mappings), 100)


    # def test_solve(self):
        # self.assertEqual(solution.solve("test.txt"), 35)


    def test_solve2(self):
        self.assertEqual(solution.solve2("test.txt"), 46)


unittest.main()
