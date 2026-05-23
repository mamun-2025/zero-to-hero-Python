
## Python Boolean
"""
Python Boolean type is one of the built-in data types provided by Python,
which represents one of the two values i.e. True or False.
Generally, it is used to represent the truth values of the expression.
"""
##### 1. Python Boolean Type
a = True
print(type(a))

b = False
print(type(b))



##### 2. Evaluate Variables and Expressions
"""
We can evaluate values and variables using the Python bool() function.
This method is used to return or convert a value to a Boolean value i.e, True or False, 
using the standard truth testing procedure.
"""
# bool() function
# Returns False as x is None
x = None
print(bool(x))

# Returns False as x is an empty sequence 
x = ()
print(bool(x))

# Returns False as x is an empty mapping
x = {}
print(bool(x))

# Returns False as x is 0
x = 0.0
print(bool(x))

# Returns True as x is a non empty string
x = "Geeks for Geeks"
print(bool(x))


##### Integers and Floats as Boolean
"""
In python, integers and floats can be used as Boolean values with the bool() function.
Any number with a value of zero (0, 0.0) is considered False while any non-zero number (positive or negative) is considered True.
"""
var1 = 0
print(bool(var1))

var2 = 1 
print(bool(var2))

var3 = -9.7
print(bool(var3))
