

## Python Lists
"""
List is built-in data structure used to store an ordered collection of items.
They are dynamic, resizable and capable of storing multiple data types.
- Mutable: List elements can be changed, updated, added, or removed after the list is created.
- Ordered: elements maintain the order in which they are inserted.
- Index-based: elements are accessed using their position, starting from index 0.


Backend Developer-এর জন্য Top List Methods

এই ১০টা সবচেয়ে গুরুত্বপূর্ণ:

append()
extend()
insert()
remove()
pop()
clear()
len()
sort()
reverse()
index()
"""

## 1. What is list ?
# List = একাধিক Data একসাথে রাখার Container।
numbers = [10, 20, 30, 40]
print(numbers)
'''
Memory:

Index
0   1   2   3

↓

10  20  30  40

'''
# String vs List
name = "Mamun" # String
print(list(name))

names = ["Mamun", "Sanjib", "Nondita", "Rudro"] # List
print(names)



## 2. List কেন দরকার?
# ধরো ৫ জন Student-এর নাম রাখতে হবে।
# Bad way
s1 = "Mamun"
s2 = "Rahim"
s3 = "Karim"
s4 = "Sakib"
s5 = "Hasan"

# Good way 
students = [
   "Mamun",
   "Rahim",
   "Karim",
   "Sakib",
   "Hasan"
]


## 3. Creating a list
# Lists can be created in several ways, such as using square brackets [], the list() constructor or by repeating elements.
# Square Brackets
numbers = [1, 2, 3]
print(numbers)

# Different Data Types
data = [
   10, 
   5.0,
   "Mamun",
   True
]

print(data)
print(type(data))
# List একসাথে বিভিন্ন Data Type রাখতে পারে।


## 4. list() constructor
li = list("Python")
print(li)


## 5. Repeated Elements
numbers = [0] * 5
print(numbers)

names = ["Mamun"] * 10
print(names)


## 6. Access Elements
# Positive Indexing
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])
print(numbers[2])


## 7. Negative Indexing
numbers = [10, 20, 30]

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])



## 8. List Mutable 
# String
# text = "ABC"
# text[0] = "X"
# print(text)
# Error 

# List 
nums = [10, 20, 30]
nums[0] = 100

print(nums)



## 9. Adding Elements: append()
nums = [1, 2]
nums.append(3)

print(nums)



## 10. insert()
# Syntax: insert(index, value)
# Specific Position a Add
nums = [0, 5, 2, 7]
nums.insert(1, 100)

print(nums)



## 11. extend()
# Multiple value add
nums = [1, 2]
nums.extend([0, 1]) # multiple value 

print(nums)

# Difference append()
nums = [1, 2]
nums.append([0, 1])

print(nums) # One value add 


## 12. Update Element
nums = [10, 20, 30]
nums[1] = 200

print(nums)



## 13. Remove Element
# Value দিয়ে Remove।
nums = [1, 2, 3]
nums.remove(3)

print(nums)



# 14. Pop()
# last element remove
nums = [1, 2, 3, 100]
nums.pop()
print(nums)

# Index দিয়ে Remove।
nums = [1, 2, 3, 100]
nums.pop(3)
print(nums)



## 15. del
nums = [10, 20, 30]
del nums[0]
print(nums)



## 16. clear()
# All remove 
nums = [1, 2, 3]
nums.clear()

print(nums)



## 17. Looping through a list
fruits = [
   "apple",
   "banana",
   "orange"
]

for fruit in fruits:
   print(fruit)



## 18: Nested List
# List-এর ভিতরে List।
matrix = [
   [1, 2],
   [3, 4]
]

print(matrix[0])
print(matrix[1])

# Specific Element
print(matrix[0][1])
print(matrix[-1])
print(matrix[-1][0])
print(matrix[-2][0])

"""
String vs List (Most Important )
string                                 List
______                                 ______
Immutable                              Mutable

Text Store                             Any data Store

"Python"                               [1, 2, 3]

Cnanot change caracter                 Can Change Element

"""


## 19. List Slicing
# String Slicing-এর মতোই।
# Syntax: list[start:end]
# Start Included = End Excluded
# Example 1:
numbers = [10, 20, 30, 40]
print(numbers[1:4])

# Example 2:
nums = [10, 20, 30, 40, 50]
print(nums[:3])

# Example 3:
nums = [10, 20, 30, 40, 50]
print(nums[2:])

# Example 4: Reverse 
numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])

# Example 5: Step(positive)
numbers = [10, 20, 30, 40, 50]
print(numbers[::2]) # take every second element

# Example 6: Step(Negative)
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[::-1])
print(numbers[::-2]) # take every second element


## 20. index()
# Element-এর Position বের করে।
nums = [10, 20, 300, 50]
res = nums.index(300)
print(res)


## 21. count()
nums = [1, 2, 1, 1]
print(nums.count(1))

text = "Python is a very powerful and Python syntax is easy"
print(text.count("Python"))


## 22. sort()
# asscending
numbers = [4, 6, 2, 1, 7, 3, 9, 5]
numbers.sort() 
print(numbers) 

numbers = ["a", "d", "b", "f", "g", "c", "e"]
numbers.sort()
print(numbers)


# descending
numbers = [4, 6, 2, 1, 7, 3, 9, 5]
numbers.sort(reverse=True) 
print(numbers)

numbers = ["a", "d", "b", "f", "g", "c", "e"]
numbers.sort(reverse=True)
print(numbers)



## 23. reverse()
numbers = [4, 6, 2, 1, 7, 3, 9, 5, "Mamun"]
numbers.reverse()
print(numbers)