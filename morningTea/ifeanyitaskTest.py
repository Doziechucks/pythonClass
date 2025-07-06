from unittest import TestCase
from ifeanyitask import validator_function

class TestInfeasibility(TestCase):
    def test_function(self):
        answer = validator_function("[()]")
        expected = True
        self.assertEqual(answer, expected)

    def test_function2(self):
        answer = validator_function("{")
        expected = False
        self.assertEqual(answer, expected)


