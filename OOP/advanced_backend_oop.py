


## Problem 41: Product Class(Basic Model)
class Product:
   def __init__(self, name, price):
      self.name = name 
      self._price = price

   def show(self):
      return f"Product: {self.name}, Price:{self._price}"
   
p1 = Product("Mouse", 1000)
print(p1.show())


## Problem 42: Cart System
class Product:
   def __init__(self, name, price):
      self.name = name 
      self._price = price

   
class Cart:
   def __init__(self):
      self.items = []

   def add_products(self, product):
      self.items.append(product)

   def show_cart(self):
      return [p.name for p in self.items]
   
cart = Cart()
cart.add_products(Product("Laptop", 50000))
cart.add_products(Product("Mouse", 500))

print(cart.show_cart())



## Problem 43: Total Cart Price
class Product:
   def __init__(self, name, price):
      self.name = name 
      self._price = price

class Cart:
   def __init__(self):
      self.items = []

   def add_product(self, product):
      self.items.append(product)

   def total_price(self):
      total = 0
      for item in self.items:
         total += item._price
      return total 
   

cart = Cart()
cart.add_product(Product("Laptop", 50000))
cart.add_product(Product("Keyboard", 2000))

print(cart.total_price())


## Problem 44: Inventory System
class Product:
   def __init__(self, name, stock):
      self.name = name 
      self.stock = stock 

class Inventory:
   def __init__(self):
      self.products = {}

   def add_products(self, name, stock):
      self.products[name] = stock 

   def sell(self, name, qty):
      if name in self.products and self.products[name] >= qty:
         self.products[name] -= qty 
         return "Sold"
      return "Not available"
   
   def show(self):
      return self.products
   
inv = Inventory()

inv.add_products("Laptop", 10)
print(inv.show())

inv.sell("Laptop", 5)
print(inv.show())


## Problem 45: User Login System
class User:
   def __init__(self, username, password):
      self.username = username
      self.password = password

class AuthSystem:
   def login(self, user, username, password):
      if user.username == username and user.password == password:
         return "Login Success"
      return "Login Failed"
   
u = User("Mamun", "12345")
auth = AuthSystem()

print(u.username)
print(u.password)
print(auth.login(u, "Mamun", "12345"))
print(auth.login(u, "Mamun", "1234"))