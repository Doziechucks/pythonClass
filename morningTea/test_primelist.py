from unittest import TestCase
import primelist 

class CheckProduct(TestCase):
   def test_that_function_exist(self):
      input = 5
      primelist.return_prime_list(input)
  
   def test_if_product_is_correct(self):
      input = 10
      actual = primelist.return_prime_list(input)
      expected = [2, 3, 5, 7]
      self.assertEqual(actual, expected)