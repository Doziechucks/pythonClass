from unittest import TestCase
import inputlistsquare

class ReturningSquaresList(TestCase):
   def test_if_function_present(self):
      number = 4
      inputlistsquare.get_squares_list(number)

   def test_if_result_is_correct(self):
      number = 4
      actual = inputlistsquare.get_squares_list(number)
      expected = [1, 4, 9, 16]
      self.assertEqual(expected, actual)