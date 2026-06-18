

## 1. Dictionary Comprehension কী?
# List Comprehension
squares = [x*x for x in range(1, 6)]
print(squares)

# Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)





## 2. Basic Structure
# {
#    key: value 
#    for item in iterable 
# }

d = {x: x*2 for x in range(1, 6)}
print(d)





## 3. Normal loop vs Comprehension
# Normal(loop)
result = {}

for item in range(1, 6):
   result[item] = item*item 

print(result)

# Comprehension
d = {item: item*3 for item in range(1, 6)}
print(d)
# একই কাজ, কিন্তু ছোট ও পরিষ্কার।





## 4. Square Dictionary
square = {x: x*x for x in range(1, 6)}
print(square)





## 5. Cube Dictionary
cube = {x: x**3 for x in range(1, 6)}
print(cube)





## 6. String Length Dictionary
words = [
   "apple",
   "banana",
   "mango",
   "lichi",
   "grape"
]

result = {word: len(word) for word in words}
print(result)





## 7. Uppercase Dictionary
words = [
   "apple",
   "banana",
   "lichi"
]

result = {word: word.upper() for word in words}
print(result)





## 8. Lowercase Dictionary
words = [
   "APPLE",
   "BANANA",
   "LICHI"
]

result = {word: word.lower() for word in words}
print(result)





## 9. Two List to Dictionary
# Normal
#________
names = [
   "Mamun",
   "Rahim",
   "Karim"
]
ages = [20, 25, 30]

print(dict(zip(names, ages)))


#
products = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

prices = [
    50000,
    1000,
    2000
]

print(dict(zip(products, prices)))


# comprehension
#_______________
names = [
   "Mamun",
   "Rahim",
   "Karim"
]
ages = [20, 25, 30]

result = {name: age for name, age in zip(names, ages)}
print(result)


#
products = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

prices = [
    50000,
    1000,
    2000
]

result = {product: price for product, price in zip(products, prices)}
print(result)





## 10. Filtering
# Even Number
result = {x: x*x for x in range(1, 11) if x % 2 == 0}
print(result)

numbers = [1, 2, 3, 4, 5,  6, 7, 8, 9]
result = {x: x for x in numbers if x % 2 == 0}
print(result)

# Odd Number
result = {x: x*x for x in range(1, 11) if x % 2 != 0}
print(result)

numbers = [1, 2, 3, 4, 5,  6, 7, 8, 9]
result = {x: x for x in numbers if x % 2 != 0}
print(result)

# Positive Number
numbers = [-1, 2, -4, 0, 3, 5]
positive_num = {x: "Positive" if x > 0 else "Negative" for x in numbers}
print(positive_num)

# double Number
numbers = [1, 2, 3, 4, 5,  6, 7, 8, 9]
result = {x: x*2 for x in numbers}
print(result)

# Triple Number
numbers = [1, 2, 3, 4, 5,  6, 7, 8, 9]
result = {x: x*3 for x in numbers}
print(result)





## 11. Conditional value
result = {x: "Even" if x % 2 == 0 else "Odd" 
          for x in range(1, 6)
}

print(result)

numbers = [2, 3, 6, 7, 11, 43, 23, 64, 88, 23]
result = {x: "Even" if x % 2 == 0 else "Odd"
          for x in numbers}

print(result)





## 12. Character Frequency
# Most Important
text = "GeeksforGeeks"

freq = {char: text.count(char) 
        for char in text
}

print(freq)

#
text = "banana"

freq = {char: text.count(char) for char in text}
print(freq)





## 13. Backend Example 
users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Habib"},
   {"id": 3, "name": "Karim"}
]

result = {user["id"]: user["name"]
          for user in users
}

print(result)

#
students = [
   "Mamun",
   "Rahim",
   "Karim"
]
marks = [80, 85, 90]

result = {student: mark for student, mark in zip(students, marks)}
print(result)

#
students = {
   "Mamun": 90,
   "Rahim": 32,
   "Karim": 85,
   "Rajib": 25, 
   "Noyon": 76,
   "Rudro": 89
}

result = {student: "Passed" if marks >= 33 else "Failed" for student, marks in students.items()}
print(result)

# loop
students = {
    "Mamun":80,
    "Rahim":35,
    "Karim":90,
    "Sohan":25
}

result = {}

for name, marks in students.items():
   if marks >= 33:
      result[name] = "Pass"
   else:
      result[name] = "Fail"

print(result)





## 14. Backend Example (Product Price)
# key-value dictionary
products = [
   {"name": "Laptop", "price": 50000},
   {"name": "Mouse", "price": 1000},
   {"name": "Keyboard", "price": 2000}
]

result = {product["name"]: product["price"]
          for product in products
}

print(result)

# total sum
products = [
   {"name": "Laptop", "price": 50000},
   {"name": "Mouse", "price": 1000},
   {"name": "Keyboard", "price": 2000}
]

result = sum(product["price"] for product in products)

print(result)




## 15. Nested Dictionary Comprehension

result = {
   x: {
      y: x*y 
      for y in range(1, 5)
   }
      for x in range(1, 5)
}

print(result)





## 16. Nested Multiplication Dictionary
multiplication_dict = {
   i: {
      j: i*j 
      for j in range(1, 4)
   }
      for i in range(1, 4)
}

print(multiplication_dict)

# Loop
multiplication_dict = {}

# বাইরের লুপ (i) ১ থেকে ৩ পর্যন্ত ঘুরবে
for i in range(1, 4):
   multiplication_dict[i] = {} # ভেতরের খালি ডিকশনারি তৈরি


   # ভেতরের লুপ (j) ১ থেকে ৩ পর্যন্ত ঘুরবে
   for j in range(1, 4):
      multiplication_dict[i][j] = i*j # গুণফল অ্যাসাইন করা হচ্ছে

print(multiplication_dict)





## 17. Character ➡️ ASCII
# লিস্টের প্রতিটি ক্যারেক্টারকে কী (key) এবং পাইথনের বিল্ট-ইন ord() ফাংশন ব্যবহার করে 
# তাদের ASCII ভ্যালুকে ভ্যালু (value) হিসেবে নিয়ে ডিকশনারি তৈরি করার সম্পূর্ণ কোড নিচে দেওয়া হলো:
chars = ["A", "B", "C"]
char_asci_dict = {char: ord(char) for char in chars}
print(char_asci_dict)

# Loop
chars = ["A", "B", "C"]
char_asci_dict = {}

for char in chars:
   char_asci_dict[char] = ord(char)

print(char_asci_dict)





## 18. Backend-এর জন্য সবচেয়ে গুরুত্বপূর্ণ ৫ Pattern
"""
pattern 1: Square
{x: x*x for x in range(....)}

pattern 2: Length Mapping
{word: len(word) for word in words}

pattern 3: Tow Lists ➡️ Dictionary
{name: age, for name, age in zip(names, ages)}

pattern 4: Filtering
{x: value for x in data if conditon}

pattern 5: API Response Processing
{obj["id]: obj["name] for obj in users}


কারণ Backend-এ API Response সাধারণত এরকম হয়:
users = [
    {"id": 1, "name": "Mamun"},
    {"id": 2, "name": "Rahim"},
    {"id": 3, "name": "Karim"}
]

আর তুমি খুব প্রায়ই লিখবে:
user_map = {
    user["id"]: user["name"]
    for user in users
}

এটাই বাস্তব Dictionary Comprehension-এর সবচেয়ে গুরুত্বপূর্ণ ব্যবহার।

"""