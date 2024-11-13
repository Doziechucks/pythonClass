from unittest import TestCase
import productfinder 

class CheckProduct(TestCase):
   def test_that_function_exist(self):
      productfinder.find_product(3, 4)
  
   def test_if_product_is_correct(self):
      actual = productfinder.find_product(3, 5)
      expected = 15
      self.assertEqual(actual, expected)
  
   def test_second_number_is_zero(self):
      actual = productfinder.find_product(3, 0)
      expected = 0
      self.assertEqual(actual, expected)

   def test_if_user_inputs_first_number_as_negative_number(self):
      actual = productfinder.find_product(-3, 2)
      expected = -6
      self.assertEqual(actual, expected)

   def test_if_user_inputs_negative_second_number(self):
      actual = productfinder.find_product(-3, -3)
      expected = 9
      self.assertEqual(actual, expected)

