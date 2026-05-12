
# 1. Take a number as input and print double of it.
# input() gives string data
# We convert it using int() and multiply by 2
num = int(input("Enter a number: "))
print(num * 2)

# 2. Take a decimal number and double it.
# We use float() for decimal numbers 
num = float(input("Enter a decimal number: "))
print(num * 2)

# 3. Find speed using distance and time.
# Speed formula: Speed = Distance/Time
distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

speed = distance / time 

print("Speed =", speed)