from unittest import TestCase
import oddevencount

class ReturningEvenOddCount(TestCase):
   def test_if_function_even_return_present(self):
      numberList = [2, 5, 3, 8, 10]
      oddevencount.odd_even_count(numberList)

   def test_if_function_can_return_even_odd_count(self):
      numberList = [2, 5, 3, 8, 10]
      actual = oddevencount.odd_even_count(numberList)
      expected = [2, 3]
      self.assertEqual(actual, expected)