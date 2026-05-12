
# 1. Print 3 numbers and print their average
# Average formula: Average = a+b+c​/3
# We add all numbers and divide by 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

average = (a + b + c) / 3
print("Average =", int(average))

# 2. Find average of 5 numbers
# Average formula: Average = a + b + c + d + e / 5
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter four number: "))
e = float(input("Enter five number: "))

average = (a + b + c + d + e) / 5
print("Average =", average)


# 3.Find remainder of two numbers
# We use %(modulus operator) to get the remainder
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Remainder =", a % b)

# 4. Find total and average marks of 3 subjects
# First add all marks to get total. Then diveie by 3 to get average .
# Average = a + b  + c / 3
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))

total = math + english + science
average = total / 3

print(f"Total ={total}marks and Average ={average}")