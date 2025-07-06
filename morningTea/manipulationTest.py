from unittest import TestCase
from manipulation import checker

class ManipulationTest(TestCase):
    def test_manipulation(self):
        user_input = "abcde"
        arrangement = "cdeab"
        result = checker(user_input, arrangement)
        answer = True
        self.assertEqual(result, answer)

    def test_manipulation2(self):
        user_input = "abde"
        arrangement = "deab"
        result = checker(user_input, arrangement)
        answer = True
        self.assertEqual(result, answer)

    def test_manipulation3(self):
        user_input = "cba"
        arrangement = "abc"
        result = checker(user_input, arrangement)
        answer = False
        self.assertEqual(result, answer)

    def test_manipulation4(self):
        user_input = "ab"
        arrangement = "ba"
        result = checker(user_input, arrangement)
        answer = True
        self.assertEqual(result, answer)
