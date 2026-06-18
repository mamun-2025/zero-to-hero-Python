
"""
Python Dictionary:
Dictionary is a data structure that stores information in key-value pairs.
While keys must be unique and immutable (like strings or numbers), values can be of any data type,
values can be of any data type, whether mutable or immutable. 
This makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list.

"""

## 1. Dictionary কী ?

# List
student = ["mamun", 25]

print(student[0])
print(student[1])
# দেখে বোঝা যায় না কোনটা name, কোনটা age।

# Dictionary 
student = {
   "name": "Mamun",
   "age": 25
}

print(student["name"])
print(student["age"])
# এখন পরিষ্কার।




## 2. Dictionary Structure
"""
student = {
    "name": "Mamun",
    "age": 20,
    "city": "Dhaka"
}

Memory:
"name" → "Mamun"
"age" → 20
"city" → "Dhaka"
"""



## 3. Key এবং Value
"""
student = {
    "name": "Mamun",
    "age": 20
}

এখানে
"name" = Key
"Mamun" = Value

"age" = Key
20 = Value

"""



## 4. Access Value
# Method 1
student = {
   "name": "Mamun",
   "age": 25
}
print(student["name"])

# Method 2
student = {
   "name": "Mamun",
   "age": 25
}
print(student.get("age"))



## 5. get() কেন গুরুত্বপূর্ণ?
student = {
   "name": "Mamun"
}

# Wrong Key
# print(student["age"]) # KeyError

# Safe Version
print(student.get("age")) # None

# Defalut value
student = {
   "name": "Mamun",
}
print(student.get("age", 25))

# Backend-এ সবচেয়ে বেশি ব্যবহার হয়:
data = {
   "name": "Mamun Bepari",
   "email": "mamun@gmail.com"
}

info1 = data.get("name")
info2 = data.get("email")

print(info1)
print(info2)




## 6. Add New Key
student = {
   "name": "mamun"
}

student["age"] = 25 # New Key
student["name"] = "Nodita" # Update value

print(student)




## 7. Update Existing Value
student = {
   "name": "Mamun"
}

student["name"] = "Rahim"
print(student)




## 8. Delete key
#
student = {
   "name": "mamun",
   "age": 25
}

del student["age"]
print(student)

#
d = {
   "a": 1,
   "b": 2
}

del d["a"]
print(d)




## 9. pop()
# Delete + return
student = {
   "name": "Mamun",
   "age": 25
}

value = student.pop("age")
print(student)
print(value)

d = {
   "a": 1,
   "b": 2
}

value = d.pop("a") 

print(value)  # Key delete but value return 
print(d) # Other key value return




## 10. clear()
student = {
   "name": "mamun",
   "age": 25
}

student.clear()
print(student)




## 11. Loop Through Keys
student = {
   "name": "Mamun",
   "age": 25
}

for key in student:
   print(key)




## 12. Loop Through Values
student = {
   "name": "Mamun",
   "age": 25
}

for value in student.values():
   print(value)




## 13. Loop Through Both 
users = {
   "id": 1,
   "name": "Mamun",
   "active": True
}

# Key through
for key in users:
   print(key)

# value through
for value in users.values():
   print(value)

# key and value both through
for key, value in users.items():
   print(key, value)




## 14. keys():
student = {
   "name": "mamun",
   "age": 25
}

print(student.keys())

# list বানাতে:
print(list(student.keys()))




## 15. values()
student = {
   "name": "mamun",
   "age": 25
}

print(student.values())
print(list(student.values()))




## 16. items()
student = {
   "name": "mamun",
   "age": 25
}

print(list(student.items()))

"""
Most Important

খেয়াল করো:
      items()

      ↓

      Tuple দেয়

এজন্য Tuple জানা গুরুত্বপূর্ণ।

"""



## 17. Nested Dictionary
# Backend-এ খুব বেশি ব্যবহার হয়।
student = {
   "name": "Mamun", 
   "address": {
      "city": "Dhaka",
      "country": "Bangladesh"
   }
}

print(student["address"]["country"])




## 18: Real API Response 
response = {
   "id": 1, 
   "name": "Mamun",
   "email": "mamun@gmail.com"
}

print(response["name"])
print(response["email"])




## 19. List of Dictionaries
users = [
   {
      "name": "Mamun",
      "age": 25
   },
   {
      "name": "Rahim",
      "age": 30
   }
]

print(users[0])
print(users[1])

# First User Name 
print(users[0]["name"])
print(users[0]["age"])




## 20. Dictionary Comprehension
# List Comprehension-এর মতো।
squares = {x: x*x for x in range(1, 6)}
print(squares)



## 21. Zip() Very Important
names = ["Mamun", "Rahim", "Karim"]
ages = [20, 25, 30]

res = list(zip(names, ages))
print(res)



## 22. Zip() with Dictionary
users = ["Mamun", "Habib", "Rudro"]
id_name = [1, 2, 3]

data = dict(zip(users, id_name))
print(data)


"""
Backend-এর জন্য সবচেয়ে গুরুত্বপূর্ণ ১০টা Dictionary Operation

1. d["key"]  # access
2. d.get["key"] # safe access
3. d["key"] = value # add/update
4. del d["key"] = # delete
5. d.pop("key") 
6. d.keys()
7. d.values()
8. d.items()
9. for k, v in d.items():
10. dict(zip(a, b))

"""