

## Default arguments in Python
"""
In Python, functions can have default arguments, which are parameters with predefined values.
This means you don't always need to pass every argument while calling a function.
- If you have provide a value, Python uses it.
- If you skip it, the default value is used automatically.

"""
# ফাংশন ডিফাইন করার সময় যদি কোনো প্যারামিটারের একটি ব্যাকআপ বা ডিফল্ট মান দিয়ে দেওয়া হয়, 
# তবে তাকে Default Argument বলে। 
# ফাংশন কল করার সময় মান না দিলে এই ডিফল্ট মানটি কাজ করে।

## 
def intro(name, country="Bangladesh"):
   print(f"My name is {name} and I live in {country}.")

intro("Mamun")
intro("Alex", "Newzland")

##
def greet(name="Guest"):
   print("Hello", name)

greet()
greet("Mamun")


# Syntax: 
"""
def function_name(parameter1 = value1, parameter2 = value2, ....):
   # function body

   
Parameters:
parameter1, parameter2, .. Names of the parameters.
value1, value2, .. Default values assigned using = 
function_name : The name of function

Rules to keep in Mind
- Non-default parameters must come before default parameters in the function definition.
- Positional arguments must come before keyword arguments when calling a function.
- If using keyword arguments, order does not matter.
- Each parameter must have only one value.
- Keyword name must match exactly with the function definition.
- For positional (non-keyword) arguments, orders matters strictly.

"""
# Positional argument
def student(funcname, lastname="Bepari", student="Fifth"):
   print(funcname, lastname, "studies in", student, "standard" )

student("Mamun")
student("Rajib", "Howlader", "seventh")
student("Johon", "Gates")
student("Rony", "Khan")


# keyword argument
# ফাংশন কল করার সময় পজিশন বা সিরিয়াল মেইনটেইন না করে, 
# সরাসরি প্যারামিটারের নাম ধরে মানpass করাকে Keyword Argument বলে।
def describe_pet(pet_name, animal_type):
   print(f"I have a {animal_type}. Her name is {pet_name}")

describe_pet(pet_name="Tommy", animal_type="Cat")

##
def student(name, blood="A+"):
   print(f"My name is {name} and my blood group is {blood}")

student("Mamun", "B+")
student("Nondita")
student(name="Mamun", blood="B+")


# mixing positional argument
def student(fn, ln="Mark", std="Fifth"):
   print(fn, ln, "studies in", std, "Standard")

# student()
# student(fn="John", "Seventh")
# student(sub="maths")
# Note: This code raises errors because 'fn' is missing, positional is placed after keyword and sub is not a valid parameter.


# Using list as a default argument
def add_item(item, list=[]):
   list.append(item)
   return list 

print(add_item("Note"))
print(add_item("Pen"))
print(add_item("eraser"))


# Using dict as a default arguemt
def add_dict(item, qty, dict={}):
   dict[item] = qty
   return dict 

print(add_dict("note", 4))
print(add_dict("pen", 1))
print(add_dict("eraser", 5))


# Using the None as the default and create a new list or dictionary inside the function.
def add_item(item, list=None):
   if list is None:
      list = []
   list.append(item)
   return list 

print(add_item("Note"))
print(add_item("Pen"))
print(add_item("Eraser"))

def add_dict(item, qty, dict=None):
   if dict is None:
      dict = {}
   dict[item] = qty
   return dict 


print(add_dict("Note", 5))
print(add_dict("Pen", 1))
print(add_dict("Eraser", 1))