from unittest import TestCase
import classworknov

class TestDivideOrSquare(TestCase):
   def test_cube_or_divide_function_exists(self):
      classworknov.divide_or_square(5)

   def test_if_number_five_equal_zero_returns_squareroot(self):
      actual = classworknov.divide_or_square(25)
      expected = 5 
      self.assertEquals(actual, expected)

   def test_if_number_returns_remainder_when_not_divisible_by_five(self):
      actual = classworknov.divide_or_square(10)
      expected = 3.16 
      self.assertEquals(actual, expected)
      actual = classworknov.divide_or_square(7)
      expected = 2 
      self.assertEquals(actual, expected)
  
   def test_if_number_input_is_float(self):
      actual = classworknov.divide_or_square(9.2)
      expected = 4.2
      self.assertEquals(actual, expected)

   def test_if_inputed_number_is_an_integer(self):
      self.assertRaises(TypeError, classworknov.divide_or_square, "man")

   def test_if_user_input_negative_number(self):
      actual = classworknov.divide_or_square(-25)
      expected = "j5.0"
      self.assertEquals(actual, expected)
     