
# 1. Taking input in Python 
value = input("Enter your value: ")
print(value)

# 2. How the input() Function works
num = input("Enter number: ")
print(num)
name1 = input("Enter name: ")
print(name1)

print("type of num", type(num))
print("type of name", type(name1))

# 3. Converting Input into Numbers
# Integer Input
num = int(input("Enter a number: "))
print(num, "is type of", type(num))
# Floatin-Point Input
floatNum = float(input("Enter a decimal number: "))
print(floatNum, "is of type", type(floatNum))
# Taking Multiple Inputs
x, y = input("Enter two numbers separed by space: ").split()
print("First number:", x)
print("Second number:", y)

# 5. Printing Output using print()
print("Hello World!")

# 6. Printing Variables
name = "Mamun"
print(name)

name = "Habib-Mamun"
age = 25
city = "Dhaka"
print(name, age, city)

# 7. Change the Type of Input in Python
color = input("What color is rose?: ")
print(color)
color = int(input("How many roses?: "))
print(color, type(color))
price = float(input("Price of each rose?: "))
print(price, type(price))
i = int(input("How old are you?: "))
j = float(input("Evaluate 7/2: "))
print(i, j)

###
# Type Casting in Python
# 1. Implicit Type Conversion
a = 7
print(type(a)) # Python automatically converts 'a' to int

b = 3.0
print(type(b)) # Python automatically converts 'b' to float 

c = a + b 
print(c)
print(type(c)) # Python automatically converts 'c' to float as it is a float addition

d = a * b 
print(d)
print(type(d)) # Python automatically converts 'd' to float as it is a float multiplication

# 2. Explicit Type Conversion
# Explicit type conversion is when the programmer manually changes a value's data type using built-in type casting functions, usually when automatic conversion is not possible or a specific type is needed.
# Int(): Python Int()
# float(): Python float()
# str(): Python str()

# 3. Python Convert int to float
a = 5 
n = float(a)
print(n)
print(type(n))

# 4. Python Convert float to int 
a = 5.9
n = int(a)
print(n)
print(type(n))

# 5. Python Convert int to String
a = 5
n = str(a)
print(n)
print(type(n))

# 6. Python Convert string to float
a = "5.9"
n = float(a)
print(n)
print(type(n))

# 7. Python Convert string to int
a = "5"
b = "t"
n = int(a)
print(n)
print(type(n))

# print(int(b))   # Python cannot convert it into an integer

# 8. Adding String an Integer without Conversation
a = 5
b = 't'
# n = a + b 
# print(n)

a = 5 
b = '7'
result = a + int(b)
print(result)
print(type(result))