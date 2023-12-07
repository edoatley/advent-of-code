import unittest
import solution

def load_engine(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

class TestGetAreaRectangle(unittest.TestCase):
    # def test_is_symbol_number(self):
    #     for i in range(10):
    #         self.assertEqual(solution.is_symbol(f"{i}"), False)

    # def test_is_symbol_stop(self):
    #     self.assertEqual(solution.is_symbol(f"."), False)

    # def test_is_symbol(self):
    #     for s in ["*", "#", "+", "*"]:
    #         self.assertEqual(solution.is_symbol(s), True)

    # def test_check_adjacent_simple(self):
    #     engine = load_engine("test.txt")

    #     self.assertEqual(solution.check_adjacent_row(engine, 1, 0, 2), True)
    #     self.assertEqual(solution.check_adjacent_row(engine, 1, 5, 7), False)
    #     self.assertEqual(solution.check_adjacent_row(engine, 1, 2, 3), True)
    #     self.assertEqual(solution.check_adjacent_row(engine, 3, 6, 8), True)

    # def test_check_for_symbol(self):
    #     engine = load_engine("test.txt")

    #     self.assertEqual(solution.check_for_symbol(engine, 0, 0, 2), 467)
    #     self.assertEqual(solution.check_for_symbol(engine, 0, 5, 7), 0)
    #     self.assertEqual(solution.check_for_symbol(engine, 2, 2, 3), 35)
    #     self.assertEqual(solution.check_for_symbol(engine, 2, 6, 8), 633)

    # def test_process_line(self):
    #     engine = load_engine("test.txt")
    #     self.assertEqual(solution.process_line(engine, 0), 467)
    #     self.assertEqual(solution.process_line(engine, 1), 0)
    #     self.assertEqual(solution.process_line(engine, 2), 668)
    #     self.assertEqual(solution.process_line(engine, 3), 0)

    # def test_solve(self):
    #     self.assertEqual(solution.solve("test.txt"), 4361)

    # def test_solve2(self):
    #     print('solution.solve2("test.txt")')
    #     self.assertEqual(solution.solve2("test.txt"), 467835)

    # def test_extract_touching_numbers(self):
    #     engine = load_engine("test.txt")
    #     self.assertEqual(solution.extract_touching_numbers(engine, 5, 9), [598])

  
    # get_gear_parts(): 
    #                            0         1         2         3 G       4         5         6         7         8         9
    #    engine[engine_index+1]='..........................*..........*....662.................88....................$..............=........................439.126...269...'
    #    engine[engine_index]=  '...........=335..............906*634..932........201...157.............423..72..103.798.......732........161...............*................' 
    #    engine[engine_index-1]='......................793........................*...=.....142...........*..*....%...................@......+...............36.......547....' 
    # engine_index=4 
    # gear_index=32 
    def test_get_gear_parts_bug(self):
        engine = load_engine("input.txt")
        self.assertEqual(solution.get_gear_parts(engine, 4, 32), [906, 634])

unittest.main()
