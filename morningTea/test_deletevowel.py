from unittest import TestCase
import deletevowel

class ReturningConsonantList(TestCase):
   def test_if_function_present(self):
      list = ["Orange", "Apple", "ice", "Beans", "Rice"]
      deletevowel.get_consonant_list(list)

   def test_if_result_is_correct(self):
      list = ["Orange", "Apple", "ice", "Beans", "Rice"]
      actual = deletevowel.get_consonant_list(list)
      expected = ["rng", "ppl", "c", "Bns", "Rc"]
      self.assertEqual(expected, actual)