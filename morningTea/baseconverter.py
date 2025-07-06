
def convert(numbers, base, base_to):
    numbers = str(numbers)
    summation = 0
    answer = ""
    new_number = ""
    counter = len(numbers) - 1

    for number in numbers:
        summation += int(number) * base ** counter

        counter -= 1

    while summation > 0:
        new_number += str(summation % base_to)

        summation = summation // base_to

    for index in range(len(new_number)-1, -1, -1):
        answer += str(new_number[index] )
    return int(answer)


