from unittest import TestCase
import palindrome

class ReturnCheckIfPalindrome(TestCase):
   def test_if_function_exist(self):
      list = ["madam", "apple", "racecar"]
      palindrome.check_if_palindrome(list)

   def test_if_function_correct(self):
      list = ["madam", "apple", "racecar"]
      actual = palindrome.check_if_palindrome(list)
      expected = [True, False, True]
      self.assertEqual(expected, actual)   