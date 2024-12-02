userInput = int(input("Enter number for day of the week: "))
if userInput < 0 or userInput > 6:
   print("Invalid Input")
else:
   match userInput:
      case 0:
         dayInput = int(input("Enter the number of days elapsed since today: "))
         day = dayInput % 7 
         match day:
            case 0: print("today is Sunday and the future day is Sunday")
            case 1: print("today is Sunday and the future day is Monday")
            case 2: print("today is Sunday and the future day is Tuesday")
            case 3: print("today is Sunday and the future day is Wednesday")
            case 4: print("today is Sunday and the future day is Thurday")
            case 5: print("today is Sunday and the future day is Friday")
            case 1: print("today is Sunday and the future day is Saturday")

      case 1:
         dayInput = int(input("Enter the number of days elapsed since today: "))
         day = (dayInput) % 7 
         match day:
            case 0: print("today is Monday and the future day is Monday")
            case 1: print("today is Monday and the future day is Tuesday")
            case 2: print("today is Monday and the future day is Wednesday")
            case 3: print("today is Monday and the future day is Thursday")
            case 4: print("today is Monday and the future day is Friday")
            case 5: print("today is Monday and the future day is Saturday")
            case 1: print("today is Monday and the future day is Sunday")

      case 2:
         dayInput = int(input("Enter the number of days elapsed since today: "))
         day = (dayInput) % 7 
         match day:
            case 0: print("today is Tuesday and the future day is Tuesday")
            case 1: print("today is Tuesday and the future day is Wednesday")
            case 2: print("today is Tuesday and the future day is Thursday")
            case 3: print("today is Tuesday and the future day is Friday")
            case 4: print("today is Tuesday and the future day is Saturday")
            case 5: print("today is Tuesday and the future day is Sunday")
            case 1: print("today is Tuesday and the future day is Monday")

      case 3:
         dayInput = int(input("Enter the number of days elapsed since today: "))
         day = (dayInput) % 7 
         match day:
            case 0: 
               print("today is  Wednesday and the future day is Wednesday")
            case 1: 
               print("today is  Wednesday and the future day is Thursday")
            case 2: 
               print("today is Wednesday and the future day is Friday")
            case 3: 
               print("today is  Wednesday and the future day is Saturday")
            case 4: 
               print("today is  Wednesday and the future day is Sunday")
            case 5: 
               print("today is  Wednesday and the future day is Monday")
            case 1: 
               print("today is  Wednesday and the future day is Tuesday")

      case 4:
         dayInput = int(input("Enter the number of days elapsed since today: "))
         day = (dayInput) % 7 
         match day:
            case 0: 
               print("today is  Thursday and the future day is Thursday")
            case 1: 
               print("today is Thursday and the future day is Friday")
            case 2: 
               print("today is  Thursday and the future day is Saturday")
            case 3: 
               print("today is  Thursday and the future day is Sunday")
            case 4: 
               print("today is  Thursday and the future day is Monday")
            case 5: 
               print("today is  Thursday and the future day is Tuesday")
            case 6: 
               print("today is  Thursday and the future day is Wednesday")

      case 5:
         dayInput = int(input("Enter the number of days elapsed since today: "))
         day = (dayInput) % 7 
         match day:
            case 0: 
               print("today is Friday and the future day is Friday")
            case 1: 
               print("today is  Friday and the future day is Saturday")
            case 2: 
               print("today is  Friday and the future day is Sunday")
            case 3: 
               print("today is  Friday and the future day is Monday")
            case 4: 
               print("today is  Friday and the future day is Tuesday")
            case 5: 
               print("today is Friday and the future day is Wednesday")
            case 6: 
               print("today is  Friday and the future day is Thursday")

      case 6:
         dayInput = int(input("Enter the number of days elapsed since today: "))
         day = (dayInput) % 7
         match day:
            case 0: 
               print("today is  Thursday and the future day is Saturday")
            case 1: 
               print("today is  Thursday and the future day is Sunday")
            case 2: 
               print("today is  Thursday and the future day is Monday")
            case 3: 
               print("today is  Thursday and the future day is Tuesday")
            case 4: 
               print("today is  Thursday and the future day is Wednesday")
            case 5: 
               print("today is  Thursday and the future day is Thursday")
            case 5: 
               print("today is Thursday and the future day is Friday")
            case 6: 
               print("today is Thursday and the future day is Friday")
