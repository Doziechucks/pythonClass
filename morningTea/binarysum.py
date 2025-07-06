def binary_adder(*kwargs):
    g_total = 0
    total = 0
    for number in kwargs:
        numbers = str(number)
        length = len(numbers) - 1
        while length >= 0:
            for binary in numbers:
                var = int(binary) *  (2 ** length)
                length = length - 1
                total += var
        g_total += total
        total = 0
    number = ""
    number_answer = ""
    while g_total != 0:
        num = g_total % 2
        g_total = g_total // 2
        number += str(num)
    for new_number in range(len(number)):
        number_answer += number[-(new_number + 1)]

    return int(number_answer)
