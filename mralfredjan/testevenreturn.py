from unittest import TestCase
import evenreturn

class ReturningEven(TestCase):
   def test_if_function_even_return_present(self):
      numberList = "gyjefguw628douo238"
      evenreturn.even_return(numberList)

   def test_if_function_can_return_even(self):
      numberList = "gyjefguw628douo238"
      actual = evenreturn.even_return(numberList)
      expected = [6, 2, 8, 2, 8]
      self.assertEqual(actual, expected)

class ReturnSquare(TestCase):
   def test_if_function_even_return_present(self):
      numberList = 4
      evenreturn.square_output(numberList)

   def test_if_function_can_return_Square(self):
      numberList = 4
      actual = evenreturn.square_output(numberList)
      expected = {1: 4, 2: 16}
      self.assertEqual(actual, expected)

