userAge = int(input("Enter your age in years: "))
maxHeartRate = 220 - userAge 
topHeartRate = maxHeartRate * 0.85
lowerheartRate = maxHeartRate * 0.5

print(f"your heart rate range is {lowerheartRate}-{topHeartRate }")