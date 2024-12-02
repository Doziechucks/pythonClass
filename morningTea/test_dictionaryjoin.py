from unittest import TestCase
import dictionaryjoin

class ReturningGreaterThanTenList(TestCase):
   def test_if_function_present(self):
      keys = ["name", "age", "city"]
      values = ["Alice", 25, "New York"]      
      dictionaryjoin.get_merched_dictionary(keys, values)

   def test_if_result_is_correct(self):
      keys = ["name", "age", "city"]
      values = ["Alice", 25, "New York"]
      actual = dictionaryjoin.get_merched_dictionary(keys, values)
      expected = {"name": "Alice", "age": 25, "city": "New York"}
      self.assertEqual(expected, actual)

class ReturnValues(TestCase):
   def test_if_function_present(self):
      input = {"name": "Alice", "age": 25, "city": "New York"}
      dictionaryjoin.get_values(input)

   def test_if_result_is_correct(self):
      input = {"name": "Alice", "age": 25, "city": "New York"}
      actual = dictionaryjoin.get_values(input)
      expected = ["Alice", 25, "New York"]
      self.assertEqual(expected, actual)

 