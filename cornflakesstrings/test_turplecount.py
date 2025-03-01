from unittest import TestCase
from turplecount import count_element

class StringCountTest(TestCase):
    def test_if_correct_count_is_returned(self):
        word = "semeboder ele"
        letter = "e"
        actual = count_element(word, letter)
        expected = ('e', 5)
        self.assertEqual(actual, expected)