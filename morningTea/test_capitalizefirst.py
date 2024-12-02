from unittest import TestCase
import capitalizefirst

class CheckProduct(TestCase):
   def test_that_function_exist(self):
      input = ["red", "yellow", "blue", "green"]
      capitalizefirst.get_first_capital(input)
  
   def test_if_product_is_correct(self):
      input= ["red", "yellow", "blue", "green"]
      actual = capitalizefirst.get_first_capital(input)
      expected = ["Red", "Yellow", "Blue", "Green"]
      self.assertEqual(actual, expected)