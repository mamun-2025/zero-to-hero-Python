
# 1. Find the sum of 1 to 5
# We use a loop to add numbers one by one
total = 0

for i in range(1, 6):
   total = total + i

print("Sum =", total)

# 2. Take a number n from the user and print the sum from 1 to n
# If user enters 5: 1 + 2 + 3 + 4 + 5 = 15
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
   total = total + i 

print("Sum =", total)

# 3. Find sum from 1 to 100
# We use a loop to add all numbers from 1 to 100
total = 0

for i in range(1, 101):
   total = total + i 

print("Sum =", total)

# 4. Print table of 5
# We use a loop to print multiplication table 
for i in range(1,  11):
   print("5 x", i, "=", 5 * i)


# 5. Print multiplication table of any number
# We use a loop to print the table
num = int(input("Enter a number: "))

for i in range(1, 11):
   print(f"{num} x {i} = {num * i}")
