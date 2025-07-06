from unittest import TestCase
from stringcalculator import calculate

class TestStringCalculator(TestCase):
    def test_calculate(self):
        user_input = "2 * 2 - 3"
        answer = calculate(user_input)
        expected = "4 - 3"
        self.assertEqual(answer, expected)