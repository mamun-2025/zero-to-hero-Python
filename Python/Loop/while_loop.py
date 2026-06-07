

res = "y"
while res == "y":
   a = int(input("A = "))
   b = int(input("B = "))

   print("Result = ", str(a + b))
   res = input("Do you want to continue? (y/n)")




# example 1:
loop = True
while loop:
   print("I love you Nondita.")
   loop = False

# example 2:
loop = True
while loop <= 10:
   print("I love you nondita.")
   loop += 1

# example 3:
n = 1 
while n <= 10:
   print(n, end=" ")
   n += 1

# example 4: 
n = 0 
while n <= 100:
   print(n, end=", ")
   n += 1

