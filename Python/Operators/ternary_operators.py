
# Ternary Operator in Python
"""
The ternary operator in Python perform conditional checks and assign values or execute expressions in a single line.\
It is also known as a conditonal expression because it evalutes a condition and returns one value if the condition is True and another if it is False.
"""
n = 6 
res = "Even" if n % 2 == 0 else "Odd"
print(res)


# 1. Nested if else
n = -5
res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)

# 2. Using Tuple
n = 7
res = ("Odd", "Even") [n % 2 == 0]
print(res)

# 3. Using Dictionary
a = 10
b = 20
m1 = {True: a, False: b} [a > b]
print(m1)

# 4. Using Python Lambda
a = 10
b = 20
m1 = (lambda x, y: x if x > y else y)(a, b)
print(m1)

# 5. Using Print Function
a = 10
b = 20
print("a is greater" if a > b else "b is greater")
