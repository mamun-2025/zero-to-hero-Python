

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