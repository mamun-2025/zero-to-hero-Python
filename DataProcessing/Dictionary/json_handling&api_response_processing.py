

##### JSON Handling
# 1. JSON কী?
# JSON = JavaScript Object Notation
# ডাটা আদান-প্রদানের সবচেয়ে জনপ্রিয় ফরম্যাট।

{
   "name": "Mamun",
   "age": 20,
   "skills": ["Python", "Django"]
}

# 2. Python Dictionary vs JSON
# Dictionary 
data = {
   "name": "Mamun",
   "age": 25
}

# JSON
{
   "name": "Mamun",
   "age": 25
}

# দেখতে প্রায় একই।
# তাই API Response সহজে Dictionary তে convert করা যায়।


# 3. JSON Module
import json 


# 4. Python Dict ➡️ JSON
# json.dumps()
import json 

data = {
   "name": "Mamun",
   "age": 25
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))


# 5. JSON ➡️ Python Dict
# json.loads()
import json 

json_data = '{"name": "Mamun", "age": 25}'

dict_data = json.loads(json_data)
print(dict_data)
print(type(dict_data))


# 6. Print JSON
import json

data = {
   "name": "Mamun",
   "age": 25
}


# 7. Print Dictionary
print(json.dumps(data, indent=4))

import json 
json_data = '{"name": "Mamun", "age": 25}'
print(json.loads(json_data))


# 8. Nested JSON
data = {
   "user": {
      "name": "Mamun",
      "age": 25
   }
}

print(data["user"]["name"])
print(data["user"]["age"])


# 9. JSON List
data = {
   "users": [
      {"name": "Mamun"},
      {"name": "Rahim"},
      {"name": "Karim"}
   ]
}

print(data["users"][0]["name"])
print(data["users"][1]["name"])
print(data["users"][2]["name"])


# 10. JSON File Write
import json

data = {
   "name": "Mamun",
   "age": 25
}

with open("data.json", "w") as file:
   json.dump(data, file)


# 11. JSON File Read
import json 

with open("data.json", "r") as file:
   data = json.load(file)

print(data)


# 12. JSON Handling Practice

# name print করো।
data = {
    "name": "Mamun",
    "age": 20
}

json_data = json.dumps(data["name"])
print(json_data)


# email বের করো।
data = {
    "user": {
        "email": "mamun@gmail.com"
    }
}

print(data["user"]["email"])


# সব names বের করো।
data = {
    "users": [
        {"name": "Mamun"},
        {"name": "Rahim"}
    ]
}

print(data["users"][0]["name"])


# 13. API Response Processing
# Backend Developer-এর সবচেয়ে গুরুত্বপূর্ণ স্কিল।
# ধরো API থেকে এলো:
response = {
   "status": "success",
   "data": [
      {
         "id": 1,
         "name": "Mamun",
         "email": "mamun@gmail.com"
      },
      {
         "id": 2,
         "name": "Rahim",
         "email": "rahim@gmail.com"
      },
      {
         "id": 3,
         "name": "Rajib",
         "email": "yahooo.com"
      }
   ]
}


# 1. Extract ALL Names
names = [
   user["name"] for user in response["data"]
]
print(names)


# 2. Extract All Names
emails = [
   user["email"] for user in response["data"]
]
print(emails)


# 3. Find User By ID
for user in response["data"]:
   if user["id"] == 2:
      print(user)


# 4. Filter Gmail Users
gmail_users = [
    user for user in response["data"]
    if "@gmail.com" in user["email"]
]

print(gmail_users)


# 5. Total Users
total_users = len(response["data"])
print(total_users)




