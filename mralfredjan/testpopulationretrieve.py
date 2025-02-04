from unittest import TestCase
import populationretrieve

class ReturningPopulation(TestCase):
   def test_if_function_even_return_present(self):
      dict_input = countries = {"USA": {"California": {"Los Angeles": 4000000, "San Francisco": 8700000}}, "Canada": {"Ontario":{"Toronto": 2930000, "Ottawa": 994837}} }
      country_input = "usa"
      state_input = "california"
      populationretrieve.population_retrive(dict_input, country_input, state_input)

   def test_if_function_can_return_population(self):
      dict_input = countries = {"USA": {"California": {"Los Angeles": 4000000, "San Francisco": 8700000}}, "Canada": {"Ontario":{"Toronto": 2930000, "Ottawa": 994837}} }
      country_input = input("Enter country: ")
      state_input = input("Enter state: ")
      actual = populationretrieve.population_retrive(dict_input, country_input, state_input)
      expected = "Los Angeles: 4000000\nSan Francisco: 8700000\n"
      self.assertEqual(actual, expected)