
## Python Inner Functions 
"""
In Python, an inner fuction(also called a nested function) is a function defined inside another function.
They are mainly used for:
- Encapsulation: Hiding helper logic from external access.
- Code Organization: Grouping related functionality for cleaner code.
- Access to Outer Variables: Inner functions can use variables of the enclosing(outer) function.
- Closures and Decorators: Supporting advanced features like closures (functions that remember values) and function decorators.

"""
##
def func1(msg):
   def func2():
      print(msg)

   func2()

func1("Hello")

## 
def func1():
   msg = "Hi , Nondita! How are you?"
   def func2():
      print(msg)
   
   func2()

func1()

##
def func1():
   a = 45
   def func2():
      nonlocal a 
      a = 54
      print(a)
   
   func2()
   print(a)

func1()

## 
def func1(a):
   def func2():
      print(a)

   return func2

closure_func = func1("Hello, Closure!")
closure_func()

##
def process_data(data):
   def clean_data():
      return [item.strip() for item in data]
   return clean_data()

print(process_data([" Python ", " Inner Function"]))


##
import logging
logging.basicConfig(level=logging.INFO)


def logger(func):
   def wrapper(*args, **kwargs):
      logging.info(f"Excuting {func.__name__} with {args}, {kwargs}")
      return func(*args, **kwargs)
   
   return wrapper 

@logger
def add(a, b):
   return a + b 

print(add(3, 4))

