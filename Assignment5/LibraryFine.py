numberOfDays = int(input("number of days you held the book: "))
if numberOfDays <= 5:
   print("Your fine is 5paise")
elif (numberOfDays > 5 and numberOfDays <=15):
   print("Your fine is 50paise")
elif(numberOfDays > 15 and numberOfDays <=30):
   print("your fine is 5rubie")
else:
   print("your membership license has been withdrawn")