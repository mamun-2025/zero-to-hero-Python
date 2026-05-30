

# In python, certain values are considered "truthy" or "falsy" when evaluated in a boolean context.
number = 7
if number:
   print("The number is truthy.")

number = 0
if number:
   print("This will not be printed because 0 is falsy.")

# 1. Truthy values include:
# - Non-zero numbers (1, -4, 3.5)
# - Non-empty strings ("Hello", "0")
# - Non-empty lists ([1, 2, 3])
# - Non-empty dictionaries ({"key": "value"})

if "Hello":
   print("This string is truthy.")

if [1, 2, 3]:
   print("This list is truthy.")

if {"key": "value"}:
   print("This dictionary is truthy.")

if -4:
   print("This negative number is truthy.")

if 3.5:
   print("This float is truthy.")


# 2. Falsy values include:
# - Zero (0, 0.0)
# - Empty strings ("")
# - Empty lists ([])
# - Empty dictionaries ({})
# - None 

if 0:
   print("This will not be printed because 0 is falsy.")

if "":
   print("This will not be printed because an empty string is falsy.")

if []:
   print("This will not be printed because an empty list is falsy.")

if {}:
   print("This will not be printed because an empty dictionary is falsy.")

if None:
   print("This will not be printed because None is falsy.")


# 3. 
# Understanding truthy and falsy values is important for writing conditional statements and controlling the flow of your program effectively.
number = 7
number2 = 4

if number % 2 == 0:
   print(number, "The number is even.")
else:
   print(number, "The number is odd.")

if number2 % 2 == 0:
   print(number2,"The number is even.")
else:
   print(number2, "The number is odd.")


# 4. Built-in boolean function
# You can use the built-in bool() function to check the truthiness of a value.

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))
print(bool([]))
print(bool([1, 2, 3]))
print(bool({}))
print(bool({"key": "value"}))
