
# 1. Take radius and find area of circle
# Formula of area of circle: A = ⊼ r2 / A=πr2
# We use 3.1416 as the value of ⊼ (PI)

# import math 
radius = float(input("Enter radius: "))

area = 3.1416 * radius * radius

# area = math.pi * radius * radius
print("Area of circle =", area)

# 2. Find circumference of a circle
# Circumference formula: C = 2 ⊼ r
# r = radius, ⊼ = 3.1416(PI)
radius = float(input("Enter radius: "))

circumference = 2 * 3.1416 * radius 

print("Circumference =", circumference)

# 3. Find area of rectangle
# Area of rectangle formula: A = l x w
# l = length, w = width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle =", area)

# 4. Find perimeter of rectangle
# Perimeter formula: P = 2(l + w)
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)

print("Perimeter ", perimeter)

# 4. Find area of triangle 
# Triangle area formula: A = 1/2 * b * h
# b = base, h = height
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height

print("Area of traingle =", area)

