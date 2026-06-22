

##### Level 1: Data Processing Projects (1-10)
## 1. User Name Extract
users = [
   {"name": "Mamun"},
   {"name": "Habib"},
   {"name": "Rudro"}
]

names_list = [user["name"] for user in users]
print("Names_list:", names_list)


## 2. User Email Extract
users = [
   {"email": "a@gmail.com"},
   {"email": "b@gmail.com"}
]

emails_list = [user["email"] for user in users]
print("Emails_list: ", emails_list)


## 3. Total Product Price Calculator
products = [
   {"price": 100},
   {"price": 200},
   {"price": 300}
]

total_price = sum(product["price"] for product in products)
print("Total Price:", total_price)


## 4. Average Marks Calculator
students = [
   {"marks": 80},
   {"marks": 90},
   {"marks": 70}
]

total_marks = sum(student["marks"] for student in students)
average_marks = total_marks / len(students)
print("Average Marks:", int(average_marks))


## 5. Active Users Counter
users = [
   {"active": True},
   {"active": False},
   {"active": True}
]

active_users = [user for user in users if user["active"] == True]
active_count = len(active_users)
print("Active Users Total Count:", active_count)


## 6. Gmail Filter
emails = [
   {"email": "a@gmail.com"},
   {"email": "b@yahoo.com"},
   {"email": "c@gmail.com"}
]

gmails_list = [email for email in emails if email["email"] == "@gmail.com"]
emails_list = [email["email"] for email in emails if email["email"].endswith("@gmail.com")]
print("Email List:", emails_list)



## 7. Passed Students Filter
students = [
   {"name": "A", "marks": 80},
   {"name": "B", "marks": 90},
   {"name": "C", "marks": 30}
]

passed_student = [student for student in students if student["marks"] > 40]
print("Passed Student:", passed_student)


## 8. Product Name List
products = [
   {"name": "Laptop"},
   {"name": "Phone"}
]

product_list = [product["name"] for product in products]
print("Product Name List:", product_list)


## 9. Unique Categories
products = [
   {"category": "Phone"},
   {"category": "Laptop"},
   {"category": "Phone"}
]

# লজিক: Set Comprehension (থার্ড ব্র্যাকেটের জায়গায় সেকেন্ড ব্র্যাকেট `{}`)
# এটি ডুপ্লিকেট 'Phone' অটোমেটিক রিমুভ করে দেবে
unique_sets = {product["category"] for product in products}
print(unique_sets)


## 10. User ID Checker
user_ids = {1, 2, 3, 4}

# লজিক: 'in' অপারেটর ব্যবহার করে ওয়ান-ক্লিকে ফাস্ট সার্চ করা
is_exists =  4 in user_ids
print("Is User ID 4 Exists:", is_exists)

# আমাদের Level 1 সফলভাবে সম্পন্ন হলো! বেসিক ডেটা প্রসেসিংয়ের এই ধারণাগুলো ক্লিয়ার |


########################################################################################

##### Level 2: JSON Handling Projects (11-20)
"""
বাস্তব ব্যাকএন্ড ডেভেলপমেন্টে ডেটাবেস বা এপিআই থেকে যখন ডেটা আসে, 
তখন নির্দিষ্ট আইডি দিয়ে ইউজার খোঁজা বা আইটেম কাউন্ট করার মতো লজিকগুলো প্রায় প্রতিটা এন্ডপয়েন্টেই লিখতে হয়।

"""

## 11. User Lookup by ID
users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"}
]

def find_user_by_id(user_id):
   for user in users:
      if user["id"] == user_id:
         return user 
   return None
   
print("User Lookup (ID 2):", find_user_by_id(2))



## 12. Find Product By Name
products = [
   {"name": "Laptop"},
   {"name": "Phone"}
]

def find_proudct(product_name):
   for product in products:
      if product["name"].lower() == product_name.lower():
         return product
      
   return None

print("Find Product ('Phone'):", find_proudct("Phone"))



## 13. Student Lookup
students = [
   {"name": "A", "marks": 80},
   {"name": "B", "marks": 90}
]

def get_student_marks(name):
   for student in students:
      if student["name"] == name:
         return student["marks"]
   return "Not found"

print("Student 'B' Marks:", get_student_marks("A"))



## 14 & 15. Highest & Lowest Price Product
products =[
   {"name": "Mouse", "price": 1000},
   {"name": "Laptop", "price": 50000},
   {"name": "keyboard", "price": 2000}
]

highest_product = max(products, key=lambda p: p["price"])
lowest_product = min(products, key=lambda p: p["price"])

print("Highest Price:", highest_product)
print("lowest Price", lowest_product)



## 16 & 17. Highest & Lowest Marks Student
students = [
   {"name": "Habib", "marks": 80},
   {"name": "Mamun", "marks": 90},
   {"name": "Rudro", "marks": 70}
]

highest_marks = max(students, key=lambda m: m["marks"])
lowest_marks = min(students, key=lambda m: m["marks"])

print("Highest Marks: ", highest_marks)
print("Lowest Marks:", lowest_marks)



## 18. User Count by Country
users = [
   {"country": "BD"},
   {"country": "BD"},
   {"country": "USA"}
]

country_count = {}

for user in users:
   country = user["country"]
   country_count[country] = country_count.get(country, 0) + 1

print("Country Analytics:", country_count)



## 19. Category Count
products = [
   {"category": "Phone"},
   {"category": "Phone"},
   {"category": "Laptop"}
]

category_count = {}

for p in products:
   cat = p["category"]
   category_count[cat] = category_count.get(cat, 0) + 1

print("Category Analytics:", category_count)



## 20. Email Domain Counter
emails = [
   "a@gmail.com",
   "b@gmail.com", 
   "c@yahoo.com"
]

domain_count = {}
for email in emails:
   domain = email.split("@")[1]
   domain_count[domain] = domain_count.get(domain, 0) + 1 

print("Domain Analytics:", domain_count)

# আমাদের Level 2-এর ১০টি প্রজেক্টও শেষ হয়ে গেল! 
# বিশেষ করে get() মেথড ব্যবহার করে ডিকশনারিতে আইটেম কাউন্ট করার লজিকটা ব্যাকএন্ডে দারুণ কার্যকরী।


######################################################################################

##### Level 3: API Response Processing (21-30)
"""
বাস্তব প্রজেক্টে যখন আমরা থার্ড-পার্টি কোনো এপিআই (যেমন: Stripe, Twilio বা 
আমাদের নিজেদের ব্যাকএন্ড এপিআই) থেকে রেসপন্স পাই, 
তখন ডেটাগুলো একটু বেশি নেস্টেড (Nested JSON) অবস্থায় থাকে।

"""

## 21. Extract All Names
response = {
   "users": [
      {"name": "Mamun"},
      {"name": "Habib"}
   ]
}

names_list = [user["name"] for user in response["users"]]
print(names_list)


## 22. Extract All Emails
response = {
   "users": [
      {"email": "a@gmail.com"},
      {"email": "b@gmail.com"}
   ]
}

emails_list = [user["email"] for user in response["users"]]
print(emails_list)


## 23. Extract All IDs
response = {
    "users": [
        {"id": 101},
        {"id": 102}
    ]
}

id_list = [user["id"] for user in response["users"]]
print(id_list)


## 24. Count Total Users
response = {
    "users": [
        {"name": "Mamun"},
        {"name": "Rahim"},
        {"name": "Karim"}
    ]
}

names_list = [user["name"] for user in response["users"]]
total_users = len(response["users"])
print(names_list)
print(total_users)


## 25. Find User By Email
response = {
    "users": [
        {"email": "a@gmail.com", "name": "Mamun"},
        {"email": "b@gmail.com", "name": "Rahim"}
    ]
}

def find_by_email(target_email):
   for email in response["users"]:
      if email["email"] == target_email:
         return email
      
   return None

print("User Profile:", find_by_email("b@gmail.com"))



##  26. Total Product Price
response = {
   "products": [
      {"price": 100},
      {"price": 200}
   ]
}

total_price = sum(p["price"] for p in response["products"])
print("Total Price: ", total_price)



## 27. Active User Count
response = {
    "users": [
        {"name": "A", "active": True},
        {"name": "B", "active": False},
        {"name": "C", "active": True}
    ]
}

active_users = len([user["active"] for user in response["users"] if user["active"] == True])

print(active_users)



## 28. Unique User Countries
response = {
    "users": [
        {"country": "BD"},
        {"country": "USA"},
        {"country": "BD"}
    ]
}

unique_countries = {user["country"] for user in response["users"]}
print(unique_countries)



## 29. Extract All Tags (Nested List)
posts = [
   {"tags": ["python", "django"]},
   {"tags": ["api", "python"]}
]

# # লজিক: Nested Loop বা জোড়া লুপ কম্প্রহেনশন ব্যবহার করে ইউনিক ট্যাগ সেট করা
unique_tags = {tag for p in posts for tag in p["tags"]}
print(unique_tags)


## 30. Most Expensive Product
response = {
    "products": [
        {"name": "Mouse", "price": 100},
        {"name": "Laptop", "price": 50000},
        {"name": "Keyboard", "price": 1500}
    ]
}

expensive_product = max(response["products"], key=lambda p: p["price"])
print(expensive_product)

# আমাদের Level 3 (API Response Processing) চমৎকারভাবে শেষ হলো!



############################################################################################
##### Level 4: Dictionary Comprehension Projects (31-40)
""""
ব্যাকএন্ডে কোনো ডেটাবেস থেকে পাওয়া লিস্টকে যখন আমরা ঝটপট 
একটা লুকআপ টেবিল বা ইনডেক্স ম্যাপে রূপান্তর করতে চাই, 
তখন ডিকশনারি কম্প্রহেনশন ({key: value for item in iterable}) সবচেয়ে শক্তিশালী ভূমিকা পালন করে।

"""

## 31. Square Dictionary
# লজিক: ১ থেকে ১০ পর্যন্ত সংখ্যার বর্গ দিয়ে ডিকশনারি তৈরি
squares = {x: x*x for x in range(1, 11)}
print("Squares Dictionary: ", squares)




## 32. Cube Dictionary
# লজিক: ১ থেকে ৫ পর্যন্ত সংখ্যার ঘন (Cube) তৈরি
cubes = {x: x**3 for x in range(1, 6)}
print("Cubes:", cubes)




## 33. Word ➡️ Length
words = ["apple", "banana", "orange"]

# লজিক: শব্দকে Key এবং তার লেন্থকে Value বানানো
word_lengths = {word: len(word) for word in words}
print(word_lengths)




## 34. Product ➡️ Price (Lookup Map)
products = [
   {"name": "Laptop", "price": 50000},
   {"name": "Phone", "price": 20000}
]

# লজিক: নাম দিয়ে সরাসরি প্রাইস খোঁজার জন্য ম্যাপ তৈরি
price_map = {product["name"]: product["price"] for product in products}
print("Price Map:", price_map)



## 35. User ID ➡️ Name
users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"}
]

# লজিক: ব্যাকএন্ডে রিলেশনাল ডেটা ওয়ান-ক্লিকে ম্যাপ করা
user_map = {user["id"]: user["name"] for user in users}
print("User Map:", user_map)



## 36. Student ➡️ Marks
students = [
   {"name": "Habib", "marks": 80},
   {"name": "Mamun", "marks": 90}
]

student_marks_map = {student["name"]: student["marks"] for student in students}
print("Student Marsk Map:", student_marks_map)



## 37. Student ➡️ Pass/Fail
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 35}
]

# লজিক: ডিকশনারি কম্প্রহেনশনের ভেতরে Inline If-Else কন্ডিশন
pass_fail_map = {student["name"]: "Pass" if student["marks"] >= 40 else "Fail" for student in students}
print("Students Map:", pass_fail_map)




## 38. Number ➡️ Even/Odd
even_odd_map = {num: "Even" if num % 2 == 0 else "Odd" for num in range(1, 11)}
print("Even/Odd Map:", even_odd_map)




## 39. Number ➡️ Positive/Negative
numbers = [-2, 1, -4, 3, 5, 0, -7]

# লজিক: পজিটিভ, নেগেটিভ নাকি জিরো তা ডাইনামিকালি সেট করা
num_status_map = {num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero" for num in numbers}
print("Number Status Map:", num_status_map)




## 40. Character ➡️ ASCII
chars = ["a", "b", "c"]

ascii_map = {char: ord(char) for char in chars}
print("ASCII Map:", ascii_map)


# আমাদের Level 4 দুর্দান্ত গতিতে শেষ হলো! 
# ডিকশনারি কম্প্রহেনশনের এই কনসেপ্টগুলো ব্যাকএন্ডে ডেটা স্ট্রাকচার রি-শেপ (Reshape) করতে সবচেয়ে বেশি কাজে লাগে।




########################################################################################

##### Level 5: Backend Interview Style (41-50)
"""
টেকনিক্যাল ইন্টারভিউতে এবং রিয়েল-টাইম প্রোডাকশন সার্ভারে 
পারমিশন চেক, 
ডুপ্লিকেট রিমুভাল, 
আর অ্যানালিটিক্স যেভাবে করা হয়-

"""

## 41. Duplicate Emails Remove
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]

unique_emails = set(emails)
print(unique_emails)




## 42. Duplicate User IDs Remove
user_ids = [101, 102, 101, 103, 102]

unique_ids = set(user_ids)
print(unique_ids)





## 43. Common Users Between Two APIs
api1 = {"mamun", "rahim", "karim"}
api2 = {"mamun", "nondita", "rahim"}

common_users = api1 & api2
print(common_users)





## 44. New Users Detection
all_registered_users = {"mamun", "rahim", "karim"}
old_database_users = {"mamun", "rahim"}

# লজিক: Difference (-) অপারেটর দিয়ে নতুন বা অমিল ডেটা বের করা
new_users = all_registered_users - old_database_users
print("New Detected Users:", new_users)





## 45. Permission Checker (RBAC)
required_permissions = {"read", "write"}
user_permissions = {"read", "write", "delete"}

has_access = required_permissions.issubset(user_permissions)
print("Access Grandted?:", has_access)





## 46. Role Matching System (Skill Gap Analytics)
fronted_skills = {"html", "css", "javascript"}
backend_skills = {"python", "sql", "javascript"}

common_skills = fronted_skills & backend_skills
print("Overlapping skills:", common_skills)





## 47. User Activity Tracker
user_activity = [1, 2, 3, 1, 2, 4, 1]

active_users = set(user_activity)
print("Unique Active Users today:", active_users)





## 48. Product Inventory Summary
products = [
   {"stock": 50},
   {"stock": 20},
   {"stock": 5}
]

total_stock = sum(product["stock"] for product in products)
print("Total Stock:", total_stock)





## 49. Order Revenue Calculator
orders = [
   {"amount": 500},
   {"amount": 700}
]

total_revenue = sum(order["amount"] for order in orders)
print("Total Sales Revenue:", total_revenue)





## 50. Mini API Analytics
users = [
   {"country": "BD", "active": True},
   {"country": "USA", "active": False},
   {"country": "BD", "active": True}
]

total_users = len(users)
active_users = len([user["active"] for user in users if user["active"] == True])
unique_countries = {user["country"] for user in users}

country_count = {}
for user in users:
   c = user["country"]
   country_count[c] = country_count.get(c, 0) + 1


analytics_dashboard = {
   "total_users": total_users,
   "active_users": active_users,
   "unique_countries": unique_countries,
   "country_count": country_count
}
print("API Analytics Dashboard Response:\n________________________________\n",analytics_dashboard)


"""
অভিনন্দন! 
তুমি এক টানে পাইথন ব্যাকএন্ড ইঞ্জিনিয়ারিংয়ের বেসিক ও ইন্টারমিডিয়েট লেভেলের 
পুরো ৫০টি মিনি প্রজেক্ট শেষ করে ফেলেছ। 
List, Dictionary, Set, Loop, এবং Comprehension-কে কীভাবে মিক্স করে রিয়েল এপিআই রেসপন্স প্রসেস করতে হয়, 
তার ওপর তোমার লজিক এখন ক্রিস্টাল ক্লিয়ার।

"""