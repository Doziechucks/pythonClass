from unittest import TestCase
import numberlist

class ReturningList(TestCase):
   def test_if_function_number_list_present(self):
      numberList = [23, 45, 12, 44, 50, 77]
      numberlist.number_list(numberList)

   def test_if_function_can_return_correct_range(self):
      numberList = [23, 45, 12, 44, 50, 77]
      actual = numberlist.number_list
      expected = [23, 45, 44]
      self.assertEqual(actual, expected)


class ReturningEven(TestCase):
   def test_if_function_even_return_present(self):
      numberList = "gyjefguw628douo238"
      evenreturn.even_return(numberList)

   def test_if_function_can_return_even(self):
      numberList = "gyjefguw628douo238"
      actual = evenreturn.even_return(numberList)
      expected = [6, 2, 8, 2, 8]
      self.assertEqual(actual, expected)