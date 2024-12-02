from unittest import TestCase
import evenraise

class ReturningDictionaryEven(TestCase):
   def test_if_function_present(self):
      evenraise.get_even_raise()

   def test_if_result_is_correct(self):
      actual = evenraise.get_even_raise()
      expected = {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
      self.assertEqual(expected, actual)