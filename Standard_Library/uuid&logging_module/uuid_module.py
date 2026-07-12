

### 1. UUID কী?
"""
UUID এর পূর্ণরূপ:
Universally Unique Identifier

সহজ ভাষায়:
UUID হলো এমন একটি unique ID যা পৃথিবীর অনেক system-এর মধ্যে conflict হওয়ার সম্ভাবনা প্রায় নেই।

Example:
550e8400-e29b-41d4-a716-446655440000

এটা একটি UUID।

কেন UUID দরকার?
ধরো একটি E-commerce website।

Database:

Products

id | name
--------------
1  | Laptop
2  | Mobile

এখানে integer ID ব্যবহার হচ্ছে।
সমস্যা:

যদি তুমি API expose করো:

api/products/1
api/products/2

তাহলে সবাই সহজে বুঝতে পারে কয়টি product আছে।
Security issue হতে পারে।

UUID:
api/products/550e8400-e29b-41d4-a716-446655440000

এটা guess করা কঠিন।

"""
import uuid




### 2. 3. uuid1()
# UUID তৈরি করার একটি method।
import uuid

id = uuid.uuid1()
print(id)

# UUID1 তৈরি হয়:
# Time
# Machine information
# এর উপর ভিত্তি করে।
# UUID1 কিছু information expose করতে পারে।
# তাই সাধারণ application-এ UUID4 বেশি ব্যবহার হয়।



### 4. uuid4() ⭐ (Most Used)
# UUID4 random UUID তৈরি করে।
# এটা সম্পূর্ণ random।
import uuid

id = uuid.uuid4()

print("Random_id:", id)

order_id = uuid.uuid4()
print("Order_id:", order_id)




### 5. UUID String এ Convert করা
import uuid

user_id = uuid.uuid4()

print(str(user_id))



### 6. UUID দিয়ে File Name তৈরি

# ধরো user image upload করলো:
# আগে:
# profile.jpg

# সমস্যা:
# দুই user একই নামের file upload করতে পারে।

import uuid

filename = f"{uuid.uuid4()}.jpg"

print(filename)




### 7. Django UUID Field
"""
import uuid
from django.db import models

class Product(models.Model):

   id = models.UUIDField(
      primary_key=True,
      default=uuid.uuid4,
      editable=False
   )

name = models.CharField(
   max_length=100
)

# database
id                                   name
------------------------------------------------
a83f...                              Laptop
b92d...                              Mobile



UUID Use Cases
Backend:
✅ User ID
✅ Order ID
✅ Payment ID
✅ API Request ID
✅ File Upload Name
✅ Distributed System Identifier

"""

## Problem 1: unique order ID return করবে।
import uuid

def generate_order_id():

   order_id = uuid.uuid4()

   return str(order_id)


print("Generate_Order_Id:", generate_order_id())


# অনেক সময় prefix যোগ করা হয়:
import uuid

def generate_order_id():

    unique_id = uuid.uuid4().hex[:5]

    return f"ORD-{unique_id}"

print(generate_order_id())


# Problem 2 : ১০টি Unique User ID তৈরি করো
import uuid

user_ids = []

for i in range(10):
    
    user_id = uuid.uuid4().hex[:5]

    user_ids.append(str(user_id))


for uid in user_ids:
    print(uid)


# আরো Backend Style: User object-এর সাথে:
import uuid

users = []

for i in range(10):
   
   user = {
       "id": str(uuid.uuid4().hex[:3]),
       "username": f"user_{i}"
   }

   users.append(user)


for user in users:
    print(user)

