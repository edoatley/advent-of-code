import unittest
import solution

class TestDay(unittest.TestCase):
   
    def test_parse(self):
         expected = [
              ('32T3K', 765),
              ('T55J5', 684),
              ('KK677', 28),
              ('KTJJT', 220),
              ('QQQJA', 483),
         ]
         self.assertEqual(solution.parse("test.txt"), expected)

    def test_hand_type(self):
        self.assertEqual(solution.hand_type("23456"), 400)
        self.assertEqual(solution.hand_type("32T3K"), 500)
        self.assertEqual(solution.hand_type("234AA"), 500)
        self.assertEqual(solution.hand_type("KK677"), 600)
        self.assertEqual(solution.hand_type("KTJJT"), 600)
        self.assertEqual(solution.hand_type("T55J5"), 700)
        self.assertEqual(solution.hand_type("QQQJA"), 700)
        self.assertEqual(solution.hand_type("22266"), 800)
        self.assertEqual(solution.hand_type("22226"), 900)
        self.assertEqual(solution.hand_type("22222"), 999)


    def test_solve(self):
       self.assertEqual(solution.solve("test.txt"), 6440)


    def test_ranker(self):
        self.assertEqual(solution.ranker(("32T3K", 0)), '50032T3Y')
        self.assertEqual(solution.ranker(("23456", 0)), '40023456')
        self.assertEqual(solution.ranker(("32T3K", 0)), '50032T3Y')
        self.assertEqual(solution.ranker(("234AA", 0)), '500234ZZ')
        self.assertEqual(solution.ranker(("KK677", 0)), '600YY677')
        self.assertEqual(solution.ranker(("KTJJT", 0)), '600YTWWT')
        self.assertEqual(solution.ranker(("T55J5", 0)), '700T55W5')
        self.assertEqual(solution.ranker(("QQQJA", 0)), '700XXXWZ')
        self.assertEqual(solution.ranker(("22266", 0)), '80022266')
        self.assertEqual(solution.ranker(("22226", 0)), '90022226')
        self.assertEqual(solution.ranker(("22222", 0)), '99922222')

    def test_ranker2(self):
        self.assertEqual(solution.ranker2(("32T3K", 0)), '50032T3Y')
        self.assertEqual(solution.ranker2(("KK677", 0)), '600YY677')
        self.assertEqual(solution.ranker2(("T55J5", 0)), '900T5515')
        self.assertEqual(solution.ranker2(("KTJJT", 0)), '900YT11T')
        self.assertEqual(solution.ranker2(("QQQJA", 0)), '900XXX1Z')
        self.assertEqual(solution.ranker2(("8JJJJ", 0)), '99981111')
        self.assertEqual(solution.ranker2(("JJJJJ", 0)), '99911111')
    
    def test_sort_order(self):
        input = [
            ('32T3K', 765),
            ('T55J5', 684),
            ('KK677', 28),
            ('KTJJT', 220),
            ('QQQJA', 483),
         ]
        expected = [
            ('32T3K', 765),
            ('KTJJT', 220),
            ('KK677', 28),
            ('T55J5', 684),
            ('QQQJA', 483),
        ]
        self.assertEqual(sorted(input, key=solution.ranker), expected)
    

    def test_sort_order2(self):
        input = [
            ('32T3K', 765),
            ('T55J5', 684),
            ('KK677', 28),
            ('KTJJT', 220),
            ('QQQJA', 483),
         ]
        expected = [
            ('32T3K', 765),
            ('KK677', 28),
            ('T55J5', 684),
            ('QQQJA', 483),
            ('KTJJT', 220),
        ]
        self.assertEqual(sorted(input, key=solution.ranker2), expected)
        

    def test_solve2(self):
        self.assertEqual(solution.solve2("test.txt"), 5905)


unittest.main()
