
# Ternary Operator in Python
"""
Ternary operator perform conditional checks and assgin values or execute expressions in a single line. 
It is also known as a conditional expression because it evaluates a condition and returns one value 
if the condition is True and another if it is False.
"""
# Example 1:
n = 9
result = "Even" if n % 2 == 0 else "Odd"
print(result)

# Example 2:
num = -5
res = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(res)

# Example 3:
n = 7 
res = ("Odd", "Even")[n % 2 == 0]
print(res)

# Example 4:
a = 30
b = 20
result = {True: a, False: b}[a > b]
print(result)

# Example 5:
a = 10
b = 20
res = (lambda x, y: x if x > y else y)(a, b)
print(res)  

# Example 6:
a = 30 
b = 20
print("a is greater" if a > b else "b is greater")