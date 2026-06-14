
"""
ডেকোরেটর হলো এমন একটি ফাংশন যা অন্য কোনো ফাংশনের মূল কোড পরিবর্তন না করেই 
তার কাজের ধরণ বা বৈশিষ্ট্য বাড়িয়ে দেয় (Modify করে)। 
এটি মূলত Closure এবং Higher Order Function এর কনসেপ্ট মিলিয়ে তৈরি।
Decorator আসলে Closure-এর Real World Application।

## Decorators in Python:
Decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.
- A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality. 
- They are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reausable way.

"""

# Step 1: Decorator ছাড়া
def greet():
   print("Hello")

greet()

"""
এখন তুমি চাইছো:
Before
Hello
After

কিন্তু greet() এর code পরিবর্তন করতে চাও না।

"""

# Step 2: Function কে Argument হিসেবে পাঠানো
def greet():
   print("Hello")

def display(func):
   func()

display(greet)
"""
এখানে

greet
একটা function হিসেবে pass হচ্ছে।

এটাই First Class Function + Higher Order Function।

"""

# Step 3: Extra Behavior যোগ করা
def display(func):

   print("Before")

   func()

   print("After")

def greet():
   print("Hello")

display(greet)


##
def greet():
   print("Hello")

def display(func):
   
   print("Before")

   func()

   print("After")

display(greet)


# Step 4: New Function Return করা
# Decorator-এর আসল শুরু এখানে।
def decorator(func):

   def wrapper():

      print("Before")

      func()

      print("After")

   return wrapper

def greet():
   print("Hello")

new_function = decorator(greet)

"""
decorator(greet)

        ↓

wrapper()

        ↓

remember func = greet


এখানে wrapper হলো Closure।
কারণ wrapper মনে রাখছে:
func

"""


# Step 5: Function call
def decorator(func):

   def wrapper():
      print("Before")

      func()

      print("After")

   return wrapper

def greet():
   print("Hello")

new_function = decorator(greet)
new_function()
"""
Flow:

wrapper()

   ↓

Before

   ↓

func()

   ↓

greet()

   ↓

Hello

   ↓

After

"""

# Step 6: @decorator আসলে কী?
@decorator
def greet():
   print("Hello")

# Python ভিতরে ভিতরে এটাকে লিখে:
def greet():
   print("Hello")

greet = decorator(greet)

"""
1. এখন greet আর original greet না।

greet এখন:

wrapper function
কে point করছে।

Visual

আগে:
greet
  ↓
original function

পরে:
greet
  ↓
wrapper

wrapper-এর ভিতরে:
remembered func
      ↓
original greet


2. সবচেয়ে Important Diagram
@decorator

greet()
    ↓

wrapper()
    ↓

Before

    ↓

original greet()

    ↓

Hello

    ↓

After

"""

# Step 7: Parameters Problem
"""
এই Decorator কাজ করবে:

def greet():
    print("Hello")

    
কিন্তু এটা কাজ করবে না:

def add(a, b):
    return a + b

কারণ wrapper কোনো argument নেয় না।
Error

add(5, 3)
Python বলবে:

wrapper() takes 0 positional arguments

"""
# Solution:
def decorator(func):

   def wrapper(*args, **kwargs):

      print("Before")

      result = func(*args, **kwargs)

      print("After")

      return result

   return wrapper

@decorator
def add(a, b):
   return a + b 

print(add(5, 3))

"""
add(5,3)

    ↓

wrapper(5,3)

    ↓

func(5,3)

    ↓

original add(5,3)

    ↓

8

    ↓

return 8



1. Decorator = Wrapper

Decorator-এর সবচেয়ে সহজ Definition:

Decorator হলো এমন Function
যা অন্য Function কে Wrap করে
এবং Extra Behavior যোগ করে।

2. Interview Definition
A decorator is a higher order function that takes a function, wraps it inside another function,
adds extra behavior, and returns the wrapped function.


"""

# Step 8: Decorator Formula
"""
Function
    ↓
Pass to Decorator
    ↓
Decorator Creates Wrapper
    ↓
Wrapper Remembers Original Function
    ↓
Wrapper Returned
    ↓
@decorator replaces original function


অথবা এক লাইনে:
Decorator = Higher Order Function + Closure + Wrapper Function

"""

# Example 1: Before & After Execution
# সবচেয়ে Basic Decorator
def decorator(func):
   
   def wrapper():
      
      print("Before")

      func()

      print("After")

   return wrapper

@decorator
def greet():
   print("Hello")

greet()


# Example 2: Logging Function Calls
def logger(func):
   
   def wrapper():
      print(f"Calling {func.__name__}")

      func()

   return wrapper

@logger
def greet():
   print("Hello") 

greet()


# Example 3: Function With Parameters
def decorator(func):
   
   def wrapper(*args, **kwargs):
      print("Running Function")

      return func(*args, **kwargs)
   
   return wrapper

@decorator
def add(a, b):
   return a + b 

print(add(5, 3))


# Example 4: Execution Time Measure
import time 
def timer(func):
   
   def wrapper(*args, **kwargs):
      
      start = time.time()

      result = func(*args, **kwargs)

      end = time.time()

      print("Time:", end - start)

      return result 
   
   return wrapper

@timer 
def task():
   time.sleep(2)

task()


# Example 5: Authentication Decorator
is_logged_in = True
def login_required(func):
   
   def wrapper():
      
      if not is_logged_in:
         print("Access Denied")
         return
      
      return func() 
   
   return wrapper

@login_required
def dashboard():
   print("Dashboard")

dashboard()


# Example 6: Admin Permission Check
role = "admin"
def admin_only(func):

   def wrapper():

      if role != "admin":
         print("Permission Denied")
         return

      return func()

   return wrapper

@admin_only
def delete_user():
   print("User Deleted.")


delete_user()    
      
      
# Example 7: Count Function Calls 
def count_cals(func):

    count = 0

    def wrapper():
       
       nonlocal count

       count += 1

       print("Call Number:", count)

       return func()
    
    return wrapper

@count_cals
def hello():
   print("Hello Chatgpt")

hello()
hello()
hello()
# এখানে Closure + Decorator একসাথে।


# Example 8: Repeat Function Multiple Times
def repeat(func):
   
   def wrapper():
      
      for _ in range(10):
         func()

   return wrapper


@repeat
def greet():
   print("Hello")

greet()


# Example 9: Cache Result
# একই Calculation বারবার না করার জন্য।
def cache(func):

    memory = {}

    def wrapper(n):
       
       if n in memory:
          print("From Cache")
          return memory[n]
       
       result = func(n)

       memory[n] = result

       return result
    
    return wrapper

@cache
def square(n):
   print("Calculating")

   return n * n 

print(square(5))
print(square(5))
   

# Example 10: functiontools.wraps
def logger(func):

   def wrapper():

      print("Before")

      func()

   return wrapper

@logger
def greet():
   print("Hello")

print(greet.__name__)
"""
এখন দেখি:
print(greet.__name__)

Output:
wrapper

কিন্তু Function-এর নাম তো:
greet
হওয়ার কথা।

কারণ Decorator apply হওয়ার পর:
greet = logger(greet)
হয়ে গেছে।

এখন greet আসলে:
wrapper function
কে point করছে।

Visual
আগে:
greet
 ↓
original greet

পরে:
greet
 ↓
wrapper

তাই:
greet.__name__

দেখায়:
wrapper

"""
# Solution:
from functools import wraps

def logger(func):

   @wraps(func)
   def wrapper():

      print("Before")

      func()

   return wrapper

@logger
def greet():
   print("Hello")

print(greet.__name__)

"""
কী করে?
@wraps(func) original function-এর metadata copy করে।

যেমন:
__name__
__doc__
__module__

ইত্যাদি।
"""


from functools import wraps

def logger(func):

   @wraps(func)
   def wrapper():

      return func()
   
   return wrapper

@logger
def greet():
   """This is greet function"""
   print("Hello")

print(greet.__doc__)

"""
Backend-এ কেন Important?

ধরো:

FastAPI
Django
Flask

Framework গুলো function metadata দেখে।

যদি wraps ব্যবহার না করো:
API docs
Debugging
Logging
Testing
Introspection

সমস্যা হতে পারে।

Rule:
Decorator লিখলে প্রায় সবসময়
@wraps(func)
ব্যবহার করবে।

"""



# # Example 11: Decorator With Arguments

"""
Normal Decorator:
@logger
def greet():
   pass

Equivalent: greet = logger(greet)


কিন্তু আমরা চাই:
@repeat(3)
def greet():
   pass
   
মানে:
Decorator-এরও parameter আছে
   
"""

from functools import wraps

def repeat(times):

   def decorator(func):

      @wraps(func)
      def wrapper():

         for _ in range(times):
            func()

      return wrapper
   
   return decorator

@repeat(3)
def greet():
   print("Repeat 3 times")

greet()
"""
Flow Diagram

Decorator apply হওয়ার সময়:

@repeat(3)

      ↓

repeat(3)

      ↓

times = 3 remembered

      ↓

return decorator

তারপর:

decorator(greet)

      ↓

func = greet

      ↓

return wrapper

তারপর:

greet()

      ↓

wrapper()

      ↓

for loop

      ↓

greet()

      ↓

3 times
Memory View
wrapper

 remembers:

 times = 3

 func = greet
"""

## 1. Role Check
from functools import wraps

user_role = "admin"

def require_role(role):

   def decorator(func):

      @wraps(func)
      def wrapper():

         if user_role != role:
            print("Access Denied")
            return 

         return func()
      
      return wrapper
   
   return decorator

@require_role("admin")
def delete_user():
   print("User Deleted")

delete_user()


## 2. Retry Decorator:
from functools import wraps

def retry(times):

   def decorator(func):

      @wraps(func)
      def wrapper():

         for _ in range(times):
            func()

      return wrapper

   return decorator

@retry(3)
def greet():
   print("Hello")

greet()


## 3. Decorator with Arguments Formula
def decorator_args(data):

   def decorator(func):

      @wraps(func)
      def wrapper(*args, **kwargs):

         return func(*args, **kwargs)
      
      return wrapper
   
   return decorator
"""
মনে রাখো:

Normal Decorator:

Function
   ↓
Decorator
   ↓
Wrapper


Decorator With Arguments:

Arguments
    ↓
Decorator
    ↓
Function
    ↓
Wrapper

"""

# 4.
def repeat(times):

    def decorator(func):
       
       def wrapper():

            for _ in range(times):
               func()

       return wrapper
    
    return decorator

@repeat(3)
def greet():
   print("Hello")

greet()


"""
1. Decorator-এর Foundation:

Decorator বুঝতে হলে এই Flow মাথায় রাখতে হবে:

Function
   ↓
First Class Function
   ↓
Higher Order Function
   ↓
Inner Function
   ↓
Closure
   ↓
Decorator


তাই Decorator আসলে নতুন কিছু না।
এটা হলো:

Higher Order Function
+
Closure
+
Wrapper Function
=
Decorator


2. Decorator চিনার Shortcut

যখন দেখবে:

def decorator(func):

    def wrapper():
        func()

    return wrapper

তখন বুঝবে:
✅ decorator = Higher Order Function
কারণ function receive করছে।

✅ wrapper = Closure
কারণ func variable মনে রাখছে।

✅ return wrapper
কারণ নতুন function return করছে।

3. Decorator কী?
A decorator is a higher-order function that takes another function as an argument, 
wraps it insdie another function, adds additional behavior, and returns the wrapped function.

"""
