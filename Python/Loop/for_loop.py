


## Loops in Python
"""
Loops are used to execute a block of code repeatedly until a condition is met or all items in a sequence are processed.
The main types are For loops (iterating over sequences) and while loops (executing code based on a condition.)

"""

## Pyhton for loops:
"""
Python for loops are used to iterate over sequences such as lists, tuples, strings and ranges.
- Allows the same operation to be applied to every item in a sequence.
- Avoids the need to manage loop indices manually.

"""
# example 1:
n = 5
for i in range(0, n):
   print("Nondita")

# example 2:
a = ["Geeks", "for", "Geeks"]
for i in a:
   print(i)

# example 3:
a = ["I", "Love", "Coding"]
for i in range(len(a)):
   print(a[i])

# example 4:
s = "Mamun"
for i in s:
   print(i)

# example 5:
name = "HABIB"
for item in name:
   print(item, end=" ")

# example 6:
sum = 0
for i in range(11):
   sum += i
   print(sum)

# example 7:
num = 0
for i in range(0, 5):
      num += i 
      print(num)

# example 8:
str = "Mamun + Nondita"
for i in range(0, 11):
   print(str)

# example 9:
user = int(input("Enter a number: "))
val = int(user)

for i in range(val):
   print(i)




# ###############################################################
# Python range() function
"""
The range() function in python is used to generate a sequence of integers within a specified range.
It is most commonly used in loops to control how many times a block of code runs.

Note: range() returns a lazy iterable, not a full list.
It generates numbers dynamically instead of storing them all in memory.
To access to control how many times a block of code runs.

"""
# Syntax: (start, stop, step)
##
for num in range(11):
   print(num, end=" ", )
   print("*****")

##
for item in range(0, 11):
   print(item)

##
for item in range(0, 10, 2):
   print(item, end=" ")

## 
for val in range(10, 0, -1):
   print(val)

## 
for val in range(100, 0, -5):
   print(val, end=" ")


# ##############################################################
# Control Statements
"""
The continue statement in Python is a loop control statement that skips the rest of the code 
inside the loop for the current iteration and moves to the next iteration immediately.

"""
## Continue
##
for item in "GeeksforGeeks":
   if item == "e":
      continue
   print(item)


##
for str in "Python":
   if str == "P" or str == "y":
      continue
   print(str)


##
for i in range(0, 11):
   if i == 5:
      continue
   print(i, end=" ")


## 
for char in "GeeksforGeeks":
   if char == "e":
      continue
   print(char, end=" ")



# #####################################################################
# Python Break Statement
"""
The break statement in Python is used to immediately terminate a for a while loop when a specified condition is met.
After the loop exits, program execution continues with the next statement followin the loop.

"""
##
a = [ 1, 3, 5, 7, 9, 11]

for item in a:
   if item == 7:
      print(f"found at {item}!")
      break
else:
   print(f"not found")


##
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 10
for item in num:
   if item == val:
      print(f"Found at {item}")
      break
else:
   print(f"Not found.")


##
for i in range(11):
   print(i)
   if i == 6:
      break 


##
num = 10
while True:
   print(num)
   num -= 1
   if num == 0:
      print("Countdown finished.")
      break


## Else statement 
for item in range(1, 5):
   print(item)
else:
   print("No Break\n")



############################################################
# # Python Pass Statement 
"""
The pass statement in Python is a placeholder that does nothing when executed.
- It is used to keep code blocks valid where a satatement is required but no logic is needed yet.
- Examples situations where pass is used are empty functions, classes, loops or conditional blocks.

"""
##
for i in "geeksforgeeks":
   pass 


## 
def fun():
   pass

fun()


## 
x = 2
if x > 5:
   pass 
else:
   print("x is less than 5.")


##
for i in range(5):
   if i == 3:
      pass 
   else:
      print(i)


##
class EmptyClass:
   pass # No methods or attributes yet

class Person:
   def __init__(self, name, age):
      self.name = name 
      self.age = age 

   def greet(self):
      pass   # Placeholder for greet method

# Creating an instance of the class
p = Person("Habib", 30)
p.greet()




########################################################
# # Python Nested Loop
##
for item1 in range(1, 4):
   for itme2 in range(1, 4):
      print(item1, itme2)


## 
for i in range(0, 11):
   for j in range(i):
      print(i, end=" ")
   print()



##
x = [1, 2, 3]
y = [4, 5, 6]

for i in x:
   for j in y:
      print(i, j)


## 
matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
val = 5
found = False

for mtrx in matrix:
   for n in mtrx:
      if n == val:
         print(f"{val} found!")
         found = True
         break
   if found:
      break 


##
for i in range(2, 4):
   for j in range(1, 11):
      print(i, "*", j, "=", i * j)
   print()


##
for i in range(2, 4):
   for j in range(1, 11):
      if i == j:
         continue
      print(i, "*", j, "=", i * j)
   print()


##
for item1 in range(2, 4):
   for item2 in range(1, 11):
      if item1 == item2:
         break
      print(item1, "+", item2, "=", item1 + item2)
   print()


## 
list1 = ["I am ", "You are "]
list2 = ["Mamun", "Happy", "Nondita", "Fine"]

size1 = len(list2)

for item in list1:

   print(f"start outer for loop = {item}")

   i = 0
   while i < size1:
      print(item, list2[i])
      i += 1
   print("end for loop")



###########################################################
# Enumerate() in Python
"""
The enumerate() function in Python is used to iterate over an iterable while keeping track of both the index and the value.
It returns pairs in the form(index, element).
This removes the need to manually maintain a counter variable during iteratioin.

"""
# Syntax: enumerate(iterable, start=0)
##
name = ["Python", "Java", "C++"]
for i, v in enumerate(name):
   print(i, v)


## 
a = ["A", "B", "C"]
r = tuple(enumerate(a))
print(r)

a = ["A", "B", "C"]
r = list(enumerate(a))
print(r)

a = ["A", "B", "C"]
r = set(enumerate(a))
print(r)

a = ["A", "B", "C"]
r = dict(enumerate(a))
print(r)


##
a = ["x", "y", "z"]
e = enumerate(a)

print(next(e))
print(next(e))
print(next(e))


##
d = {"a": 10, "b": 20}
for i, (k, v) in enumerate(d.items()):
   print(i,"=", k,"=", v)

#Note: enumerated(d.items()) returns index with(key, value) pairs.


