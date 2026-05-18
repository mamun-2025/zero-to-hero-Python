
# Indentity Operators
"""
The Identity Operators are used to compare the objects if both objects are actually of same data type and share same memory location.
There are different indentity operators such as:
"""

# 1. IS Operator
n1 = 5
n2 = 5
print(n1 is n2) # integers

a = [1, 2, 3]
b = [1, 2, 3]
c = a 
print(a is b) # lists
print(a is c) # reference

s1 = "hello world"
s2 = "hello world"
print(s1 is s2) # strings


# 2. IS NOT Operator
n1 = 5
n2 = 5
print(n1 is not n2) # integers

a = [1, 2, 3]
b = [1, 2, 3]
c = a 
print(a is not b) # lists
print(a is not c) # reference

s1 = "hello world"
s2 = "hello world"
print(s1 is not s2) # strings




# 3. Differnce between == and is operator in Python
# == Operator (Equality Operator)
x = [1, 2, 3]
y = [1, 2, 3]
z = x 

if x == y:
   print("x and y have the same values")
else:
   print("x and y do not have the same values.")


# is operator (Identity Operator)
x = [1, 2, 3]
y = [1, 2, 3]
z = x 

# case 1: x and y
if x is y:
   print("X and y are the same objects")
else:
   print("x and y are not the same object")


# case 2: x and z 
if x is z:
   print("x and z are the same object.")
else:
   print("x and z are not the same object.")

