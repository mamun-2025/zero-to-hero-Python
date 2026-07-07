

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
class Animal:
   def eat(self):
      print("Animal is eating")

class Dog(Animal):
   def bark(self):
      print("Dog is barking")

d = Dog()
d.eat() # inherited from Animal
d.bark()

"""
কী হলো?

Dog class Animal-কে inherit করেছে।

তাই Dog-এর নিজের method:
bark()

এবং Animal-এর method:
eat()

দুটাই আছে।

"""
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email

   def login(self):
      print(f"{self.name} logged in.")

class Admin(User):
   def delete_user(self):
      print(f"{self.name} can delete users.")

class Customer(User):
   def place_order(self):
      print("Customer Placed an order.")

a = Admin("Mamun", "mamun@gmail.com")
c = Customer("Nondita", "nondita@gmail.com")

a.login()
a.delete_user()

c.login()
c.place_order() 






##### 16) Multiple Inheritance
# একটা child class একাধিক parent class inherit করতে পারে।
class Flyer:
   def fly(self):
      print("Can fly")

class Swimmer:
   def swim(self):
      print("Can swim")

class Duck(Flyer, Swimmer):
   pass 

d = Duck()
d.fly()
d.swim()
"""
এখানে Duck কী পেল?
Flyer থেকে fly()
Swimmer থেকে swim()
কিন্তু note:

Multiple inheritance powerful, কিন্তু confusing হতে পারে।
সাবধানে use করতে হয়।

"""





##### 17) Method Overriding
# Child class parent-এর method নিজের মতো করে বদলে দিতে পারে।
class Animal:
   def sound(self):
      print("Animal makes sound.")

class Dog(Animal):
   def sound(self):
      print("Dog barks")

class Cat(Animal):
   def sound(self):
      print("Cat meows")


a = Animal()
a.sound()

d = Dog()
d.sound()

c = Cat()
c.sound()
"""
এটাকেই বলে overriding

Parent-এ ছিল:
sound()

Child-এ same method name দিয়ে নতুন behavior দিলাম।

"""

# Backend Example:
class Notification:
   def send(self):
      print("Sending generic notification.")

class EmailNotification(Notification):
   def send(self):
      print("Sending Email")

class SMSNotification(Notification):
   def send(self):
      print("Sending SMS.")


n = Notification()
n.send()

e = EmailNotification()
e.send()

s = SMSNotification()
s.send()






##### 18) super()
# super() দিয়ে parent class-এর method বা constructor call করা হয়।
# Example 1:
class User:
   def __init__(self, name, age):
      self.name = name 
      self.age = age 

   
class Admin(User):
   def __init__(self, name, age, email, role):
      super().__init__(name, age)
      self.email = email
      self.role = role 

a = Admin("Mmaun", 25, "mamun@gmail.com", "Jr Software engineer")
print(a.name)
print(a.age)
print(a.email)
print(a.role)

# কেন super() দরকার?
# কারণ parent class-এর code reuse করতে পারি।
# না হলে child class-এ সব manually লিখতে হতো।


# Example 2: parent method call + extra behavior
class User:
   def login(self):
      print("User login")

class Admin(User):
   def login(self):
      super().login()
      print("Admin dashboard loaded")


a = Admin()
a.login()





##### 19) Polymorphism
# Polymorphism মানে:
# একই method name, কিন্তু different object-এ different behavior
class Dog:
   def sound(self):
      print("Dog barks")

class Cat:
   def sound(self):
      print("Cat mews")

class Cow:
   def sound(self):
      print("Cow Moos")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
   animal.sound()

print()

d = Dog()
d.sound()

c = Cat()
c.sound()

c = Cow()
c.sound()

# সব object-এর sound() method আছে,
# কিন্তু behavior আলাদা।

# Backend Example:
class BkashPayment:
   def pay(self, amount):
      print(f"Paid {amount} using bkash")

class CardPyment:
   def pay(self, amount):
      print(f"Paid {amount} using Card.")

class NagadPayment:
   def pay(self, amount):
      print(f"Paid {amount} using Nagad.")

payments = [
   BkashPayment(),
   CardPyment(),
   NagadPayment()
]

for payment in payments:
   payment.pay(500)


print()


b = BkashPayment()
b.pay(1000)

c = CardPyment()
c.pay(2000)

n = NagadPayment()
n.pay(3000)

# একই pay() method, different behavior → polymorphism.





##### 20) Abstract Class
# Abstract class হলো blueprint class।
# এটা বলে দেয় child class-এ কোন method অবশ্যই implement করতে হবে।
# Python-এ এটা abc module দিয়ে করা হয়।

from abc import ABC, abstractmethod

class Payment(ABC):
   @abstractmethod
   def pay(self, amount):
      pass 


class BkashPayment(Payment):
   def pay(self, amount):
      print(f"Paind {amount} with bkash.")

class CardPayment(Payment):
   def pay(self, amount):
      print(f"Paid {amount} with card")

class NagadPayment(Payment):
   def pay(self, amount):
      print(f"Paid {amount} with nagad.")


b = BkashPayment()
b.pay(5000)

# কেন abstract class দরকার?
# যখন তুমি enforce করতে চাও:

# সব payment class-এর pay() method থাকতেই হবে
# সব notification class-এর send() method থাকতেই হবে
# সব serializer class-এর serialize() method থাকতেই হবে

# যদি child method না লেখে?
# তাহলে object তৈরি করতে গেলে error হবে।





##### 21) Magic Methods
# Magic methods (dunder methods) হলো special methods যেগুলো Python automatically call করে।

# যেমন:
# __init__
# __str__
# __len__
# __add__

# এগুলো দিয়ে class-কে Pythonic করা যায়।

# 1. __str__
# without __str__
class User:
   def __init__(self, name):
      self.name = name 

u = User("Mamun")
print(u)


# with __str__
class User:
   def __init__(self, name):
       self.name = name 

   def __str__(self):
      return f"User(name = {self.name})"

u = User("Nondita")
print(u)



# 2. __repr__
class User:
   def __init__(self, name):
      self.name = name 

   def __repr__(self):
      return f"User ('{self.name}')"
   
u = User("Mamun")
print(u)

"""
__str__ vs __repr__
__str__
user-friendly
display-এর জন্য

__repr__
developer/debug-friendly
ideally object recreate করার মতো info

"""

# 3. __len__
# len(obj) কাজ করাতে ব্যবহার হয়।
class Cart:
   def __init__(self, items):
      self.items = items 

   def __len__(self):
      return len(self.items)

cart = Cart(["Book", "Pen", "Mouse"])
print(len(cart))


# __add__

class Money:
   def __init__(self, amount):
      self.amount = amount 

   def __add__(self, other):
      return Money(self.amount + other.amount)
   
   def __str__(self):
      return f"{self.amount} BDT"
   
m1 = Money(20000)
m2 = Money(20000)

result = m1 + m2
print(result)
   

# __eq__

class User:
   def __init__(self, email):
      self.email = email 

   def __eq__(self, other):
      return self.email == other.email 
   
u1 = User("mamun@gmail.com")
u2 = User("mamun@gmail.com")
u3 = User("rahim@gmail.com")

print(u1 == u2)
print(u1 == u3)





print()
##### 22. # Combined backend-style example
# নিচের example-এ inheritance, property, encapsulation, 
# class variable, magic method—অনেক কিছু একসাথে আছে।

class User:
   total_users = 0

   def __init__(self, name, email):
      self.name = name
      self.email = email
      self._active = True
      User.total_users += 1

   @property
   def active(self):
      return self._active

   @active.setter
   def active(self, value):
      if isinstance(value, bool):
         self._active = value 

   def login(self):
      return f"{self.name} logged in"
   
   def __str__(self):
      return f"User(name={self.name}, email={self.email})"
   

class Admin(User):
   def __init__(self, name, email, role):
      super().__init__(name, email)
      self.role = role 

   def login(self):
      base = super().login()
      return f"{base} as admin ({self.role})"


u1 = User("Rahim", "rahim@gmail.com")
a1 = Admin("Mamun Bepari", "mamun@gmail.com", "superadmin")

print(u1.name)
print(u1.email)
print(u1.active)
print(u1.login())
print()

print(a1.name)
print(a1.email)
print(a1.active)
print(a1.login())
print()

print(User.total_users)

print(u1.active)
u1.active = False
print(u1.active)

print(a1.active)
a1.active = False
print(a1.active)

"""
Output mentally বুঝো:

User.total_users
দুইটা object তৈরি হয়েছে → 2

a1.login()
Admin নিজের login method use করবে,
কিন্তু super().login() দিয়ে parent-এর logic-ও নেবে।

active
property getter/setter দিয়ে controlled access হচ্ছে।

"""






##### 23. Intermediate + Advanced + Magic Methods = quick cheat sheet
# 1. Class variable
class User:
   count = 0

# সব object share করবে।



# 2. Class Method
@classmethod
def from_dict(cls, data):
   return cls(data["name"], data["email"])



# 3. Static Method
@staticmethod
def add(a, b):
   return a + b 

@staticmethod
def validate_email(email):
   return "@" in email 

# helper function



# 4. Property 
class Item:
   def __init__(self, price, qty):
      self.price = price 
      self.qty = qty

   @property
   def total(self):
      return self.price * self.qty
   
i = Item(200, 2)
print(i.total)
# method-কে attribute-এর মতো use।



# 5. Encapsulation
class Bank:
   def __init__(self, owner, balance):
      self.owner = owner 
      self._balance = balance

# internal data protect করার convention।



# 6. Getter/Setter
"""
@property
def balance(self):
  
@balance.setter
def balance(self, value):

# controlled read/write।

"""


# 7. Inheritance
class Admin(User):
   pass 

# parent থেকে features inherit।


# 8. Overriding
def login(self):
   ...

# child parent method বদলে দেয়।



# 9. super()
super().__init__(...)
super().login()

# parent method call



# 10. Polymorphisim
class Bkash:
   def pay(self, amount):
      print(f"Paid {amount} with bkash.")

class Card:
   def pay(self, amount):
      print(f"Paid {amount} with card.")

# একই method name → different behavior।



# 11. Abstract Class
from abc import ABC, abstractmethod

# child-কে বাধ্য করে method implement করতে।



# 12. Magic Methods
"""
__str__ → print সুন্দর করা
__repr__ → debug-friendly
__len__ → len(obj)
__add__ → obj1 + obj2
__eq__ → obj1 == obj2

"""


# 13. Django / Backend-এ OOP-এর ব্যবহার:
"""
User, Product, Order, Cart, Payment, Invoice class
model methods
serializers / service classes
validation classes
inheritance based roles (Admin, Customer)
payment gateways (BKashPayment, CardPayment)
notification system (EmailNotification, SMSNotification)
API response wrapper classes
repository/service pattern

"""