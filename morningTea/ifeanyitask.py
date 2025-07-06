def validator_function(user_input):
    user_list = []
    for element in user_input:
        if not element.isdigit():
            user_list.append(element)
    if len(user_list) % 2 != 0:
        return False
    else:
        return True