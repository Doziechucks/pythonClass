
def return_hcf(*kwargs):
    numbers = []
    for element in kwargs:
         numbers.append(element)
    new_number = numbers[0]

    answer = 1
    for number in range(new_number, 1, -1):
        checker = 1
        for num in numbers:
            if num % number != 0:
                checker += 1
        if checker == 1:
            answer = number
            break

    return answer


