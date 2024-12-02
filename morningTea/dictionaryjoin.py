def get_merched_dictionary(keys, values):
   return {key: value for key, value in zip(keys, values)}

def get_values(dictionary):
   return[values for values in dictionary.values()]
      