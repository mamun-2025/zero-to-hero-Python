
# Membership Operators
"""
The Membership operators test for the membership of an object in a sequence, 
such as strings, lists or tuples.Python offers two membership operators to check
or variable the membership of a value. They are us follows:
"""
# 1. IN Operator
l = [1, 2, 3, 4, 5]
s = "Hello World"
d = {1: "Geeks", 2: "for", 3: "geeks"}

print(2 in l)
print("O" in s)
print(3 in d)

# 2. Not IN Operator
l = [1, 2, 3, 4, 5]
s = "Hello World"
d = {1: "Geeks", 2: "for", 3: "geeks"}

print(0 not in l)
print("H" not in s)
print(4 not in d)

# 3. Operator.contains() Method
import operator

print(operator.contains([1, 2, 3, 4, 5], 2)) # list
print(operator.contains("Hello World", "O")) # strings
print(operator.contains({1, 2, 3, 4, 5}, 6)) # set
print(operator.contains({1: "Geeks", 2: "for", 3: "geeks"}, 3)) # dictionary
print(operator.contains((1, 2, 3, 4, 5), 9)) # tuple