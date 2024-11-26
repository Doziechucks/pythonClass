from unittest import TestCase
import listsum

class MergingList(TestCase):
   def test_if_function_present(self):
      arrayOne = [3, 4, 9, 19]
      arrayTwo = [1, 5, 7, 8]
      listsum.list_sum(arrayOne, arrayTwo)

   def test_function_working_properly(self):
      arrayOne = [3, 4, 9, 19]
      arrayTwo = [1, 5, 7, 8]
      actual = listsum.list_sum(arrayOne, arrayTwo)
      expected = [1, 3, 4, 5, 7, 8, 9, 19]
      self.assertEqual(expected, actual)

   def test_if_inputed_array_sorted(self):
      arrayOne = [3, 4, 9, 19, 1, 4]
      arrayTwo = [1, 5, 7, 8]
      actual = listsum.list_sum(arrayOne, arrayTwo)
      expected = [1, 1, 3, 4, 4, 5, 7, 8, 9, 19]
      self.assertEqual(expected, actual)

      