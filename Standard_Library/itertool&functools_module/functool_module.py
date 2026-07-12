

### functools কী?
"""
functools হলো এমন module যেখানে function নিয়ে কাজ করার 
কিছু powerful tools আছে।

ব্যবহার:
Higher order function
Decorator
Function optimization

"""
import functools


### 1. reduce()
# reduce কী?
# অনেকগুলো value নিয়ে একটি final result দেয়।
# normal 
numbers = [1, 2, 3, 4]

total = 1

for n in numbers:
   total *= n

print(total)


# reduce দিয়ে:
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x*y, numbers)

print(result)

##
from functools import reduce
prices = [
   100,
   200,
   300,
]

total = reduce(
   lambda x, y: x+y, prices
)

print(total)




### 2. partial()
# partial কী?
# partial() একটি existing function থেকে নতুন function তৈরি করে 
# যেখানে কিছু argument আগে থেকেই fixed থাকে।
def multiply(a, b):
   return a * b 


from functools import partial

multiply_by_10 = partial(
   multiply,
   10
)

print(multiply_by_10(5))

# Backend Real Example: Database Connection
def connect_database(host, port, username):
   print(host, port, username)


from functools import partial

production_db = partial(
   connect_database,
   host="loacalhost",
   port="5432"
)

production_db(username="admin ")


##
from functools import partial

def send_email(to, smtp, port):
   print(f"Sending email to {to} using {smtp}:{port}")


gmail_email= partial(
   send_email,
   smtp="gmail",
   port=5432
)

gmail_email("user1@email.com")
gmail_email("user2@gmail.com")




### 3. wraps()
# এটা Decorator-এর জন্য খুব গুরুত্বপূর্ণ।
# আমরা আগে decorator শিখেছি।
def decorator(func):

   def wrapper():

      return func()
   
   return wrapper
# Function information হারিয়ে যায়।
# solution:
from functools import wraps

def decorator(func):

   @wraps(func)
   def wrapper():

      return func()
   
   return wrapper

# Django middleware/decorator:

# Login required
# Permission check
# Logging

# এখানে wraps ব্যবহার করা হয়।
   




### 4. lru_cache()
# lru_cache কী?
# Function result cache করে।
# যাতে একই calculation বারবার করতে না হয়।
from functools import lru_cache

@lru_cache
def fibonacci(n):

   if n <= 1:
      return n 
   
   return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))

"""
Without cache:
অনেক calculation হয়।

With cache:
আগের result মনে রাখে।

Backend Example:

Expensive calculation
API data caching
Repeated query optimization


itertools vs functools
| itertools            | functools            |
| -------------------- | -------------------- |
| Data processing      | Function processing  |
| Iterator tools       | Function tools       |
| Loop optimization    | Function reuse       |
| combinations/product | reduce/partial/cache |

"""

# Problem 1: Product list থেকে সব possible pair বের করা
from itertools import combinations

products = [
   "A",
   "B",
   "C"
]

pairs = combinations(
   products,
   2
)

for pair in pairs:
   print(pair)


# Problem 2: E-commerce Variation Generator
from itertools import product

colors = [
   "Black",
   "White"
]

sizes = [
   "M",
   "L"
]

variations = product(
   colors,
   sizes
)

for variation in variations:
   print(variation)

# Real ecommerce example:
from itertools import product

colors = [
   "Red",
   "Black"
]

sizes = [
   "M",
   "S"
]

products = []

for color, size in product(colors, sizes):

   products.append(
     {
      "color":color,
      "size": size
     }
   )

print(products)


# Problem 3: Cart Price using reduce()
from functools import reduce

prices = [
   100,
   200,
   500
]

total = reduce(
   lambda x, y: x + y, prices
)

print("Cart Total:", total)


# Problem 4: Decorator with @wraps
# Requirement:
# ✅ Function name দেখাবে
# ✅ Execution message দেখাবে
# ✅ @wraps ব্যবহার করবে

from  functools import wraps

def execution_logger(func):

   @wraps(func)
   def wrapper(*args, **kwargs):

      print(
         "Function started", 
         func.__name__
      )

      result = func(
         *args,
         **kwargs
      )

      print(
         "Function Finished",
         func.__name__
      )

      return result
   
   return wrapper

@execution_logger
def create_order():
   print("Order Created")
   
create_order()

print(create_order.__name__)


# Problem 5: Backend Mini Project
# Order ID Generator System

# Features:
# ✅ Automatic ID generation
# ✅ Product combination
# ✅ Cart total calculation
# ✅ Function cachingfrom itertools import product
from functools import reduce, lru_cache
import uuid



# --------------------------
# Order ID Generator
# --------------------------

def generate_order_id():

    return "ORD-" + str(uuid.uuid4())[:8]



# --------------------------
# Product Combination
# --------------------------

def create_variations(colors, sizes):

    variations = []

    for color, size in product(colors, sizes):

        variations.append(
            {
                "color": color,
                "size": size
            }
        )

    return variations



# --------------------------
# Cart Total
# --------------------------

def calculate_total(prices):

    return reduce(
        lambda x,y: x+y,
        prices
    )



# --------------------------
# Function Caching
# --------------------------

@lru_cache(maxsize=100)
def product_price(product_id):

    print(
        "Database Query Running..."
    )

    prices = {
        1:500,
        2:1000,
        3:1500
    }

    return prices.get(
        product_id
    )



# --------------------------
# Testing
# --------------------------


order_id = generate_order_id()

print(
    "Order ID:",
    order_id
)


colors = [
    "Black",
    "White"
]

sizes = [
    "M",
    "L"
]


print(
    "\nProduct Variations:"
)

print(
    create_variations(
        colors,
        sizes
    )
)



cart = [
    500,
    1000,
    2000
]


print(
    "\nCart Total:",
    calculate_total(cart)
)



print(
    "\nFirst Call:"
)

print(
    product_price(1)
)


print(
    "\nSecond Call:"
)

print(
    product_price(1)
)