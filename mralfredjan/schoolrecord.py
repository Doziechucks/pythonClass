

school_records = {"class_1": {"students":[{"name": "Harry", "scores":{"Maths": 88, "English": 76}}, {"name": "Solomon", "scores": {"Maths": 95, "English": 89}},] },
 "class_2": {"students": [{"name": "Daniel", "scores":{"Maths": 78, "English": 72}},
 {"name": "Samuel", "scores":{"Maths": 85, "english": 80}}, 
]}}

total = 0
count_2 = 0
for grade in school_records.values():
   summation = 0
   count = 0
   for numbers in grade["students"]:
      summation += numbers["scores"]["Maths"]
      count = count + 1
      count_2 += 1
      averages = summation / count
      total += numbers["scores"]["Maths"]
   print(averages)
total_average = total / count_2
print(total_average)