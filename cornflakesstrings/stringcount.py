def string_count(input_string):
    new_dictionary = {}
    for letter in input_string:
        if letter in new_dictionary:
            new_dictionary[letter] = new_dictionary[letter] + 1
        else:
            new_dictionary.update({letter: 1})
    return new_dictionary
    
    