import unittest
import solution

class TestDay(unittest.TestCase):
   
    def test_parse(self):
        expected_map = {
            'AAA': ('BBB', 'CCC'),
            'BBB': ('DDD', 'EEE'),
            'CCC': ('ZZZ', 'GGG'),
            'DDD': ('DDD', 'DDD'),
            'EEE': ('EEE', 'EEE'),
            'GGG': ('GGG', 'GGG'),
            'ZZZ': ('ZZZ', 'ZZZ')
        }
        actual_directions, actual_map = solution.parse("test.txt")
        self.assertEqual(actual_directions, 'RL')
        self.assertEqual(actual_map, expected_map)


    def test_solve(self):
        self.assertEqual(solution.solve("test.txt"), 2)
        self.assertEqual(solution.solve("test2.txt"), 6)


    # def test_solve(self):
    #     self.assertEqual(solution.solve("test.txt"), None)


unittest.main()
