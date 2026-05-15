
"""
The and keyword in Python is a logical operator used to combine two conditions.
It returns True if both conditions are true, otherwise, it returns False.
It is commonly used in if statements, loops and Boolean expressions.
"""

x = 10
y = 5

if x > 0 and y > 0:
   print("Both conditions are true.")

if x < 0 and y > 0:
   print("One condition is false.")

if x < 0 and y < 0:
   print("Both conditions are false.")


# 1. Using and in conditional Statements
age = 25
salary = 22000

if age > 18 and salary > 20000:
   print("Eligible for a credit card")


# 2. Using and in loops
a = 1

while a < 10 and a % 2 != 0:
   print(a)
   a += 2


# 3. Using and with Boolean Values
a = True
b = False

print(a and b)
print(a and True)
print(False and False)