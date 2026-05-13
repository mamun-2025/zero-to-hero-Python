
# In Python programming, Operators in general are used to perform operations on values and varaibles.
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Bitwise Operators
# 5. Assignment Operators
# 6. Identity Operators
# 7. Membership Operators
# 8. Ternary Operators
# 9. Precedence and Associativity of Operators



# ARITHMETIC OPERATORS
"""
Python operators are fundamental for performing mathematical calculations.
Arithmetic operators are symbols used to perform methematical operations on numerical values.
Arithmetic operators include addition(+), subtraction(-), multiplication(*), division(/) and modulas(%).
"""
# 1. Addition operator
value1 = 10
value2 = 5
result = value1 + value2
print(result) 


# 2. Subtraction Operator
value1 = 10
value2 = 5
result = value1 - value2
print(result)


# 3. Multiplication Operator
value1 = 2 
value2 = 3
result = value1 * value2
print(result)


# 4. Division Operator
# There are two types iof division operators
# 1. Float division
print(5/5)
print(10/2)
print(-10/2)
print(20.0/2)
print("__________________________")
result = 10 / 3
print(result)
print(type(result))
print(-17/5)
print("__________________________")


# 2. Foor division(interger)
print(10//3)
print(-5//2)
print(5.0//2)
print(-5.0//2)
print("__________________________")
res = 10 // 3 
print(res)
print(type(res))
print(-17 // 5)
print("__________________________")

# Explanation:
# / gives the exact decimal value (-3.4).
# // rounds down towards negative infinity, so instead of -3, it becomes -4.

# Division
# -9 / 2 = -4.5
# -22 / 4 = -5.5	

# Floor division
# -9 // 2 = -5
# -22 // 4 = -6


# 5. Modulus Operator
value1 = 3
value2 = 2

result = value1 % value2
print(result)


# 6. Exponentiation Operator

value1 = 2
value2 = 3
result = value1 ** value2
print(result)


# 7. Operator Precedence
"""
Parentheses()
↓
Power
↓
Multiply/Divide
↓
Add/Subtract
"""
# 1. ** = Exponentiation(power)
# right to left

# 2. * / // %
# left to right 

# 3. + -
# left to right (that's mean ending)

"""
BODMAS মানে:

B → Brackets ()
O → Orders / Powers / Exponent
D → Division
M → Multiplication
A → Addition
S → Subtraction

Python এও প্রায় একইভাবে calculation হয়।

"""