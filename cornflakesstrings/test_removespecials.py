from unittest import TestCase
from removespecials import remove_special

class StringCountTest(TestCase):
    def test_if_special_characters_is_removed(self):
        user_input = "he.lloe.1/34/DE"
        actual = remove_special(user_input)
        expected = "helloe134DE"
        self.assertEqual(expected, actual)