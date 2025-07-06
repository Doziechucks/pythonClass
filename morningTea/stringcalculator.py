def space_remove(input_string):
    equation = []
    for element in input_string:
        if element != " ":
            equation.append(element)
    return equation
def calculate(input_string):
    answer = ""
    user_input = space_remove(input_string)
    for number in range(len(user_input)):
        if user_input[0] == "/" or user_input[0] == "*" or user_input[0] == ")" or user_input[0] == "^" or user_input[0] == "%":
            return "Invalid input"
    counter = len(user_input)
    for number in range(counter):
        print(len(user_input))
        new_list = []
        if user_input[number] == "*":
            new_number = int(user_input[number - 1]) * int(user_input[number + 1])
            user_input.insert(number, new_number)
            new_list.insert(number - 1, str(new_number))
            print(len(user_input))
            user_input.pop(number)
            user_input.pop(number + 1)
            new_list.pop(number + 2)

            print(user_input[number])
        for element in new_list:
            answer += element


    return answer


















