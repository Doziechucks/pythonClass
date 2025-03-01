def count_element(user_input, element):
    counter = 0
    for letter in user_input:
        if letter == element:
            counter += 1
    output = (element, counter)
    return output