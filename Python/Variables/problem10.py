

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
