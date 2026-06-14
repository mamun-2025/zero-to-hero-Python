
"""
1. Closure বুঝতে হলে আগে ৩টা জিনিস পরিষ্কার হতে হবে:

Nested Function (Function-এর ভিতরে Function)
First Class Function (Function return করা যায়)
Scope (Inner function outer variable access করতে পারে)


2. Closure কী?
যখন একটি Nested Function (ফাংশনের ভেতরের ফাংশন) তার বাইরের ফাংশনের (Outer Function) ভেরিয়েবলকে মনে রাখে— 
এমনকি বাইরের ফাংশনটির কাজ শেষ হয়ে যাওয়ার পরেও, তখন তাকে Closure বলে।

Closure হলো:

Function
    +
Remembered Variable
    =
Closure

অর্থাৎ একটা function শুধু function না, সাথে কিছু data-ও মনে রাখে।

"""

# Step 1: Nested Function
def outer():

   def inner():
      print("Hello")

   inner()

outer()
"""
Flow:

outer()
   ↓
inner() create
   ↓
inner() call
   ↓
Hello

এখানে Closure নেই।

"""

# Step 2: Inner Function Outer variable Uses
def outer():

   name = "mamun"

   def inner():
      print(name)

   inner()

outer()
"""
Flow:

name = Mamun
      ↓
inner()
      ↓
print(name)

এখনও Closure না।

"""

# Step 3: Inner Function Return
def outer():
   name = "Mamun"

   def inner():
      print(name)

   return inner
# এখানে inner function return হচ্ছে।


# Step 4: Return হওয়া Function Variable-এ রাখি
def outer():

   name = "Mamun"

   def inner():
      print(name)

   return inner

result = outer()
"""
Flow:

outer()
   ↓
inner return
   ↓
result = inner

এখন result আসলে একটা function।

"""


# Step 5: Return হওয়া Function Call করি
def outer():

   name = "mamun"

   def inner():
      print(name)

   return inner 

result = outer()
result()
"""
এখানে মজার ঘটনা ঘটেছে।

outer() শেষ হয়ে গেছে।
তাহলে name variable তো মুছে যাওয়ার কথা!
কিন্তু result() call করলে এখনও "Mamun" print হচ্ছে।

কেন?
কারণ Python inner function-এর সাথে name variable-টাও save করে রেখেছে।
Python variable-টাকে special memory-তে রেখে দিয়েছে।
এই saved environment-ই Closure।


Visual Diagram:
_______________

outer()

name = Mamun

      ↓
return inner

      ↓
outer() finished

      ↓
name should disappear

      ↓
But Python keeps it

      ↓
result()

      ↓
Mamun

"""
def multiplier(x):

   def multiply(y):

      return x * y 
   
   return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))


# Step 6: Closure কেন লাগে?
# Decorator বানাতে।
# Decorator-এর ভিতরে Closure থাকে।
def decorator(func):

   def wrapper():
      print("Before")

      func()

      print("After")
   
   return wrapper

"""
এখানে:

wrapper
remember করে:

func

এই remembered func-এর কারণেই Decorator কাজ করে।

"""


# Step 7: Closure চিনার Shortcut
def outer():

   name = "mamun"

   def inner():
      print(name)

   return inner

result = outer()
result()
# এটাই Closure-এর ক্লাসিক structure।

"""
যদি এই ৩টা জিনিস একসাথে দেখো:

✅ Function-এর ভিতরে Function
✅ Inner Function return হচ্ছে
✅ Inner Function outer variable ব্যবহার করছে

তাহলেই ৯৯% ক্ষেত্রে Closure।

Outer Function
      ↓
Inner Function
      ↓
Return Inner Function
      ↓
Remember Outer Variable
      ↓
Closure

"""

## Example 1: Greeting Factory
def make_greeting(word):

   def greet(name):
      return f"{word}, {name}!"
   
   return greet

hello = make_greeting("Hello")
asslamu = make_greeting("Assalamu Alaikum")

print(hello("Mamun"))
print(asslamu("Habib"))


## Example 2: Tax Calculator
def tax_calculator(rate):

   def calculate(amount):
      return amount * rate 
   
   return calculate

bd_tax = tax_calculator(0.15)
usa_tax = tax_calculator(0.10)

print(bd_tax(1000))
print(usa_tax(1000))


## Example 3: Login checker
def login_required(password):

   def check(user_password):

      if user_password == password:
         return "Login Success"
      
      return "Wrong Password"
   
   return check

admin_login = login_required("12345")

print(admin_login("12344"))
print(admin_login("12345"))


## Example 4: Counter 
def counter():

   count = 0

   def increment():

      nonlocal count 
      count += 1
      return count 
   
   return increment

c = counter()
print(c())
print(c())
print(c())
print(c())
print(c())
print(c())


## Example 5: Bank Account 
def bank_account(balance):

   def deposit(amount):

      nonlocal balance
      balance += amount 
      return balance
   
   return deposit

account = bank_account(1000)

print(account(500))
print(account(700))
print(account(400))


## Example 6: Power Function Factory
def power_factory(power):

   def calculate(number):

      return number * power 
   
   return calculate

square = power_factory(2)
cube = power_factory(3)

print(square(5))
print(cube(5))


## Example 7: Backend Developer Sytle 
def api_client(base_url):
   
   def get(endpoint):
      return base_url + endpoint
   
   return get  

github = api_client(
   "https://github.com/mamun-2025/"
)

print(github("users"))

"""
Closure-এর Pattern
সব Example-এ একই Structure দেখবে:

def outer(data):

    def inner(value):

        # data ব্যবহার করছে

        return something

    return inner


অর্থাৎ:
Outer Function
      ↓
Creates Data
      ↓
Inner Function Uses Data
      ↓
Return Inner Function
      ↓
Data Remembered
      ↓
Closure

"""