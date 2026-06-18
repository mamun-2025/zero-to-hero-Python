

## Problem 1:
user = {
   "name": "Mamun",
   "age": 25
}

print(user.get("name"))
print(user.get("age"))

print(user["name"])
print(user["age"])




## Problem 2:
student = {
   "name": "Mamun"
}

# get() মেথডের দ্বিতীয় আর্গুমেন্ট হিসেবে ডিফল্ট মেসেজটি পাস করতে হয়
result = student.get("city", "Not found")
print(result)
"""

"""




## Problem 3:
student = {
   "name": "Mamun",
   "age": 25,
   "city": "Dhaka"
}

# len() ফাংশনটি যেকোনো সিকোয়েন্স বা কালেকশনের (যেমন: লিস্ট, ডিকশনারি, স্ট্রিং) মোট উপাদানের সংখ্যা রিটার্ন করে। 
# ডিকশনারির ক্ষেত্রে এটি সরাসরি মোট Key-Value Pair বা কী-এর সংখ্যাটি গণনা করে দেয়।
total_keys = len(student)
print(total_keys)



## Problem 4: 
student = {
   "name": "Mamun"
}

student["age"] = 25 # Add
student["city"] = "Dhaka" # Add
student["name"] = "Nondita" # Update
print(student)




## Problem 5:
product = {
   "name": "Laptop",
   "price": 50000
}

product["price"] = 32000
print(product) 





## Problem 6:
data = {}

data["name"] = "Mamun"
data["age"] = 25
data["city"] = "Madaripur"

print(data)

#
data = {}

data.update({"name": "Mamun", "age": 25, "city": "Bashundhara"})
print(data)





## Problem 7:
student = {
   "name": "Mamun",
   "age": 25
}

del student["age"]
print(student)




## Problem 8:
student = {
   "name": "HABIB",
   "age": 25
}

# pop() দিয়ে age remove করো।
# Removed value print করো।
value = student.pop("age")
print(value)


# pop() দিয়ে name remove করো।
# Removed value print করো।
value = student.pop("name")
print(value)




## Problem 9:
data = {
   "a": 1,
   "b": 2,
   "c": 3
}

print(data.popitem())




## Problem 10:
data = {
   "a": 1, 
   "b": 2
}

# clear() মেথড ব্যবহার করে ডিকশনারি খালি করা হলো
data.clear()
print(data)




## Problem 11:
student = {
   "name": "Mamun",
   "age" : 20
}

result = "age" in student
print(result)

result = "city" in student
print(result)




# Problem 12:
student = {
   "name": "Nondita",
   "age": 25
}

print(student.keys())




## Problem 13:
student = {
   "name": "Nondtia",
   "age": 25
}

print(student.values())




## Problem 14:
user = {
   "name": "Mamun",
   "age": 30
}

print(user.items())




## Problem 15:
user = {
   "name": "Mamun",
   "age": 30
}

for k, v in user.items():
   print(k, v)




## Problem 16:
scores = {
   "math": 80,
   "english": 90,
   "science": 85
}

total_sum = sum(scores.values())
print(total_sum)




## Problem 17:
scores = {
   "math": 80,
   "english": 90,
   "science": 85
}

print(list(scores.keys()))
print(list(scores.values()))




## Problem 18:
student = {
    "name": "Mamun",
    "age": 20
}

# items() ব্যবহার করে tuple-এর list তৈরি করা হলো
result = list(student.items())
print(result)



## Problem 19:
d1 = {
   "a": 1,
   "b": 2
}

d2 = {
   "c": 3,
   "d": 4
}

# update() ব্যবহার করে d1 এর সাথে d2 মার্জ করা হলো
d1.update(d2)
print(d1)




## Problem 20:
key_list = ["a", "b", "c"]

result = dict.fromkeys(key_list, "Mamun")
print(result)





## Problem 21:
squares = {x: x*x for x in range(1, 6)}
print(squares)




## Problem 22:
even_dict = {x: x for x in range(1, 11) if x % 2 == 0}
print(even_dict)

# Loop
even_dict ={}

for x in range(1, 11):
   if x % 2 == 0:
      even_dict[x] = x 

print(even_dict)




## Problem 23:
words = [
   "apple",
   "banana",
   "mango"
]

words_length = {word: len(word) for word in words}
print(words_length)


# loop
words = [
   "apple",
   "banana",
   "mango"
]

words_length = {}
for word in words:
   words_length[word] = len(word)

print(words_length)




## Problem 24:
users = [
   {
      "name": "mamun",
      "age": 25
   },
   {
      "name": "Habib",
      "age": 28
   },
   {
      "name": "Rudro",
      "age": 30
   }
]

names_list = [user["name"] for user in users]
print(names_list)


# Loop
users = [
   {
      "name": "mamun",
      "age": 25
   },
   {
      "name": "Habib",
      "age": 28
   },
   {
      "name": "Rudro",
      "age": 30
   }
]
names_list = []

for user in users:
   names_list.append(user["name"])

print(names_list)





## Problem 30:
products = [
   {
      "name": "Laptop",
      "price": 50000
   },
   {
      "name": "Mouse",
      "price": 1000
   },
   {
      "name": "keyboard",
      "price": 2000
   }
]

total_price = sum(product["price"] for product in products)
print(total_price)

# Loop
products = [
    {
        "name": "Laptop",
        "price": 50000
    },
    {
        "name": "Mouse",
        "price": 1000
    },
    {
        "name": "Keyboard",
        "price": 2000
    }
]

total_price = 0

for product in products:
   total_price += product["price"]

print(total_price)





## Problem 31:
users = [
   {"email": "a@gmail.com"},
   {"email": "b@yahoo.com"},
   {"email": "c@gmail.com"}
]

gamil_users = [user for user in users if user["email"].endswith("@gmail.com")]

print(gamil_users)


# Loop
users = [
   {"email": "a@gmail.com"},
   {"email": "b@yahoo.com"},
   {"email": "c@gmail.com"}
]

gamil_users = []

for user in users:
   if user["email"].endswith("@gmail.com"):
      gamil_users.append(user)

print(gamil_users)




## Problem 32:
response = {
   "user": {
      "name":"Mamun",
      "email": "mamun@gmail.com"
   }
}

print(response["user"]["email"])





## Problem 33:
students = [
   {"name": "Habib", "marks": 89},
   {"name": "Mamun", "marks": 80},
   {"name": "Rudro", "marks": 90}
]

# ১. সব marks-এর যোগফল বের করা হলো
total_marks = sum(student["marks"] for student in students)

# ২. মোট ছাত্র সংখ্যা বের করা হলো
total_students = len(students)

# ৩. গড় (Average) বের করা হলো
average_marks = total_marks/total_students



print(total_marks)
print(total_students)
print(int(average_marks))