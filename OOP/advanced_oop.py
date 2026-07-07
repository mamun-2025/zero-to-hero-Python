

"""
Problem 21–30 শুরু করি —
এখানে থাকবে:

Inheritance
Multiple Inheritance
Method Overriding
super()
Polymorphism
Abstract Class
Magic Methods শুরু

"""
## Problem 21: Method Overriding
class Animal:
   def sound(self):
      return "Animal makes sound."

class Dog(Animal):
   def sound(self):
      return "Dog barks"
"""
এখানে Dog, Animal থেকে inherit করেছে।
কিন্তু Dog নিজের sound() method লিখেছে।
এটাই method overriding।
"""

a = Animal() 
print(a.sound())

d = Dog()
print(d.sound())



## Problem 22: Method Overriding with super()
class Employee:
   def show_role(self):
      return "Employee"
   

class Manager(Employee):
   def show_role(self):
      parent_role =  super().show_role()
      return f"{parent_role} - Manager"
   
m = Manager()
print(m.show_role())

"""
যদি parent class-এর logic রাখতে চান, 
কিন্তু child class-এ extra behavior যোগ করতে চান — 
তখন super() দরকার হয়।
"""


## Problem 23: super() with Constructor
class Person:
   def __init__(self, name):
      self.name = name 

class Student(Person):
   def __init__(self, name, student_id):
      super().__init__(name)
      self.student_id = student_id

   def show_info(self):
      return f"Name: {self.name}, ID: {self.student_id}"
   

s = Student("mamun", "101")

print(s.name)
print(s.student_id)
print(s.show_info())



## Problem 24: Polymorphisim(Same method name, different behavior)
class Cat:
   def speak(self):
      return "Cat meow"

class Dog:
   def speak(self):
      return "Dog bark"
   
class Cow:
   def speak(self):
      return "Cow moo"
   
animals = [Cat(), Dog(), Cow()]

for animal in animals:
   print(animal.speak())

# একই method name → different object → different behavior


## Problem 25: Polymorphisim with Payment System 
class BkashPayment:
   def pay(self, amount):
      return f"Paid {amount} using bkash."
   
class CardPayment:
   def pay(self, amount):
      return f"Paid {amount} using card."


class CashPayment:
   def pay(self, amount):
      return f"Paid {amount} using cash."


payments = [BkashPayment(), CardPayment(), CashPayment()]

for payment in payments:
   print(payment.pay(500))

"""
কেন এটা important?
Backend-এ payment gateway / notification / file storage system-এ এই pattern খুব common।

যেমন:
StripePayment
PaypalPayment
SSLCommerzPayment

সবগুলোর method name same হতে পারে

"""


## Problem 26: Abstract Class(Basic):
from abc import ABC, abstractmethod

class Shape(ABC):
   @abstractmethod
   def area(self):
      pass 

class Rectangle(Shape):
   def __init__(self, weight, height):
      self.weight = weight
      self.height = height

   def area(self):
      return self.weight * self.height
   

r = Rectangle(10, 5)
print(r.area())
"""
Important
যদি Rectangle area() না লিখত, 
তাহলে object তৈরি করতে error দিত।
"""


## Problem 27: Abstract Class With Multiple Child Classes
from abc import ABC, abstractmethod

class Notification(ABC):
   @abstractmethod
   def send(self, message):
      pass 

class EmailNotification(Notification):
   def send(self, message):
      return f"Email Sent: {message}"
   
class SmsNotification(Notification):
   def send(self, message):
      return f"Sms Sent: {message}"
   

notifications = [EmailNotification(), SmsNotification()]

for n in notifications:
   print(n.send("Your OTP is 1234"))

"""
কেন useful?
Real backend-এ notification system এভাবে design করা হয়:

email notification
sms notification
push notification

সবগুলোর common interface:
send(message)

"""


## Problem 28: Magic Method __str__
# __str__
# print(obj) readable করার জন্য।
class User:
   def __init__(self, name, email):
      self.name = name 
      self.email = email

   def __str__(self):
      return f"User(Name:{self.name}, Email:{self.email})"
   
u = User("Mamun", "mamun@gmail.com")
print(u)
print(u.__str__())



## Problem 29: Magic Method __len__
# __len__
# len(obj) support করার জন্য।
class Cart:
   def __init__(self):
      self.items = []
      
   def add_item(self, item):
      self.items.append(item)

   def __len__(self):
      return len(self.items)

   
cart = Cart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

print(len(cart))


## Problem 30: Magic Method __add__ and __eq__
# __add__, __eq__
# object + object, object == object support করার জন্য।
class Money:
   def __init__(self, amount):
      self.amount = amount

   def __add__(self, other):
      return Money(self.amount + other.amount)

   def __eq__(self, other):
      return self.amount == other.amount

   def __str__(self):
      return f"{self.amount}Taka" 
   

m1 = Money(500)
m2 = Money(1000)
m3 = Money(1500)

print(m1.amount)
print(m2.amount)

result = m1 + m2 

print(result)
print(result == m1)
print(result == m2)
print(result == m3)
