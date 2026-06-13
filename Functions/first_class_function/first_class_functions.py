
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
# পাইথনে ফাংশনকে "First Class Citizen" বা First Class Function বলা হয়। 
# এর মানে হলো, ফাংশনকে সাধারণ ভেরিয়েবলের মতোই ব্যবহার করা যায়— ভেরিয়েবলে অ্যাসাইন করা যায়, 
# অন্য ফাংশনের আর্গুমেন্ট হিসেবে পাঠানো যায়, 
# বা ফাংশন থেকে রিটার্ন করা যায়।
"""
First Class Function কী?

সহজ ভাষায়:
Python-এ Function-কে Variable-এর মতো ব্যবহার করা যায়।

অর্থাৎ Function কে:
Variable-এ রাখা যায়
Argument হিসেবে পাঠানো যায়
Function থেকে Return করা যায়
List/Dictionary-তে রাখা যায়

এই ক্ষমতা থাকলে Function-কে First Class Citizen বলা হয়।

"""
def shout(text):
   return text.upper()

result = shout
print(result("hello"))


"""
Step 1: Function একটি Object

def greet():
    print("Hello")

এখানে greet শুধু কোড না।
এটা একটি object।

প্রমাণ:
def greet():
    print("Hello")

print(greet)

Output:
<function greet at 0x...>

Python বলছে:
"greet হলো একটি function object"

"""


# 2. Assigning Functions to Variables
def greet():
   print("Hello Assign TO Variables.")

say_hello = greet # Function Store হলো। Function Run হয়নি।
say_hello()
say_hello = greet() # Function সাথে সাথে Run হবে।


##
def msg(name):
   return f"Hello, {name}"

f = msg
print(f("Mamun"))


# 2. Passing Functions as Arguments

def greet():
   print("execute(greet) means: func = greet after that: func() is greet()")

def execute(func):
   func()

execute(greet)

##
def square(x):
   return x * x 

numbers = [1, 2, 3]

result = map(square, numbers) # Function হিসেবে Argument 'square' গেছে।

print(list(result))


##
def msg(name):
   return f"Hello, {name}"

def func1(func2, name):
   return func2(name)

# Passing the msg function as an argument
print(func1(msg, "Nondita"))



# 3. Returning Functions from Other Functions
def outer():

   def inner():
      print("Hello starting the closure.")
   
   return inner 

result = outer() 
result()


##
def outer():

   def inner():
      print("Hello")
      
   return inner

func = outer()
func()


##
def func1(msg):

   def func2():
      return f"Message: {msg}"
   
   return func2 

func = func1("Hello, World!")
print(func())


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


# 4. Function List-এ রাখা
def add():
   print("Add")

def sub():
   print("Subtract")

operations = [add, sub]

operations[0]()
operations[1]()

# 5. Function Dictionary-তে রাখা
def add(a, b):
   return a + b 

def sub(a, b):
   return a * b 

operations = {
   "add": add, 
   "sub": sub
}

print(operations["add"](10, 5))
print(operations["sub"](10, 5))
           
# What is a first_class function
# A first-class function is a function that can be assgined to a variable, 
# passed as an argument, returned from another funcion, and stored in data stratures.


