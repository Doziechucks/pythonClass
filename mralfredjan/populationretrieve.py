countries = {"USA": {"California": {"Los Angeles": 4000000, "San Francisco": 8700000}}, "Canada": {"Ontario":{"Toronto": 2930000, "Ottawa": 994837}} }


def population_retrive(dict_input, country_input, state_input):
   answer = ""
   for key in dict_input.keys():
      if(country_input.lower() == key.lower()):
         for value in dict_input[key].keys():
            if(state_input.lower() == value.lower()):
               for city, pop in dict_input[key][value].items():
                  answer += f"{city}: {pop}\n"
               print(answer)
            elif(state_input.lower() != value.lower()):
               return "Invalid State"

      elif(country_input.lower() != key.lower()):
         return "Invalid Input(do you mean USA OR Canada)"
      