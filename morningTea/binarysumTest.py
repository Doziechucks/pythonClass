from unittest import TestCase
from binarysum import binary_adder

class TestBinarySum(TestCase):
    def test_binary_adder(self):
        binary = binary_adder(111, 101)
        actual = 1100
        self.assertEqual(actual, binary)

    def test_binary_adder2(self):
        binary = binary_adder(111, 101, 10)
        actual = 1110
        self.assertEqual(actual, binary)
