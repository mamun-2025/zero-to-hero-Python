
## Python Functions
"""
Python functions are reusable blocks of code used to perform a specific task.
They help organize programs into samller sections and execute the same logic whenever needed by calling the function.

"""
## Python def Keyword
"""
The def keyword is used to define user-defined functions.
Functions help organize code into reusable bloks, making programs easier to read, maintain, and reuse. 
They can accept input values through parameters, perform specific tasks and optionally return results.

"""

# ১. Basic Function (মৌলিক ফাংশন)
# ফাংশন হলো কোডের একটি ব্লক, যা নির্দিষ্ট একটি কাজ করে এবং প্রয়োজন অনুযায়ী বারবার ব্যবহার করা যায়।
# def কীওয়ার্ড দিয়ে ফাংশন তৈরি করা হয়।
# ফাংশনের নাম দেওয়ার পর বন্ধনী () দিতে হয়।


## 2. Defining a Function
def fun():
   print("Welcome to GeeksforGeeks")

##
def func(name):
   print("Hello,", name)

func("Nondita")



## 3. Calling a Function
def fun():
   print("Welcome to GeeksforGeeks")

fun()

## 
def greeting():
   print("Hello, Welcome to python function!")

greeting()


## 
def greet(name, age):
   print(name, age)

greet("Mamun", 25)


##
def func():
   print("Hello")

func()
# Exaplanation: 
# def func(): Defines a function named func.
# print("Hello"): Code inside the function that runs when called.
# func(): Calls the function, printing Hello to the output.

# Syntax: 
"""
def function_name (parameters):
   # Code to execute
   return value # Optional

"""

## 4. Function Arguments
# ফাংশনের ভেতরে বাইরে থেকে কোনো ডেটা বা মান পাঠানোর জন্য যে ভেরিয়েবল ব্যবহার করা হয়, তাকে Parameter বলে। 
# আর কল করার সময় যে আসল মান পাঠানো হয়, তাকে Argument বলে।

def greet_user(name): # 'name' is a parameter
   return f"Hello {name}, How are you ?"

print(greet_user("Mamun")) # 'Mamun' is a argument

# Syntax:
"""
def function_name(arguments):
   # function body
   return value

"""


##
def subtract(x, y):
   return (x - y)

a = 90
b = 50

result = subtract(a, b)

print("Subtraction of", a, "and", b, "is", result)


##
def evenOdd(x):
   if (x % 2 == 0):
      return "Even"
   else:
      return "Odd"
   
print(evenOdd(16))
print(evenOdd(7))



## 5. Types of Function Arguments
##
def myFunc(x, y=50):
   print("X: ", x)
   print("Y: ", y)

myFunc(10)

## 
def fun(name, age):
   print(name, "is", age, "Years old.")

fun(name = "Mamun", age = 30)

## 
def student(fname, lname):
   print(fname, lname)

student(fname="Mamun", lname="Bepari")


##
def nameAge(name, age):
   print("Hi", "I am", name)
   print("My age is ", age, "years old.")

nameAge(name="Mamun", age=30)



## 6. Function within Functions
def f1():
   s = "I love coding"
   def f2():
      print(s)

   f2()
f1()




## 7. Return statement
# ফাংশন তার কাজ শেষ করে কোনো ফলাফল বা মান যদি মূল কোডে ফেরত পাঠাতে চায়, তখন return ব্যবহার করা হয়। 
# return এক্সিকিউট হওয়ার সাথে সাথে ফাংশনের কাজ শেষ হয়ে যায়।
##
def add_numbers(a, b):
   result = a * b 
   return result 

total = add_numbers(10, 10) # Return value is kept a variable.
print(f"Total: {total}")

##
def value(num):
   return num**2

print(value(10))
print(value(5))

##
def fun(num):
   return num * num 

res = fun(5)
print(res)


