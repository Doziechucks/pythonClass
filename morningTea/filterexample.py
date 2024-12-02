def is_odd(x):
  return x % 2 != 0
numbers = [10, 9 , 3, 7, 8, 5, 4]
holder = list(filter(is_odd, numbers))

print(holder)