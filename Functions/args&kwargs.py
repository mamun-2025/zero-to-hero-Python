

# *args and **kwargs in Python
"""
In Python, *args and **kwargs are used to allow functions to accept an arbitrary number of arguments.
These features provide great flexibility when designing functions that need to handle a varying number of inputs.

"""
## 1. *args
# ধরো তুমি এমন function বানাতে চাও যেখানে কতগুলো সংখ্যা আসবে আগে থেকে জানো না।

##
def add(a, b):
    return a + b # এখানে ৩টা সংখ্যা দিলে error হবে।


##
def add(*args):
   print(args)

add(10, 20, 30)
# অর্থাৎ args একটি tuple।


##
def fun(*args):
   return sum(args)

print(fun(5, 10, 15))


##
def add(*args):
   total = 0

   for num in args:
      total += num 
   return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))


## 
def multiply(*args):
   result = 1 
   for num in args:
      result *= num
   return result

print(multiply(2, 3, 4))



## 2. **kwargs
##
def student(**kwargs):
   print(kwargs)

student(
   name="Mamun",
   age=25,
   city="Dhaka"
)

##
def person(**kwars):
   print(kwars)

person(
   name="Mamun",
   age= 26,
   city="Dhaka"
)

##
def person(**kwargs):

   for key, value in kwargs.items():
      print(key, value)

person(
   name="Mamun",
   age= 26,
   country= "Bangladesh"
)


## 
def fun(**kwargs):
   for k, val in kwargs.items():
      print(k, val)

fun(s1="Python", s2="is", s3="Awesome.")


##
def introduce(**kwargs):
   details = []

   for k, v in kwargs.items():
      details.append(f"{k}: {v}")

   return ", ".join(details)

print(introduce(Name="mamun", age=25, city="New york"))


##
def introduce(**kwargs):
   return ", ".join(f"{k}: {v}" for k, v in kwargs.items())

print(introduce(Name="Mamun", age=26, city="New york"))


## 3. *args + **kwargs together
def show(*args, **kwargs):
   print(args)
   print(kwargs)

show(
   10, 20, 30, name="Mamun", city="Dhaka"
)


## 
def student_info(*args, **kwargs):
   print("Subjects:", args)
   print("Details:", kwargs)

student_info("Math", "Science", "English", Name="Mamun", Age=26, city="New york")



## 4. Unpacking
# List unpacking
nums = [10, 20, 30]
a, b, c = nums 

print(a)
print(b)
print(c)

# Star unpacking
nums = [10, 20, 30, 40, 50]
a, *b = nums 

print(a)
print(b)

##
nums = [10, 20, 30, 40, 50]

a, *b, c= nums 

print(a)
print(b)
print(c)




## 5. Function Call Unpacking
def add(a, b, c):
   return a + b + c 

print(add(10, 20, 30)) # simple 

nums = [10, 20, 30]
print(add(*nums))




## 6. Dictionary Unpacking
def person(name, age):
   print(name, age)


data = {
   "name": "Mamun",
   "age": 25
}
person(**data)

## 7. Real Django Example
def logger(func):
   def wrapper(*args, **kwargs):
      print("Function Called")

      return func(*args, **kwargs)
   
   return wrapper

@logger
def add(a, b):
   return a + b 

add(10, 20)



