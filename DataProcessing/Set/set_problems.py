


##### Level 1: Basic Set Problems (1-10)
## Problem 1: Duplicate Number Remove
nums = {1, 2, 2, 2, 3, 3, 4, 5}
unique_nums = set(nums)
print(unique_nums)


## Problem 2: Duplicate Email Remove
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
unique_emails = set(emails)
print(unique_emails)


##  Problem 3: Check করো "rahim" আছে কিনা।
users = {"mamun", "rahim", "karim"}
check = "rahim" in users
print(check)


## Problem 4: নতুন User Add করো।
users = {"mamun", "rahim"}
users.add("nondita")
print(users)


## Problem 5: একসাথে 3 জন User Add করো।
users = {"mamun", "habib"}
users.update(["rahim", "karim", "rudro"])
print(users)


## Problem 6: Remove করো "rahim"।
users = {"mamun", "rahim", "karim"}
users.remove("rahim")
print(users)


## Problem 7: Safe Remove করো discard() ব্যবহার করে।
users = {"mamun", "rahim"}
users.discard("karim") # "karim" না থাকলেও কোড ক্র্যাশ করবে না
print(users)


## Problem 8: Set Empty করো।
users = {"Mamun", "Habib", "Rudro"}
users.clear()
print(users)


## Problem 9: Length বের করো।
users = {"mamun", "rahim", "karim"}
print(len(users))


## Problem 10: Loop ব্যবহার করে সব User Print করো।
users = {"mamun", "rahim", "karim"}
for user in users:
   print(user)


###############################################################################

##### Level 2: Set Operations (11-20)

## Problem 11: Union বের করো।
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))
print(A | B)


## Problem 12: Intersection বের করো।
A = {1, 2, 3}
B = {2, 3, 4}
print(A.intersection(B))
print(A & B)


## Problem 13: Difference বের করো।
A = {1, 2, 3}
B = {2, 3, 4}
print(A.difference(B))
print(B.difference(A))
print(A - B)


## Problem 14: Symmetric Difference বের করো।
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))


## Problem 15: Check করো A কি B-এর subset?
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))


## Problem 16: Check করো A কি B-এর superset?
A = {1, 2, 3, 4}
B = {1, 2}
print(A.issuperset(B))


##  Problem 17: Check করো Disjoint কিনা।
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))


## Problem 18, 19, 20: Operator ব্যবহার করে Union, Intersection & Difference।
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Problem 18 (Union) -> {1, 2, 3, 4, 5}
print(A & B)  # Problem 19 (Intersection) -> {3}
print(A - B)  # Problem 20 (Difference) -> {1, 2}


######################################################################################

##### Level 3: Backend Style Problems (21-30)

## Problem 21: API Response থেকে Unique User IDs বের করো।
users = [1, 2, 2, 3, 1, 2, 4, 5]
unique_ids = set(users)
print(unique_ids)


## Problem 22: Unique Countries বের করো।
countries = ["BD", "USA", "BD", "UK", "USA"]
unique_country = set(countries)
print(unique_country)


## Problem 23: Unique Categories বের করো।
products = [
   {"category": "Phone"},
   {"category": "Laptop"},
   {"category": "Phone"},
   {"category": "Tablet"}
]

unique_categories = {p["category"] for p in products}
print(unique_categories)


## Problem 24: Unique Emails Count করো।
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
print(len(set(emails)))


## Problem 25: দুই API Response-এর Common Users বের করো।
api1 = {"mamun", "rahim", "karim"}
api2 = {"karim", "rahim", "sakib"}

common_users = api1 & api2
print(common_users)


## Problem 26: API1-এ আছে কিন্তু API2-এ নেই।
api1 = {"mamun", "rahim", "karim"}
api2 = {"karim", "rahim"}
only_in_api1 = api1 - api2
print(only_in_api1)


## Problem 27: Permission Check
required = {"read", "write"}
user = {"read", "write", "delete"}
has_permission = required.issubset(user)
print(has_permission)


## Problem 28: Role Matching (Common Skill)
frontend = {"html", "css", "javascript"}
backend = {"python", "sql", "javascript"}
common_skill = frontend & backend
print(common_skill)


##Problem 29: Registered Users vs Active Users (Inactive Users)
registered = {1, 2, 3, 4, 5}
active = {2, 3}
inactive = registered - active
print(inactive)


## Problem 30: API থেকে Duplicate Product IDs Remove করো।
products = [101, 102, 103, 101, 102, 104]
unique_products = set(products)
print(unique_products)  # Output: {101, 102, 103, 104}


############################################################
## Bonus Backend Problems (31-35)
## Problem 31: Gmail Users বের করো এবং Unique রাখো।
emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "a@gmail.com"]
gmail_users = {email for email in emails if email.endswith("@gmail.com")}
print(gmail_users)

## Problem 32: Unique Tags বের করো (Nested List)।
posts = [
   {"python", "django"},
   {"python", "api"}, 
   {"django", "backend"}
]

unique_tags = set()
for tag_list in posts:
   unique_tags.update(tag_list)

print(unique_tags)


## Problem 33: সব Students-এর Unique Subjects বের করো।
students = [
   {"subjects": ["math", "English"]},
   {"subjects": ["math", "Physics"]}
]

unique_subjects = set()
for student in students:
   unique_subjects.update(student["subjects"])

print(unique_subjects)


## Problem 34: Duplicate Usernames Detect করো।
usernames = ["mamun", "rahim", "mamun", "karim", "rahim"]

seen = set()
duplicates = set()

for username in usernames:
   if username in seen:
      duplicates.add(username)
   else:
      seen.add(username)

print("Duplicates:", duplicates)


## Problem 35: সব API Response-এর Unique Keys বের করো।
responses = [
   {"id": 1, "name": "Mamun"},
   {"id": 2, "email": "a@gmail.com"},
   {"phone": "123"}
]
unique_keys = set()
for respon in responses:
   unique_keys.update(respon.keys())

print(unique_keys)