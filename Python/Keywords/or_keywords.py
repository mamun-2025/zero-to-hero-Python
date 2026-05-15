

# Python OR Keyword
"""
Python OR is a logical operator keyword. The OR operator returns True if at least
one of the operands becomes to be True.

Note:
In Python 'or' operator does npt return True of False.
The 'or' operator in Python returns the first operand if it is True else the second operand.
"""

age = 15
p = False

if age >= 18 or p:
   print("Access granted")
else:
   print("Access denied")

"""
Input 1	Input2	Output
True	   True	   True
True   	False    True
False	   True	   True
False	   False	   False

"""

# 1. Use of "or" in conditional Statements
a = 55
b = 33

if b > a :
   print("b is greater than a")
elif a == b:
   print("a and b are equal.")
else:
   print("a is greater than b")


# 2. Use of "or" in Loops
i = 0
name = "geeksforgeeks"

while i < len(name):
   if name[i] == "k" or name[i] == "f":
      i += 1
      break

   print(name[i])
   i += 1


# 3. Using "or" for Default Values
user = ""
cur_user = user or "Guest"

print(cur_user) # When user is empty

user = "geeks"
cur_user = user or "Guest"

print(cur_user) # When user is not empty