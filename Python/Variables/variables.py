
"""
Variables are used to store data that can be referenced and manipulated during program execution.
A variable is essentially a name that is assigned to a value.
Unlike Java and many other languages, Python variables do not require explicit declaration of type.
Type of the variable is inferred based on the value assigned.
"""

x = 5 
name = "Mamun"
print(x)
print(name)

# (1). Rules for Naming Variables
# 1. Variable names can only contain letters, digits and underscores(_)
# 2. A variable name cannot start with a digit.
# 3. Variable names are case-sensitive like myVar and myvar are different.
# 4. Avoid using Keywords like if, else, for as variable names.

# Valid variables:
age = 25
_color = "Black"
total_score = 90

# Invalid variables:
# 1name = "Error" # starts with a digit
# class = 10 # 'class' is a reserved keyword
# user-name = "Jhon" # Contains a hyphen


# (2). Assigning Values to Variables
# Basic Assignment: Variables as assigned values using the = operator
x = 5
y = 3.14
z = "Hi"

# Dynamic Typing: Variables are dynamically typed, meaning the same variable can hold different types of values during execution.
x = 10
x = "Now a string"
print(x)

# Assigning same Value: allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
a = b = c = 100
print(a, b, c)

# Assigning Different Values: We can assign different values to multiple variables simultaneously, making the code concise and easier to read.
x, y, z = 1, 2.5, "Python"
print(x, y, z)


# (3). Concept of Object Reference
x = 5 # Garbage collection
y = x
x = "Geeks"
y = "Computer"
print(x)
print(y)
"""
Python creates yet another object for "Computer" and updates y to reference it.
The original object 5 no longer has any references and becomes eligible for garbage collection.
Python variables hold references to objects, not the actual objects themselves.
Reassigning a variable does not affect other variables referencing the same object unless explicitly updated.
"""
# shared reference and In-place changes
L1 = [1, 2, 3, 4, 5]
L2 = L1
L1[0] = 0
print(L1)
print(L2)

L1 = [1, 2, 3, 4, 5]
L2 = L1[:]
L1[0] = 0
print(L1)
print(L2)

L1 = [1, 2, 3, 4, 5]
L2 = L1 
print(L1 == L2)
print(L1 is L2)

L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, 5]
print(L1 == L2)
print(L1 is L2)

a = 50
b = 50
print(a == b)
print(a is b)


# Understanding variable Reassignment
x = 1
y = x 
y = y + 1
print(x)
print(y)
"""
Initially, both x and y reference the same object 1
When y = y + 1 is executed, python creates a new object 2
y now references this new object and x still references the original object 1
So, changing y does NOT affect x
"""

# (4). Type and Casting a Variable
"""
Type of a variable can be determine using type() function which returns the type of the object passed to it.
Type casting means converting the value of one data type into another. 
Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.
For example, int() converts compatible values to an integer, float() to a floating point number and str() to a string.
"""

# (5). deleting a Variable
'''
 We an remove a variable from the namesapce using the del keyword.
 This deletes the variable and frees up the memory it was using.
 The delete keyword in Python is used to delete objects like variables, lists, dictionary entires, or slices of a list.
 Since everything in Python is an object, del helps remove references to these objects 
 and can free up memory del Keyword removes the reference to an object. 
 If that object has no other references, it gets cleared from memory. 
 Trying to access a deleted variable or object will raise a NameError.
'''
# Del Keyword for Deleting Objects
class GFG_class:
   a = 20

# Creating instance of class
obj = GFG_class()

# delete object
del obj

# we can also delete class
del GFG_class


# Deleting Variables
a = 20
b = "GeeksforGeeks"

# delete both the variables
del a, b

# check of a and b exists after deleting
# print(a)
# print(b)

# List Slicing Using del Keyword
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete second element of 'a'
del a[1]
print(a)

# slice 'a' from index 3 to 5
del a[2:5]
print(a)

# Deleting Dictionary and Removing key-value Pairs
dict1 = {"name": "mamun", "age": 25, "blood": "B+"}

# delete key-value pair with key "blood" from dict1
del dict1["blood"]
print(dict1)

# (6). Swapping Two Variables
a, b = 5, 10
a, b = b, a 
print(a, b)

# Counting characters in a String
word = "GeeksforGeeks"
length = len(word)
print("Length of the word:", length)