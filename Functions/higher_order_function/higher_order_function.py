

"""
Higher Order Functions in Python
- In Python, Higher Order Functions(HOFs) play an important role in functional programming and allow for writing more modular, reusable and readable code.
A Higher-Order Function is a function that either:
1. Takes another function as an argument.
2. Returns a function as a result.

"""
# 1. Higher Order Function
# যে ফাংশন অন্য একটি ফাংশনকে আর্গুমেন্ট (Argument) হিসেবে গ্রহণ করে 
# অথবা অন্য কোনো ফাংশনকে রিটার্ন (Return) করে, তাকে Higher Order Function বলে।
def transform(func, text):
   # এখানে 'func' একটি ফাংশন যা আর্গুমেন্ট হিসেবে এসেছে
   return func(text)

def lowercase(text):
   return text.lower()

# transform একটি Higher Order Function কারণ এটি lowercase ফাংশনকে ইনপুট হিসেবে নিয়েছে
result = transform(lowercase, "HELLO PYTHON")
print(result)

##
def greet(func):
   return func("hello")

def uppercase(text):
   return text.upper()

print(greet(uppercase))


##
def apply(func, x):
   return func(x)

def square(n):
   return n * n 

result = apply(square, 5)
print(result)
"""
Explanation:

apply(func, x) takes another function as an argument.
square(n) computes the square of n.
apply(square, 5) executes square(5), resulting in 25.

"""


##
def greet():
   print("Hello")

def execute(func):
   func()
   
execute(greet)

"""
একটি Function আরেকটি Function Receive করছে।

তাই:
execute
একটি Higher Order Function।

"""

# 2: HOF-এর দুই ধরনের
"""
Type 1
Function Receive করে

def execute(func):
    func()


Type 2
Function Return করে

def outer():
    return inner

"""
# 3. Real Example 
def square(x):
   return x * x 

numbers = [1, 2, 3, 4]

result = list(map(square, numbers))

print(result)

# 4. Lambda including
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x ** x, numbers))

print(result)


# 5. Function Return 
def outer():

   def inner():
      print("Function Return")

   return inner 

result = outer()
result()

## 
# Higher Order Function returning a function 
def fun(n):
   return lambda x: x *n 

double = fun(2)
tripple = fun(3)

print(double(5))
print(tripple(5))
"""
Explanation:

fun(n) returns a lambda function that multiplies a number by n.
double and triple are function instances that multiply by 2 and 3, respectively.
Calling double(5) results in 5 * 2 = 10 and triple(5) results in 5 * 3 = 15.

"""


# 6. Real backend Example
def login_required(func):

   def wrapper():
      print("Checking Login")

      func()

   return wrapper

def dashboard():
   print("Dashboard")

secure_dashboard = login_required(dashboard)
secure_dashboard()



# 7. HOF কোথায় কোথায় ব্যবহার হয়?
"""
map()
map(func, iterable)
"""
a = [1, 2, 3, 4]
res = list(map(lambda x: x ** 2, a))
print(res)



"""
filter()
filter(func, iterable)
"""
a = [1, 2, 3, 4, 5, 6]
res = list(filter(lambda x: x % 2 == 0, a))
print(res)



"""
sorted()
sorted(data, key=func)
"""
a = ["Python", "Java", "JavaScript"]
res = sorted(a, key=len)
print(res)


"""
min()
min(data, key=func)

max()
max(data, key=func)

reduce()
reduce(func, data)

সবগুলোই Higher Order Function।

"""


# 8. Application of Higher Order functions
"""
They are widely used in functiona programming, closures, decorators
and callbacks to improve code modularity, resuability and abstractiion. 

"""
# Using closure and Using decorator
