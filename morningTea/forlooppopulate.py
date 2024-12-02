def total(list):
   total = 0
   for number in range(len(list) + 1):
      total += number
   return total
  
def add_to_loop():
   List = []
   for number in range(1, 6):
      List.append(number)
   return List
print(add_to_loop())

def uzo():
   return total([number for number in range(1, 6)])
print(uzo())


def get_cube(a_list):
   cube = []
   for number in a_list:
      cube.append(number**(3))
   return cube
print(get_cube(add_to_loop()))


def return_cube(numbers):
	return [number ** 3 for number in numbers]
print(return_cube(add_to_loop()))
   