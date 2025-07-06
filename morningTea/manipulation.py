def checker(user_input, arrangement):
    new_num = ""
    count = len(user_input)
    number = len(user_input)
    while count > 0:
        print(user_input)
        for number_count in range(count - 1, number):
            new_num += user_input[number_count]
        for number_count in range(count - 1):
            new_num += user_input[number_count]
        if user_input == arrangement:
            return True
        elif count == 0:
            return False
        else:
            print(new_num)
            user_input = new_num
            new_num = ""


