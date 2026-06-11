
## Python Lambda Functions 
"""
Lambda functions are small anonymous functions, meaning they do not hava defined name.
These are small, short-lived functions used to pass simple logic to another function.
- Contain only one expression
- Result of that expression is returned automatically (no return keyword needed).

1. Lambda Function কী?
Lambda Function Python-এর একটি ছোট anonymous function (নামবিহীন ফাংশন)।
Lambda Function হলো Python-এর anonymous function যা lambda arguments: expression syntax ব্যবহার করে এক লাইনে ছোট function তৈরি করতে সাহায্য করে। 
এটি সাধারণত map(), filter(), sorted() ইত্যাদির সাথে ব্যবহৃত হয়।

2. Lambda-এর Limitations
Lambda-তে শুধু একটি expression লেখা যায়।

❌ এটা ভুল:

lambda x:
    print(x)
    return x

❌ Loop লেখা যায় না।

❌ Multiple statement লেখা যায় না।

"""
# # simple function
# def add(a, b):
#    return a + b 

# print(add(10, 20))

# # Lambda version:
# add = lambda a, b: a + b 
# print(add(10, 20))

# # Lambda Syntax: lambda arguments : expression
# # example:
# square = lambda x: x * x 
# print(square(5))

# # same thing
# def square(x):
#    return x * x 

# print(square(5))

# ######## Use cases
# # 1. Condition checking:
# check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

# print(check(5))   
# print(check(-3))  
# print(check(0))


# # 2. List Comprehension
# func = [lambda arg=x: arg * 10 for x in range(1, 5)]
# for i in func:
#    print(i())


# # 3. Returning Multiple Results
# calc = lambda x, y: (x + y , x * y)
# res = calc(2, 4)
# print(res)


# 4. filter()
## 
def starts_a(w):
   return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
result = list(filter(starts_a, li))
print(result)

##
def even_number(n):
   return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(filter(even_number, numbers))
print(result)

##
c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))

##
a = [1, 2, 3, 4, 5, 6]
res = list(filter(lambda x: x % 3 == 0, a))
print(res)

##
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

##
a = ["apple", "banana", "cherry", "kiwi", "grape"]
res = list(filter(lambda l: len(l) > 5, a))
print(res)

## 
l = ["apple", "", None, "banana", 0, "cherry"]
res = list(filter(None, l))
print(res)

##
users = [
   {"name": "Mamun", "active": True},
   {"name": "Rahim", "active": False},
   {"name": "Habib", "active": True}
]
active_users = list(
   filter(
      lambda user: user["active"], 
      users
))
print(active_users)


# # 5. map()
# ##
# s = ['1', '2', '3', '4']
# res = list(map(int, s))
# print(res)

# ##
# def double(val):
#    return val * 2

# a = [1, 2, 3, 4]
# res = list(map(double, a))
# print(res)

# ##
# a = [1, 2, 3, 4]
# double = map(lambda x: x * 2, a)
# print(list(double))

# ##
# a = [1, 2, 3, 4]
# res = list(map(lambda x: x ** 2, a))
# print(res)
# ##
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x*x, numbers))
# print(result)

# ## 
# salaries = [10000, 20000, 30000]
# new_salaries = list(
#    map(lambda salary: salary * 10.0, salaries
# ))
# print(new_salaries)

# ##
# a = [1, 2, 3]
# b = [4, 5, 6]
# res = list(map(lambda x, y: x + y, a, b))
# print(res)

# ##
# fruits = ["apple", "banana", "cherry"]
# res = list(map(str.upper, fruits))
# print(res)

# ##
# words = ["apple", "banana", "cherry"]
# res = list(map(lambda s: s[1], words))
# print(res)

# ## 
# s = [" hello ", " world ", " python "]
# res = list(map(str.strip, s))
# print(res)

# ## 
# celsius = [0, 20, 37, 100]
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# print(fahrenheit)



# # 6. reduce()
# from functools import reduce
# a = [1, 2, 3, 4]
# multiply = reduce(lambda x, y: x * y, a)
# print(multiply)


# # 7. sorted()
# students = [
#    {"name": "Mamun", "age": 25},
#    {"name": "Habib", "age": 30},
#    {"name": "Karim", "age": 28}
# ]
# result = sorted(students, key=lambda student: student["age"])
# print(result)


# # 8. min()
# employees = [
#    {"name": "mamun", "salary": 50000},
#    {"name": "habib", "salary": 70000},
#    {"name": "Rudro", "salary": 20000}
# ]

# lowest_salary = min(
#    employees,
#    key=lambda emp: emp["salary"]
# )

# print(lowest_salary)


# # 9. max()
# ##
# employees = [
#     {"name": "A", "salary": 50000},
#     {"name": "B", "salary": 20000},
#     {"name": "C", "salary": 70000}
# ]

# highest_salary = max(
#     employees,
#     key=lambda emp: emp["salary"]
# )

# print(highest_salary)

# ## 
# users = [
#     {"name": "Mamun", "age": 25},
#     {"name": "Rahim", "age": 18},
#     {"name": "Karim", "age": 30}
# ]

# oldest = max(
#     users,
#     key=lambda user: user["age"]
# )

# print(oldest)

#######################################################################

# # Example 1: দুই সংখ্যার যোগ
# add = lambda a, b: a + b 
# print(add(10, 10))

# # Example 2: তিনটি সংখ্যার যোগ
# add = lambda a, b, c: a + b + c
# print(add(10, 10, 10))

# # Example 3: Even/Odd Check
# is_even = lambda x: x % 2 == 0
# print(is_even(8))
# print(is_even(7))

# # Example 4: বড় সংখ্যা বের করা
# largest = lambda a, b: a if a > b else b 
# print(largest(10, 3))

# # function 
# def largest(a, b):
#    if a > b:
#       return a 
#    else:
#       return b 
   
# print(largest(10, 5))

# # Example 5: String Uppercase 
# upper = lambda name: name.upper()
# print(upper("mamun"))

# # Example 6: String Lowercase
# lower = lambda name: name.lower()
# print(lower("NONDITA"))

# # Example 7: String Length
# length = lambda text: len(text)
# print(length("GeeksforGeeks"))

# # Exampole 8: List এর সব সংখ্যা Double করা
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x*2, numbers))
# print(result)

# # Example 9: সব নাম Capital Letter করা
# names = ["mamun", "nondita", "sanjib"]
# result = list(map(lambda name: name.upper(), names))
# print(result)

# # Example 10: শুধু Positive Number বের করা
# numbers = [1, -3, 4, -8, -5, 7, 9]
# positive_number = list(filter(lambda x: x > 0, numbers))
# print(positive_number)

# # Example 11: শুধু Odd Number
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers ))
# print(even_numbers)
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)

# # Example 12: নামের Length অনুযায়ী Sort
# names = ["Mamun", "A", "Nondita", "Kobi"]
# sorted_names = sorted(names, key=lambda x: len(x))
# print(sorted_names)

# # Example 13: Employee Salary Sort
# employees = [
#    {"name": "Mamun", "salary": 50000},
#    {"name": "Rahim", "salary": 70000},
#    {"name": "Karim", "salary": 60000}
# ]

# result = sorted(
#    employees, key=lambda x: x["salary"]
# )
# print(result)

# # Example 14: Django Backend Type Example 
# users = [
#    {"username": "mamun", "age": 15},
#    {"username": "habib", "age": 30},
#    {"username": "karim", "age": 18}
# ]

# adults = list(
#    filter(
#       lambda user: user["age"] >= 18 ,
#       users
#    )
# )

# print(adults)

# # Example 15: Lambda Returning Lambda
# def mutiplier(n):
#    return lambda x: x * n 

# double = mutiplier(2)
# triple = mutiplier(3)

# print(double(5))
# print(triple(5))

# # Example 16: Multiple Condition
# check = lambda x: "Even" if x % 2 == 0 else "Odd"

# print(f"This number is:", check(10))
# print(f"This number is:", check(7))

# # Example 17: Backend Interview Level Example
# orders = [
#    {"id": 1, "amount": 5000},
#    {"id": 2, "amount": 3000},
#    {"id": 3, "amount": 9000}
# ]

# highest_orders = max(
#    orders, 
#    key=lambda order: order["amount"]
# )
# print(highest_orders)


# #################################################################
# ## Real Backend Project Exmple
# orders = [
#    {"id": 1, "amount": 500},
#    {"id": 2, "amount": 700},
#    {"id": 3, "amount": 400}
# ]

# # সবচেয়ে বড় Order
# max_order = max(
#    orders, 
#    key=lambda order: order["amount"]
# )
# print(max_order)

# # সবচেয়ে ছোট Order
# min_order = min(
#    orders,
#    key=lambda order: order["amount"]
# )
# print(min_order)

# # Amount অনুযায়ী Sort
# sorted_orders = sorted(
#    orders,
#    key=lambda order: order["amount"]
# )
# print(sorted_orders)

# # 500 টাকার বেশি Order
# big_orders = list(
#    filter(
#       lambda order: order["amount"] > 500,
#       orders
#    )
# )
# print(big_orders)

"""
map() = ➡️ Transform / পরিবর্তন করে
filter() = ➡️ Filter / বাছাই করে
sorted() = ➡️ Sort করে
min() = ➡️ সবচেয়ে ছোট খুঁজে
max() = ➡️ সবচেয়ে বড় খুঁজে

আর lambda হলো সেই ছোট function যা এদেরকে বলে দেয় কোন field দেখে কাজ করতে হবে। 
যেমন:
lambda user: user["age"]

মানে:
"প্রতিটি user-এর age ব্যবহার করো।"

"""