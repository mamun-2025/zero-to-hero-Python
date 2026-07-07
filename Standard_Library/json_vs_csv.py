


import json 
#### What is json?
# json = JavaScript Object Notation
"""
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


##### 2. json.dumps() = dictionary to json string
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

##### What is Csv?
"""
CSV = Comma Separated Values
Excel Data Favorite format

"""


#### 2. CSV Write
import csv 

with open("students.csv", "w", newline="") as file:

   writer = csv.writer(file)

   writer.writerow(["Name", "Age"])

   writer.writerow(["Mamun", 25])

   writer.writerow(["Nondtia", 16])



#### 3. CSV Read
import csv 

with open("students.csv") as file:
   reader = csv.reader(file)

   for row in reader:
      print(row)



##### 4. DictWriter
import csv 

with open("users.csv", "w", newline="") as file:

   fields = ["id", "name"]

   writer = csv.DictWriter(file, fieldnames=fields)

   writer.writeheader()

   writer.writerow({"id": 1, "name": "Mamun"})
   writer.writerow({"id": 2, "name": "Nondita"})



##### 5. DictReader
import csv 

with open("users.csv") as file:
   reader = csv.DictReader(file)

   for row in reader:
      print(row["name"])



##### 6. Export Users
import csv 

users = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "name": "Rahim"}
]

with open("export.csv", "w", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=["id", "name"])

   writer.writeheader()

   writer.writerows(users)


##### 7. Export Products
import csv 

products = [
   {"name": "Mouse", "price": 1000},
   {"name": "Keyboard", "price": 2000}
]

with open("products.csv", "w", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=["name", "price"])

   writer.writeheader()

   writer.writerows(products)


# Import Products
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
