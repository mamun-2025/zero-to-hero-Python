

##### Level 1 : Extract Data(1-10)

## (1). শুধু names-এর list বানাও।

users = [
   {"name": "Mamun"},
   {"name": "Rahim"},
   {"name": "Karim"}
]

names_list = [user["name"] for user in users]
print(names_list)

# for loop
users = [
   {"name": "Mamun"},
   {"name": "Rahim"},
   {"name": "Karim"}
]

names_list = []

for user in users:
   names_list.append(user["name"])

print(names_list)



#_____________________________________________________________________________________________
## (2). শুধু emails বের করো।
users = [
   {"email": "a@gmail.com"},
   {"email": "b@gmail.com"},
   {"email": "c@gmail.com"}
]

emails_list = [user["email"] for user in users]
print(emails_list)

# for loop
users = [
   {"email": "a@gmail.com"},
   {"email": "b@gmail.com"},
   {"email": "c@gmail.com"}
]

emails_list = []

for user in users:
   emails_list.append(user["email"])

print(emails_list)



#____________________________________________________________________________________
## (3). শুধু price list বের করো।
products = [
   {"price": 100},
   {"price": 500},
   {"price": 700}
]

price_list = [product["price"] for product in products]

print(price_list)

# for loop
products = [
   {"price": 100},
   {"price": 500},
   {"price": 700}
]

price_list = []

for product in products:
   price_list.append(product["price"])

print(price_list)





#_____________________________________________________________________________________________
## (4). শুধু ids বের করো।
users = [
    {"id": 1},
    {"id": 2},
    {"id": 3}
]

id_list = [user["id"] for user in users]
print(id_list)

# for loop
users = [
    {"id": 1},
    {"id": 2},
    {"id": 3}
]

id_list = []

for user in users:
   id_list.append(user["id"])

print(id_list)




#________________________________________________________________________________________________
## (5). শুধু marks বের করো।
students = [
    {"marks": 80},
    {"marks": 90},
    {"marks": 70}
]

mark_list = [mark["marks"] for mark in students]
print(mark_list)

# for loop
students = [
    {"marks": 80},
    {"marks": 90},
    {"marks": 70}
]

mark_list = []

for mark in students:
   mark_list.append(mark["marks"])

print(mark_list)





#______________________________________________________________________________________________
## (6). শুধু product names বের করো।
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 1000}
]

product_list = [product["name"] for product in products]
print(product_list)

# for loop
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 1000}
]

product_list = []

for product in products:
   product_list.append(product["name"])

print(product_list)





#______________________________________________________________________________________________
## (7). শুধু ages বের করো।

users = [
    {"name": "Mamun", "age": 20},
    {"name": "Rahim", "age": 25}
]

# আউটপুট যদি ডিকশনারি আকারে চাও (যেমন: নাম হবে key, বয়স হবে value)
user_dict = {user["name"]: user["age"] for user in users}

print(user_dict)
# আউটপুট: {'Mamun': 20, 'Rahim': 25} <- এবার ডিকশনারি আকারে বের হয়েছে!

# for loop 
users = [
    {"name": "Mamun", "age": 20},
    {"name": "Rahim", "age": 25}
]

# list আকারে
user_list = [user["age"] for user in users]
print(user_list)

# ডিকশনারি আকারে
user_dict = {user["name"]: user["age"] for user in users}
print(user_dict)





#________________________________________________________________________________________________
## (8). শুধু title list বের করো।
books = [
    {"title": "Python"},
    {"title": "Django"}
]

book_list = [name["title"] for name in books]
print(book_list)


# লিস্টের ভেতর থেকে কোনো একটা নির্দিষ্ট ডিকশনারিকে ইনডেক্স ([0], [1]) দিয়ে ডাকলে 
# সে কিন্তু ডিকশনারি আকারেই বের হবে।
book1 = books[0]
print(book1)
print(type(book1))





#__________________________________________________________________________________________________
## (9). সব order id বের করো।
orders = [
    {"order_id": 101},
    {"order_id": 102}
]

order_id = [order["order_id"] for order in orders]
print(order_id)

# for loop
orders = [
    {"order_id": 101},
    {"order_id": 102}
]

order_list = []

for order in orders:
   order_list.append(order["order_id"])

print(order_list)




#___________________________________________________________________________________________
## (10). সব salary বের করো।
employees = [
   {"name": "Mamun", "salary": 25000},
   {"name": "Habib", "salary": 20000},
   {"name": "Rudro", "salary": 28000}
]

employee_salary = [employee["salary"] for employee in employees]
print(employee_salary)

# for loop(name list)
employees = [
   {"name": "Mamun", "salary": 25000},
   {"name": "Habib", "salary": 20000},
   {"name": "Rudro", "salary": 28000}
]
employee_list = []

for employee in employees:
   employee_list.append(employee["name"])

print(employee_list)



###############################################################################################



##### Level 2: Filtering(1-10)

## (1). শুধু active users বের করো।
users = [
   {"name": "Mamun", "active": True},
   {"name": "Habib", "active": False},
   {"name": "Rudro", "active": True}
]

active_users = [user for user in users if user["active"]]
print(active_users)

# for loop
users = [
   {"name": "Mamun", "active": True},
   {"name": "Habib", "active": False},
   {"name": "Rudro", "active": True}
]

active_users = []

for user in users:
   if user["active"]:
      active_users.append(user)

print(active_users)





#___________________________________________________________________________________________
## (2). যাদের price > 1500 তাদের বের করো।
products = [
   {"name": "Laptop", "price": 50000},
   {"name": "Mouse", "price": 1000},
   {"name": "keyboard", "price": 2000}
]

proudct_price = [product for product in products if product["price"] > 1500]
print(proudct_price)

# for loop
products = [
   {"name": "Laptop", "price": 50000},
   {"name": "Mouse", "price": 1000},
   {"name": "keyboard", "price": 2000}
]

expensive_products = []

for product in products:
   if product["price"] > 1500:
      expensive_products.append(product)

print(expensive_products)





#____________________________________________________________________________________
## (3). Pass students বের করো। Pass Mark = 40
students = [
    {"name":"A","marks":80},
    {"name":"B","marks":30},
    {"name":"C","marks":90}
]

passed_student = [student for student in students if student["marks"] > 33]
print(f"Passed Student: {passed_student}")

# for loop 
students = [
    {"name":"A","marks":80},
    {"name":"B","marks":30},
    {"name":"C","marks":90}
]

passed_student = []

for student in students:
   if student["marks"] > 33:
      passed_student.append(student)

print(passed_student)





#__________________________________________________________________________________
## (4). শুধু gmail users বের করো।
users = [
   {"email": "a@gmail.com"},
   {"email": "b@yahoo.com"},
   {"email": "c@gmail.com"}
]

gmail_list = [user for user in users if user["email"].endswith("@gmail.com")]
print(gmail_list)

# for loop
users = [
   {"email": "a@gmail.com"},
   {"email": "b@yahoo.com"},
   {"email": "c@gmail.com"}
]

gmail_list = []

for user in users:
   if user["email"].endswith("@gmail.com"):
      gmail_list.append(user)

print(gmail_list)






#__________________________________________________________________________
## (5). Adults (18+) বের করো।
users = [
   {"age": 17},
   {"age": 20},
   {"age": 15},
   {"age": 30}
]

adult_list = [user for user in users if user["age"] > 18]
print("Adult:", adult_list)

# for loop 
users = [
   {"age": 17},
   {"age": 20},
   {"age": 15},
   {"age": 30}
]

adult_list = []

for user in users:
   if user["age"] > 18:
      adult_list.append(user)

print(f"Adult: {adult_list}")





#_________________________________________________________________________________________
## (6). Available products বের করো।
products = [
   {"stock": 0},
   {"stock": 5},
   {"stock": 10}
]

available_product = [product for product in products if product["stock"] > 0]
print(f"Available: {available_product}")

# for loop 
products = [
   {"stock": 0},
   {"stock": 5},
   {"stock": 10}
]

available_product = []

for product in products:
   if product["stock"] > 0:
      available_product.append(product)

print(available_product)






#_______________________________________________________________________________________
## (7). Completed orders বের করো।
orders = [
   {"status": "completed"},
   {"status": "completed"},
   {"status": "pending"}
]

completed_list = [order for order in orders if order["status"] == "completed"]
print(f"Completed Order: {completed_list}")

# for loop
orders = [
   {"status": "completed"},
   {"status": "completed"},
   {"status": "pending"}
]

completed_list = []
for order in orders:
   if order["status"] == "completed":
      completed_list.append(order)

print(completed_list)






#____________________________________________________________________________________________
## (8). Verified users বের করো।
users = [
   {"verified": True},
   {"verified": False},
   {"verified": True}
]

verified_list = [user for user in users if user["verified"]]
# যেহেতু "verified" কী-এর ভেতরের ভ্যালুগুলো ইতিমধ্যেই বুলিয়ান (True অথবা False) আকারে আছে, 
# তাই শুধু if user["verified"] লিখলেই পাইথন বুঝে নেয় যে মানটি সত্য (True) কিনা। 
# শর্ত সত্য হলে ডিকশনারিটি নতুন লিস্টে যুক্ত হয়।

print(verified_list)

# for loop
users = [
   {"verified": True},
   {"verified": False},
   {"verified": True}
]

verified_list = []

for user in users:
   if user["verified"]:
      verified_list.append(user)

print(f"Verified_User: {verified_list}")






#_______________________________________________________________________________
## (9). 90+ students বের করো।
students = [
    {"marks":90},
    {"marks":60},
    {"marks":99}
]

top_marks = [student for student in students if student["marks"] >= 90]
print(top_marks)

# for loop 
students = [
    {"marks":95},
    {"marks":60},
    {"marks":99}
]

top_marks = []

for student in students:
   if student["marks"] >= 90:
      top_marks.append(student)

print(f"Top marks: {top_marks}")







#_________________________________________________________________________________________
## (10). 500 টাকার বেশি products বের করো।
products = [
    {"price":100},
    {"price":500},
    {"price":1000}
]

expensive_products = [product for product in products if product["price"] > 500]
print(expensive_products)

# for loop 
products = [
    {"price":100},
    {"price":500},
    {"price":1000}
]

expensive_products = []

for proudct in products:
   if proudct["price"] > 500:
      expensive_products.append(proudct)

print(f"Expensive Product: {expensive_products}")




############################################################################################



##### Level 3: Aggregation (1-10)

## (1). সব product price-এর sum বের করো।
products = [
   {"price": 100},
   {"price": 200},
   {"price": 300}
]

total_price = sum([product["price"] for product in products])
print(total_price)

# for loop
products = [
   {"price": 100},
   {"price": 200},
   {"price": 300}
]

total_price = 0

for product in products:
   total_price += product["price"] # প্রতিটি দাম total_price এর সাথে যোগ হচ্ছে

print(total_price)






#_____________________________________________________________________________________
## (2). সব salary-এর total বের করো।
employees = [
   {"salary": 20000},
   {"salary": 30000},
   {"salary": 35000}
]

total_salary = sum([employee["salary"] for employee in employees])
print(total_salary)

# for loop
employees = [
   {"salary": 20000},
   {"salary": 30000},
   {"salary": 35000}
]

total_salary = 0

for employee in employees:
   total_salary += employee["salary"]

print(total_salary)





#_____________________________________________________________________________________________
## (3). Average marks বের করো।
students = [
   {"marks": 60},
   {"marks": 90},
   {"marks": 85}
]

# ১. সব marks-এর যোগফল বের করা হলো
total_marks = sum([student["marks"] for student in students])

# ২. মোট ছাত্র সংখ্যা বের করা হলো
total_length = len(students)

# ৩. গড় (Average) বের করা হলো
average_marks = total_marks/total_length

# আউটপুট যদি পূর্ণসংখ্যায় (Integer) দেখতে চাও
print(int(average_marks))

# for loop
students = [
   {"marks": 60},
   {"marks": 90},
   {"marks": 85}
]

total_marks = 0

for student in students:
   total_marks += student["marks"]

average_marks = total_marks/ len(students)

print(int(average_marks))






#__________________________________________________________
## (4). সব age-এর average বের করো।
users = [
   {"age": 25},
   {"age": 39},
   {"age": 30}
]

total_age = sum([user["age"] for user in users])

total_length = len(users)

average_age = total_age / total_length

print(int(average_age))





#_____________________________________________________________________________________
## (5). সব order amount-এর sum বের করো।
orders = [
   {"amount": 3000},
   {"amount": 3500},
   {"amount": 4000}
]

total_amount = sum([order["amount"] for order in orders])

print(total_amount)

# for loop
orders = [
   {"amount": 3000},
   {"amount": 3500},
   {"amount": 4000}
]

total_amount = 0

for order in orders:
   total_amount += order["amount"]

print(total_amount)






#__________________________________________________________________________________
## (6). সব quantity-এর sum বের করো।
items = [
   {"quantity": 5},
   {"quantity": 10},
   {"quantity": 15}
]

total_quantity = sum([item["quantity"] for item in items])
print(total_quantity)

# for loop
items = [
   {"quantity": 5},
   {"quantity": 10},
   {"quantity": 15}
]

total_quantity = 0

for item in items:
   total_quantity += item["quantity"]

print(total_quantity)





#_________________________________________________________________________________
## (7). Maximum price বের করো।
products = [
   {"price": 100},
   {"price": 500},
   {"price": 250}
]

max_price = max(product["price"] for product in products)

print(max_price)

# for loop
products = [
   {"price": 100},
   {"price": 500},
   {"price": 250}
]

# প্রথম প্রোডাক্টের প্রাইসকে শুরুতে সর্বোচ্চ ধরে নেওয়া হলো
max_price = products[0]["price"]

for product in products:
   if product["price"] > max_price:
      max_price = product["price"]

print(max_price)







#_______________________________________________________________________________
## (8). Minimum price বের করো।

products = [
    {"price": 100},
    {"price": 500},
    {"price": 250}
]

min_price = min(product["price"] for product in products)
print(min_price)

# for loop
products = [
    {"price": 100},
    {"price": 500},
    {"price": 250}
]

min_price = products[0]["price"]

for product in products:
   if product["price"] < min_price:
      min_price = product["price"]

print(min_price)






#__________________________________________________________________________________
## (9). Highest marks বের করো।
## (10). Lowest marks বের করো।
students = [
    {"marks": 85},
    {"marks": 95},
    {"marks": 70}
]

highest_marks = max(student["marks"] for student in students)
lowest_marks = min(student["marks"] for student in students)

print(highest_marks)
print(lowest_marks)


# for loop
# highest marks:
students = [
    {"marks": 85},
    {"marks": 95},
    {"marks": 70}
]

highest_marks = students[0]["marks"]

for student in students:
   if student["marks"] > highest_marks:
      highest_marks = student["marks"]

print("Highest Marks:", highest_marks)

# lowest marks
students = [
    {"marks": 85},
    {"marks": 95},
    {"marks": 70}
]

lowest_marks = students[0]["marks"]

for student in students:
   if student["marks"] < lowest_marks:
      lowest_marks = student["marks"]


print(f"Lowest_marks: {lowest_marks}")







