
"""
Python Tuples:
A tuple is a immutable ordered collection of elements.
- Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
- Can hold elements of different data types.
- These are ordered, heterogeneous and immutable.

"""
# Tuple আসলে List-এর মতোই, কিন্তু একটা বিশাল পার্থক্য আছে:
# Tuple vs List 
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 100 # List mutable
print(my_list)

# my_tuple[0] = 100
# print(my_tuple) # Tuple Immutable


## 1. Tuple কি?
# Tuple is Ordered, Indexed, Immutable.
person = ("Mamun", 25, "Bangladesh")
print(person)


## 2. Tuple কেন ব্যবহার করে?
"""
ধরো জন্ম তারিখ:

birth_date = (12, 5, 2005)

এটা পরিবর্তন হওয়ার কথা না।
তাই Tuple ব্যবহার করা ভালো।

"""


## 3. Empty Tuple and Creating Tuple 
# Empty tuple 
t = ()
print(t)

# Using string
tup = ("Mamun", "habib")
print(tup)

# Using List
li = [1, 2, 3, 4, 5]
print(li)

# Using Built-in Function
tup = [1, 2, 3, 4, 5]
print(tuple(tup))




## 4. Different type of making tuple 
# method 1:
t = (1, 2, 3)
print(t)

# method 2:
t = tuple([1, 2, 3])
print(t)

# method 3:
t = tuple("ABC")
print(t)




## 5. Mixed Data Types
# Tuple-এ সব ধরনের Data রাখা যায়।
tup = (5, "welcome", 5.0, True, [1, 2, 3], {"key": "value"})
print(tup)




## 6. Indexing
t = ("Mamun", "Python", "Java", "JavaScript")
print(t[0])
print(t[1])
print(t[2])
print(t[3])




## 7. Slicing
t = ("A", "B", "C", "D", "E")
print(t[0:])
print(t[0:3])
print(t[1:3])
print(t[:3])




## 8. Reverse Tuple 
tup = (1, 2, 3, 4, 5)
print(tup[::-1])
print(tup[::-2])
print(tup[1:-2])




## 9. Tuple Concatenation
t1 = (1, 2)
t2 = (3, 4)

result = t1 + t2
print(result)

# 
tup1 = (1, 2, 3, 4, 5)
tup2 = ("Geeks", "for", "Geeks")

result = tup1 + tup2
print(result)




## 10. Tuple Unpacking
# Most Important 
t = ("Mamun", 25)
name, age = t 

print(name)
print(age)

#
tup = ("Geeks", "for", "Geeks")
a, b, c = tup 

print(a)
print(b)
print(c)



## 11. Unpacking Error

#      t = (1, 2, 3)
#      a, b = t 
#      print(a)
#      print(b)

# Error: Because 3 values and 2 variables



## 12. Star Unpacking (*)
t = (1, 2, 3, 4, 5)

a, *b, c = t 

print(a)
print(c)
print(b)

# 
tup = ("mamun", 20, "Python", "Django")
name, age, *skills = tup

print(name)
print(age)
print(skills)



## 13. Tuple Immutable

#     t = (1, 2, 3)
#     t[0] = 100
#     print(t)

# TypeError: কারণ Tuple Change করা যায় না।


## 14. Tuple Delete
"""
Element Delete করা যায় না।
t = (1, 2, 3)
del t[1]
print(t)


পুরো Tuple Delete করা যায়।
t = (1, 2, 3, 4, 5)
del t 
print(t)
"""



## 15. Tuple Methods
# Tuple-এর Method খুব কম।

# count()
t = (1, 2, 2, 2, 3, 4, 5)
result = t.count(2)
print(result)

# index()
t = (10, 20, 30, 40, 50)
print(t.index(20))
print(t.index(40))
print(t.index(50))


## 16. Backend Developer হিসেবে Tuple কোথায় লাগে?

## Function Return Multiple Values
def get_user():
   return ("Mamun", 25)

name, age = get_user()

print(name)
print(age)


#
def get_user():
   return ("mamun", 25, "Python", "Django", "PostgreSQL")

name, age, *skills = get_user()

print(name)
print(age)
print(skills)


## Database Row
user = (
   1, 
   "Mamun",
   "mamun@gmail.com"
)

print(user)


## Coordinates
point = (10, 20)