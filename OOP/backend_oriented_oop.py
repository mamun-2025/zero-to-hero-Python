


"""
তোমার _balance ব্যবহার করার মাধ্যমে encapsulation-এর protected convention অনুসরণ করা হয়েছে।
যদি সত্যিকারের private attribute দেখাতে চাও, তাহলে __balance ব্যবহার করবে।
"""

## Problem 31: Simple Bank Account
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self._balance = balance

   def deposit(self, amount):
      if amount > 0:
         self._balance += amount 
      
   def withdraw(self, amount):
      if amount <= self._balance and amount > 0:
         self._balance -= amount 
      else:
         print("Insufficeint balance")

   def get_balance(self):
      return self._balance
   

b = BankAccount("Rudro Ahamed", 30000)
print(b.owner)
b.deposit(5000)
print(b.get_balance())

b.withdraw(5000)
print(b.get_balance())

b.withdraw(-100)
print(b.get_balance())


## Problem 32: Encapsulation with Validation
class BankAccount:
   def __init__(self, owner, balance=0):
      self.owner = owner
      self.__balance = balance

   def deposit(self, amount):
      if amount <= 0:
         return "Invalid deposit"
      self.__balance += amount
      return "Deposited"
   
   def withdraw(self, amount):
      if amount <= 0:
         return "Invalid withdraw"
      
      if amount > self.__balance:
         return "Not enough balance"
      
      self.__balance -= amount
      return "Withdraw Successful"
   
   def get_balance(self):
      return self.__balance
   

b = BankAccount("Nondita", 35000)
print(b.owner)
print(b.get_balance())

print(b.deposit(100))
print(b.deposit(-100))
print(b.get_balance())

print(b.withdraw(-100))
print(b.withdraw(35200))
print(b.withdraw(100))
print(b.get_balance())



## Problem 33: Class Variable(Shared Data)
class Student:
   total_students = 0
   
   def __init__(self, name):
      self.name = name 
      Student.total_students += 1

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")
s4 = Student("D")
s5 = Student("E")

print(Student.total_students)



## Problem 34: Class Method
class Student:
   total_students = 0

   def __init__(self, name):
      self.name = name 
      Student.total_students += 1

   @classmethod
   def get_total_students(cls):
      return cls.total_students
   
s1 = Student("Mamun")
s2 = Student("Habib")

print(Student.get_total_students())


## Problem 35: Static Method
class MathUtils:
   @staticmethod
   def is_even(number):
      return number % 2 == 0
   
print(MathUtils.is_even(10))
print(MathUtils.is_even(17))
"""
Explanation
object দরকার নেই
class namespace এর ভিতরে function
"""


## Problem 36: Property Decorator
class Person:
   def __init__(self, name, age):
      self.name = name 
      self._age = age 

   @property
   def age(self):
      return self._age
   
   @age.setter
   def age(self, value):
      if value < 0:
         print("Invalid age")
      else:
         self._age = value


p = Person("Alex", 30)
print(p.name)
print(p.age)

p.age = 25
print(p.age)

p.age = -5


## Problem 37: Inheritance(User System)
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email

   def login(self):
      return f"{self.name} logged in."

class Admin(User):
   def delete_user(self):
      return f"{self.name} deleted a user."
   
a = Admin("Mamun", "mamun123@gmail.com")

print(a.name)
print(a.email)
print(a.login())
print(a.delete_user())


## Problem 38: Method Overriding(API Style)
class User:
   def login(self):
      return "User logged in."
   
class Admin(User):
   def login(self):
      return "Admin logged in with extra security."
   
u = User()
a = Admin()

print(u.login())
print(a.login())


## Problem 39: Polymorphisim(Notification System)
class EmailNotification:
   def send(self):
      return "Email sent."
   
class SmsNotification:
   def send(self):
      return "Sms sent."
   
class PushNotification:
   def send(self):
      return "Push sent."
   
notifications = [EmailNotification(), SmsNotification(), PushNotification()]

for n in notifications:
   print(n.send())



## Problem 40: __repr__(Debug friendly object)
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email 

   def __repr__(self):
      return f"User(name={self.name}, email={self.email})"
   

u = User("Mamun" , "mamun@gmail.com")
print(u.name)
print(u.email)
print(u)
print(u.__repr__())

"""
Explanation
__repr__ → developer-friendly output
debugging time খুব useful
"""

