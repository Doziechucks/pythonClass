from unittest import TestCase
import complex

class CheckingComplex(TestCase):
   def test_if_function_is_present(self):
      list = [1, 2, 3, 4, 5]
      complex.add_complex(list)

   def test_if_fuction_works_properly(self):
      list = [1, 2, 3, 4, 5, 6]
      expected = 105
      actual = complex.add_complex(list)
      self.assertEquals(actual, expected)
