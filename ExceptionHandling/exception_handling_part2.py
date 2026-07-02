

"""
Exception Handling in Python- Part 2

আজ যা শিখবে

raise → নিজের হাতে error throw করা
Custom Exception → নিজের error class বানানো
Multiple except → একাধিক error আলাদা handle করা
Nested try-except → try-এর ভিতরে try
Function-এর ভিতরে exception handling
Real backend style validation example

"""

## 1) raise — নিজের হাতে error throw করা
"""
যখন Python নিজে error দেয় না, কিন্তু তুমি business rule ভাঙলে error দিতে চাও।

যেমন:
age negative হতে পারবে না
password খুব ছোট হলে হবে না
balance insufficient হলে transaction হবে না

"""
# Negative age হলে error দাও
# age = -5

# if age < 0:
#    raise ValueError("Age cannot be negative.")

# print("Valid age")

# Positive age হলে ঠিক চলবে
age = 10

if age < 0:
   raise ValueError("Age cannot be negative.")

print("Valid age")



## 2) raise + try-except একসাথে
try:
   age = 10

   if age < 0:
      raise ValueError("Age cannot be negative.")
   
   print("Age is valid.")

except ValueError as e:
   print("Error:", e)

"""
Step by step:

try block শুরু
age = -10
if age < 0 → True
raise ValueError("Age cannot be negative")
control চলে যাবে except ValueError as e
e-তে error message থাকবে

"""



## 3) Practical Example — password validation
password = "1234"

try:
   if len(password) < 6:
      raise ValueError("Password must be at least 6 charecters long.")
   
   print("Password is valid.")

except ValueError as e:
   print("Validation Error:", e)



## 4) raise কেন important?
"""
কারণ backend-এ অনেক rule থাকে:

email required
age must be positive
amount must be greater than 0
stock must be available
username already exists
invalid role
unauthorized access

এইসব জায়গায় raise খুব কাজে লাগে।

"""



## 5) Custom Exception — নিজের error class বানানো
"""
এখন ধরো, তুমি generic ValueError না দিয়ে নিজের meaningful error দিতে চাও।

যেমন:

InvalidAgeError
InsufficientBalanceError
ProductOutOfStockError
AuthenticationError

এগুলোর জন্য custom exception বানানো হয়।

"""



## 6) Custom Exception basic syntax

class MyError(Exception):
   pass 

# MyError = তোমার custom error class
# Exception = Python-এর base exception class
# pass = এখনো ভিতরে কিছু লিখছি না




## 7) Example: InvalidAgeError
class InvalidAgeError(Exception):
   pass 

age = -2

try:
   if age < 2:
      raise InvalidAgeError("Age cannot be negative.")
   
   print("Age is valid.")

except InvalidAgeError as e:
   print("Custom Error:", e)




## 8) আরেকটা Custom Exception — InsufficientBalanceError
class InsufficientBalanceError(Exception):
   pass 

balance = 500
withdraw = 1000

try:
   if withdraw > balance:
      raise InsufficientBalanceError("Not enough balance")
   
   balance -= withdraw
   print("Withdraw Successful. Remaining balance:", balance)

except InsufficientBalanceError as e:
   print("Transaction Failed:", e)




## 9) Custom Exception কেন useful?
"""
কারণ এতে error meaningful হয়।

ValueError দেখলে বোঝা যায় না কোন business rule ভাঙছে।
কিন্তু InsufficientBalanceError দেখলে সাথে সাথে বোঝা যায়:

“Balance কম ছিল”

এটাই backend code-এ clean design।

"""



## 10) Multiple except - আলাদা error আলাদা handle করা
try:
   number1 = int(input("Enter first number: "))
   number2 = int(input("Enter second number: "))

   result = number1 / number2
   print("Result:", int(result))

except ValueError:
   print("Please enter valid interges.")

except ZeroDivisionError:
   print("Cannot divide by zero.")



## 11) একই error message variable-এ ধরতে চাইলে
try:
   x = int("abc")
except ValueError as e:
   print("Error message:", e)




## 12) Multiple exceptions in one block
# যদি দুইটা exception একইভাবে handle করতে চাও:
try:
   num = int(input("Enter number: "))
   result = 10 / num 
   print(result)

except (ValueError, ZeroDivisionError) as e:
   print("Invalid input or division by zero.")




## 13) Nested try-except
try:
   print("Outer try started")

   try:
      num = int(input("Enter a number: "))
      result = 10 / num 
      print("Result:", int(result))

   except ZeroDivisionError:
      print("Inner Error: Cannot divide by zero.")

except ValueError:
   print("Outer Error: Invalid number")





## 14) Nested try-except বুঝার সহজ rule
# Inner try আগে error ধরার চেষ্টা করবে
# inner না পারলে outer try ধরবে




## 15) Function-এর ভিতরে exception handling
# Example 1: divide function
def divide(a, b):
   try: 
      result = a / b 
      return result
   
   except ZeroDivisionError:
      return "Cannot divide by zero"
   
print(divide(10, 2))
print(divide(10, 0))




## 16) Function + raise
def get_age(age):
   if age < 0:
      raise ValueError("Age cannot be negative.")
   return age 

try:
   print(get_age(-5))
except ValueError as e:
   print("Error:", e)




## 17) Function + custom exception
class InvalidAmountError(Exception):
   pass 


def deposit(amount):
   if amount <= 0:
      raise InvalidAmountError("Deposit amount must be greater than 0")
   return f"Deposited {amount} seuccessfully."

try:
   print(deposit(10000))
except InvalidAmountError as e:
   print("Deposit Error:", e)




## 18) Real Backend Style Example — Login Validation
# Problem:
# username empty হলে error
# password empty হলে error
# password 6 characters-এর কম হলে error

def login(username, password):
   if not username:
      raise ValueError("Username is required.")
   
   if not password:
      raise ValueError("Password is required.")
   
   if len(password) < 6:
      raise ValueError("Password must be at least 6 characters.")
   
   return "Login Validation Passed."

try:
   result = login("mamun", "123456")
   print(result)

except ValueError as e:
   print("Login Error:", e)




## 19) আরেকটা backend-style example — Withdraw System
class InsufficientBalanceError(Exception):
   pass 

def withdraw(balance, amount):
   if amount <= 0:
      raise ValueError("Withdraw amount must be greater than 0")
   
   if amount > balance:
      raise InsufficientBalanceError("Insufficient balance")
   
   return balance - amount


try:
   new_balance = withdraw(10000, 1500)
   print("New Balance:", new_balance)

except ValueError as e:
   print("Value Error:", e)

except InsufficientBalanceError as e:
   print("Balance Error:", e)




## 20) খুব important summary
"""
raise:
নিজে error তৈরি করতে
raise ValueError("message")


Custom Exception:
নিজের error class
class MyError(Exception):
    pass
    

Multiple except:
ভিন্ন error আলাদা handle
except ValueError:
except ZeroDivisionError:


Nested try:
try-এর ভিতরে try

Function exception handling:
backend-এ সবচেয়ে বেশি কাজে লাগে

"""



## 21) Backend-এর জন্য কোনগুলো সবচেয়ে important?

"""
আমি priority দিয়ে বলছি:

Must know first
try
except
else
finally
raise
ValueError
KeyError
FileNotFoundError
Then must know
custom exception
function-এর ভিতরে exception handling
validation error handling
multiple except

"""