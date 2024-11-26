from unittest import TestCase
import secondlistnumber

class RemovingSecondElement(TestCase):
   def test_if_function_second_remove_present(self):
      numberList = [1, 2, 3, 4]
      secondlistnumber.second_remove(numberList)

   def test_if_function_can_return_second_value_in_a_list(self):
      numberList = [1, 2, 3, 4]
      actual = secondlistnumber.second_remove(numberList)
      expected = [1, 3, 4]
      self.assertEquals(actual, expected)
   
   def test_if_input_list_is_a_string(self):
      numberList = ["a", "b", "c", "d"]
      actual = secondlistnumber.second_remove(numberList)
      expected = ["a", "c", "d"]
      self.assertEquals(actual, expected)   