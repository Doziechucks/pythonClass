def upper_first(input_string):
    new_string = ""
    for letter in input_string:
        if letter.isupper() == True:
            new_string = new_string + letter
            input_string.strip(letter)
    new_string = new_string + input_string
    return new_string
            