

"""
Part 2 — Python OOP (Intermediate → Advanced)

এই Part-এ আমরা কভার করবো:
OOP Intermediate:
________________
Class Variable
Class Method
Static Method
Property
Encapsulation
Getter
Setter

OOP Advanced:
_____________
Inheritance
Multiple Inheritance
Method Overriding
super()
Polymorphism
Abstract Class
Magic Methods

"""
##### 8) Class Variable
"""
আগে বুঝো: Instance Variable vs Class Variable

ধরো তুমি User class বানালে।
Instance Variable → প্রতিটি object-এর নিজের data
Class Variable → পুরো class-এর shared data

"""
class User:
   platform = "CodeMama" # Class Variable

   def __init__(self, name, email):
      self.name = name  # Instance Variable
      self.email = email # Instance Variale 


user1 = User("Mamun", "mamun@gmail.com")
user2 = User("Nondita", "nondita@gmail.com")

print(user1.name)
print(user1.email)

print(user2.name)
print(user2.email)

print(user1.platform)
print(user2.platform)
print(User.platform)
"""
এখানে কী হলো?

Class-এর ভিতরে এটা:
platform = "CodeMama"
এটা class variable।
মানে User class-এর সব object এই value share করবে।

আর এগুলো:
self.name = name
self.email = email
এগুলো instance variable
কারণ প্রতিটি user-এর name আর email আলাদা।

"""

# Backend analogy
# ধরো একটা app-এ সব user-এর জন্য default role "customer"।
class User:
   role = "Customer"

   def __init__(self, name):
      self.name = name 

u1 = User("Nondita")
print(u1.name)
print(u1.role)
# এখন সব user-এর role by default customer.


# আরেকটা example: object count
class User:
   total_users = 0 # class Variable 

   def __init__(self, name):
      self.name = name 
      User.total_users += 1

u1 = User("Mamun")
u2 = User("Habib")
u3 = User("Rudro")

print(User.total_users)

# কেন useful?
# Backend-এ অনেক সময় দরকার হয়:
# total object count
# default tax rate
# app-wide config
# shared settings
# status labels
# fixed category list






##### 9) Class Method
"""
Class method হলো এমন method যা class-এর উপর কাজ করে, 
object-এর উপর না।

এটা @classmethod দিয়ে লেখা হয়।
এখানে প্রথম parameter হয় cls।

"""
# Syntax:
class Myclass:
   @classmethod
   def my_method(cls):
      pass 


# Example 1
class User:
   total_users = 0

   def __init__(self, name, email):
      self.name = name 
      self.email = email
      User.total_users += 1

   @classmethod
   def get_total_users(cls):
      return cls.total_users
   
user1 = User("Mamun", "mamun@gmail.com")

print(user1.name)
print(user1.email)

print(User.get_total_users())
"""
এখানে:

@classmethod
def get_total_users(cls):
    return cls.total_users

cls মানে class নিজে (User)
তাই cls.total_users মানে User.total_users

কেন class method দরকার?
কারণ এটা object-specific না, class-level কাজ।

যেমন:
total users count
from dictionary / from JSON object create করা
factory method
class-level configuration

"""
# খুব important backend use case: alternative constructor
# ধরো API থেকে dictionary পেলাম:
data = {
   "name": "Mamun",
   "email": "mamun@gmail.com"
}
# এখন এটা দিয়ে object বানাতে চাই।


# Without classmethod
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email 

data = {"name": "habib", "email": "habib@gmail.com"}
user = User(data["name"], data["email"])
print(user.name)
print(user.email)
# এটা কাজ করে, কিন্তু clean না।

print()

# With classmethod
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email

   @classmethod
   def from_dict(cls, data):
      return cls(data["name"], data["email"])
   

data = {"name": "Tamim", "email": "tamim@gmail.com"}
user = User.from_dict(data)

print(user.name)
print(user.email)

# এটা backend-এ huge useful
# কারণ API response / JSON / DB row → object বানাতে হয়।






##### 10) Static Method
"""
Static method হলো এমন method যেটা class-এর ভিতরে থাকে,
কিন্তু না object-এর data use করে, না class-এর data use করে।

মানে এটা logically class-এর সাথে related, কিন্তু self বা cls লাগে না।

"""
# Syntax:
class MyClass:
   @staticmethod
   def my_method():
      pass 


# Example:
class MathHelper:
   @staticmethod
   def add(a, b):
      return a + b 
   
print(MathHelper.add(10, 20))
math = MathHelper.add(10, 20)
print(math)

# আরেকটা backend-friendly example
class UserValidator:
   @staticmethod
   def is_valid_email(email):
      return "@" in email and "." in email
   
valid = UserValidator.is_valid_email("mamun@gmail.com")
print(UserValidator.is_valid_email("mamun@gmail.com"))
print(valid)

valid = UserValidator.is_valid_email("mamun")
print(UserValidator.is_valid_email("mamun"))
print(valid)

# 1. Static method কবে ব্যবহার করবো?

# যখন functionটা:
# class-এর conceptually অংশ
# কিন্তু object state লাগছে না
# class state-ও লাগছে না

# যেমন:
# validation
# formatting
# utility function
# calculation


# 2. Class Method vs Static Method:

# Class Method:
# cls পায়
# class variable access করতে পারে
# alternative constructor বানাতে পারে

# Static Method:
# self না
# cls না
# শুধু helper logic






##### 11) Property
class Product:
   def __init__(self, price, quantity):
      self.price = price 
      self.quantity = quantity

# এখন total price চাই।


# তুমি method লিখতে পারো:
class Product:
   def __init__(self, price, quantity):
      self.price = price
      self.quantity = quantity

   def total_price(self):
      return self.price * self.quantity
   
p = Product(100, 3)
print(p.total_price())

# এটা ঠিক আছে।
# কিন্তু total_price আসলে একটা calculated attribute টাইপ জিনিস।
# আমরা চাইলে এটাকে property করতে পারি।


# Property Version
class Product:
   def __init__(self, price, quantity):
      self.price = price 
      self.quantity = quantity

   @property
   def total_price(self):
      return self.price * self.quantity
   

p = Product(100, 3)
print(p.total_price)

"""
খেয়াল করো:
print(p.total_price)

এখানে () নেই।
কারণ এটা method হলেও attribute-এর মতো access হচ্ছে।

কেন useful?
কারণ user code clean হয়।

cart.total_price
user.full_name
order.is_paid
product.discounted_price

এগুলো natural লাগে।

"""
# Real Example:
class User:
   def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name

   @property
   def full_name(self):
      return f"{self.first_name} {self.last_name}"
   

user1 = User("Mamun", "Bepari")
user2 = User("Nondita", "Biswsas")

print(user1.full_name)
print(user2.full_name)






##### 12) Encapsulation
# Encapsulation মানে হলো data + behavior একসাথে class-এর ভিতরে রাখা
# এবং কিছু data/logic বাইরের direct access থেকে protect করা।

# সহজ ভাষায়:
# “যা দরকার শুধু তা expose করবো, ভিতরের sensitive জিনিস লুকিয়ে রাখবো।”

class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance
    

"""
এখন বাইরে থেকে যে কেউ করতে পারে:
acc.balance = -5000

এটা dangerous।
তাই আমরা data control করতে চাই।

Python-এ encapsulation কিভাবে করা হয়?
Python-এ strict private নেই, কিন্তু convention আছে:

_name → internal / protected style
__name → name mangling (stronger private-like behavior)

"""
# Example with _balance
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self._balance = balance

   def deposit(self, amount):
      if amount > 0:
         self._balance += amount

   def get_balance(self):
      return self._balance
   
acc = BankAccount("Mamun", 50000)
acc.deposit(500)
print(acc.get_balance())

# এখানে _balance বলে বুঝানো হচ্ছে:
# “এটা internal data, direct touch না করাই ভালো।”





##### 13) Getter
# Getter হলো data read করার controlled method।
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner 
      self._balance = balance

   def get_balance(self):
      return self._balance


# ব্যবহার:
acc = BankAccount("Nondita", 20000)
print(acc.get_balance())

# Getter কেন দরকার?

# কারণ:
# direct access বন্ধ করা যায়
# value modify করে return করা যায়
# permission check করা যায়
# formatting করা যায়






##### 14) Setter
# Setter হলো data update করার controlled method।
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner 
      self._balance = balance

   def get_balance(self):
      return self._balance
   
   def set_balance(self, amount):
      if amount >= 0:
         self._balance += amount
      else:
         print("Balance cannot be negative.")


acc = BankAccount("Sanjib", 30000)

acc.set_balance(5000)
print(acc.get_balance())

acc.set_balance(-5000)
print(acc.get_balance())


# Better way: Property + setter
# এটাই বেশি Pythonic।
class BankAccount:
   def __init__(self, owner, balance):
      self.owner  = owner
      self._balance = balance

   @property
   def balance(self):
      return self._balance
   
   @balance.setter
   def set_balance(self, amount):
      if amount < 0:
         print("Balance cannot be negative.")
      else:
         self._balance += amount


acc = BankAccount("Alex", 50000)
print(acc.balance) # getter

acc.set_balance = 50000 # setter
print(acc.balance)


acc.set_balance = -1000 # balance cannot be negative
print(acc.balance)




################################################################################################




## এখন Advanced OOP
##### 15) Inheritance

