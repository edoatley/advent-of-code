import unittest
import solution

class TestDay(unittest.TestCase):
   
    # def test_parse(self):
    #      expected = [
    #           ('32T3K', 765),
    #           ('T55J5', 684),
    #           ('KK677', 28),
    #           ('KTJJT', 220),
    #           ('QQQJA', 483),
    #      ]
    #      self.assertEqual(solution.parse("test.txt"), expected)

    # def test_hand_type(self):
    #     self.assertEqual(solution.hand_type("23456"), 400)
    #     self.assertEqual(solution.hand_type("32T3K"), 500)
    #     self.assertEqual(solution.hand_type("234AA"), 500)
    #     self.assertEqual(solution.hand_type("KK677"), 600)
    #     self.assertEqual(solution.hand_type("KTJJT"), 600)
    #     self.assertEqual(solution.hand_type("T55J5"), 700)
    #     self.assertEqual(solution.hand_type("QQQJA"), 700)
    #     self.assertEqual(solution.hand_type("22266"), 800)
    #     self.assertEqual(solution.hand_type("22226"), 900)
    #     self.assertEqual(solution.hand_type("22222"), 999)


    def test_solve(self):
       self.assertEqual(solution.solve("test.txt"), 6440)


    # def test_ranker(self):
    #     self.assertEqual(solution.ranker(("32T3K", 0)), '50032T3K')
    #     self.assertEqual(solution.ranker(("23456", 0)), '40023456')
    #     self.assertEqual(solution.ranker(("32T3K", 0)), '50032T3K')
    #     self.assertEqual(solution.ranker(("234AA", 0)), '500234AA')
    #     self.assertEqual(solution.ranker(("KK677", 0)), '600KK677')
    #     self.assertEqual(solution.ranker(("KTJJT", 0)), '600KTJJT')
    #     self.assertEqual(solution.ranker(("T55J5", 0)), '700T55J5')
    #     self.assertEqual(solution.ranker(("QQQJA", 0)), '700QQQJA')
    #     self.assertEqual(solution.ranker(("22266", 0)), '80022266')
    #     self.assertEqual(solution.ranker(("22226", 0)), '90022226')
    #     self.assertEqual(solution.ranker(("22222", 0)), '99922222')

    
    # def test_sort_order(self):
    #     input = [
    #         ('32T3K', 765),
    #         ('T55J5', 684),
    #         ('KK677', 28),
    #         ('KTJJT', 220),
    #         ('QQQJA', 483),
    #      ]
    #     expected = [
    #         ('32T3K', 765),
    #         ('KTJJT', 220),
    #         ('KK677', 28),
    #         ('T55J5', 684),
    #         ('QQQJA', 483),
    #     ]
    #     self.assertEqual(sorted(input, key=solution.ranker, reverse=True), expected)
        


    # def test_solve(self):
    #     self.assertEqual(solution.solve("test.txt"), None)


unittest.main()
