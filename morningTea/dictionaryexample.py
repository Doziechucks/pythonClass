my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)

print(my_dict["name"]) 
if "city" in my_dict:
   print("city is in dictionary")

del my_dict["city"]
print(my_dict)
print(my_dict.get("name"))
print(my_dict.get("city", "Not Available"))
for key in my_dict:
   print(key)

for value in my_dict.values():
   print(value)

for key, value in my_dict.items():
   print(f"{key}: {value}")

print({x: x**2 for x in range(1, 6)})
