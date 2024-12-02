from unittest import TestCase
import numberinstring

class ReturnCheckIfPalindrome(TestCase):
   def test_if_function_exist(self):
      word = "abc124def456"
      numberinstring.get_int_list(word)

   def test_if_function_correct(self):
      word = "abc123def456"
      actual = numberinstring.get_int_list(word)
      expected = [1, 2, 3, 4, 5, 6]
      self.assertEqual(expected, actual)   