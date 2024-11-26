from unittest import TestCase
import sumnumberlist

class SumInputedNumbers(TestCase):
   def test_if_function_exists(self):
      sumnumberlist.number_adder(input)

   def test_if_functions_sum_numbers(self):
      actual = sumnumberlist.number_adder(input)
      expected = 28 
      self.assertEquals(actual, expected)
   
   def test_if_list_contain_negative_integer(self):
      actual = sumnumberlist.number_adder(input)
      expected = 18
      self.assertEquals(actual, expected)
   
   def test_if_list_contains_string(self):
      self.assertRaises (TypeError, sumnumberlist.number_adder(input), "man")
    