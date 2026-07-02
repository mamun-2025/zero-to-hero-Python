

"""
Exception Handling Part 3 — 30 Problems

আমি problems গুলো level-wise সাজাচ্ছি:

Level 1 — Basic try/except
Invalid integer input
Divide by zero
String → int conversion
List index error
Dictionary key error
Multiple exception handling
else block use
finally block use
Safe file open
User input validation

Level 2 — raise + validation
Negative age validation
Empty username validation
Short password validation
Invalid marks validation
Withdraw amount validation
Product stock validation
Price validation
Email validation
Mobile number validation
Positive number validation

Level 3 — Custom Exception + function/backend style
Custom InvalidAgeError
Custom InsufficientBalanceError
Custom ProductOutOfStockError
Custom InvalidRoleError
Login function validation
Register function validation
Deposit/withdraw system
API response key handling
JSON-like nested data validation
Full mini backend-style order processing

"""

## Problem 1 — Invalid integer input handle করো
try:
   number = int(input("Enter a number: "))
   print("You entered:", number)
except ValueError:
   print("Invalid input! Please enter a integer.")





## Problem 2 — Divide by zero handle করো
try:
   number = int(input("Enter number: "))
   print(100 / number)
except ZeroDivisionError:
   print("Cannot divide by zero.")


try:
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))

   result = num1 / num2 
   print(result)

except ZeroDivisionError:
   print("Error. Cannot division by zero.")






## Problem 3 — String কে int করতে গিয়ে error handle
s = "abc"

try:
   num = int(s)
   print("Converted number:", num)
except ValueError:
   print("Cannot convert string to integer.")






## Problem 4 — List index error handle করো
li = [10, 20, 30]

try:
   index = int(input("Enter index: "))
   print("Value:", li[index])
except IndexError:
   print("Invalid Index")





## Problem 5 — Dictionary key error handle করো
user = {
   "name": "mamun",
   "age": 25
}

try:
   print(user["email"])
except KeyError:
   print("Key not found in dictionary.")






## Problem 6 — Multiple exception handling
try:
   num = int(input("Enter number: "))
   result = 100 / num 
   print("Result:", result)
except ValueError:
   print("Invalid input. Please inter a integer number.")
except ZeroDivisionError:
   print("Division cannot by zero.")






## Problem 7 — else block use করো
try:
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   result = a / b 
except ZeroDivisionError:
   print("Divide cannot by zero.")
except ValueError:
   print("Invalid input.")
else:
   print("Division successfully.")
   print("Result:", result)





## Problem 8 — finally block use করো
try: 
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   print("Result:", a / b)
except Exception as e:
   print("Error:", e)
finally:
   print("Program Ended.")





## Problem 9 — File open safely
try:
   file = open("data.txt", "r")
   content = file.read()
   print(content)
   file.close()
except FileNotFoundError:
   print("File not found.")





## Problem 10 — Input validation with retry-like logic
try:
   user = int(input("Enter age: "))
   print("Your age is:", user)
except ValueError:
   print("Age must be interger number.")






## Problem 11 — Negative age validation with raise
try:
   age = int(input("Enter age:"))

   if age < 0:
      raise ValueError("Age cannot be negative.")
   
   print("Valid age:", age)

except ValueError as e:
   print("Error:", e)






## Problem 12 — Empty username validation
try:
   username = input("Enter username: ")

   if username == "":
      raise ValueError("Username must cannot be empty")
   
   print("Username is valid.")

except ValueError as e:
   print("Error:", e)






## Problem 13 — Short password validation
try:
   password = input("Enter a password: ")

   if len(password) < 6:
      raise ValueError("Password must be 6 characters.")
   
   print("Password is valid.")

except ValueError as e:
   print("Error:", e)






## Problem 14 — Invalid marks validation
try:
   marks = int(input("Enter marks: "))

   if marks < 0 or marks > 100:
      raise ValueError("Marks must be between 0 and 100")
   
   print("Valid marks: ", marks)

except ValueError as e:
   print("Error:", e)






## Problem 15 — Withdraw amount validation
try:
   amount = float(input("Enter withdraw amount: "))

   if amount <= 0:
      raise ValueError("Enter amount must be greater than 0.")
   
   print("Withdraw request accepted.")

except ValueError as e:
   print("Error:", e)






## Problem 16 — Product stock validation
stock = 10

try:
   quantity = int(input("Enter product: "))
   if quantity > stock:
      raise ValueError("Not enough stock available.")
   
   print("Order placed successfully.")

except ValueError as e:
   print("Error:", e)






## Problem 17 — Price validation
try:
   price = float(input("Enter product price: "))

   if price < 0:
      raise ValueError("Price cannot be negative.")
   
   print("Valid Price")

except ValueError as e:
   print("Error:", e)






## Problem 18 — Email validation
try:
   email = input("Enter Email: ")

   if "@" not in email:
      raise ValueError("Invalid email address.")
   
   print("Valid Email")

except ValueError as e:
   print("Error:", e)






## Problem 19 — Mobile number validation
try:
   phone = input("Enter your phone number: ")

   if not phone.isdigit():
      raise ValueError("Phone number must contain only digits.")
   
   if len(phone) != 11:
      raise ValueError("Phone number must be exactly 11 digits")
   
   print("Phone number is valid.")

except ValueError as e:
   print("Error:", e)






## Problem 20 — Positive number validation
try:
   number = int(input("Enter a number: "))

   if number < 0:
      raise ValueError("Number must be positive")
   
   print("Number is valid.")

except ValueError as e:
   print("Error:", e)





## Problem 21 — Custom Exception: InvalidAgeError
class InvalidAgeError(Exception):
   pass 

try:
   age = int(input("Enter age: "))

   if age < 0:
      raise InvalidAgeError("Age cannot be negative.")
   
   print("Age is valid")

except InvalidAgeError as e:
   print("Custorm Error:", e)





## Problem 22 — Custom Exception: InsufficientBalanceError
class InsufficientBalanceError(Exception):
   pass 

balance = 1000

try:
   amount = float(input("Enter withdraw amount: "))

   if amount > balance:
      raise InsufficientBalanceError("Insufficient Balance")
   
   balance -= amount 
   print("Withdraw successfully")
   print("Remaining balance:", balance)

except InsufficientBalanceError as e:
   print("Transaction Error:", e)

   




## Problem 23 — Custom Exception: ProductOutOfStockError
class ProductOutOfStockError(Exception):
   pass 


stock = 20
try:
   qty = int(input("Enter product of stock: "))
   if qty > stock:
      raise ProductOutOfStockError("Product is out of stock.")
   
   print("Product avaiable")

except ProductOutOfStockError as e:
   print("StockError:", e)
   





## Problem 24 — Custom Exception: InvalidRoleError
class InvalidRoleError(Exception):
   pass 

allowed_roles = ["admin", "user", "manager"]

try: 
   role = input("Enter role: ")

   if role not in allowed_roles:
      raise InvalidRoleError("Invalid role selected")
   
   print("Role is valid")

except InvalidRoleError as e:
   print("Role Error:", e)






## Problem 25 — Login function validation
def login(username, password):
   if username == "":
      raise ValueError("Username is required.")
   
   if password == "":
      raise ValueError("Password is required.")
   
   return "Login validation passed"

try:
   result = login("", "1234")
   print(result)

except ValueError as e:
   print("Login error:", e)






## Problem 26 — Register function validation
def register(username, email, password):
   if username == "":
      raise ValueError("Username is required")
   
   if "@" not in email:
      raise ValueError("Invalid email")
   
   if len(password) < 6:
      raise ValueError("Password must be at least 6 characters.")
   

try:
   result = register("Mamun", "mamun@gmail.com", "12345")
   print(result)

except ValueError as e:
   print("Register Error:", e)






## Problem 27 — Deposit/Withdraw system
class InsufficientBalanceError(Exception):
   pass 

def deposit(balance, amount):
   if amount <= 0:
      raise ValueError("Depostit must be greater than 0")
   return balance + amount

def withdraw(balance, amount):
   if amount <= 0:
      raise ValueError("Withdraw amount must be greater than 0")
   
   if amount > balance:
      raise InsufficientBalanceError("Insufficient balance.")
   
   return balance - amount

try:
   balance = 10000

   balance = deposit(balance, 500)
   print("After deposit:", balance)

   balance = withdraw(balance, 300)
   print("After withdraw:", balance)

   balance = withdraw(balance, 2000)
   print("After withdraw:", balance)

except ValueError as e:
   print("Value Error:", e)

except InsufficientBalanceError as e:
   print("Balance Error:", e)






## Problem 28 — API response key handling
response = {
   "success": True,
   "data": {
      "name": "Mamun"
   }
}

try:
   user = response["data"]["email"]
   print(user)
except KeyError as e:
   print("Missing key in API response:", e)






## Problem 29 — Nested JSON-like data validation
students = {
   "name": "Mamun", 
   "address": {
      "country": "Bangladesh"
   }
}

try:
   student = students["address"]["city"]
   print(student)

except KeyError as e:
   print("Missing nessted key:", e)






## Problem 30 — Mini backend-style order processing system
class OutofStockError(Exception):
   pass 

def place_order(product_name, quantity, stock, price):
   if product_name == "":
      raise ValueError("Product name is required.")
   
   if quantity <= 0:
      raise ValueError("Quantity must be greater than 0")
   
   if stock <= 0:
      raise OutofStockError("Product is out of stock.")
   
   if quantity > stock:
      raise OutofStockError("Requested quantity exceeds stock")
   
   if price < 0:
      raise ValueError("Price cannot be negative")
   
   total = quantity * price
   return total

try:
   total_price = place_order(
      product_name="Keyboard",
      quantity=3,
      stock=5,
      price=1000
   )

   print("Order placed successfully.")
   print("Total Price:", total_price)

except ValueError as e:
   print("Validation Error:", e)

except OutofStockError as e:
   print("Stock Error:", e)




# What you leaned from these 30 problems:
"""
Basic:
try
except
else
finally

Built-in Exceptions:
ValueError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError

Validation:
empty input validation
age validation
marks validation
phone validation
email validation
price validation
quantity validation

Advanced:
raise
custom exception
function-based validation
backend-style flow
API response key handling
nested JSON validation

"""
