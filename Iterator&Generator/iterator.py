

##### Step 1 — Iterable কী?
"""
যে Object থেকে একটার পর একটা Value নেওয়া যায় তাকে Iterable বলে।

Python-এ অনেক Built-in Iterable আছে।

List
Tuple
String
Dictionary
Set
Range
"""
# 1. List
nums = [10, 20, 30]
for num in nums:
   print(num)

# List হচ্ছে Iterable।


# 2. String
name = "Mamun"
for char in name:
   print(char)

# String-ও Iterable।


# 3. Tuple
tup = (10, 20, 30)
for t in tup:
   print(t)

# Tuple-ও Iterable।


# 4. Set
s = {1, 2, 3}
for i in s:
   print(i)

# Set-ও Iterable।


# 5. Dictionary
student = {
   "name": "Mamun",
   "age": 25
}

for key in student:
   print(key)

for key in student.keys():
   print(key)

for key in student.items():
   print(key)

# Dictionary-ও Iterable।


# 6. Range
for r in range(1, 11):
   print(r)

# Range ও Iterable।

# Iterable মানে = Loop করা যায়।




##### Step 2: for Loop ভিতরে কী করে?
"""
Python ভিতরে ভিতরে এটা করে

nums

↓

Iterator তৈরি

↓

10

↓

20

↓

30

↓

Stop

অর্থাৎ
for Loop নিজে Data বের করে না।
সে Iterator ব্যবহার করে।

"""




##### Step 3 — Iterator কী?
"""
Iterator হচ্ছে এমন Object, যে একটা একটা করে Data দেয়।

Example

List

↓

Iterator

↓

10

↓

20

↓

30

↓

StopIteration

Iterator কখনো
সব Data একসাথে দেয় না।
একটা করে দেয়।

"""



##### Step 4: Iterable vs Iterator
"""
Iterable	               Iterator
______________          _________

Data Store করে	         Data দেয়
Loop করা যায়	          next() করা যায়
List	                  iter(list)
Tuple                	iter(tuple)
String	               iter(string)

"""
nums = [10, 20, 30] # iterable
it = iter(nums) # iterator
print(it)

name = "Python" # iterable
it = iter(name) # iterator
print(it)

dic = {
   "name": "NOndita", 
   "age": 25
}
it = iter(dic)
print(it)

tup = (1, 2, 3)
it = iter(tup)
print(it)

s = {1, 2, 3}
it = iter(s)
print(it)


# iter() এর কাজ
"""
Iterable

↓

Iterator
"""


# next() Iterator থেকে পরবর্তী Value আনে।
nums = [10, 20, 30] # iterable
it = iter(nums) # iterator
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # StopIteration কারণ আর কোনো Value নেই।
"""
Internal Flow
Iterator

↓

next()

↓

10

↓

next()

↓

20

↓

next()

↓

30

↓

next()

↓

StopIteration
"""




##### Step 5: next() with Default Value
# StopIteration এড়াতে
nums = [10, 20]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it, "Finished")) # এখানে Error হবে না।
print(next(it, "Finished"))




##### Step 6 — for Loop vs next()
# for loop
nums = [10, 20, 30]

for n in nums:
   print(n)

# Manual
nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

# দুইটিই একই কাজ করে।

"""
Iterator-এর বড় সুবিধা

ধরো

1 কোটি Data

List

সব Data Memory-তে

Iterator

একটা করে Data

↓

কম Memory

এই কারণে Iterator Backend Development-এ খুব গুরুত্বপূর্ণ।

"""
# Backend Example
# ফাইলে ১০ লাখ Line আছে।
with open("source.txt", "r") as file:
    
    for line in file:
       print(line)

# এখানে Python পুরো File Memory-তে Load করে না।
# Iterator ব্যবহার করে একটা একটা Line পড়ে।

# Django Example:
"""
for user in User.objects.all():
   print(user.username)

এখানেও Django একসাথে সব Object নিয়ে কাজ না করে 
Iterator-এর ধারণা ব্যবহার করে Data Efficiently Process করে।

"""



##### Step 7: Custom Iterator

# Example 1:
class Counter:
   def __init__(self):
      self.current = 1

   def __iter__(self):
      return self 
   
   def __next__(self):
      if self.current <= 5:
         value = self.current
         self.current += 1
         return value
      raise StopIteration
   
count = Counter()
for num in count:
   print(num)


## 
class Number:
   def __init__(self):
      self.start = 1

   def __iter__(self):
      return self
   
   def __next__(self):
      if self.start <= 10:
         value = self.start
         self.start += 1
         return value
      raise StopIteration
   
num = Number()

for n in num:
   print(n)



# Example 2: Even Number Iterator
class EvenNumbers:
   def __init__(self):
      self.number = 2

   def __iter__(self):
      return self 
   
   def __next__(self):
      if self.number <= 10:
         value = self.number
         self.number += 2
         return value
      raise StopIteration
   
even_num = EvenNumbers()

for num in even_num:
   print(num)


# Odd Number
class OddNumber:
   def __init__(self):
      self.odd = 1
   
   def __iter__(self):
      return self 
   
   def __next__(self):
      if self.odd <= 10:
         value = self.odd
         self.odd += 2
         return value
      raise StopIteration
   
odd = OddNumber()

for od in odd:
   print(od)



# Example 3: Countdown Iterator 
class CountDown:
   def __init__(self, start):
      self.start = start

   def __iter__(self):
      return self 
   
   def __next__(self):
      if self.start > 0:
         value = self.start
         self.start -= 1
         return value
      raise StopIteration
   
count_down = CountDown(5)

for count in count_down:
   print(count)


# Example 4: Name Iterator
class NameIterator:
   def __init__(self):
      self.names = ["Mamun", "Habib", "Rudro"]
      self.index = 0

   def __iter__(self):
      return self
   
   def __next__(self):
      if self.index < len(self.names):
         value = self.names[self.index]
         self.index += 1
         return value
      raise StopIteration
   
obj = NameIterator()

for name in obj:
   print(name)



# Example 5 — Manual next()
obj = NameIterator()
print(next(obj))
print(next(obj))
print(next(obj))
"""
__iter__()-এর কাজ
def __iter__(self):

    return self

এর অর্থ:
"আমি নিজেই Iterator।"

__next__()-এর কাজ
def __next__(self):

    ...

এর কাজ:
পরের Value Return করা
শেষে StopIteration Raise করা

Iterator Life Cycle:
Create Object

↓

__init__()

↓

for Loop

↓

__iter__()

↓

__next__()

↓

Value

↓

__next__()

↓

Value

↓

...

↓

StopIteration

↓

Loop শেষ

"""


# Real Backend Example: 6
# ধরো Database-এ ১০ লক্ষ User আছে।
# আমরা একসাথে সব User Memory-তে Load করতে চাই না।
# তাই Iterator দিয়ে এক এক করে User Process করা যায়।
users = [
   {"name": "Mamun"},
   {"age": 25},
   {"city": "Dhaka"}
]

for user in users:
   print(user)
# এখানেই Iterator-এর শক্তি।

# Django Connection
"""
for user in User.objects.all():
print(user.username)

এখানে QuerySet-এর উপর Loop করার সময় Django Iterator-এর ধারণা ব্যবহার করে 
Data Efficiently Process করে।

"""


