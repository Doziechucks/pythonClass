from unittest import TestCase
import dictionaryadd

class ReturnValues(TestCase):
   def test_if_function_present(self):
      input = {"Alice": 30, "age": 25, "city": 40}
      dictionaryadd.get_switched_dictionary(input)

   def test_if_result_is_correct(self):
      input = {"Alice": 30, "age": 25, "city": 40}
      actual =  dictionaryadd.get_switched_dictionary(input)
      expected = {30: "Alice", 25: "age", 40 :"city"}
      self.assertEqual(expected, actual)