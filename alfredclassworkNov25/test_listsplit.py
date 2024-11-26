from unittest import TestCase
import listsplit

class SplittingList(TestCase):
   def test_if_function_is_present(self):
      listInput = [1, 2, 3, 4, 6, 7, 9]
      listsplit.get_split_list(listInput)
      
   def test_if_function_is_working(self):
      listInput = [1, 2, 3, 4, 6, 7, 9]
      expected = [[1, 2, 3, 4], [6, 7, 9]]
      actual = listsplit.get_split_list(listInput)
      self.assertEquals(expected, actual)