

## Global and Local Variables in Python
"""
Variable store data in memory and scope defines the specific region of a program where a variable i accessible.
It dictates the visibility and lifetime of the variable within the source code.
Variables are categorized into two primary scopes: Global and Local.

"""
## 1. Local Variables
"""
Local Variables are defined inside a function and exist only during its execution.
They cannot be accessed from outside the function.

"""

# একটি ভেরিয়েবল কোডের কোন কোন জায়গা থেকে অ্যাক্সেস করা যাবে, তা নির্ধারণ করে Scope।

# Local Scope: ফাংশনের ভেতরে তৈরি করা ভেরিয়েবল শুধু ওই ফাংশনের ভেতরেই কাজ করে।
# Global Scope: ফাংশনের বাইরে তৈরি করা ভেরিয়েবল পুরো কোডের যেকোনো জায়গা থেকে অ্যাক্সেস করা যায়।

##
global_var = "I am global scope."

def my_function():
   local_var = "I am local scope."
   print(local_var)
   print(global_var) # See global scope inside the function.

my_function()
# print(local_var) # it's error because don't get local variable from the outside.

   

# print(my_function(local_var))
## 
def greet():
   msg = "Hello from the inside the function!"
   print(msg)

greet()

##
def greet():
   msg = "Hello!"
   print("Inside function:", msg)

greet()
# print("Outside function:", msg) # NameErrr: name 'msg' is not defined.


## 2. Global Variables
msg = "Python is awesome."
def display():
   print("Inside function: ", msg)

display()
print("Outside function: ", msg)


## 3. Use of Local and Global variables 
def func():
   s = "Me too"
   print(s)

s = "I love coding"
func()
print(s)


## 4. Modifying Global Variables inside a function
s = "Python is great!"
def fun():
   global s 
   s += " GFG" # Modify Global Variable 
   print(s)
   s = "Look for GeeksforGeeks Python Section" # Reassign global
   print(s)

fun()
print(s)


## 5. Global vs Local with Same Name
a = 1 # Global variable 

def f():
   a = 2 
   print("f(): ", a) # Uses global a

print("global:", a)
f()

#___________#
def g():
   a = 2
   print("g(): ", a) # Local shadows global

print("global:", a)
g()

#__________#
def h():
   global a
   a = 3 # Modifies global a 
   print("h(): ", a) 

h()
print("global:", a)


## 6. Global Keyword in Python
x = 10
def fun():
   global x 
   x = 20
  

fun()
print(x)

#__________#
a = 15
b = 10

def add():
   c = a + b 
   print(c)

add()

#________#
a = 15
def change():
   global a
   a = a + 15 
   print(a)

change()
print(a)


#________#
a = [10, 20, 30]

def fun():
   for item in range(len(a)):
      a[item] + 10 

print("before", a)
fun()
print("After", a)  


#_______#
a = [10, 20, 30]
def func():
   global a 
   a = [1, 2, 3]

print("Before:" , a)
func()
print("After: ", a)


## 7. Global in Nested functions
def add():
   x = 15
   def change():
      global x 
      x = 20
   print("Before changing:", x)
   print("Making Change")
   change()
   print("After changing:", x)


add()
print("Value of x outside:", x)
