from unittest import TestCase
from middleadd import stringadd

class StringCountTest(TestCase):
    def test_if_ce_is_added_appropriately(self):
        input_string = "hello"
        actual = stringadd(input_string)
        expected = "helloce"
        self.assertEqual(actual, expected)
        