from unittest import TestCase

from baseconverter import *

class TestBaseConverter(TestCase):
    def test_function1(self):
        actual = convert(111, 2, 3)
        expected = 21
        self.assertEqual(actual, expected)

    def test_function2(self):
        actual = convert(110, 2, 6)
        expected = 10
        self.assertEqual(actual, expected)

