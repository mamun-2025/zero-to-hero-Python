
## First Class Functions in Python
"""
In python, functions are treated as first-class objects. 
This means they can used just like numbers, strings or any other variable.
You can:
- Assign functions to variables
- Pass them as arguments to other functions.
- Return them from functions
- Store them in data structures such as lists or dictionaries.

"""

# 1. Assigning Functions to Variables
def msg(name):
   return f"Hello, {name}"

f = msg
print(f("Mamun"))


# 2. Passing Functions as Arguments
def msg(name):
   return f"Hello, {name}"

def func1(func2, name):
   return func2(name)

# Passing the msg function as an argument
print(func1(msg, "Nondita"))


# 3. Returning Functions from Other Functions
##
def func1(msg):
   def func2():
      return f"Message: {msg}"
   return func2 

func = func1("Hello, World!")
print(func())

##
def outer():
   def inner():
      print("Hello")
   return inner

func = outer()
func()

##
def B():
   print("Inside method B")

def A():
   print("Inside method A")
   return B
func = A()
func()

## 
def calc(a, b):
   x = a + b 
   y = a - b 
   return lambda: x * y 

func = calc(5, 2)
print(func())

## 
def power(exp):
   return lambda num:  num ** exp 

square = power(2)
cube = power(3)

print(square(6))
print(cube(5))