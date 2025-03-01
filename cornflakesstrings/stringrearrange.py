def string_rearrange(string_one, string_two):
    new_string = ""
    store = string_two[0]
    store_two = string_one[0]
    fan = string_two.replace(store, store_two)
    new_string = new_string + fan + " "
    belt = string_one.replace(store_two, store)
    new_string = new_string + belt + ""
    return new_string

    