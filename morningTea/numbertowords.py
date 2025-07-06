def length_check(number):
    if number.isdigit():
        number = int(number)
        string_number = str(number)
        return str(number), len(string_number)
    else:
        return "invalid number"

# def length(number):
#     if number.isdigit():
#         number = int(number)
#         return number
#     else:
#         return "invalid number"


def convert_single_digit(number):

    if number == "0":
        return "zero"
    elif number == "1":
        return "one"
    elif number == "2":
        return "two"
    elif number == "3":
        return "three"
    elif number == "4":
        return "four"
    elif number == "5":
        return "five"
    elif number == "6":
        return "six"
    elif number == "7":
        return "seven"
    elif number == "8":
        return "eight"
    elif number == "9":
        return "nine"

def convert_multiple_digits(number):
    if length_check(number)[1] == 1:
        number = length_check(number)[0]
        return convert_single_digit(number)


    if length_check(number)[1] == 2:

        if length_check(number)[0] == "11":
            return "eleven"
        elif length_check(number)[0] == "12":
            return "twelve"
        elif length_check(number)[0] == "13":
            return "thirteen"
        elif length_check(number)[0] == "14":
            return "fourteen"
        elif length_check(number)[0] == "15":
            return "fifteen"
        elif length_check(number)[0] == "16":
            return "sixteen"
        elif length_check(number)[0] == "17":
            return "seventeen"
        elif length_check(number)[0] == "18":
            return "eighteen"
        elif length_check(number)[0] == "19":
            return "nineteen"
        elif length_check(number)[0] == "20":
            return "twenty"
        elif length_check(number)[0] == "10":
            return "ten"

        elif length_check(number)[0][0] == "2":
            return "twenty"
        elif length_check(number)[0][0] == "3":
            return "thirty"
        elif length_check(number)[0][0] == "4":
            return "forty"
        elif length_check(number)[0][0] == "5":
            return "fifty"
        elif length_check(number)[0][0] == "6":
            return "sixty"
        elif length_check(number)[0][0] == "7":
            return "seventy"
        elif length_check(number)[0][0] == "8":
            return "eighty"
        elif length_check(number)[0][0] == "9":
            return "ninety"

def three_digits_converter(number):
    if number == "1":
        return "one hundred"
    elif number == "2":
        return "two hundred"
    elif number == "3":
        return "three hundred"
    elif number == "4":
        return "four hundred"
    elif number == "5":
        return "five hundred"
    elif number == "6":
        return "six hundred"
    elif number == "7":
        return "seven hundred"
    elif number == "8":
        return "eight hundred"
    elif number == "9":
        return "nine hundred"


def convert_multiples(number):
    if length_check(number)[1] == 1:
        number = length_check(number)[0]
        return convert_single_digit(number)

    elif length_check(number)[1] == 2:
        number = length_check(number)[0]
        return convert_multiple_digits(number) + " " + convert_single_digit(str(number)[1])

    elif length_check(number)[1] == 2 and int(length_check(number)[0][1]) > 0:
        number = length_check(number)[0]
        return convert_multiple_digits(number) + " " + convert_single_digit(length_check(number)[0][1])

    elif length_check(number)[1] == 3 and int(length_check(number)[0][1]) > 0 and int(length_check(number)[0][2]) > 0:
        number = length_check(number)[0]
        return three_digits_converter(number[0][0]) + " and " + convert_multiple_digits(length_check(number)[0][1] + length_check(number)[0][2]) + " " + convert_single_digit(length_check(number)[0][2])

    elif length_check(number)[1] == 3 and int(length_check(number)[0][1]) == 0 and int(length_check(number)[0][2]) == 0:
        number = length_check(number)[0]
        return three_digits_converter(number[0][0])

    elif length_check(number)[1] == 3 and int(length_check(number)[0][1]) > 0 and int(length_check(number)[0][2]) == 0:
        number = length_check(number)[0]
        return three_digits_converter(number[0][0]) + " and " + convert_multiple_digits(length_check(number)[0][1] + length_check(number)[0][2])

    elif length_check(number)[1] == 3 and int(length_check(number)[0][1]) == 0 and int(length_check(number)[0][2]) > 0:
        number = length_check(number)[0]
        return three_digits_converter(number[0][0]) + " and " + convert_single_digit(length_check(number)[0][2])












