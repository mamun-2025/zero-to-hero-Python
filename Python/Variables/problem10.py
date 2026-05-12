
# 13. Find BMI (Body Mass Index)
# BMI formula: BMI = Weight(kg) / Height(m)2
# Weight in Kilograms(kg) and Height in meters
# ৫.৭ ফুট ≈ ১.৭৩৭ মিটার।
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)
print("BMI =", bmi) 
# 1. Find percentage of marks
# Percentancge formula: Percentage = Obtained Marks/Total Marks x 100

obtained_marks = float(input("Enter obtained marks: "))

total_marks = float(input("Enter total marks: "))

percentage = (obtained_marks / total_marks) * 100
print("Percentage =", percentage)

# 2. Find simple interest
# Simple interest formula: SI = P x R X T / 100
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

simple_interest = (principal * rate * time) / 100

print(simple_interest)

# 3. Convert minutes into second
# 1 minutes = 60 seconds
minutes = int(input("Enter minutes: "))

seconds = minutes * 60

print("Seconds =", seconds)

# 4. Convert hours into minutes
# I know , 1 hours = 60 minutes
hours = int(input("Enter hours: "))

minutes = hours * 60

print("minutes =", minutes)

# 5. Convert days into hours
# 1 day = 24 hours 
# Hours = days x 24
days = int(input("Enter days: "))

hours = days * 24

print("Hours =", hours)

# 6. Convert kilograms into grams
# 1 Kilogram/Kg = 1000 grams
# Grams = kilograms * 1000
kilograms = int(input("Enter kilograms: "))

grams = kilograms * 1000
print("Grams =", grams)

# 7. Convert weeks into days
# 1 week = 7 days
# Days = weeks x 7
weeks = int(input("Enter weeks: "))
days = weeks * 7

print("Days =", days)

# 8. Convert centimeters into meters
# 1 meter = 100 centimeters
# Meters = centimeters/100
centimeters = float(input("Enter centimeters: "))
meters = centimeters / 100

print("Meters =", meters)

# 9. Convert years into months
# 1 year = 12 months
# Month = years x 12
years = int(input("Enter years: "))
months = years * 12

print("Months =", months)

# 10. Convert megabytes into gigabytes
# 1 gigabyte = 1024 megabytes
# Gigabyte = megabyte / 1024
megabytes = float(input("Enter megabytes: "))
gigabytes = megabytes / 1024

print("Gigabyte =", gigabytes)

# 11. Find power of a number
# Power menas multiplying a number by itself multiple times.
# 2^3 = 8 , In python, we use **

base = int(input("Enter base number: "))
power = int(input("Enter power: "))

result = base ** power

print("Result =", result)

# 12. Convert feet into meter
feet = float(input("Enter feet: "))
meters = feet * 0.3048

print("Meters =", meters)

