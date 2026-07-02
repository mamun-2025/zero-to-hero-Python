


# ##### Step 1: Generator কী?
# """
# ধরো তোমার কাছে ১ কোটি Number আছে।

# List ব্যবহার করলে

# nums = [1, 2, 3, ..., 10000000]

# Memory

# RAM

# ↓

# সব Number একসাথে Load হবে

# এতে অনেক Memory লাগবে।

# Generator

# 1

# ↓

# 2

# ↓

# 3

# ↓

# 4

# ↓

# ...

# ↓

# একটা একটা করে তৈরি হবে

# Memory খুব কম লাগবে।
# Generator হলো এমন একটি Function, যা একসাথে সব Value Return না করে, 
# yield ব্যবহার করে একবারে একটি করে Value দেয়।

# """
# def numbers():
#    yield 1
#    yield 2
#    yield 3

# g = numbers()
# print(g)
# """
# দেখো,
# Function Call করার পর
# Value Return হয়নি।
# Generator Object Return হয়েছে।
# """


# g = numbers()
# print(next(g))
# print(next(g))
# print(next(g))

# """
# Internal Flow:
# Generator

# ↓

# yield 1

# ↓

# Pause

# ↓

# next()

# ↓

# yield 2

# ↓

# Pause

# ↓

# next()

# ↓

# yield 3

# ↓

# Pause

# ↓

# StopIteration

# সবচেয়ে গুরুত্বপূর্ণ বিষয়:

# Generator
# Pause হতে পারে।

# Function
# Pause হতে পারে না।
# """




# ##### Step 2 — yield কী?

# def demo():
#    print("A:")

#    yield 10

#    print("B:")

#    yield 20

#    print("C:")

# g = demo()
# print(next(g))
# print(next(g))

# """
# দেখো

# Generator
# যেখান থেকে Pause হয়েছিল
# সেখান থেকেই আবার শুরু হয়েছে।

# Memory Diagram:
# Start

# ↓

# A

# ↓

# yield 10

# ↓

# Pause

# ↓

# Resume

# ↓

# B

# ↓

# yield 20

# ↓

# Pause

# ↓

# Resume

# ↓

# C

# ↓

# Finish
# """




# ##### Step 3 — return vs yield
# # Normal function
# def test():
#     return 10

#     return 20

# print(test()) # প্রথম return-এই Function শেষ।

# # Generator function
# def test():
#    yield 10

#    yield 50

# t = test()
# print(next(t))
# print(next(t))

# """
# Difference

# return	                       yield
# Function শেষ	                 Pause করে
# একবার Return                    অনেকবার Value দেয়
# Memory বেশি	                     Memory কম
# Resume হয় না	                   Resume হয়
# """




# ##### Step 4 — for Loop
# # Generator-ও Loop করা যায়।
# def numbers():
#    yield 1
#    yield 2
#    yield 3

# num = numbers()

# for n in num:
#    print(n)

# # Generator with Loop
# def count():

#    for i in range(1, 11):
      
#       yield i

# for c in count():
#    print(c)


# # Square Generator
# def square():

#    for g in range(1, 6):

#       yield g*g 

# for s in square():
#    print(s)





# ##### Step 5: Generator Expression
# # 1.list comprehension
# # []
# # সব Memory-তে
# # Fast Access
# nums = [x*x for x in range(1, 6)]
# print(nums)
# # [1, 4, 9, 16, 25]
# # সব Memory-তে থাকবে।


# # 2.Generator Expression
# # ()
# # একটার পর একটা
# # কম Memory
# nums = (x*x for x in range(1, 6))
# print(nums) # <generator object <genexpr> at 0x0000021217D3A4D0>

# for g in nums:
#    print(g)


# # 3.Backend Example:
# # List
# with open("source.txt", "r") as file:
#    lines = file.readlines()
#    print(lines)  
# # সব RAM-এ যাবে। 

# # Iterator / Generator
# with open("source.txt", "r") as file:
#    lines = file.readlines()
   
#    for line in lines:
#       print(line)

# # একটা Line

# # ↓

# # Process

# # ↓

# # পরের Line

# # 4.Django Example
# """
# for user in User.objects.iterator():
#    print(user.username)

# এখানে Django Generator/Iterator ব্যবহার করে 
# Memory Efficientভাবে Data Process করে।

# """




# ##### Step 6: Generator vs Iterator
# """
# Iterator	                  Generator
# Class লিখতে হয়	         শুধু Function
# __iter__()	               দরকার নেই
# __next__()	               দরকার নেই
# Code বেশি	               Code কম
# Complex	                  Simple
# """
# # Iterator
# class Counter:
#    def __init__(self):
#       self.number = 1

#    def __iter__(self):
#       return self 
   
#    def __next__(self):
#       if self.number <= 10:
#          value = self.number
#          self.number += 1
#          return value
#       raise StopIteration
   
# counter = Counter()

# for num in counter:
#    print(num)


# # Generator
# def Counter():

#    for i in range(1, 11):
      
#       yield i

# counter = Counter()

# for c in counter:
#    print(c)

# # একই কাজ
# # কিন্তু Generator-এর Code অনেক ছোট।




##### Step 7: send()
def Calculator():
   for c in range(1, 11):

      yield c 

calc = Calculator()

for i in calc:
   print(i)


def calculator():
   while True:
      num = yield
      print("Received:", num)

g = calculator()

next(g)

g.send(100)


def multiply():
   while True:
      number = yield
      print(number * 2)

g = multiply()

next(g)

g.send(5)
g.send(10)
g.send(100)
# এখানে Generator প্রতিবার নতুন Value গ্রহণ করছে।




##### Step 2: yield from
# ধরো দুটি Generator আছে।
def first():
   yield 1

   yield 2

def second():
   yield 1

   yield 2

def all_numbers():
   yield from first()

   yield from second()


for i in all_numbers():
   print(i)





##### Step 3 — yield from vs Loop
# আগে
def all_numbers():
   for i in first():
      yield i 

   for i in second():
      yield i 


# Short Version
def all_numbers():
   yield from first()

   yield from second()

# দুইটিই একই কাজ করে।



##### Step 4 — Nested Generator
def odd():

   yield 1

   yield 3

   yield 5

def even():

   yield 2

   yield 4

   yield 6


def numbers():
   yield from odd()

   yield from even()


for num in numbers():
   print(num)




###### Step 5 — Generator Pipeline
# এটি Backend-এ অনেক ব্যবহৃত হয়।
# ধরো
# ১০ লাখ User আছে।

# প্রথম Generator
def users():
   
   for i in range(1, 6):

      yield {
         "id": i,
         "active": i % 2 == 0
      }

# দ্বিতীয় Generator
def active_users(data):

   for user in data:
      
      if user["active"]:

         yield user


for user in active_users(users()):
   print(user)

"""
Flow

Database

↓

users()

↓

Generator

↓

active_users()

↓

Generator

↓

Print

একসাথে পুরো Data Memory-তে আসে না।
"""



##### Step 6 — Large File Example
# Bad 
with open("source.txt", "r") as file:
   
   data = file.readlines()

   print(data)

# সব RAM-এ যাবে।


# Good
with open("source.txt", "r") as file:

   for line in file:

      print(line)




##### Step 7 — JSON Processing
users = [
   {"name": "A"},
   {"name": "B"},
   {"name": "C"}
]

def get_users():

   for user in users:

      yield user 

for user in get_users():
   print(user)




##### Step 8: CSV Processing
import csv

def read_csv():

   with open("source.txt", "r") as file:

      reader = csv.DictReader(file)

      for row in reader:

         yield row 

# এটি বড় CSV File-এর জন্য খুবই কার্যকর।




##### Step 9: Django Example 
# for user in User.objects.iterator():
#    print(user.username)

# iterator() ব্যবহার করলে Django সব Row একসাথে Memory-তে আনে না।




##### Step 10: Generator কোথায় ব্যবহার করবে?
"""
1. Large File 
for line in file 

2. CSV 
csv.DictReader()

3. Database
QuerySet.iterator()

4. Large JSON
yield user 

5. API Streaming
yield response


yield	                   Value দিয়ে Pause করে
next()	                পরের Value নেয়
send()	                Generator-এ Value পাঠায়
yield from	             অন্য Generator-এর Value দেয়
Generator Expression	    (x for x in range(...))
Memory	                খুব কম ব্যবহার করে



Backend-এ কোথায় লাগবে?

তুমি যেহেতু Python Backend → Django Engineer হতে চাও, Generator খুব কাজে লাগবে:
বড় CSV Import
বড় JSON Export
লক্ষাধিক Database Row Process
Log File পড়া
API Streaming
Background Data Processing
"""



##### 🎯 Practice Challenge (নিজে করার জন্য)
"""
১–১০ পর্যন্ত Generator লিখো।
Even Number Generator।
Odd Number Generator।
Fibonacci Generator।
Prime Number Generator।
Square Generator।
Cube Generator।
Character Generator ("Python" থেকে এক অক্ষর করে)।
JSON User Generator (yield করে এক User করে)।
File Line Generator (এক লাইন করে পড়বে)।
"""


