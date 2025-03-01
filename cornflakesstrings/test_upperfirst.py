from unittest import TestCase
from upperfirst import upper_first

class StringCountTest(TestCase):
    def test_if_upper_comes_first(self):
        input_string = "SemiCOLon"
        actual = upper_first(input_string)
        expected = "SCOLemion"
    