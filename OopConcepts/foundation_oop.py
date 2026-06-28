


"""
OOP Problem 1-10

Focus:
Class
Object
Attribute
Method
__init__()
Instance Variable
Instance Method

"""


# Problem 1: Create a Simple class
class Car:
   def __init__(self, brand):
      self.brand = brand

c = Car("Toyota")
print(c.brand)


# Problem 2: Student Class with Name and Age
class Student:
   def __init__(self, name, age):
      self.name = name 
      self.age = age 


student1 = Student("Mamun" , 25)
student2 = Student("Nondita", 16)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# Problem 3: Add an Instance Method
class Student:
   def __init__(self, name):
      self.name = name 

   def introduce(self):
      return (f"My name is {self.name}.")

s1 = Student("Mamun Bepari")
print(s1.introduce())


# Problem 4: Rectangle Area
class Rectangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height

   def area(self):
      return self.width * self.height
   

r = Rectangle(10, 5)
print(r.area())


# Problem 5: BankAccount Balance Show
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

   def show_balance(self):
      return f"{self.owner}'s current balance is {self.balance}tk."
   

account = BankAccount("Habib Mamun", 25000)
print(account.show_balance())


# Problem 6: Update Attribute value
class Book:
   def __init__(self, title):
      self.title = title


book = Book("Python Basics")
print("Old title:", book.title)

book.title = "Advanced Python"
print("New title:", book.title)


# Problem 7: Add Method to Increase Balance 
class BankAccount:
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount 


account = BankAccount("Nondita Biswsas", 20000)
print(account.balance)

account.deposit(20000)
print(account.balance)


# Problem 8: Product Price with Discount
class Product:
   def __init__(self, name, price):
      self.name = name 
      self.price = price

   def discount_price(self, discount):
      self.price -= discount
      return f"{self.name}'s price is: {self.price}"
   
product = Product("Laptop", 50000)
print(product.name)
print(product.price)

print(product.discount_price(10000))


# Problem 9. Employee Annual Salary
class Employee:
   def __init__(self, name, monthly_salary):
      self.name = name 
      self.monthly_salary = monthly_salary

   def annual_salary(self):
      return self.monthly_salary * 12
   

emp = Employee("MarkJukarbark", 25000)
print(emp.name)
print(emp.monthly_salary)
print(emp.annual_salary())


# Problem 10: Counter Class
class Counter:
   def __init__(self):
      self.value = 0

   def increament(self):
      self.value += 1

c1 = Counter()
print(c1.value)

c1.increament()
c1.increament()
print(c1.value)



## খুব গুরুত্বপূর্ণ Pattern (এগুলো মুখস্থ না, বুঝে ফেলো)
# Pattern 1: Basic Class 
class ClassName:
   def __init__(self, value):
      self.value = value 

# Pattern 2: Print Method 
class Student:
   def __init__(self, name):
      self.name = name 

   def show(self):
      print(self.name)

# Pattern 3: Clacultion Method:
class Rectangle:
   def __init__(self, w, h):
      self.w = w 
      self.h = h 

   def area(self):
      return self.w * self.h 
   
# Pattern 4: Update Value
class Counter:
   def __init__(self):
      self.value = 0

   def increment(self):
      self.value += 1




## Task 1:
class Dog:
   def __init__(self, name, color):
      self.name = name 
      self.color = color 

   def bark(self):
      return f"Woof! I am {self.name}."
   
d = Dog("Tommy", "Brown")

print("Name:", d.name)
print("Color:", d.color)
print(d.bark())


## Task 2:
class Circle:
   def __init__(self, radius):
      self.radius = radius

   def area(self):
      return 3.1416 * self.radius ** 2
   
circle = Circle(5)

print(circle.radius)
print(int(circle.area()))


## Task 3:
class User:
   def __init__(self, username, email):
      self.username = username
      self.email = email

   def show_info(self):
      return f"My name is {self.username} and My email is {self.email}."
   
u = User("Mamun Bepari", "mamun@gmail.com")

print(u.username)
print(u.email)
print(u.show_info())


## Task 4:
class Wallet:
   def __init__(self, balance):
      self.balance = balance

   def add_money(self, amount):
      self.balance += amount 
      return f"Add New Balance: {amount}"

   def spend_money(self, amount):
      if amount <= self.balance:
         self.balance -= amount
      else:
         print("Insufficient Balance")
   

w = Wallet(10000)

print(w.balance)
print(w.add_money(10000))
print(w.balance)

w.spend_money(15000)
print(w.balance)

w.spend_money(10000)
print(w.balance)


## Task 5:
class Movie:
   def __init__(self, title, rating):
      self.title = title
      self.rating = rating

   def is_hit(self):
      return self.rating >= 8
   

m = Movie("12th fail", 9)
print(m.title)
print(m.rating)
print(m.is_hit())

m2 = Movie("Inception", 6.5)
print(m2.title)
print(m2.rating)
print(m2.is_hit())