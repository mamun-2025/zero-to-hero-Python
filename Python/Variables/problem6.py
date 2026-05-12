
# 1. Take two numbers and print the multiplication
# We can two numbers using input()
# Then we multiply them using *

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Multiplication: ", a * b)

# 2. Take a number and print triple of it
# Triple means multiplying the number by 3
num = int(input("Enter a number: "))
print("Trple: ", num * 3)

# 3. Print square of a number
# Square means multiplying a number by itself
num = int(input("Enter a number: "))
print("Square =", num * num)

# 4. Print cube of a number
# Cube means multiplying the number 3 times 
num = int(input("Enter a number: "))
print("Cube =", num * num * num)

# 5. Print half of a number
# Half means dividing the number by 2
num = int(input("Enter a number: "))
print("Half =", num / 2)

# 6. Find square root of a number
# Square root means a number multiplied by itself gives the original number.
# we use ** 0.5 to find square root.
num = float(input("Enter a number: "))
square_root = num ** 0.5
print("Square Root =", square_root)

# 7. Find cube root of a number
# Cube root means: ∛x
# We use **(1/3) in Python 
num = float(input("Enter a number: "))

cube_root = num ** 1 / 3

print("Cube Root ", cube_root)

