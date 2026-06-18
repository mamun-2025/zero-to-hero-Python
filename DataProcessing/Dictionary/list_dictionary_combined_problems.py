

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





## (7). Completed orders বের করো।

## (8). Verified users বের করো।

## (9). 90+ students বের করো।

## (10). 500 টাকার বেশি products বের করো।







##### Level 3: Aggregation (1-10)

## (1). সব product price-এর sum বের করো।

## (2). সব salary-এর total বের করো।

## (3). Average marks বের করো।

## (4). সব age-এর average বের করো।

## (5). সব order amount-এর sum বের করো।

## (6). সব quantity-এর sum বের করো।

## (7). Maximum price বের করো।

## (8). Minimum price বের করো।

## (9). Highest marks বের করো।

## (10). Lowest marks বের করো।







##### Level 4: Dictionary Comprehension + Mapping (1-10)

## (1).

## (2).

## (3).

## (4).

## (5).

## (6).

## (6).

## (7).

## (8).

## (9).

## (10).