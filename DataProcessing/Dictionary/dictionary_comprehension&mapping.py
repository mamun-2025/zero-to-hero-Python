

##### Level 4: Dictionary Comprehension + Mapping (1-10)


## Problem 1: 
# লিস্ট অফ ডিকশনারি থেকে একটি নতুন ডিকশনারি ম্যাপিং তৈরি করার জন্য 
# Dictionary Comprehension-ই পাইথনে সবচেয়ে Best, Standard এবং Fast (সবচেয়ে দ্রুত কাজ করে) নিয়ম। 
# পাইথনে একে বলা হয় "Pythonic way" (পাইথনের নিজস্ব আদর্শ স্টাইল)।
## Rule 1: dictionary comprehension
users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"},
   {"id": 3, "name": "Karim"}
]

# Dictionary Comprehension ব্যবহার করে id-র সাথে name-এর ম্যাপিং করা হলো
dict_map = {user["id"]: user["name"] for user in users}
print(dict_map)


## Rule 2: for loop
# কেন জানবে: কোডটি পড়তে এবং বুঝতে খুব সহজ। 
# তবে Dictionary Comprehension-এর চেয়ে লাইনের সংখ্যা বেশি লাগে।
users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"},
   {"id": 3, "name": "Karim"}
]

dict_map = {}

for user in users:
   dict_map[user["id"]] = user["name"]

print(dict_map)


## Rule 3: dict() এবং Generator ব্যবহার করে
# কেন জানবে: অনেকে সেকেন্ড ব্র্যাকেটের চেয়ে ফাংশন ব্যবহার করতে বেশি পছন্দ করেন, 
# তবে এটি Comprehension থেকে সামান্য ধীরগতির হতে পারে।
users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"},
   {"id": 3, "name": "Karim"}
]

dict_map = dict((user["id"], user["name"]) for user in users)

print(dict_map)


## Rule 4: map() এবং lambda ব্যবহার করে (Advanced/Functional)
# কেন জানবে: ইন্টারভিউ বা কোনো জটিল ডেটা প্রসেসিং পাইপলাইনে এটি দেখা যেতে পারে। 
# তবে এটি দেখতে একটু জটিল এবং সাধারণ মানুষের জন্য পড়া কঠিন।

users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"},
   {"id": 3, "name": "Karim"}
]

dict_map = dict(map(lambda user: (user["id"], user["name"]), users))
print(dict_map)

"""
পারফরম্যান্স তুলনা (Speed Test)
ভেতরের মেকানিজমের কারণে পাইথনে এই ৪টি নিয়মের স্পিড বা পারফরম্যান্স সাধারণত এমন হয়:

1. Dictionary Comprehension 🥇 (সবচেয়ে দ্রুত ও বেস্ট)

2. For Loop 🥈 (সহজ, কিন্তু একটু ধীরগতির)

3. dict() with Generator 🥉 (মাঝারি স্পিড)

4. map() with lambda ❌ (সবচেয়ে ধীরগতির এবং কম রিডেবল)

"""





#_______________________________________________________________________________
## Problem 2: 
# Rule 1: Dictionary Comprehension
products = [
   {"id": 101, "name": "Laptop"},
   {"id": 102, "name": "Mouse"}
]

product_map = {product["id"]: product["name"] for product in products}

print("1. Dictionary Comprehension:", product_map)

# Rule 2: for loop
products = [
   {"id": 101, "name": "Laptop"},
   {"id": 102, "name": "Mouse"}
]

product_map = {}

for product in products:
   product_map[product["id"]] = product["name"]

print("2. For loop:", product_map)


# Rule 3: Dict() with Generator
products = [
   {"id": 101, "name": "Laptop"},
   {"id": 102, "name": "Mouse"}
]

product_map = dict((product["id"], product["name"]) for product in products)
print("3. Generator Expression: ", product_map)


# Rule 4: map() with lambda (Functional Approach)
products = [
   {"id": 101, "name": "Laptop"},
   {"id": 102, "name": "Mouse"}
]

product_map = dict(map(lambda product: (product["id"], product["name"]), products))

print("map() with lambda:", product_map)






#__________________________________________________________________________________
## Problem 3:
students = [
   {"student": "Mamun", "marks": 86},
   {"student": "Habib", "marks": 90}
]

# dictionary
student_map = {s["student"]: s["marks"] for s in students}
print("Dictionary: ", student_map)

# for loop
student_map = {}
for student in students:
   student_map[student["student"]] = student["marks"]

print("For loop:", student_map)

# dict() with generator
student_map = dict((s["student"], s["marks"]) for s in students)
print("Dict() with Generator: ", student_map)

# map() with lambda
student_map = dict(map(lambda s: (s["student"], s["marks"]), students))
print("map() with lambda: ", student_map)






#___________________________________________________________________________________
## Problem 4:
products = [
   {"name": "Laptop", "price": 50000},
   {"name": "Mouse", "price": 2000},
   {"name": "Keyboard", "price": 1000}
]






#______________________________________________________________________________________
## Problem 5:
users = [
   {"user": 1, "email": "mamun@gmail.com"},
   {"user": 2, "email": "habib@gmail.com"},
]






#________________________________________________________________________________
## Problem 6:
users = [
   {"username": "Mamun", "age": 25},
   {"username": "Habib", "age": 30},
   {"username": "Sanjib", "age": 28}
]







#____________________________________________________________________________________________
## Problem 7:
books = [
   {"id": 1, "title": "Python"},
   {"id": 2, "title": "Java"},
   {"id": 3, "title": "JavaScript"}
]






#__________________________________________________________________________________
## Problem 8: 
employees = [
   {"id": 1, "salary": 50000},
   {"id": 2, "salary": 30000},
   {"id": 3, "salary": 25000}
]







#________________________________________________________________________________
## Problem 9:
orders = [
   {"order_id": 1, "amount": 1000},
   {"order_id": 2, "amount": 500},
   {"order_id": 3, "amount": 700}
]







#_____________________________________________________________________________________________________
## Problem 10
courses = [
   {"id": 101, "name": "Python"},
   {"id": 102, "name": "Linux"}
]

# Dictionary 
course_dict = {course["id"]: course["name"] for course in courses}
print(f"Dicitionary: {course_dict}")

# For loop
course_dict = {}

for course in courses:
   course_dict[course["id"]] = course["name"]

print(f"For loop: {course_dict}")

# dict() with generator expression
course_dict = dict((course["id"], course["name"]) for course in courses)
print("dict() with generator: ", course_dict)

# map() with lambda
course_dict = dict(map(lambda course: (course["id"], course["name"]), courses))
print(f"map with lambda: {course_dict}")
