from unittest import TestCase
from stringrearrange import string_rearrange

class StringCountTest(TestCase):
    def test_if_string_is_counted(self):
        input_one = "xyz"
        input_two = "abc"
        expected = "xbc ayz"
        actual = string_rearrange(input_one, input_two)
        self.assertEqual(expected, actual)
        