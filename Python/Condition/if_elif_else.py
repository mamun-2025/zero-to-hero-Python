

#### Conditional Statements in Python

"""
Conditional statements are used to control the flow of execution in a program based on specific conditions.
They allow programs to execute different blocks of code depending on whether a condition evaluates to True or False.
"""

#################################################
# 1.If statement:
# The if statement is used to execute a block of code only when a given condition is True.
# If the condition is False, the code inside the if block is skipped.

##
i = 10
if i > 15:
   print("10 is less than 15.")

print("I am Not in if.")

##
age = 20
if age >= 18:
   print("Eligible to vote.")


# Short Hand if statement:
age = 19
if age >= 18: print("Eligible to vote.")



###################################################
# 2. If-else statement:
# The if-else statement is used to execute one block of code when a condition is True and another block when condition is False.
# It helps programs make decisions based on different conditons.

## 
age = 18
if (age >= 12 and age <= 25):
   print("You are allowed. WELCOME!")
else:
   print("Sorry! You arre not allowed.")

##
i = 10 
if i > 0:
   print("i is positive number.")
else:
   print("i is 0 or negative number.")


# if-else in oneline:
i = 10 
result = "positive number" if i > 0 else "0 or negative number"
print(result)


# Logical operators with if-else:
age = 20
experience = 5
if age >= 18 and experience >= 3:
   print("You are eligible for the job.")
else:
   print("You are not eligible for the job.")


##
a = 1 
b = 1
c = 1
if (a == 1 and b == 1 and c == 1):
   print("Working")
else:
   print("Stopped")

########################################################

# 3. If-elif-else statement:
age = 20
if age < 18 and age > 0:
   print("You are a minor.")
elif age >= 18 and age < 65:
   print("You are an adult.")
elif age >= 65:
   print("You are a senior citizen.")
else:
   print("Invalid age.")


##
user = input("Enter Y(yes) or N(no): ")
if (user == "Y" or user == "y"):
   print("You said Yes.")
elif(user == "N" or user == "n"):
   print("You said No.")
else:
   print("Invalid input. Please enter (yes) or (no).")


## 
a = 76
b = 9
c = 31
if a > b and a > c:
   print(a, "is the largest number.")
elif b > a and b > c:
   print(b, "is the largest number.")
elif c > a and c > b:
   print(c, "is the largest number.")
else:
   print("All numbers are equal.")













































# # example 1:
# age = 19
# if age >= 18:
#    print("You are old enough to vote.")
#    print("Have you registered to vote yet? ")


# # example 2:
# age = int(input("Your age is: "))
# if age >= 18:
#    print("You are old enough to vote!")
#    print("Have you registered to vote yet?")
# else:
#    print("Sorry! you are too young to vote.")
#    print("Please register to vote as soon as you turn 18.")


# example 3:
# a, b = 10, 10

# if a > b:
#    print("A is Greater.")
# elif b > a:
#    print("B is Greater.")
# else:
#    print("Both are same.")

   
# example 4:
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#    if car == "audi":
#       print(car.upper())
#    else:
#       print(car.title())


# example 5:
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#    print("Hold the anchovies!")


# example 6:
# answer = 17
# if answer != 42:
#    print("That is not the correct answer, Please try again. ")


# example 7:
# age = int(input("Your age is: "))
# if age >= 18:
#    print("You are eligible.")
# elif age < 17 and age > 0:
#    print("You are too young.")
# else:
#    print("Zero or Negative is not allowed")


# example 8:
# banned_users = ["andrew", "john", "cargo", "amila"]
# select_users = "mamun"
# if select_users not in banned_users:
#    print(select_users.title() + ", you can post a response if you wish.")


# # example 9:
# age = int(input("Your age here is: "))
# if age >= 18:
#    print("Your admission cost is: $10")
# elif age >= 12:
#    print("Your admission cost is: $5")
# elif age >= 8:
#    print("Your admission cost is: $2")
# else:
#    print("Your admission cost is: $0")


# # example 10:
# age = 12
# if age < 4:
#   price = 0
# elif age < 18:
#    price = 5
# else:
#    price = 10
# print("Your admission cost is $" + str(price) + ".")



# # example 11:
# requested_toppings = ["mushrooms", "extra_cheese"]

# if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms")

# if 'pepperoni' not in requested_toppings:
#    print("Adding pepperoni.")

# if 'extra_cheese' in requested_toppings:
#    print("Adding extra_cheese")

# print("-------------------------------")
# print("\nFinished making your pizza.")


# example 12:
# requested_toppings = ["mushrooms", "green pippers", "extra cheese"]

# for requested_toppings in requested_toppings:
#    print("Adding " + requested_toppings + ".")

# print("\nFinished making your pizza.")


# example 13:
# avaiable_toppings = ["mushrooms", "pepperoni", "pineapple", "green_pippers", "Olives", "extra_cheese"]

# requested_toppings = ["mushrooms", "french_fries", "pineapple"]

# for requested_topping in requested_toppings:
#    if requested_topping in avaiable_toppings:
#       print("Adding " + requested_topping + ".")
#    else:
#       print("Sorry, we don't have" + requested_topping + ".")

# print("\nFinished making your pizza.")


# example 14:
