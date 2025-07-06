
digit = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine" }
double_digits = { 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"}

def convert_time(time):
    numbers = time.split(":")
    if numbers[0].isdigit() and int(numbers[0]) <= 23:
        hour = numbers[0]
    else:
        return "Invalid time"
    if numbers[1].isdigit() and int(numbers[1]) <= 59:
        minutes = numbers[1]
    else:
        return "Invalid time"

    return hour, minutes

def zero_remover(unit):
    if unit[0] == "0":
        unit = str(unit[1:])
    return unit



def number_to_words(number):
    if len(number) == 1:
        for key in digit.keys():
            if int(number) == key:
                return digit[key]
    elif len(number) == 2 and int(number[1]) == 0:
        for key in tens.keys():
            if int(number) == key:
                return tens[key]
    elif len(number) == 2 and int(number[1]) > 0 and int(number[0]) > 1:
        new_number = ""
        number_n = int(number[0] + "0")
        for key in tens.keys():
            if number_n == key:
                new_number += tens[key]
        for key in digit.keys():
            if int(number[1]) == key:
                new_number += " " + digit[key]
        return new_number
    elif len(number) == 2 and int(number[0]) == 1:
        for key in double_digits.keys():
            if int(number) == key:
                return double_digits[key]

def accumulator(time):
    hour = convert_time(time)[0]
    minutes = convert_time(time)[1]
    if int(minutes) > 30:
        minutes_n = str(60 - int(minutes))
        hour = str(int(hour) + 1)
    else:
        minutes_n = minutes
    if int(hour) > 12:
        hours_n = str(int(hour) - 12)
    else:
        hours_n = str(int(hour))
    new_hour = zero_remover(hours_n)
    new_minutes = zero_remover(minutes_n)

    new_hour = number_to_words(new_hour)
    new_minutes = number_to_words(new_minutes)
    print(new_hour)
    print(new_minutes)
    if int(minutes) > 30 and int(minutes_n) > 0:
        if int(hour) > 12 and int(hours_n) != 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute to " + new_hour + " PM"
            else:
                new_minutes + " minutes to " + new_hour + " PM"
        elif int(hour) > 12 and int(hours_n) == 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute to " + new_hour + " AM"
            else:
                return new_minutes + " minutes to " + new_hour + " AM"
        elif int(hours_n) == 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute to " + new_hour + " PM"
            else:
                return new_minutes + " minutes to " + new_hour + " PM"
        elif int(hour) < 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute to " + new_hour + " AM"
            else:
                return new_minutes + " minutes to " + new_hour + " AM"

    elif int(minutes) < 30 and int(minutes_n) > 0:
        print(minutes_n)
        if int(hour) > 12 and int(hours_n) != 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute past " + new_hour + " PM"
            else:
                return new_minutes + " minutes past "+ new_hour +" PM"
        elif int(hour) > 12 and int(hours_n) == 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute past " + new_hour + " AM"
            else:
                return new_minutes + " minutes past "+ new_hour +" AM"
        elif int(hours_n) == 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute past " + new_hour + " PM"
            else:
                return new_minutes + " minutes past "+ new_hour + " PM"
        elif int(hour) < 12:
            if int(minutes_n) == 1:
                return new_minutes + " minute past " + new_hour + " AM"
            else:
                return new_minutes + " minutes past "+ new_hour + " AM"

    elif int(minutes_n) == 0 and int(hour) >= 12:
        return new_hour + " PM"
    elif int(minutes_n) == 0 and int(hour) < 12:
        return new_hour + " AM"







