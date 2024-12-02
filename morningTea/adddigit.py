def get_sum_digit(digit):
  # return sum([int(number) for number in str(digit)])
   return sum(list(map(lambda number: int(number), str(digit))))