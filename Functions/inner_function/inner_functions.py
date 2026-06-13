
## Python Inner Functions 
"""
In Python, an inner fuction(also called a nested function) is a function defined inside another function.
They are mainly used for:
- Encapsulation: Hiding helper logic from external access.
- Code Organization: Grouping related functionality for cleaner code.
- Access to Outer Variables: Inner functions can use variables of the enclosing(outer) function.
- Closures and Decorators: Supporting advanced features like closures (functions that remember values) and function decorators.

"""
# 1. Inner Function কী?
# একটি function-এর ভিতরে আরেকটি function তৈরি করলে তাকে Inner Function বলে।
def outer():

   def inner():
      print("I am Inner Function.")

   inner()

outer()

# 2. Inner Function কেন ব্যবহার করি?
# বাইরের function-এর data ভেতরের function ব্যবহার করতে পারে।
def outer():
   message = "Hello Python!"

   def inner():
      print(message)

   inner()

outer()

##
def outer_function():
   msg = "Hello Mamun"

   def inner_function():
      print(msg)

   inner_function()

print(outer_function())

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


# 3. Outer variable Access
# Inner Function Outer Variable Access করতে পারে।
def outer():

   name = "Mamun"

   def inner():
      print("Hello", name)

   inner()

outer()


# 4. Multiple Inner Functions:
def outer():

   def add():
      print("Addition.")
   
   def subtract():
      print("Subtration")

   add()
   subtract()

outer()


# 5. Inner Function Return
# এখান থেকেই Closure শুরু হবে।
def outer():

   def inner():
      print("Hello")

   return inner

result = outer()
result()

def outer():

   def inner():
      print("Hello! Closure.")

   return inner

result = outer()
result()


# 6. Parameter Use
## 
## 
def func1(a):
   
   def func2():
      print(a)

   return func2

closure_func = func1("Hello, Closure!")
closure_func()

##
def outer(name):

   def inner():
      print("Hello", name)

   return inner 

greet = outer("Parameter")
greet()
"""
Memory Picture
greet = outer("Mamun")

Outer শেষ হয়ে গেছে।

তবুও:
name = "Mamun"
মনে আছে।

কারণ inner function এটা ধরে রেখেছে।

এটাই Closure-এর শুরু।

"""

# 7. Real Life Example 
def calculator():

   def add(a, b):
      return a + b 
   
   return add 

calc = calculator()

print(calc(10, 20))


# 8. Most Important Example 
def outer():

   count = 0

   def inner():
      print(count)

   return inner 

show = outer()
show()
"""
প্রশ্ন:

Outer Function তো শেষ হয়ে গেছে।
তাহলে count কোথা থেকে আসলো?
কারণ Inner Function count-কে ধরে রেখেছে।
এই ধারণাটাই পরে Closure হবে।

"""

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
def process_data(data):

   def clean_data():
      return [item.strip() for item in data]
   
   return clean_data()

print(process_data([" Python ", " Inner Function"]))
"""
এটা কেন Inner Function?

কারণ
clean_data() = ফাংশনটা শুধু

process_data() এর ভেতরে দরকার।
বাইরে দরকার নেই।

Backend-এ এরকম দেখবে:
def create_user(data):

   def validate():
      pass 
   def save()
      pass 
      
   validate()
   save()

এটা এখন মুখস্থ করার দরকার নেই।
শুধু বুঝো:
Inner Function Helper Function হিসেবেও ব্যবহার করা যায়।

"""


