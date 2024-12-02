from unittest import TestCase
import evencount 

class CheckProduct(TestCase):
   def test_that_function_exist(self):
      input = [2, 4, 5, 7, 8]
      evencount.return_even(input)
  
   def test_if_product_is_correct(self):
      input = [2, 4, 5, 7, 8]
      actual = evencount.return_even(input)
      expected = 3
      self.assertEqual(actual, expected)