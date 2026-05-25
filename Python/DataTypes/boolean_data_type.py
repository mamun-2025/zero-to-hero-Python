
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


##### Boolean Operators 
"""
Boolean Operations in Python are simple arithmetic of True and False values.
These values can be manipulated by the use of boolean operators which include AND or and NOT.
Common boolean operations are-
1. or 
2. and 
3. not
4. == (equivalent)
5. != (not equivalent)
"""

# 1. Boolean OR Operator
# Boolean or operator returns True if any of the inputs is True else returns False.
a = 5
b = 2
c = 8

if a > b or b < c:
   print("True")

"""
Explanation:
The condition a > b or b < c uses the or operator, which returns True if any one of the conditions is True.
a > b is True because 5 > 3 and b < c is also True because 3 < 8.
Since at least one condition is True, the if block executes and "True" is printed.
"""

# 2. Boolean And Operator
# Boolean operator returns False if any one of the inputs is False else returns True.
a = 0
b = 2
c = 4

if a > b and b < c:
   print(True)
else:
   print(False)

if a and b and c:
   print("True")
else:
   print("False")

"""
Explanation:
In the first part, the condition a > b and b < c evaluates to False because a > b is False, causing the else block to print False.
In the second part, a is 0 (which is considered False), so the entire condition evaluates to False and the else block prints "False".
"""

# 3. Boolean Not Operator
# Boolean Not operator only requires one argument and returns the negation of the argument i.e returns the True for False and False for True.
a = 0
if not a:
   print("False")

"""
Explanation:
The not operator inverts the Boolean value of the expression.
Since a = 0 (which is considered False), not a evaluates to True.
As a result, the condition if not a is true and the program prints "Boolean value of a is False".
"""

# 4. Boolean equivalent (==) and not equivalent(!=) Operator
"""
Both operators are used to compare two results. '==' equivalent operator returns True if two results are equal 
and '!=' not equivalent operator returns True if the two results are not same.
"""
a = 0
b = 1

if a == 0:
   print(True)

if a == b:
   print(True)

if a != b:
   print(True)


# 5. Python is Operator
"""
is keyword is used to test whether two variables belong to the same object. 
The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal.
"""
x = 10
y = 11

if x is y:
   print(True)
else:
   print(False)


# 6. Python in Operator
"""
in operator checks for the membership i.e. checks if the value is present in a list, tuple, range, string, etc.
"""
a = [1, 2, 2]

if 1 in a:
   print(True)

