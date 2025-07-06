from timeprint import accumulator, number_to_words, zero_remover
from unittest import TestCase

class TestTimePrint(TestCase):
    def test_zero_remover(self):
        actual = zero_remover("04")
        expected = "4"
        self.assertEqual(actual, expected)

    def test_number_to_words(self):
        actual = number_to_words("22")
        expected = 'twenty two'
        self.assertEqual(actual, expected)

    def test_number_to_words_2(self):
        number = zero_remover("01")
        actual = number_to_words(number)
        expected = 'one'
        self.assertEqual(actual, expected)


    def test_time_print(self):
        expected = "fifteen minutes to twelve AM"
        actual = accumulator("23:45")
        self.assertEqual(expected, actual)

    def test_time_print_2(self):
        actual = accumulator("11:45")
        expected = "fifteen minutes to twelve PM"
        self.assertEqual(actual, expected)

    def test_time_print_3(self):
        actual = accumulator("04:22")
        expected = "twenty two minutes past four AM"
        self.assertEqual(actual, expected)

    def test_time_print_4(self):
        actual = accumulator("01:00")
        expected = "one AM"
        self.assertEqual(actual, expected)

    def test_time_print_5(self):
        actual = accumulator("01:01")
        expected = "one minute past one AM"
        self.assertEqual(actual, expected)