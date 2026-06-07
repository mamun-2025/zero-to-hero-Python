
age = int(input("What is your age? "))

if age >= 18:
   nationality = input("Do you have your NID card? (y/n)")
   if nationality == "y":
      tradelicense = input("Do you have trade license? (y/n)")
      if tradelicense == "y":
         print("Congratulations.")
      else:
         print("You are nor eligible.")
   else:
      print("You must your NID Card.")
else:
   print("You are too young.")


## 
age = 70
is_member = True 
if age >= 60:
   if is_member:
      print("30% discount for senior members.")
   else:
      print("20% discount for senior members.")
else:
   print("Not eligible for senior discount.")


##
i = 10
if i == 10:

   if i < 15:
      print("i is less than 15.")
   
   if i < 12:
      print("i is less than 12.")
   else:
      print("i is greater than 15.")

else:
   print("i is not equal to 10.")


## 
i = 20
if i == 10:
   print("i is 10.")
elif i == 15:
   print("i is 15.")
elif i == 20:
   print("i is 20.")
else:
   print("i is not 10, 15, or 20.")


##
age = 15
member = True
if age >= 18:
   if member:
      print("Ticket price is $15.")
   else:
      print("Ticket price is $25.")
else:
   if member:
      print("Ticket price is $5.")
   else:
      print("Ticket price is $10.")


## 
i = -18
if i != 0:
   if i > 0:
      print("Positive number.")
   if i < 0:
      print("Negative number.")
else:
   print("Zero.")
