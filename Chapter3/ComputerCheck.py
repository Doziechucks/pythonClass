userInput = input("what problem are you having: ")
response = input("have you had this problem before: ")
responseInput = response.lower()
if responseInput == "yes":
   print("well, you have it again.")
elif responseInput == "no":
   print("well, you have it now.")