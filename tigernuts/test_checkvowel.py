from unittest import TestCase
import checkvowel

class CheckingForVowel(TestCase):
   
   def test_if_funtction_is_present(self):
      userInput = input("Enter a word or sentence: ")
      checkvowel.vowel_check(userInput)
  
   def test_if_my_funtion_is_working(self):
      userInput = input("Enter a word or sentence: ") 
      expected = 4;
      actual = checkvowel.vowel_check(userInput)
      self.assertEqual(expected, actual)