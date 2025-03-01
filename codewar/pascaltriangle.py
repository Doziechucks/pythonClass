def pascal(number):
    final_array = []
    single_array = [1]
    double_array = [1, 1]
    if number == 1:
        final_array.append(single_array)
    elif number == 2:
        final_array.append(single_array)
        final_array.append(double_array)
    elif number > 2:
        final_array.append(single_array)
        final_array.append(double_array)
        for num in range(3, number + 1):
            new_array = [final_array[num - 2][0]]
            for element in range(num - 2):
                new_array.append(final_array[num - 2][element] + final_array[num - 2][element + 1])
            new_array.append(final_array[num -2][-1])
            final_array.append(new_array)


    return final_array

print(pascal(10))