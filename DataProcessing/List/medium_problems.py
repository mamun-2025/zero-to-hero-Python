

# Problem 1: 1-10 পর্যন্ত সংখ্যা
nums = [i for i in range(1, 11)]
print(nums)

# Problem 2: Square Numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i * i for i in nums]
print(result)

nums = [i * i for i in range(1, 11)]
print(nums)

# Problem 3: Cube Numbers 
cubes = [i ** 3 for i in range(1, 6)]
print(cubes)

# Problem 4: Even Numbers 
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [i for i in nums if i % 2 == 0]
print(evens)

# Problem 5: Odd Numbers 
odds = [i for i in range(1, 11) if i % 2 != 0]
print(odds)

# Problem 6: Double Values
nums = [1, 2, 3, 4, 5]
double = [i * 2 for i in nums]
print(double)

# Problem 7: Triple Values
nums = [1, 2, 3, 4, 5]
triple = [i * 3 for i in nums]
print(triple)

# Problem 8: UpperCase Names
names = ["mamun", "habib", "rudro"]
result = [word.upper() for word in names]
print(result)

# Problem 9: LowerCase Names
names = ["MAMUN", "HABIB", "RUDRO", "SANJIB"]
result = [word.lower() for word in names]
print(result)

# Problem 10: Length of Each Word
words = ["c++", "java", "python", "javaScript"]
lengths = [len(word) for word in words]
print(lengths)

# Problem 11: First Character
words = ["c++", "java", "python", "javaScript"]
result = [word[0] for word in words]
print(result)

# Problem 12: Last character
words = ["c++", "java", "python", "javaScript"]
result = [word[-1] for word in words]
print(result)

# Problem 13: 
words = ["python", "javaScript"]
result = [word[::-1] for word in words]
print(result)

# Problem 14:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [i*i for i in nums if i % 2 == 0]
print(result)

# Problem 15:
nums = [5, 10, 15, 20, 25, 30]
result = [n for n in nums if n > 10]
print(result)

# Problem 16: Names Starting With A
names = ["Alex", "Mamun", "Alice", "Rahim"]
result = [name for name in names if name.startswith("A")]
print(result)

# Problem 17: String Length > 5
words = ["cat", "python", "django", "api"]
result = [word for word in words if len(word) > 5]
print(result)

# Problem 18: Convert String Numbers to Integers
nums = [ "1", "2", "3", "4", "5"]
result = [int(x) for x in nums]
print(result)

# Problem 19: Convert Intergers to Strings
nums = [1, 2, 3, 4]
result = [str(x) for x in nums]
print(result)

# Prolem 20: Remove Spaces
words = [" Python", " Java  ", "api    "]
result = [word.strip() for word in words]
print(result)

# Problem 21: Boolean Check(Even?)
nums = [1, 2, 3, 4]
result = [n % 2 == 0 for n in nums]
print(result)

# Problem 22: Replace Negative Numbers 
nums = [-5, 2, -1, 8]
result = ["Negaive" if n < 0 else n for n in nums]
print(result)

# Problem 23: Label Even/Odd
nums = [1, 2, 3, 4, 5]
result = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(result)

# Problem 24: Capitalize Names
names = ["mamun", "nondita", "sanjib"]
result = [word.capitalize() for word in names]
print(result)

# Problem 25: Extract Prices
products = [
   {"name": "Pen", "price": 10},
   {"name": "Book", "price": 500},
   {"name": "Laptop", "price": 25000}
]

result = [product["price"] for product in products]
print(result)

# Problem 26: Extract Names
users = [
   {"name": "Mamun"},
   {"name": "Rahim"},
   {"name": "Karim"}
]

names = [user["name"] for user in users]
print(names)

# Problem 27: Gmail Filter
##
emails = [
   "a@gmail.com",
   "b@gmail.com",
   "c@gmail.com"
]

result = [email for email in emails if email.endswith("@gmail.com")]
print(result)

##
users = [
   {"active": True},
   {"active": False},
   {"active": True}
]

active_users = [
   user
   for user in users
   if user["active"]
]
print(active_users)

# Problem 28: Flatten Nested List
matrix = [
   [1, 2],
   [3, 4],
   [5, 6]
]

result = [
   item 
   for row in matrix 
   for item in row
]
print(result)

# Problem 29: Multiplication Table of 5
table = [5*i for i in range(1, 11)]
print(table)

# Problem 30: Create Coordinate Pairs
pairs = [
   (x,y)
   for x in range(1, 4)
   for y in range(1, 4)
]
print(pairs)

# Problem 31: Sum
##
nums = [1, 2, 3, 4, 5]
total = sum(nums)
print(total)

##
nums = [1, 2, 3, 4, 5]
total = 0

for num in nums:
   total += num 

print(total)

# Problem 32: Product
nums = [2, 4, 6]
product = 1

for num in nums:
   product *= num

print(product)

# Problem 33: max
nums = [1, 2, 3, 4, 5]
print(max(nums))

prices = [100, 250, 800, 500]
print(max(prices))

# Problem 34: min
nums = [2, 5, 0, 4]
print(min(nums))

prices = [100, 250, 800, 500]
print(min(prices))

# Problem 35: String Processing
##
names = [
   "mamun",
   "rahim", 
   "karim"
]
result = [name.upper() for name in names]
print(result)

##
emails = [
   " MAMUN@gmail.com",
   "  RAHIM@gmail.com",
   "youtube.com  ",
   "  INSTRAgram.com"
]

clean = [
   email.strip().lower()
   for email in emails
   if email.endswith("@gmail.com")
]
print(clean)

## API Response
response = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"}
]

names = [
   user["name"]
   for user in response
]
print(names)

## Aggregate Data
products = [
    {"price":100},
    {"price":200},
    {"price":300}
]
total = sum(
   product["price"]
   for product in products
)

print(total)

##
orders = [
   {"amount": 500},
   {"amount": 700},
   {"amount": 300}
]

total_sales = sum(
   order["amount"]
   for order in orders
)

print(total_sales)



"""
তুমি যখন Django/FastAPI-তে API তৈরি করবে, তখন প্রায় প্রতিদিন এরকম Pattern দেখবে:

names = [user["name"] for user in users]

active_users = [
    user
    for user in users
    if user["active"]
]

total = sum(
    product["price"]
    for product in products
)

এই ৩টা Pattern Backend-এর "bread and butter" বলা যায়। 
এগুলো যত বেশি Practice করবে, JSON, API এবং Database Data Handle করা তত সহজ হবে।
"""