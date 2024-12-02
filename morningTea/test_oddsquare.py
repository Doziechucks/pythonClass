from unittest import TestCase
import oddsquare

class GetIfMultiples(TestCase):
   def test_if_numbers_present(self):
      input = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
      oddsquare.return_odd_square(input)
   
   def test_if_function_works(self):
      input = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
      actual = oddsquare.return_odd_square(input)
      expected = [9, 49, 1, 81, 25]
      self.assertEqual(expected, actual)