

# not Operator in Python
"""
The not keyword in Python is a logical operator used to obtain the negation or opposite Boolean value of an operand.

- It is a unary operator, meaning it takes only one operand and returns its complementary Boolean value.
- For example, if False is given as an operand to not, it returns True and vice versa.
"""

# 1. Python "not" operator with Variables
a = True
print(not a)

b = False
print(not b)

# 2. Using the "not" Boolean Operator in Python with Specific condition
print(not False)
print(not True)
print(not(True and False))
print(not(True or False))
print(not (5 > 7))

# 3. Using the Not Operator with different Value
s = "geek"
print(not s)

a = [1, 2, 3, 4]
print(not a)

d = {"geek": "sam",
     "collage": "Mit"
     }
print(not d)

es = ""
print(not es)

ed = {}
print(not ed)


# 4. Logical NOT operator with the list
a = [5, 10, 15, 20, 59, 86]
if not a:
   print("Inputted list is empty")
else:
   for i in a:
      if not(i % 5):
         if i not in (0, 10):
            print(i, "is not in range")
         else:
            print(i, "in range.")
      else:
         print(i, "is not multiple of 5")
