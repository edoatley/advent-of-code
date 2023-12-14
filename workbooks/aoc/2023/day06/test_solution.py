import unittest
import solution

class TestDay(unittest.TestCase):
   
    def test_distance(self):
        self.assertEqual(solution.distance(0, 7), 0) 
        self.assertEqual(solution.distance(1, 7), 6) 
        self.assertEqual(solution.distance(2, 7), 10) 
        self.assertEqual(solution.distance(3, 7), 12)   
        self.assertEqual(solution.distance(4, 7), 12) 
        self.assertEqual(solution.distance(5, 7), 10) 
        self.assertEqual(solution.distance(6, 7), 6) 
        self.assertEqual(solution.distance(7, 7), 0) 


    def test_calculate_winning_combinations(self):
        self.assertEqual(solution.calculate_winning_combinations(7, 9), [2, 3, 4, 5]) 


    def test_read_file_data_structure(self):
        self.assertEqual(solution.read_file_data_structure("test.txt"), [(7,9), (15, 40), (30, 200)]) 
        

    def test_solve(self):
        self.assertEqual(solution.solve("test.txt"), 288)


    # def test_solve(self):
    #     self.assertEqual(solution.solve("test.txt"), None)


unittest.main()
