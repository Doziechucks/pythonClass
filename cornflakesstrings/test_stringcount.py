from unittest import TestCase
from stringcount import string_count

class StringCountTest(TestCase):
    def test_if_string_is_counted(self):
        input_string = "semicolon.africa"
        actual = string_count(input_string)
        expected = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEqual(expected, actual)