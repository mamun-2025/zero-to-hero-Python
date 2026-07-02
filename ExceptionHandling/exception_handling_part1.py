

"""
Exception Handling in Python — Part 1

আজ আমরা এই ১০টা জিনিস শিখব:

1. Exception / Error আসলে কী
2. কেন exception handling দরকার
3. try
4. except
5. try + except flow
6. specific exception
   ValueError
   ZeroDivisionError
   TypeError
   IndexError
   KeyError
   FileNotFoundError
7. else
8. finally
9. multiple except
10. backend-style real examples

"""

## 1) Exception / Error আসলে কী?
"""
Python program run করার সময় যদি এমন কিছু ঘটে যেটা Python execute করতে পারে না, 
তখন error / exception হয়।

print(10/0)
এখানে error হবে, কারণ 0 দিয়ে division করা যায় না।
(ZeroDivisionError)

num = int("abc")
print(num)
"abc" কে integer বানানো যাবে না।
তাই Python ValueError দিবে।

num = [10, 20, 30]
print(num[5])
এখানে list-এ index 5 নেই।
তাই IndexError হবে।

data = {"name": "mamun"}
print(data["age"])
এখানে "age" key নেই।
তাই KeyError হবে।

"""




## 2) Exception Handling কেন দরকার?
"""
যদি error handle না করো, program সাথে সাথে crash করবে।

# Without exception handling
num = int(input("Enter a number: "))
print(int(100/num))
print("Program Ended.")

যদি user 0 দেয় → ZeroDivisionError
যদি user abc দেয় → ValueError
তখন program crash করবে, নিচের line run হবে না।

# With exception handling
আমরা চাই:
program crash না করুক
user-friendly message দিক
system stable থাকুক
backend API fail না করে proper response দিক

"""




## 3) try কী?
"""
try block-এর ভিতরে সেই code রাখি যেটা error দিতে পারে।

Syntax:

   try:
      risky_code

কিন্তু try একা ব্যবহার করা যায় না।
এর সাথে except বা finally লাগবে।

"""




## 4) except কী?
"""
except block error ধরার জন্য ব্যবহার হয়।

Syntax:
      try:
         risky_code
      except:
         error_handle_code

"""




## 5) example — try + except
try:
   num = int(input("Enter a number: "))
   print(100/num)
except:
   print("Something went wrong.")

"""
Problem with bare except:

উপরে code কাজ করে, কিন্তু এটা best practice না।

কারণ:
কোন error হয়েছে বোঝা যাচ্ছে না
সব error একসাথে ধরে ফেলছে

তাই আমাদের specific exception ধরতে হবে।

"""




## 6) Specific Exception — একদম গুরুত্বপূর্ণ অংশ
# 1.ValueError
try:
   age = int(input("Enter age: "))
   print(age)
except ValueError:
   print("Please enter a valid integer.")


# 2. ZeroDivisionError
try:
   num = int(input("Enter number: "))
   print(100/num)
except:
   print("Cannot divide by division.")


# 3. TypeError
try:
   result = "10" + 5
   print(result)
except TypeError:
   print("Cannot add string and integer.")


# 4. IndexError
try:
   numbers = [10, 20, 30]
   print(numbers[5])
except IndexError:
   print("Index out of range")

nums = [10, 20, 30]
try: 
    index = int(input("Enter index: "))
    print(nums[index])
except IndexError:
    print("Index out of range.")

    

# 5. KeyError
user = {"name": "mamun", "age": 25}
try:
   print(user["email"])
except KeyError:
   print("Key not found.")


# 6. FileNotFoundError
try:
   file = open("data.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
   print("File not found.")



## 7) একসাথে multiple exception handle করা
try:
   num = int(input("Enter number: "))
   print(100/num)
except ValueError:
   print("Please enter a number.")
except ZeroDivisionError:
   print("Cannot divide by zero.")



## 8) else block কী?
# else block তখনই run হবে যখন try block-এ কোনো error হবে না।
"""
   try:
      risky_code
   except SomeError:
      handle_error_code
   else:
      success_code

"""
# Example:
try:
   num = int(input("Enter a number: "))
   result = 100 / num 
except ValueError:
   print("Invalid Number")
except ZeroDivisionError:
   print("Cannot divide by zero")
else:
   print("Result:", int(result))



## 9) finally block কী?
# finally সবসময় run হবে, error হোক বা না হোক।
try:
   num = [10, 20, 30]
   print(num[3])
except IndexError:
   print("Index out of range.")
finally:
   print("Program finished.")

"""
finally কোথায় useful?

file close করা
database connection close করা
cleanup করা
resource release করা

"""


## 10) try + except + else + finally একসাথে
# এটা খুব important structure।
try:
   num = int(input("Enter a number: "))
   result = 100 / num 
except ValueError:
   print("Enter a valid number, Please.")
except ZeroDivisionError:
   print("Cannot divide by zero")
else:
   print("Result:", result)
finally:
   print("Execution Completed.")



## 11) Real Backend-Style Example 1 — 
# API Response থেকে age বের করা
user = {
    "name": "Mamun",
    "age": "25"
}

try:
    age = int(user["age"])
except KeyError:
    print("age key missing")
except ValueError:
    print("age is not a valid number")
else:
    print("Age:", age)



## 12) Real Backend-Style Example 2 — 
# Login input validation
try:
    username = input("Enter username: ")
    age = int(input("Enter age: "))

except ValueError:
    print("Age must be a number")

else:
    print(f"Username: {username}, Age: {age}")

finally:
    print("Program finished.")



## 13) Real Backend-Style Example 3 — 
# Dictionary + List + Exception
users = [
    {"name": "Mamun", "age": 25},
    {"name": "Rahim", "age": 22}
]

try:
    print(users[1]["name"])
except IndexError:
    print("User index not found")
except KeyError:
    print("Name key missing.")
finally:
    print("Execution Completed")



## 14) except Exception as e — এটা কী?
try:
    num = int("abc")
except Exception as e:
    print("Error:", e)

# কিন্তু এটা কি সবসময় ব্যবহার করা উচিত?
# Best practice:
# আগে specific exception ধরো
# generic Exception fallback হিসেবে রাখতে পারো
try:
    num = int(input("Enter number: "))
    print(100 / num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("Unexpected error:", e)



## 15) Common Exception Summary Table
"""
ValueError	         ভুল value/type conversion, যেমন int("abc")
ZeroDivisionError	   0 দিয়ে divide করলে
TypeError	         incompatible types নিয়ে operation
IndexError	         invalid list index
KeyError	            dictionary key না থাকলে
FileNotFoundError	   file না থাকলে

"""

name = input("Enter Name: ")

try:
    age = int(input("Age:" ))
    result = 100 / age 
except ValueError:
    print("Invalid age")
except ZeroDivisionError:
    print("Age cannot be zero")
else:
    print("Hello", name)
    print(result)



## 16) Mini mental model
"""
   try

   “এই অংশে error হতে পারে”

   except

   “যদি error হয়, তাহলে এভাবে handle করো”

   else

   “যদি error না হয়, তাহলে এটা চালাও”

   finally

   “যাই হোক, এটা সবসময় চালাও”

"""


## 21) Backend-style Example: 
# JSON-like dictionary access
response = {
   "users": {
      "name": "Mamun"
   }
}

try:
   print(response["users"]["email"])
except KeyError:
   print("Email key is missing.")




## 22) Backend-style Example: 
# API price calculation
product = {
   "name": "Phone",
   "price": "20000"
}

try: 
   price = int(product["price"])
   discount = int(input("Enter discount percent: "))
   final_price = price - (price * discount / 100)
   print("Final Price: ", int(final_price))

except ValueError:
   print("Discount must be a number.")

except KeyError:
   print("Product data is missing")




## 23) One except for multiple exeptions
# তুমি চাইলে একসাথে একাধিক exception ধরতে পারো:
try:
   num = int(input("Enter number: "))
   print(100 / num)

except (ValueError, ZeroDivisionError) as e:
   print("Error:", e)




## 24) Mini Example: Login Simulation
user = {
   "username": "mamun",
   "password": "1234"
}

try:
   username = input("Enter username: ")
   password = input("Enter password: ")

   if username != user["username"]:
      raise ValueError("Invalid username")

   if password != user["password"]:
      raise ValueError("Invalid password")
   
   print("Login successful.")

except ValueError as e:
   print("Login failed:", e)


raise ValueError("Invalid username")