def remove_special(user_input):
    new_string = ""
    for letter in user_input:
        if letter.isalpha() == True or letter.isnumeric() == True:
            new_string = new_string + letter
            
    return new_string