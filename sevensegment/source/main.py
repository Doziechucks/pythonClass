from segments import Segments

checker = -1

def number_check(user_input):
    if user_input.isnumeric() == True:
        check_one = 1 
    else:
        check_one = -1
        print("only numbers should be inputed")
    return check_one
        
def range_check(user_input):
    for element in user_input:
        if int(element) == 0 or int(element) == 1:
            check_ = 1
        else:
            check_ = -1
            print("only 0's amd 1's are acceptable")
            break    
    return check_

def length_check(user_input):
    if len(user_input) == 8:
        check = 1
    else:
        check = -1
        print("only eight digit inputs are allowed") 
    return check
    
    
def display():
    user_input = ""
    checker = -1
    while checker == -1:
        user_input = input("Enter an 8 digit binary number to display segment: ")
        if length_check(user_input) == 1 and range_check(user_input) == 1 and number_check(user_input) == 1:
            checker = 1
        else:
            checker = -1

    upper = user_input[0]
    right_up = user_input[1]
    right_down = user_input[2]
    down = user_input[3]
    left_down = user_input[4]
    left_up = user_input[5]
    middle = user_input[6]
    switch = user_input[7]

    upper = int(upper)
    right_down = int(right_down) 
    right_up = int(right_up) 
    down = int(down) 
    left_down = int(left_down) 
    left_up = int(left_up) 
    switch = int(switch) 
    middle = int(middle)

    segments = Segments(upper, right_up, right_down, down, left_down, left_up, middle ,switch)

    segments.upper_on()
    segments.right_up_on()
    segments.right_down_on()
    segments.down_on()
    segments.left_down_on()
    segments.left_up_on()
    segments.middle_on()

    printer = segments.get_board()

    for number in range(5):
        for count in range(4):
            print(printer[number][count], end = '')
        print()
        
        
def main():
    choice = 1
    while choice == 1:
        runner = int(input("1. to run segment \n0. to quit \n"))
        if runner == 1:
            display()
        if runner == 0:
            choice = 0
            
            
main()
        

    

         