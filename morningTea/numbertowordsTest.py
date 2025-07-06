from unittest import TestCase

import numbertowords
from numbertowords import convert_single_digit, length_check, convert_multiple_digits, convert_multiples



class TestNumberToWords(TestCase):
    def test_can_read_zero_to_one(self):
        expected = "zero"
        actual = convert_single_digit("0")
        self.assertEqual(expected, actual)

    def test_return_actual_number(self):
        expected = "100", 3
        actual = length_check("000100")
        self.assertEqual(expected, actual)

    def test_return_double_digit(self):
        expected = "ten"
        actual = convert_multiple_digits("00010")
        self.assertEqual(expected, actual)

    def test_return_multiple_digits(self):
        expected = "twenty"
        actual = convert_multiple_digits("20")
        self.assertEqual(expected, actual)

    def test_return_single_digit(self):
        expected = "seven"
        actual = convert_multiple_digits("007")
        self.assertEqual(expected, actual)

    def test_return_multiple_words(self):
        expected = "fifty"
        actual = convert_multiple_digits("50")
        self.assertEqual(expected, actual)

    def test_return_in_word(self):
        expected = "sixty five"
        actual = convert_multiples("65")
        self.assertEqual(expected, actual)

    def test_change_to_words(self):
        expected = "seventy three"
        actual = convert_multiples("73")
        self.assertEqual(expected, actual)

    def test_change_three_digits(self):
        expected = "seven hundred"
        actual = convert_multiples("700")
        self.assertEqual(expected, actual)

    def test_change_three_digits_two(self):
        expected = "nine hundred and forty"
        actual = convert_multiples("940")
        self.assertEqual(expected, actual)

    def test_change_three_digits_three(self):
        expected = "eight hundred and ninety"
        actual = convert_multiples("890")
        self.assertEqual(expected, actual)

    def test_change_three_digits_four(self):
        expected = "eight hundred and thirty three"
        actual = convert_multiples("833")
        self.assertEqual(expected, actual)

    def test_change_three_digits_five(self):
        expected = "one hundred and three"
        actual = convert_multiples("103")
        self.assertEqual(expected, actual)

    def test_change_three_digits_six(self):
        expected = "one hundred and thirty six"
        actual = convert_multiples("136")
        self.assertEqual(expected, actual)










