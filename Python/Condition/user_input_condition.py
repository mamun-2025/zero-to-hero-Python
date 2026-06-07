


# Example 1: Check if the user is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
   print("Eligible to vote.")
else:
   print("Not eligible to vote.")


# Example 2: Check if the number is positive or negative 
number = int(input("Enter a number: "))
if number > 0:
   print("The number is positive.")
else:
   print("The number is not positive.")


# Example 3: Check if the marks for grade calculation
marks = int(input("Enter your marks: "))
if marks >= 90:
   print("Grade: A")
elif marks >= 80:
   print("Grade: B")
elif marks >= 70:
   print("Grade: C")
elif marks >= 60: 
   print("Grade: D") 
elif marks >= 50:
   print("Grade: E")
else:
   print("Grade: F")


# Example 4: Check if the user input is a vowel or consonant
char = input("Enter a character: ").lower()

if char in ['a', 'e', 'i', 'o', 'u']:
   print(f"{char} is a vowel.")
else:
   print(f"{char} is a consonant.")


# Example 5: Check if the user input is a valid email address 
email = input("Enter your email address: ")
if "@" in email and "." in email:
   print("Valid email address.")
else: 
   print("Invalid email address.")


# Example 6: Check if the user login request is successful
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
   if password == "1234":
      print("Login successful.")
   else: 
      print("Incorrect password.")
else:
   print("Unknown username.")


# Example 7: Check if the user input is a prime number

number = int(input("Enter a number: "))
if number > 1:
   is_prime = True

   for i in range(2, int(number**0.5) + 1):
      if number % i == 0:
         is_prime = False
         break 

   if is_prime:
      print(f"{number} is a prime number.")
   else:
      print(f"{number} is not a prime number.")

else:
   print(f"{number} is not a prime number.")


# Example 8: Check if the user correct password
password = input("Enter a password: ")
while len(password) < 8:
   print("Password must be at least 8 characters long.")
   password = input("Enter a password: ")
print("Password accepted.")

password = ""
while password != "python123":
   password = input("Enter the correct password: ")

print("Access granted!")


# Example 9: Check if the user invalid input 
while True:
   try: 
      age = int(input("Enter your age: "))
      break 
   except ValueError:
      print("Invalid input! Please enter a number.")

print("Thank you! You entered:", age)

