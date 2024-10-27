from datetime import datetime


currentDate = datetime.now()

   
myDate =  currentDate.strftime("%a, %b %d, %H:%M:%S")
timezonel = currentDate.now().astimezone().strftime("%Z")
myYear =  currentDate.strftime("%Y")
print(f"Current date time: {myDate} {timezonel} {myYear}")