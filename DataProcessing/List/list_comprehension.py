

"""
Formula of List Comprehension:

1.
[expression for item in iterable]

2. Filter:
[  
   expression 
   for item in iterable 
   if condition
]

3. if else:
[
   value_of_true
   if condition
   else value_if_false
 
   for item in iterable
]

4. Nested Loop:
[
   Expression
   for x in list1
   for y in list2
]


সবচেয়ে গুরুত্বপূর্ণ ১০টি List Comprehension Pattern
1. [i for i in range(...)]

2. [i*i for i in range(...)]

3. [x for x in nums if condition]

4. [value if condition else other for x in nums]

5. [word.upper() for word in words]

6. [len(word) for word in words]

7. int(x) for x in strings]

8. [obj["key"] for obj in data]

9. [row for row in matrix]

10. [item for row in matrix for item in row]

এই ১০টা Pattern ভালোভাবে বুঝতে পারলে Django, FastAPI, API Response Processing, JSON Handling 
এবং LeetCode Easy-এর অনেক Problem খুব সহজে করতে পারবে।

"""

## Pattern 1:
#___________________
# simple loop
result = []

for i in range(5):
   result.append(i)

print(result)


# list comprehesion for loop
# [expression for variable in iterable]
numbers = [i for i in range(5)]
print(numbers)
# Expression = i
# Variable = i
# Iterable = range(5)



## Pattern 2:
#______________
# normal loop
result = []

for i in range(5):
   result.append(i * i)

print(result)

# list comprehesion for loop
nums = [i * i for i in range(5)]
print(nums)
# Expression = i * i
# মানে Store করার আগে Calculation হচ্ছে।



## Pattern 3:
#____________
# [x for x in nums if condition]
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = [x for x in nums if x % 2 == 0]
print(result)


nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = []

for x in nums:
   if x % 2 == 0:
      result.append(x)

print(result)
# if = Filter হিসেবে কাজ করে।



## Pattern 4:
# ___________
# Normal loop
nums = [1, 2, 3, 4, 5, 6]
result = []
for x in nums:
   if x % 2 == 0:
      result.append("Even")
   else:
      result.append("Odd")

# if = Filter হিসেবে কাজ করে।
# if-else = সব Element রাখে, শুধু Value Change করে।


# list coprhension for loop
# [value if condition else other for x in nums]
nums = [1, 2, 3, 4, 5, 6]
result = [
   "Even"
   if x % 2 == 0
   else "Odd"
   for x in nums
]

print(result)



## Pattern 5:
#______________
# expression = word.upper()
# [word.upper() for word in words]
words = [
   "mamun",
   "rahim",
   "karim"
]

result = [word.upper() for word in words]
print(result)



## Pattern 6:
#_____________
# expression = len(word)
# [len(word) for word in words]
words = [
   "mamun",
   "Python",
   "FastAPI",
   "postgreSQL"
]

result = [len(word) for word in words]
print(result)



## Pattern 7:
#_____________
# [int(x) for x in strings]
# Backend-এ API Data Handle করার সময় খুব লাগে।
strings = [
   "10",
   "20",
   "30",
   "40"
]
result = [int(x) for x in strings]
print(result)



## Pattern 8:
#____________
# [obj[key] for obj in data]
# এটা Django/FastAPI-তে অনেক ব্যবহার হবে।
data = [
   {"name": "Mamun"},
   {"name": "Habib"},
   {"name": "Rudro"}
]

result = [obj["name"] for obj in data]
print(result)



## Pattern 9:
# [row for row in matrix]
matrix = [
   [1, 2],
   [3, 4], 
   [5, 6]
]

result = [row for row in matrix]
print(result)



## Pattern 10:
#_____________
# Normal loop
matrix = [
   [1, 2],
   [3, 4],
   [5, 6]
]

result = []

for row in matrix:
   for item in row:
      result.append(item)

print(result)


# list comperhesion for loop
# [item for row in matrix
#       for item in row ]
matrix = [
   [1, 2],
   [3, 4],
   [5, 6]
]

result = [item 
          for row in matrix
          for item in row ]

print(result)
