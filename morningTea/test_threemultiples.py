from unittest import TestCase
import threemultiples

class GetIfMultiples(TestCase):
   def test_if_numbers_present(self):
      threemultiples.get_multiples()
   
   def test_if_function_works(self):
      actual = threemultiples.get_multiples()
      expected = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
      self.assertEqual(expected, actual)
