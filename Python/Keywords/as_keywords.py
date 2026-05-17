
# as keyword - Python
"""
as keyword in Python plays a important role in simplifying code,
making it more readable and avoiding potential naming conflicts.
It is mainly used to create aliases for modules, exceptions and file operations.
The powerful feature reduces verbosity, helps in naming clarity and can be essential 
when multiple modules have similar names or when managing file operations.
"""
import math as m 
print(m.sqrt(25))

# 1. Create alias for the module

# Import random moudle with alias
import random as mamun

# Using random module with alias to generate random numbers
a = mamun.randint(5, 10)
b = mamun.randint(1, 5)

# Printing the generated random numbers
print(a, b)


# 2. as with a file

# Using 'as' keyword with 'open' function
with open('open.txt') as file:
   
   # Reading text with alias
   mamun_file = file.read()

# Printing the text read from the file
print("Text read with alias: ")
print(mamun_file)


# 3. as in Except clause
try:
   import maths as mt 
except ImportError as err:
   print(err)


try:
   with open("geek.txt") as geek:
      geek_read = geek.read()

   print("Reading alias: ")
   print(geek_read)
except FileNotFoundError as err2:
   print("No file found.")