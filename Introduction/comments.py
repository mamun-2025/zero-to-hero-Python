
# Comments in Python are the lines in the code that are ignored by the interpreter during the execution of the program. 
# 1. It enhance the readability of the code 
# 2. It can be used ot identify functionality or structure the code-base.
# 3. It can help understanding unusual or tricky scenarios handled by the code to prevent accidental removal or changes.
# 4. It can be used to prevent executing any specific part of your code, while making changes or testing.

# 1. Single Line Comments:
# sample comment
name = "geeksforgeeks"
print(name)



# 2. Multi-line Comments:
# Python does not provide the option for muliline comments.
# However, there are different ways through which we can write muliline comments.
# A multiline comment in Python is a comment that spans multiple lines, used to provide detailed explanations, disable large sections of code, or improve code readability.
# Python does not have a dedicated syntqasx for multiline comments, but developers typically use on of the following approaches:
# It help to improve code readability, provide documentation, enhance collaboration, Aids in debugging. 
# Types of Multline Comments

# 1. #symbol
# Using multiple #symbols on separate lines is the most efficient and Pythonic way to write multiline comments.
# This is a multiline comment
# Each line starts with#
# This method is efficient and preferred
print("Geeks For Geeks") # Inline comment
# Explanation: Here, the first three lines contain a hash charqacter(#) and the interpreteer prevents the three lines from execution. The it prints the "Geeks For Geeks" and finally, it will prevent the #line from execution.

# 2. Triple Quotes(''' or """)
# In Python, triple quotes let us write strings that span multiple lines, using either three single quotes(''') or three double quotes(""").
# While they're most often used in docstrings (the text that explains how code works) , they also have other features that can be used in a variety of situations Example:
s = """
Line 1
Line 2
Line 3
"""
print(s)
# Explanation: triple quotes let you write a string across multiple lines without using newline characters(\n)
# Note: Triple quotes are docstrings or multi-line docstrings and are not considered comments according to official Python documentation.

# 1. Triple single quotes:
s = '''This is
a triple-quoted 
string.'''
# 2. Triple double quotes:
s = """This is 
also a triple-quoted
string."""

# 3. Triple quotes for String creation:
# We can also declare strings in python using triple quote. Here's an example of how can declare string in python using triple quote.
# Example:
s1 = '''I '''
s2 = """am a """ 
s3 = """Mamun."""
print(type(s1))
print(type(s2))
print(type(s3))
print(s1 + s2 + s3) 
# Exaplanation: 
# Even though the strings are declared with triple quotes, they behave exactly like normal strings. The + operator concatenates them.

# 4. Triple quotes for Docstrings
# Docstrings are string literals that appear as the first statement ina function, class, or mudule.
# These are used to explain what the code does and are enclosed in triple quotes.
# Example:
def msg(name):
   """Greets the person with the given name."""
   print(f"Hello, {name}")

str = "Habib"
msg(str)
result = msg("Mamun")
# Explanation:
# In this example, the string"""Greets the person with the given name.""" is the docstring for the msg function.

## Accessing Docstrings:
# Docstrings can be accessed using the __doc__ attribute or the built-in help() function.
def area(radius):
   """Calculates the area of a circle given its radius."""
   import math 
   return math.pi * radius ** 2

print(area.__doc__)
help(area)

# Explanation:
# area.__doc__ returns the docstring associated with the area() function.
# help() function displays the docstring along with the function signature.
def fun():
   """This function demonstrates docstrings."""
   return None 

print(fun.__doc__)
print("\n")
# Python allows the use of triple single (''') or triple double (""") quotes to define multi-line strings. Although these are technically string literals and not comments, they can be used as comments if they are not assigned to a variable.
# This triple-quoted strings are ignored by Python if not assigned to a variable.
# This method is widely used for docstrings

# 4. help() function
help(print)

# 5. \method
# Backslash Method for commenting out multiple lines in Python is an unconvesational and lesser-known approach.
# It involves using the line continuation character(\) to extend a statement across multiple lines, effectively preventting Python from executing the code.
# Example:
# In Python, a backslash(\) is used to indicate that a statement continues on the next line. If you use a backslash at the end of multiple lines without forming a valid statement, Python will treat it as incomplete and ignore it.
# Using backslash for multiline comments
# This is a long comment \
# that spans multiple lines \
# using the backslash continuation method.
