from unittest import TestCase
import prime

class PrimeChecker(TestCase):
   def test_if_function_is_present(self):
      userInput = int(input("Enter integer: "))
      prime.check_prime(userInput)

   def test_if_function_performs_function(self):
      userInput = int(input("Enter integer: "))
      expected = "prime"
      actual = prime.check_prime(userInput)
      self.assertEqual(expected, actual)