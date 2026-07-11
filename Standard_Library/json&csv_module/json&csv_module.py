

# 1. JSON কী?
"""
JSON এর পূর্ণরূপ:
JavaScript Object Notation

সহজ ভাষায়:

JSON হলো data exchange করার একটি standard format, যা মানুষ পড়তে পারে এবং machine সহজে বুঝতে পারে।

Backend এ:

Frontend ↔ Backend

এর মধ্যে data পাঠানোর জন্য JSON ব্যবহার হয়।

Example:

একজন User:

{
    "id": 1,
    "name": "Mamun",
    "email": "mamun@gmail.com"
}

এখানে:

key → "name"
value → "Mamun"
2. Python Dictionary vs JSON

Python Dictionary:

user = {
    "name": "Mamun",
    "age": 25
}

JSON:

{
    "name": "Mamun",
    "age": 25
}

দেখতে একই রকম।

কিন্তু:

Dictionary হলো Python object।

JSON হলো text format।


Python Dictionary:(Python object)
user = {
   "id": 1,
   "name": "Mamun",
   "age": 25
}


Json String:(String Format)
{
   "id": 1, 
   "name": "Mamun",
   "age": 25
}

"""

"""
| Function | কাজ               |
| -------- | ----------------- |
| dump()   | JSON file এ write |
| dumps()  | JSON string তৈরি  |
| load()   | JSON file read    |
| loads()  | JSON string read  |


| Python | JSON   |
| ------ | ------ |
| dict   | object |
| list   | array  |
| str    | string |
| int    | number |
| True   | true   |
| False  | false  |
| None   | null   |

"""

import json 
# dictionary to json file write
user = {
   "name": "mamun",
   "age": 25
}
with open('user.json', "w") as file:
   json.dump(user, file, indent=4)

# dictionary to json string
user = {
   "name": "mamun",
   "age": 25
}
json_data = json.dumps(user)
print(json_data)
print(type(json_data))

# json file read to dictionary
with open("user.json", "r") as file:
   data = json.load(file)

print(data)

# json file to dictionary
response = '{"name": "mamun", "age":25}'

user = json.loads(response)
print(user)
print(type(user))





#### 2. json.dumps() = dictionary to json string
import json 
user = {
   "name": "Mamun",
   "age": 25
}

json_data = json.dumps(user)
print(json_data)
print(type(json_data))

## json.dump() = dictionary to json file write
import json
user = {
   "name": "Mamun",
   "age": 25
}

with open("user.json", "w") as file:
   json.dump(
      user, 
      file,
      indent=4
   )



##### 3. json.loads() = json_string to dictionary
import json

json_string = '{"name":"Mamun", "age":25}'

user = json.loads(json_string)
print(user)
print(type(user))

## json.load() = json file read to dictionary
import json
with open("user.json", "r") as file:
   data = json.load(file)

print(data)




##### 4. Backend Example 1
# dictionary to json_string
response = {
   "status": "success",
   "user": "Mamun"
}

import json 

json_data = json.dumps(response)
print(json_data)
print(type(json_data))

# json_string to dictionary
response = """
{
   "status": "Success",
   "user": "Mamun"
}
"""

import json 
json_data = json.loads(response)
print(json_data["user"])
print(json_data["status"])


# dictionary to json file write
import json 
response = {
   "status": "success",
   "user": {
      "name": "Mamun",
      "age": 25
   }
}

with open("user.json", "w") as file:
   json.dump(
      response,
      file,
      indent=4
   )

# users save 
import json 

users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"}
]

with open("users.json", "w") as file:
   json.dump(
      users,
      file,
      indent=4
   )


# json file read to dictionary
import json 

with open("user.json", "r") as file:
   users = json.load(file)

print(users)



##########################################################################################

# ##### What is Csv?
"""
CSV এর পূর্ণরূপ:

Comma Separated Values

সহজ ভাষায়:

CSV হলো table format data রাখার একটি file format।

Example:

students.csv

id,name,age
1,Mamun,25
2,Rahim,22

এটা Excel-এর মতো।

"""


# #### 2. CSV File Write করা

import csv 

students = [
   ["id", "name", "age"],
   [1, "mamun", 25],
   [2, "habib", 30]
]

with open("students.csv", "w", newline="") as file:
   writer = csv.writer(file)

   writer.writerow(students)


import csv 
with open("students.csv", "w", newline="") as file:

   writer = csv.writer(file)

   writer.writerow(["Name", "Age"])

   writer.writerow(["Mamun", 25])

   writer.writerow(["habib", 16])





# #### 3. CSV File Read করা
import csv 

with open("students.csv") as file:
   reader = csv.reader(file)

   for row in reader:
      print(row)



# ##### 4. DictWriter
import csv

users = [
   {
      "name": "Mamun",
      "email": "mamun@gmail.com"
   },
   {
      "name": "Rahim",
      "email": "rahim@gmail.com"
   }
]

with open("user.csv", "w", newline="") as file:
   
   writer = csv.DictWriter(
      file,
      fieldnames=[
         "name",
         "email"
      ]
   )

   writer.writeheader()

   writer.writerows(users)



import csv 

with open("users.csv", "w", newline="") as file:

   fields = ["id", "name"]

   writer = csv.DictWriter(file, fieldnames=fields)

   writer.writeheader()

   writer.writerow({"id": 1, "name": "Mamun"})
   writer.writerow({"id": 2, "name": "Habib"})



# ##### 5. DictReader
import csv 

with open("users.csv") as file:
   reader = csv.DictReader(file)

   for row in reader:
      print(row["name"])


import csv 
with open("user.csv", "r", newline="") as file:
   reader = csv.DictReader(file)

   for user in reader:
      print(user)





# ##### 6. Export Users
import csv 

users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"}
]

with open("export.csv", "w", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=["id", "name"])

   writer.writeheader()

   writer.writerows(users)


# ##### 7. Export Products
import csv 

products = [
   {"name": "Mouse", "price": 1000},
   {"name": "Keyboard", "price": 2000}
]

with open("products.csv", "w", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=["name", "price"])

   writer.writeheader()

   writer.writerows(products)


# # Import Products
import csv 

with open("products.csv") as file:
   reader = csv.DictReader(file)

   for product in reader:
      print(product["name"])

   # for product in reader:
   #    print(product["price"])



##### Django Example
# from django.http import JsonResponse

# data = {
#    "message": "Success"
# } 

# return JsonResponse(data)



##### Backend Real Examples
"""
JSON ব্যবহার:
REST API response
JWT payload
Configuration
Request/Response data

Example:

Django REST Framework:

{
"id":1,
"title":"Laptop"
}
CSV ব্যবহার:
User export
Sales report
Order report
Database backup

Example:

Admin:

"Download all users"

↓

users.csv


"""
