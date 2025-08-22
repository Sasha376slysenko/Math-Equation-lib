import unittest
from math_equations import equation_lib

class TestEvalEquation(unittest.TestCase):
    def setUp(self)-> None:
        self.object_config = equation_lib.EquationConfig(500)
        self.eq = equation_lib.EvalEquation(self.object_config)

    def test_eval_fast_one(self)-> None:
        self.assertEqual(self.eq._eval_fast('7+5'), 12)
        self.assertEqual(self.eq._eval_fast('3-3'), 0)
        self.assertEqual(self.eq._eval_fast('2*3'), 6)
        self.assertEqual(self.eq._eval_fast('3/3'), 1)
        self.assertEqual(self.eq._eval_fast('3^3'), 27)

    def test_eval_fast_two(self)-> None:
        self.assertEqual(self.eq._eval_fast('-3+3+7'), 7)
        self.assertEqual(self.eq._eval_fast('-7+8'), 1)
        self.assertEqual(self.eq._eval_fast('-1-7+8'), 0)

    def test_eval_fast_three(self)-> None:
        self.assertEqual(self.eq._eval_fast('1--1'), 2)

    def test_eval_fast_four(self)-> None:
        self.assertEqual(self.eq._eval_fast('(3+4)*1'), 7)
        self.assertEqual(self.eq._eval_fast('(3*4)/2'), 6)
        self.assertEqual(self.eq._eval_fast('(3*4)*2'), 24)

    def test_eval_fast_five(self)-> None:
        self.assertEqual(self.eq._eval_fast('(1+8-9-1+2)+5'), 6)
        self.assertEqual(self.eq._eval_fast('(5*9-6+3)*6'), 252)
        self.assertEqual(self.eq._eval_fast('(-1-7+8)'), 0)
        self.assertEqual(self.eq._eval_fast('(1+2)'), 3)
        self.assertEqual(self.eq._eval_fast('-1+5'), 4)

    def test_eval_fast_six(self) -> None:
        self.assertEqual(self.eq._eval_fast('-1-5'), -6)
        self.assertEqual(self.eq._eval_fast('(-1+2)+5'), 6)
        self.assertEqual(self.eq._eval_fast('(1+2)'), 3)
        self.assertEqual(self.eq._eval_fast('1--1+5'), 7)
        self.assertEqual(self.eq._eval_fast('1-(2-3)+3+5'), 10)
        self.assertEqual(self.eq._eval_fast('1+(3-4)+3'), 3)
        self.assertEqual(self.eq._eval_fast('-3*5'), -15)
        self.assertEqual(self.eq._eval_fast('-7-8'), -15)
        self.assertEqual(self.eq._eval_fast('(5*9-6+3)*6'), 252)
        self.assertEqual(self.eq._eval_fast('6+(1+5)+2+4-9'), 9)
        self.assertEqual(self.eq._eval_fast('8-1^(3/4/2)'), 7)
        self.assertEqual(self.eq._eval_fast('8-1^(3^4^2)'), 7)
        self.assertEqual(self.eq._eval_fast('5+3-(9-8)^6'), 7)
        self.assertEqual(self.eq._eval_fast('5+3-(8-9)^3'), 9)
        self.assertEqual(self.eq._eval_fast('2/3*6'), 4)
        self.assertEqual(self.eq._eval_fast('(9-6)^(9-6)'), 27)
        self.assertEqual(self.eq._eval_fast('(8-9)^(9-6)'), -1)
        self.assertEqual(self.eq._eval_fast('(8-9)^(9-5)'), 1)
        self.assertEqual(self.eq._eval_fast('(9-8)^(6-9)'), 1)
