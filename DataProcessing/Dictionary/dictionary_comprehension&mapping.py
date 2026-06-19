

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

## Problem 3:

## Problem 4:

## Problem 5:

## Problem 6:

## Problem 7:

## Problem 8: 

## Problem 9:

## Problem 10


