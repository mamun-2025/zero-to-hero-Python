
if False:
   print("This will never execute.")


# 1. Using False in Conditonal Statements
x = 10
f = x < 5

if f:
   print("x is less than 5")
else:
   print("x is not less than 5")


# 2. Using False to Initialize Flags
f = False
a = [1, 3, 5, 7, 9]

for i in a:
   if i == 5:
      f = True
      break

if f:
   print("Number found!")
else:
   print("Number not found.")


# 3. Using False as 0 in Arithmetic
print(False + 5)
print(False * 5)
