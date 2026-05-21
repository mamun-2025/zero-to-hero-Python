
# Python Data Types
"""
Data types are used to define the type of value stored in a variable.
They determine what kind of operations can be performed on the data.
In Python, everything is treated as an object and each value belongs to a specific data type.
"""
x = 50
x = 50.5
x = "Hello World"
x = ["Geeks", "for", "geeks"]
x = ("geeks", "for", "geeks")

# Numeric Data Types
"""
Numeric data types are used to store numeric values.
It can be an integer, floating number or even a complex number.
Python supports three main numeric types:
1. Integer: value is represented by int class. It contains positive or negative whole numbers(with fractions or decimals).
2. Float: value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point.
3. Complex: It is represented by a complex class. It stores numbers with real and imaginary parts. For example: 2 + 3j
"""
a = 5
b = 5.0
c = 2 + 4j
print(type(a))
print(type(b))
print(type(c))