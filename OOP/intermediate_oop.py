

"""
OOP Problem 11–20

Focus:
Class Variable
Class Method
Static Method
Property
Encapsulation
Getter
Setter

"""
# Problem 11: Class Variable 
class Student:
   total_students = 0 # class variable

   def __init__(self, name):
      self.name = name 
      Student.total_students += 1

s1 = Student("Mamun")
s2 = Student("Habib")
s3 = Student("Karim")

print(s1.name)
print(s2.name)
print(s3.name)
print(Student.total_students)


## Problem 12: Show Class Variable with Class Method
class Student:
   total_students = 0

   def __init__(self, name):
      self.name = name 
      Student.total_students += 1

   @classmethod
   def show_total_students(cls):
      print("Total Students:", cls.total_students)

s1 = Student("Mamun")
s2 = Student("Nondita")

Student.show_total_students()

# এটা object দিয়েও call করা যায়, 
# কিন্তু সাধারণত class দিয়েই call করা ভালো।
s2.show_total_students()
"""
@classmethod
def show_total_students(cls):

এটা class method।
এখানে self না, cls ব্যবহার হয়।

self → object কে represent করে
cls → class কে represent করে

"""


## Problem 13: Alternative Constructor using Class Method
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email

   @classmethod
   def from_string(cls, data):
      name, email = data.split(",")
      return cls(name, email)
   
# return cls(name, email)
# এখানে cls মানে User class।
# মানে এটা essentially করছে:
# return User(name, email)

u1 = User.from_string("Mamun,mamun@gmail.com")
print(u1.name)
print(u1.email)
"""
কেন এটা useful?

Backend-এ অনেক সময় data আসে:
CSV line
config string
API string format
তখন class method দিয়ে object বানানো useful হয়।

"""

## Problem 14: Static Method
class MethaHelper:
   @staticmethod
   def is_even(number):
      return number % 2 == 0
   
print(MethaHelper.is_even(7))
print(MethaHelper.is_even(4))

"""
Static method:
self লাগে না
cls লাগে না
object/class data use না করেও কাজ করতে পারে

"""
class MathHelper:
   @staticmethod
   def is_odd(number):
      return number % 2 != 0
   
print(MathHelper.is_odd(5))
print(MathHelper.is_odd(8))


## Problem 15: Static Method for Validation
class EmailValidator:
   @staticmethod
   def is_valid(email):
      return "@" in email and "." in email
   
print(EmailValidator.is_valid("mamun@gmail.com"))
print(EmailValidator.is_valid("mamungmail.com"))
print(EmailValidator.is_valid("mamun"))

"""
কারণ email validation করার জন্য object state দরকার নেই।
এটা একটা utility কাজ।
"""


## Problem 16: Basci Encapsulation
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self._balance = balance # protected-like / internal use

   def show_balance(self):
      print(f"Balance:", self._balance)

b = BankAccount("Mamun", 20000)
print(b.owner)
b.show_balance()


## Problem 17: Getter Method 
# Getter কী?
# Getter হলো এমন method যেটা private/internal data read করতে দেয়।
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self._balance = balance

   def get_balance(self):
      return self._balance
   
acc = BankAccount("Nondita", 20000)

print(acc.owner)
print(acc.get_balance())


## Problem 18: Setter Method
# Setter কী?
# Setter হলো এমন method যেটা private/internal data update করতে দেয়, কিন্তু rules/check দিয়ে।
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self._balance = balance

   def get_balance(self):
      return self._balance
   
   def set_balance(self, new_balance):
      if new_balance >= 0:
         self._balance = new_balance
      else:
         print("Balance cannot be negative.")

acc = BankAccount("Sanjib", 50000)
print(acc.get_balance())

acc.set_balance(80000)
print(acc.get_balance())

acc.set_balance(-1000)
print(acc.get_balance())


## Problem 19: Property Getter
# @property কী?
# @property দিয়ে method-কে এমনভাবে ব্যবহার করা যায় যেন সেটা attribute মনে হয়।
class Product:
   def __init__(self, item, price):
      self.item = item
      self._price = price 

   @property
   def set_price(self):
      return self._price
   
p = Product("Mouse", 1000)
print(p.set_price)



## Problem 20: Property Setter
class Product:
   def __init__(self, name, price):
      self.name = name 
      self._price = price 

   # Getter
   @property
   def get_price(self):
      return self._price
   
   # Setter
   @get_price.setter
   def get_price(self, new_price):
      if new_price >= 0:
         self._price = new_price
      else:
         print("Price cannot be negative")

p = Product("Laptop", 40000)
print(p.name)
print(p._price)
print(p.get_price)

p.get_price = -10000
print(p.get_price)



#########################################################################
## খুব গুরুত্বপূর্ণ pattern summary
# Pattern 1: Class Variable
class A:
   count = 0
   
   def __init__(self):
      A.count += 1


# Pattern 2: Class Method
class A:
   total = 0

   @classmethod
   def show_total(cls):
      print(cls.total)


# Pattern 3: Static Method
class A:
   @staticmethod
   def helper(number):
      return number * 2
   

# Pattern 4: Getter/Setter
class A:
   def __init__(self, value):
      self._value = value
   
   def get_value(self):
      return self._value
   
   def set_value(self, new_value):
      if new_value >= 0:
         self._value = new_value
      else:
         print("Value cannot be negative.")

   
# Pattern 5: Property
class A:
   def __init__(self, value):
      self._value = value

   @property
   def get_value(self):
      return self._value
   
   @get_value.setter
   def get_value(self, new_value):
      if new_value >= 0:
         self._value = new_value
      else:
         print("Value cannot be negative.")


######
"""
Backend perspective থেকে কেন এগুলো গুরুত্বপূর্ণ ?

Class Variable:
total users count
default config
shared tax rate
role list

Class Method:
alternative constructor
DB row / JSON / CSV data থেকে object বানানো

Static Method:
validation
utility logic
helper calculation

Encapsulation / Getter / Setter / Property:
direct data access বন্ধ করা
validation enforce করা
business rule protect করা

"""

## Task 1:
class Employee:
   company = "Google"

   def __init__(self, name):
      self.name = name 

   def show_info(self):
      return f"Your company name is {Employee.company}"
   

e = Employee("Mamun")
print(e.name)
print(e.company)

print(e.show_info())


## Task 2:
class Temperture:
   @staticmethod
   def celcius_to_fahrenheit(number):
      return (number * 9/5) + 32
   
print(Temperture.celcius_to_fahrenheit(0))
print(Temperture.celcius_to_fahrenheit(25))
print(Temperture.celcius_to_fahrenheit(100))


## Task 3:
class User:
   def __init__(self, name, password):
      self.name = name 
      self._password = password

   # Getter
   def get_password(self):
      return self._password
   
   # Setter
   def set_password(self, new_password):
      if len(new_password) < 6:
         print("Password must be at least 6 characters.")
      else:
         self._password = new_password
         print("Password updated successfully.")

user = User("Habib Mamun", "abc123")
print(user.name)
print(user.get_password())

user.set_password("123abcd")
print(user.get_password())

user.set_password("123")
print(user.get_password())


## Task 4:
class Course:
   def __init__(self, name, fee):
      self.name = name 
      self._fee = fee

   @property
   def get_fee(self):
      return self._fee 
   
   @get_fee.setter
   def get_fee(self, new_fee):
      if new_fee > 0:
         self._fee = new_fee
      else:
         print("Fee cannot be negative.")


c = Course("Python Basics", 15000)
print(c.name)
print(c.get_fee)

c.get_fee = -10000
print(c.get_fee)
      

