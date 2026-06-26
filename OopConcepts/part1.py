

"""
Part 1 — OOP Foundation
Class
Object
Attribute
Method
Constructor (__init__)
Instance Variable
Instance Method

"""

##### 0) OOP আসলে কী?
"""
OOP = Object Oriented Programming
এখানে আমরা data + behavior একসাথে একটি structure-এর মধ্যে রাখি।

ধরো backend-এ তোমার কাছে User, Product, Order, Cart, Payment আছে।
এগুলোকে আমরা object হিসেবে model করতে পারি।

উদাহরণ:
User → name, email, password, login()
Product → title, price, stock, discount()
Order → items, total, place_order()

মানে:
data = name, email, price, stock
behavior = login(), logout(), update_stock(), calculate_total()

এই data + function একসাথে রাখাই OOP-এর core idea।

"""





##### 1) Class কী?
"""
1) Class কী?
সহজ ভাষায়:

Class হলো blueprint / design / template

যেমন:

“User” বানানোর নকশা
“Car” বানানোর নকশা
“Product” বানানোর নকশা

Class নিজে real user না,
বরং user বানানোর ফর্মুলা / কাঠামো।

Real-life analogy

ধরো “ঘর বানানোর নকশা” আছে।

নকশা = Class
বাস্তব ১টা ঘর = Object

একই নকশা থেকে অনেক ঘর বানানো যায়।
তেমনি, এক class থেকে অনেক object বানানো যায়।

"""





##### 2) Object কী?
"""
সহজ ভাষায়:

Class থেকে তৈরি real instance-ই object

যেমন:
User class আছে
Mamun একটা user
Rahim আরেকটা user

তাহলে:
User = class
Mamun, Rahim = object

"""






##### 3) প্রথম OOP Example — Class + Object
class User:
   pass  

user1 = User()
user2 = User()

print(user1)
print(user2)

# User
# এটা class

# User()
# এটা object create করার call






##### 4) Attribute কী?
"""
সহজ ভাষায়:
Attribute = object-এর data / property / information

যেমন একজন user-এর থাকতে পারে:
name
email
age
password
country

এগুলোই attribute।

"""

# Example 1 — Attribute manually add করা
class User:
   pass 

user1 = User()
user1.name = "Mamun"
user1.email = "beparimamun708@gmail.com"
user1.age = 25
user1.password = "12345"
user1.country = "Bangladesh"

print(user1.name)
print(user1.email)
print(user1.age)
print(user1.password)
print(f"My country is {user1.country}")

"""
এখানে:
user1.name = "Mamun"
মানে user1 object-এর মধ্যে name নামে data রাখলাম।

user1.email = "mamun@gmail.com"
মানে email রাখলাম।
এগুলোই attribute।


Problem: 
এভাবে manually attribute set করা ভালো practice না।

কারণ:
সব object-এ একই structure enforce হয় না
কেউ name দেবে, কেউ email দেবে, কেউ ভুলে যাবে
code messy হয়ে যায়

এজন্য আমরা ব্যবহার করি constructor = __init__

"""





##### 5) Constructor (__init__) কী?
"""
Object তৈরি হওয়ার সময় initial data set করার special method হলো __init__

যখন তুমি লিখো:
user1 = User("Mamun", "mamun@gmail.com")
তখন object create হওয়ার সাথে সাথে __init__ run হয়।

Syntax
class ClassName:
    def __init__(self, ...):
        ...

"""
# Example 2 — Constructor use করা
class User:
   def __init__(self, name, email):
      self.name = name
      self.email = email

user1 = User("Mamun", "beparimamun708@gmail.com")
user2 = User("Rahim", "rahim@gmail.com")

print(user1.name)
print(user1.email)

print(user2.name)
print(user2.email)





##### 6) self কী?
"""
এটা OOP-এর সবচেয়ে গুরুত্বপূর্ণ জিনিসগুলোর একটা।

সহজ ভাষায়:
self = বর্তমান object নিজে

মানে:
user1 এর জন্য self = user1
user2 এর জন্য self = user2

"""
class User: 
   def __init__(self, name, age):
      self.name = name 
      self.age = age 

u1 = User("mamun", 25)
print(u1.name)
print(u1.age)

u2 = User("Nondita", 16)
print(u2.name)
print(u2.age)

"""
Example আবার দেখি
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

যখন লিখি:
user1 = User("Mamun", "mamun@gmail.com")

তখন Python ভিতরে প্রায় এমনভাবে কাজ করে:
User.__init__(user1, "Mamun", "mamun@gmail.com")

অর্থাৎ:
self = user1
name = "Mamun"
email = "mamun@gmail.com"

তাই:
self.name = name
মানে হচ্ছে:
user1.name = "Mamun"

এবং

self.email = email
মানে
user1.email = "mamun@gmail.com"

"""




##### 7) Constructor flow পুরোটা
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email 

user1 = User("Mamun", "mamun@gmail.com")
print(user1.name)
print(user1.email)

"""
Step by step flow:
Step 1:
User class থেকে নতুন object তৈরি হলো → user1

Step 2:
Python automatically __init__ call করল

Step 3:
self = newly created object (user1)

Step 4:
name = "Mamun"
email = "mamun@gmail.com"

Step 5:
self.name = name
self.email = email

এখন user1 object-এর মধ্যে data save হয়ে গেল।

"""




##### 8) Instance Variable কী?
"""
সহজ ভাষায়:

প্রতিটি object-এর নিজের আলাদা variable = instance variable
যেগুলো সাধারণত self.variable_name আকারে থাকে।

যেমন:

self.name
self.email
self.age

এগুলো instance variable।

কেন “instance” variable বলা হয়?
কারণ প্রতিটি object (instance)-এর value আলাদা হতে পারে।

"""
# Example 3:
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email

user1 = User("Mamun", "mamun@gmail.com")
user2 = User("Sanjib", "sanjib@gmail.com")

print(user1.name)
print(user2.name)

# এখানে:
# user1.name = Mamun
# user2.name = Rahim

# দুই object-এর data আলাদা।
# তাই name, email হলো instance variable





##### 9) Method কী?
"""
Class-এর ভিতরে লেখা function = method

যেমন:
login()
logout()
get_profile()
change_password()

"""
# Exmaple 4: Method
class User:
   def __init__(self, name):
      self.name = name 

   def greet(self):
      print("Hello", self.name)

user1 = User("Alex")
user1.greet()

"""
Explain
Method:
def greet(self):
    print("Hello,", self.name)

এটা User class-এর method।
এখানে self.name মানে যে object method call করেছে, তার name।

যখন:
user1.greet()

তখন ভিতরে প্রায় এমন হয়:
User.greet(user1)
অর্থাৎ self = user1

তাই:
self.name

হয়ে যায়:
user1.name

"""





##### 10) Instance Method কী?
# যে method specific object-এর data নিয়ে কাজ করে এ
# বং first parameter হিসেবে self নেয়, সেটাই instance method।
"""
def greet(self):
   ....

def get_email(self):
   ....

def change_name(self, new_name):
   ....

এগুলো instance method।

"""





##### 11) Method + Instance Variable together
class User:
   def __init__(self, name, age, email):
      self.name = name 
      self.age = age 
      self.email = email

   def show_info(self):
      print("Name:", self.name)
      print("Age:", self.age)
      print("Email:", self.email)
      
   def change_name(self, new_name):
      self.name = new_name

u1 = User("Rudro", 25 , "rudro@gmail.com")

u1.show_info()

u1.change_name("Mamun Bepari")
u1.show_info()

"""
এখানে কী হলো?
show_info()
এই method object-এর info print করছে।

change_name("Mamun Bepari")
এখানে object-এর name update হচ্ছে।

self.name = new_name
মানে object-এর নিজের name change হচ্ছে।

"""





##### 12) Full backend-style example
# Example 5: Product class
class Product:
   def __init__(self, title, price, stock):
      self.title = title
      self.price = price 
      self.stock = stock 

   def show_info(self):
      print("Title:", self.title)
      print("Price:", self.price)
      print("Stock:", self.stock)

   def is_in_stock(self):
      return self.stock > 0 
   
   def reduce_stock(self, quantity):
      self.stock = self.stock - quantity

Product1 = Product("keyboard", "2000", 10)
Product1.show_info()
print("In Stock?", Product1.is_in_stock())

print()

Product2 = Product("Mouse", "1000", 20)
Product2.show_info()
print("In Stock?", Product2.is_in_stock())

print()
Product1.reduce_stock(5)
Product1.show_info()

print()
Product2.reduce_stock(5)
Product2.show_info()

"""
Backend thinking দিয়ে বুঝো
Product class

একটা product model করলাম।

Attributes / instance variables
self.title
self.price
self.stock
Methods
show_info() → info দেখায়
is_in_stock() → stock আছে কি না check করে
reduce_stock(quantity) → stock কমায়

এটাই backend model thinking।

"""






##### 13) আরেকটা strong example — BankAccount
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

   def deposit(self, amount):
      self.balance = self.balance + amount 
      print("Deposited:", amount)

   def withdraw(self, amount):
      if amount <= self.balance:
         self.balance = self.balance - amount
         print("Withdrown:", amount)
      else:
         print("Insufficient balance")

   def show_balance(self):
      print("Owner:", self.owner)
      print("Balance:", self.balance)



acc1 = BankAccount("Nondita Biswsas", 10000)
acc1.show_balance()

print()

acc1.deposit(20000)
acc1.show_balance()

print()

acc1.withdraw(29000)
acc1.show_balance()

print()

acc1.withdraw(2000)

"""
এখানে কী শিখলে?
Class:
BankAccount

Object:
acc1

Instance Variables:
self.owner
self.balance

Instance Methods:
deposit()
withdraw()
show_balance()

"""


      



##### 14) Constructor ছাড়া vs Constructor দিয়ে
## Constructor ছাড়া
class User:
   pass

u1 = User()
u1.name = "Mamun"
u1.email = "mamunbepari@gmail.com"

# Problem:
# messy
# standard না
# object incomplete হতে পারে


## Constructor দিয়ে
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email

u1 = User("Mamun", "mamun@gmail.com")
print(u1.name)
print(u1.email)

# Benefit:
# object create হওয়ার সময়ই data set
# cleaner
# safer
# real backend style






##### 15) self নিয়ে confusion দূর করি
"""
এই code:
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


যদি লিখো:
u1 = User("Mamun")
u2 = User("Rahim")

u1.greet()
u2.greet()


internally বুঝো:
User.greet(u1)
User.greet(u2)

তাই:
first call-এ self = u1
second call-এ self = u2

তাই output:
Hello Mamun
Hello Rahim

"""






##### 16) OOP Foundation Summary Table
"""
Topic	                           Meaning
Class                            blueprint / template
Object	                        class থেকে তৈরি real thing
Attribute	                     object-এর data / property
Method	                        class-এর ভিতরের function
__init__	                        object create হলে automatically run হওয়া constructor
Instance Variable	               self.name, self.price — object-specific data
Instance Method	               self নেয়, object-এর data নিয়ে কাজ করে

"""






##### 17) একসাথে সব concept — Master Example
class User:
   def __init__(self, name, email, age):
      self.name = name  # instance variable
      self.email = email # instance variable
      self.age = age  # instance variable


   def show_profile(self): # instance method
      print("Name:", self.name)
      print("Email:", self.email)
      print("Age:", self.age)


   def is_adult(self): # instance method
      return self.age > 18
   
   def change_email(self, new_email): # instance method
      self.email = new_email


user1 = User("Jhon", "jhon123@gmail.com", 25)
user1.show_profile()
print("Adult?:", user1.is_adult())

user1.change_email("jhon@gmail.com")
user1.show_profile()

print("___________________________________\n")

user2 = User("Alex", "alex123@gmail.com", 16)
user2.show_profile()
print("Adult?:", user2.is_adult())

user2.change_email("alex@gmail.com")
user2.show_profile()

"""
এখানে identify করো
Class:
User

Objects:
user1
user2

Constructor:
def __init__(self, name, email, age):


Instance Variables:
self.name
self.email
self.age


Instance Methods:
show_profile()
is_adult()
change_email()

"""







##### 18) Backend-এর জন্য কেন এত important?
"""
কারণ backend-এ তুমি এ ধরনের class অনেক বানাবে:

User
Product
Order
Cart
Invoice
Payment
BlogPost
Comment

"""
# উদাহরণ:
class Order:
   def __init__(self, user, items):
      self.user = user 
      self.items = items 

   def total_items(self):
      return len(self.total_items)
   
# এভাবেই real project-এ data model করা হয়।






##### 19) Common mistakes
"""
Mistake 1: self না লেখা
❌ Wrong
class User:
    def __init__(name, email):
        self.name = name

✅ Correct
class User:
    def __init__(self, name, email):
        self.name = name

        

Mistake 2: self.name = name না দিয়ে শুধু name = name
❌ Wrong
class User:
    def __init__(self, name):
        name = name

এতে object-এ কিছু save হবে না।

✅ Correct
class User:
    def __init__(self, name):
        self.name = name



Mistake 3: method call না করে print করা
user1.show_info
এটা method execute করবে না।

সঠিক:
user1.show_info()

"""







