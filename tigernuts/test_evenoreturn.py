from unittest import TestCase
import evenoreturn

class CheckEvenReturn(TestCase):
   def test_that_function_exist(self):
      list = [1, 3, 4, 6, 9] 
      evenoreturn.even_add(list)
      
   
   def test_if_function_retuens_even_sum(self):
      list = [1, 3, 4, 6, 9]
      expected = 10
      actual =  evenoreturn.even_add(list)
      self.assertEqual(actual, expected)
   
   def test_if_negative_number_in_list_will_work(self):
      list = [1, 3, 4, -6, 9]
      expected = -2
      actual = evenoreturn.even_add(list)
      self.assertEqual(actual, expected)