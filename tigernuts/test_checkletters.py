from unittest import TestCase
import checkletters

class AnagranCheck(TestCase):
   def test_if_function_is_present(self):
      word = input("enter word: ")
      anagram = input("enter anagram: ")
      checkletters.word_anagram(word, anagram)

   def test_if_function_returns_correct_result(self): 
      word = input("enter word: ")
      anagram = input("enter anagram: ")    
      actual = checkletters.word_anagram(word, anagram)
      expected = True
      self.assertEqual(actual, expected)