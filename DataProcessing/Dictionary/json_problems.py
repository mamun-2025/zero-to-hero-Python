

# Level 1: Basic JSON Access (1-10)

# Problem 1: name প্রিন্ট করো।
response = {
   "name": "Mamun",
   "age": 25
}

# যেহেতু এটি একটি সিঙ্গেল লেয়ার ডিকশনারি, সরাসরি Key ধরে ডেটা অ্যাক্সেস করা যাবে।
# পদ্ধতি ১: Direct Key Access (সবচেয়ে কমন)
print(response["name"])

# পদ্ধতি ২: .get() Method (ব্যাকএন্ডে নিরাপদ, কী না থাকলে ক্র্যাশ করে না)
print(response.get("name"))


# Problem 2: name বের করো।
response = {
   "user": {
      "name": "Mamun"
   }
}

# এটি একটি Nested Dictionary (ডিকশনারির ভেতর ডিকশনারি)। প্রথমে user কী-তে ঢুকতে হবে, তারপর name কী-তে।
# পদ্ধতি ১: Chained Key Access
print(response["user"]["name"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("user", {}).get("name"))


# Problem 3: email বের করো।
response = {
   "user": {
      "email": "mamun@gmail.com"
   }
}

# ঠিক আগের প্রবলেমটির মতোই চেইনড ইনডেক্সিং বা কী (Key) ব্যবহার করতে হবে।
# পদ্ধতি ১: Chained Key Access
print(response["user"]["email"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("user", {}).get("email"))


# Problem 4: price বের করো।
response = {
   "product": {
      "price": 50000
   }
}

# পদ্ধতি ১: Chained Key Access
print(response["product"]["price"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("product", {}).get("price"))


# Problem 5: marks বের করো।
response = {
   "student": {
      "marks": 95
   }
}

print(response.get("student", {}).get("marks"))
print(response["student"]["marks"])


# Problem 6: city বের করো।
response = {
   "user": {
      "address": {
         "city": "Madaripur"
      }
   }
}

# এটি ৩ লেয়ারের ডিকশনারি। প্রথমে user $\rightarrow$ তারপর address $\rightarrow$ তারপর city।

# পদ্ধতি ১: Chained Key Access
print(response["user"]["address"]["city"])

# পদ্ধতি ২: Safe .get() Method (রিয়েল প্রজেক্টে ক্র্যাশ এড়াতে এটি সেরা)
print(response.get("user", {}).get("address", {}).get("city"))


# Problem 7: employee name বের করো।
response = {
   "company": {
      "employee": {
         "name": "Rahim"
      }
   }
}

# পদ্ধতি ১: Chained Key Access
print(response["company"]["employee"]["name"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("company", {}).get("employee", {}).get("name"))


# Problem 8: customer email বের করো।
response = {
   "order": {
      "customer": {
         "email": "abc@gmail.com"
      }
   }
}

print(response["order"]["customer"]["email"])
print(response.get("order", {}).get("customer", {}).get("email"))


# Problem 9: age বের করো।
response = {
    "data": {
        "user": {
            "profile": {
                "age": 22
            }
        }
    }
}

# এটি ৪ লেয়ারের ডিকশনারি। ভয় পাওয়ার কিছু নেই, লজিক একই — data ➡️ user ➡️ profile ➡️ age।
# পদ্ধতি ১: Chained Key Access
print(response["data"]["user"]["profile"]["age"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("data", {}).get("user", {}).get("profile", {}).get("age"))


# Problem 10: theme বের করো।
response = {
    "settings": {
        "theme": "dark"
    }
}

print(response["settings"]["theme"])
print(response.get("settings", {}).get("theme"))

# Level 1 (Basic JSON Access) শেষ হলো!



########################################################################################


##### Level 2: JSON List Processing (11-20)

## Problem 11 & 12:
response = {
   "users": [
      {"name": "Mamun"},
      {"name": "Rahim"},
      {"name": "Karim"}
   ]
}

# প্রথম user-এর name বের করো।
print(response["users"][0]["name"])

# সব names-এর list বানাও (৪টি নিয়মে)।
# 1. List comprehension
names_list = [user["name"] for user in response["users"]]
print(names_list)

# 2. For loop
names_list = []
for user in response["users"]:
   names_list.append(user["name"])

print(names_list)

# 3. Generator Expression (memory friendly)
names_list = list(user["name"] for user in response["users"])
print(names_list)

# 4. map() with lambda (functional)
names_list = list(map(lambda user: user["name"], response["users"]))
print(names_list)




## Problem 13 & 14:
response = {
   "products": [
      {"price": 100},
      {"price": 200},
      {"price": 300}
   ]
}

# সব price বের করো।
print([p["price"] for p in response["products"]])

# সব price-এর sum (যোগফল) বের করো।
# 1. List comprehension
total_price = sum(p["price"] for p in response["products"])
print(total_price)

# 2. For loop
total_price = 0
for p in response["products"]:
   total_price += p["price"]

print(total_price)

# 3. Generator Expression + sum() (মেমরির জন্য হুবহু ১ এর মতোই কাজ করে)
total_price = sum(p["price"] for p in response["products"])
print(total_price)

# 4. map() with lambda
total_price = sum(map(lambda p: p["price"], response["products"]))
print(total_price)




## Problem 15, 16 & 17:
response = {
   "users": [
      {"age": 25},
      {"age": 30},
      {"age": 20}
   ]
}

# সব age-এর average বের করো।
# 1. list comprehension
total_age = sum([user["age"] for user in response["users"]])
average_age = total_age / len(response["users"])
print(int(average_age))

# 2. For loop
total_age = 0
for user in response["users"]:
   total_age += user["age"]

average_age = total_age / len(response["users"])
print(int(average_age))

# Maximum age বের করো।
max_age = max(user["age"] for user in response["users"])
print(max_age)

# Minimum age বের করো।
min_age = min(user["age"] for user in response["users"])
print(min_age)




## Problem 18, 19 & 20
response = {
   "students": [
      {"marks": 80},
      {"marks": 60},
      {"marks": 95}
   ]
}

# Highest marks বের করো।
highest_marks = max(student["marks"] for student in response["students"])
print(highest_marks)

# Lowest marks বের করো।
lowest_marks = min(student["marks"] for student in response["students"])
print(lowest_marks)

# সব marks-এর average বের করো।
# 1. List comprehension
total_marks = sum(student["marks"] for student in response["students"])
average_marks = total_marks / len(response["students"])

print(int(average_marks))

# 2. For loop
total_marks = 0
for student in response["students"]:
   total_marks += student["marks"]

average_marks = total_marks / len(response["students"])
print(int(average_marks))


# Level 2 (JSON List Processing) এর ১০টি প্রবলেম শেষ! 
# লুপ, কম্প্রহেনশন আর এগ্রিগেশন ফাংশন (sum, max, min) এর কম্বিনেশন




################################################################################

##### Level 3: API Filtering (21-25)
"""
API Filtering (21-25) হলো ব্যাকএন্ড ডেভেলপমেন্টের অন্যতম প্রধান ভিত্তি। 
ডেটাবেস বা এপিআই থেকে আসা হাজার হাজার ডেটা থেকে শুধু নির্দিষ্ট শর্ত (Condition) মিলে যাওয়া ডেটা ফিল্টার করে বের করা আমাদের প্রতিদিনের কাজ।

এখানেও আমরা আমাদের ৪টি ম্যাজিক্যাল নিয়ম (Comprehension, For Loop, Generator, Map) ব্যবহার করব, 
যাতে ফিল্টারিংয়ের সাথে if কন্ডিশন কীভাবে জুড়ে দিতে হয় তা তুমি নিখুঁতভাবে শিখতে পারো।

"""

## Problem 21: শুধু Gmail users বের করো।
response = {
   "users": [
      {"email": "a@gmail.com"},
      {"email": "b@yahoo.com"},
      {"email": "c@gmail.com"}
   ]
}

# 1. List comprehension
gmail_list = [user["email"] for user in response["users"] if user["email"].endswith("@gmail.com")]
gmail_list = [user for user in response["users"] if "@gmail.com" in user["email"]]
print(gmail_list)

# 2. For loop
gmail_list = []
for user in response["users"]:
   if "@gmail.com" in user["email"]:
      gmail_list.append(user)

print(gmail_list)

# 3. generator expression
gmail_list = list(user for user in response["users"] if "@gmail.com" in user["email"])
print(gmail_list)

# 4. filter() with lambda (ম্যাপের চেয়ে ফিল্টারিংয়ের জন্য filter() ফাংশনটি বেস্ট)
gmail_list = list(filter(lambda user: "@gmail.com" in user["email"], response["users"]))
print(gmail_list)





## Prolem 22: Pass students বের করো (Pass Mark = 40)।
response = {
    "students": [
        {"name": "A", "marks": 80},
        {"name": "B", "marks": 30},
        {"name": "C", "marks": 90}
    ]
}

# 1. List comprehension
pass_student = [student for student in response["students"] if student["marks"] > 40]
print(f"Passed Student: {pass_student}")

# 2. For loop
pass_student = []
for student in response["students"]:
   if student["marks"] > 40:
      pass_student.append(student)

print(f"Passed Student: {pass_student}")

# 3. Generator Expression
pass_student = list(student for student in response["students"] if student["marks"] > 40)
print(pass_student)

# 4. filter() with lambda
pass_student = list(filter(lambda student: student["marks"] >= 40, response["students"]))
print(pass_student)





## Problem 23: price > 1500 এমন products বের করো।
response = {
    "products": [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 1000},
        {"name": "Keyboard", "price": 2000}
    ]
}

# 1. List Comprehension
highest_price = [product for product in response["products"] if product["price"] > 1500]
print(highest_price)

# 2. For loop
highest_price = []
for product in response["products"]:
   if product["price"] > 1500:
      highest_price.append(product)

print(highest_price)

# 3. Generator Expression (memory friendly)
highest_price = list(product for product in response["products"] if product["price"] > 1500)
print(highest_price)

# 4. filter() with lambda
highest_price = list(filter(lambda product: product["price"] > 1500, response["products"]))
print(highest_price)




## Problem 24: active users বের করো (যাদের "active": True)।
response = {
    "users": [
        {"name": "Mamun", "active": True},
        {"name": "Rahim", "active": False},
        {"name": "Karim", "active": True}
    ]
}

# List comprehension
active_users = [user for user in response["users"] if user["active"]]
print(active_users)

# For loop 
active_users = []
for user in response["users"]:
   if user["active"]:
      active_users.append(user)

print(active_users)

# 3. generator expression
active_users = list(user for user in response["users"] if user["active"])
print(active_users)

# 4. filter() with lambda
active_users = list(filter(lambda user: user["active"], response["users"]))
print(active_users)






## Problem 25: completed orders বের করো।
response = {
    "orders": [
        {"status": "completed"},
        {"status": "pending"},
        {"status": "completed"}
    ]
}

# 1. List Comprehension
completed_orders = [order for order in response["orders"] if order["status"] == "completed"]
print(completed_orders)

# 2. For loop 
completed_orders = []
for order in response["orders"]:
   if order["status"] == "completed":
      completed_orders.append(order)

print(completed_orders)

# 3. Generator expression
completed_orders = list(order for order in response["orders"] if order["status"] == "completed")
print(completed_orders)

# 4. filter() with lambda
completed_orders = list(filter(lambda order: order["status"] == "completed", response["orders"]))
print(completed_orders)

# Level 3 (API Filtering) সফলভাবে শেষ হলো! 
# খেয়াল করেছ কি, চার নম্বর নিয়মে আমরা এ বার map() এর জায়গায় filter() ব্যবহার করেছি? 
# কারণ পাইথনে ফাংশনাল পদ্ধতিতে ডেটা ফিল্টার করার জন্য filter()-ই সবচেয়ে পারফেক্ট বিল্ট-ইন টুল।




########################################################################################

##### Level 4: Level 4: Real Backend Tasks (26-30)
"""
বাস্তব জীবনে ব্যাকএন্ড এপিআই ডেভেলপ করার সময় ডেটার ম্যাপিং করা 
(যেমন: ফ্রন্টএন্ডে বা ড্রপডাউনে দেখানোর জন্য আইডি দিয়ে নাম খোঁজা) 
এবং অবজেক্ট বা লিস্টের মধ্য থেকে ম্যাক্সিমাম/মিনিমাম ভ্যালু বের করার মতো জটিল কাজগুলো প্রতিনিয়ত করতে হয়।

"""
## Problem 26:  ID ➡️ Name dictionary বানাও।
response = {
    "users": [
        {"id": 1, "name": "Mamun"},
        {"id": 2, "name": "Rahim"}
    ]
}

# 1. Dictionary Comprehension
map_1 ={user["id"]: user["name"] for user in response["users"]}
print(map_1)

# 2. For loop 
map_1 = {}
for user in response["users"]:
   map_1[user["id"]] = user["name"]

print(map_1)

# 3. dict() with generator expression
map_1 = dict((user["id"], user["name"]) for user in response["users"])
print(map_1)

# 4. map() with lambda
map_1 = dict(map(lambda user: (user["id"], user["name"]), response["users"]))
print(f"ID - Name Map: ", map_1)






## Problem 27: Product ID ➡️ Product Name dictionary বানাও।
response = {
    "products": [
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Mouse"}
    ]
}

# 1. List comprehension
map_1 = {product["id"]: product["name"] for product in response["products"]}
print(map_1)

# 2. For loop
map_1 = {}
for product in response["products"]:
   map_1[product["id"]] = product["name"]

print(map_1)

# 3. Generator expression
map_1 = dict((product["id"], product["name"]) for product in response["products"])
print(map_1)

# 4. map() with lambda
map_1 = dict(map(lambda product: (product["id"], product["name"]), response["products"]))
print(map_1)






## Problem 28: Email list বের করো।
response = {
    "users": [
        {"id": 1, "email": "a@gmail.com"},
        {"id": 2, "email": "b@gmail.com"}
    ]
}

# 1. list comprehension
email_list = [user["email"] for user in response["users"]]
print(email_list)

# 2. For loop 
email_list = []
for user in response["users"]:
   email_list.append(user["email"])

print(email_list)

# 3. generator expression
email_list = list(user["email"] for user in response["users"])
print(email_list)

# 4. map() with lambda
email_list = list(map(lambda user: user["email"], response["users"]))
print(email_list)






## Problem 29: Most Expensive Product (সবচেয়ে দামি প্রোডাক্টের পুরো ডিকশনারি অবজেক্টটি) বের করো।
response = {
    "products": [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 1000},
        {"name": "Keyboard", "price": 2000}
    ]
}


# 1. List comprehension(সবচেয়ে দামি প্রোডাক্ট)
expensive_product = max(product["price"] for product in response["products"])
print(expensive_product)

# max() with lambda (সবচেয়ে প্রফেশনাল ও এক লাইনের সমাধান)
expensive_product = max(response["products"], key=lambda product: product["price"])
print(expensive_product)

# 2. For loop
expensive_product = response["products"][0]
for product in response["products"]:
   if product["price"] > expensive_product["price"]:
      expensive_product = product

print(expensive_product)

# 3. sorted() function ব্যবহার করে (লিস্ট শর্ট করে শেষেরটা নেওয়া)
expensive_product = sorted(response["products"], key=lambda product: product["price"])[-1]
print(expensive_product)

# 4. 
def get_price(product):
   return product["price"]

expensive_product = max(response["products"], key=get_price)
print(f"Most Expensive Product: ", expensive_product)





## Problem 30: Lowest Price Product (সবচেয়ে কম দামি প্রোডাক্ট) বের করো।
response = {
    "products": [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 1000},
        {"name": "Keyboard", "price": 2000}
    ]
}

# 1. min() with lambda (সবচেয়ে প্রফেশনাল)
cheapest_product = min(response["products"], key=lambda product: product["price"])
print(cheapest_product)

# 2. For loop
cheapest_product = response["products"][0]
for product in response["products"]:
   if product["price"] < cheapest_product["price"]:
      cheapest_product = product

print(cheapest_product)

# 3. sorted() function ব্যবহার করে (শর্ট করে প্রথমটা নেওয়া)
cheapest_product = sorted(response["products"], key=lambda product: product["price"])[0]
print(cheapest_product)

# 4. 
def get_price(product):
   return product["price"]

cheapest_product = min(response["products"], key=get_price)
print(f"Cheapest Product: {cheapest_product}")


"""
অভিনন্দন! 🎉
তুমি সফলভাবে JSON Handling এবং API Response Processing-এর 
পুরো ৩০টি প্রবলেম একাধিক ডাইনামিক নিয়মে সলভ করে ফেলেছ। 
এই প্র্যাকটিসটি তোমার ব্যাকএন্ড লজিক তৈরিতে বিশাল এক বুস্ট দেবে।

"""