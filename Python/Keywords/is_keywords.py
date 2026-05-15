
# Python is keyword
"""
The 'is' keyword in Python is used to test object identity.
The 'is keyword' is used to test whether two variables belong to the same object.
The test will return True if the two objects are the same else
it will return False even if the two objects are 100% equal.

Note: The == relational operator is used to test if two objects are the same.
"""

# 1. Compare List Elements using is keyword
x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"]

print(x is y)
print(x == y)

# 2. Python 'is' keyword in For Loop Expression
x = 10
y = 10

if x is y:
   print(True)
else: 
   print(False)
