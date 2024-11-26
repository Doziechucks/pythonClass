from unittest import TestCase
import palindrome

class CheckingPalindrome(TestCase):
   def test_if_function_exist(self):
      input = "madam"
      palindrome.check_palindrome(input)

   def test_if_largest_is_returned(self):
      input = "madam"
      actual = palindrome.check_palindrome(input)
      expected = "palindrome"
      self.assertEquals(actual, expected)