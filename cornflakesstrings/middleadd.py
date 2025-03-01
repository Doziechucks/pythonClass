def stringadd(input_string):
    number = len(input_string)
    new_string = ""
    if number % 2 == 0:
        for number_one in range(number // 2):
            new_string = new_string + input_string[number_one]
        new_string = new_string + "ce"
        for index in range(number // 2, number):
            new_string = new_string + input_string[index]
    else:
        new_string = new_string + input_string + "ce"
    return new_string