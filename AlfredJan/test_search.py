from unittest import TestCase
import search


class TestIfIntegerPresent(TestCase):
   def test_if_searcher_exist(self):
      numbers = [2, 4, -5, 20, -29]
      constant = 2
      search.searcher(constant, numbers)

   def test_if_searcher_returns_correct_index(self):
      numbers = [2, 4, -5, 20, -29] 
      constant = 4
      actual = search.searcher(constant, numbers)
      expected = "index 1"
      self.assertEqual(actual, expected)


class TestSearcherTwoSIgngs(TestCase):
   def test_if_searcher_two_exist(self):
      numbers = [2, 4, -5, 20, -29] 
      search.searcher_two(numbers)

   def test_if_searcher_returns_correctly(self):
      numbers = [2, 4, -5, 20, -29, 0] 
      
      actual = search.searcher_two(numbers)
      expected = """
negatives: 2 
zeros: 1 
positives: 3"""
      self.assertEqual(actual, expected)
