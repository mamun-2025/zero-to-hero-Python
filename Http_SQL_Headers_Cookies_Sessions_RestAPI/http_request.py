

# 1. HTTP Request কী?
"""
যখন Client Server-এর কাছে কোনো কাজের জন্য request পাঠায়, সেটাকে HTTP Request বলে।

Example:
তুমি একটি E-commerce App খুললে:

Mobile App (Client)

        |
        |
        | HTTP Request
        |
        ↓

Django Server

Client বলছে:
"আমাকে products দাও"

একটি HTTP Request-এর অংশ:
HTTP Request

|
|-- Method
|
|-- URL
|
|-- Headers
|
|-- Body

Example:
GET /products HTTP/1.1

Host: shop.com

Authorization: Token xyz

"""


# 2. HTTP Methods কী?
"""
HTTP Method বলে দেয়:
Client Server-কে কী করতে বলছে।

যেমন:
| Method | কাজ              |
| ------ | ---------------- |
| GET    | Data নেওয়া       |
| POST   | Data তৈরি করা    |
| PUT    | পুরো Data Update |
| PATCH  | আংশিক Update     |
| DELETE | Data Delete      |

একটি CRUD System:
Create  → POST
Read    → GET
Update  → PUT/PATCH
Delete  → DELETE

"""


# 3. GET Method
"""
Server থেকে data নেওয়ার জন্য।

Example:
তুমি products দেখতে চাও:

GET /products

Server Response:

[
 {
  "id":1,
  "name":"Laptop",
  "price":50000
 }
]


GET Example
Browser:

https://shop.com/products

এটা আসলে:

GET /products
Django Example

urls.py:
path(
   "products/",
    product_list
)


views.py
def product_list(request):
   products = Product.objects.all()
   return JsonResponse(
      products,
      sage=False
   )

GET-এর বৈশিষ্ট্য:
✅ Data read করে
✅ Body সাধারণত থাকে না
✅ Safe method
✅ Idempotent method

"""


# 4. POST Method
"""
নতুন data তৈরি করা।

Example:
User Registration:
POST /users

Body:
JSON:
{
"name": "Mamun",
"email": "mamun@gmail.com",
"password": "12345
}

Server:
Json:
{
"message": "User Created"
}


Django REST Framework Example

Request:
JSON:
POST /api/users/

{
"username":"mamun",
"password":"12345"
}

Serializers:
serializer.save()

Database:
User Created

POST কোথায় ব্যবহার হয়?
Registration
Login
Order Create
Payment
Upload


Example:
Order:
POST /orders

Body:
JSON:
{
"product_id": 10,
"quantity": 2
}

POST বৈশিষ্ট্য:

❌ Safe নয়
❌ Idempotent নয়

কারণ:
একই request দুইবার পাঠালে দুইটি object তৈরি হতে পারে।

Example:

প্রথম:

POST /orders
Order ID 1

দ্বিতীয়:

POST /orders
Order ID 2

"""


# 5. PUT Method
"""
পুরো resource update করা।
ধরো User:

Before:
{
"name":"Mamun",
"email":"old@gmail.com",
"age":25
}

PUT Request:
PUT /users/1

Body:
{
"name":"Mamun",
"email":"new@gmail.com",
"age":26
}

After:
{
"name":"Mamun",
"email":"new@gmail.com",
"age":26
}

PUT মানে:
পুরো object replace করা।


Django Example:
def update_user(request, id):
   user = User.objects.get(id=id)

   user.name = request.data["name"]
   user.email = request.data["email"]
   user.age = request.data["age"]

   user.save()

"""


# 6. PATCTH Method
"""
Partial update।
মানে শুধু যে field change করতে চাই সেটাই পাঠানো।

Before:
{
"name": "Mamun",
"email": "old@gmail.com",
"age": 25
}

PATCH:
PATCH /users/1

Body:
{
"email": "new@gmail.com"
}

After:
{
"name": "Mamun",
"email": "new@gmail.com",
"age": 25
}


PUT vs PATCH
| PUT           | PATCH                |
| ------------- | -------------------- |
| Full update   | Partial update       |
| সব field লাগে | শুধু পরিবর্তিত field |
| Replace করে   | Modify করে           |


Real Example:
Profile update:

User শুধু নাম পরিবর্তন করলো:
{
"name":"Rahim"
}

এখানে PATCH ভালো।

"""


# 7. DELETE Method
"""
Resource delete করা।

Example:
DELETE /products/10

Server:
{
"message":"Product deleted"
}

Django:

def delete_product(request,id):

    product = Product.objects.get(id=id)

    product.delete()

    return Response(
        {
        "message":"Deleted"
        }
    )

ব্যবহার:
Delete account
Remove product
Cancel order

"""


# 8. Safe Methods
"""
Safe Method মানে:
Server-এর data পরিবর্তন করে না।

Safe methods:

GET
HEAD
OPTIONS

Example:
GET:
GET /products

শুধু দেখে।


Database:

Before:
Products = 100

After:
Products = 100

POST safe নয়:

POST /products

Database:

Before:
Products =100

After:
Products=101

"""


# 9. Idempotent Methods
"""
Idempotent মানে:
একই request বারবার পাঠালেও final result একই থাকবে।

Idempotent Methods:

✅ GET
✅ PUT
✅ DELETE

Example GET:

Request:
GET /products/1
১০ বার পাঠাও:

Result:
একই product।

Example PUT:

Request:
PUT /user/1

{
"name":"Mamun"
}

প্রথমবার:
Name = Mamun

দ্বিতীয়বার:
Name = Mamun

Result একই।

Example DELETE:

প্রথম:
DELETE /product/1

Product deleted.

দ্বিতীয়:
DELETE /product/1

Already deleted.

Final state:

Product নেই
একই।

POST কেন Idempotent নয়?

Example:

POST /orders
দুইবার পাঠালে:

Order 1 created
Order 2 created

Final state পরিবর্তন হয়।

Real E-commerce CRUD Example
Product System

Create:
POST /products
{
"name":"Laptop",
"price":50000
}

Read:
GET /products

Update:
Full:
PUT /products/1

Partial:
PATCH /products/1

Delete:
DELETE /products/1



Django REST Framework Mapping
| HTTP   | DRF                |
| ------ | ------------------ |
| GET    | list(), retrieve() |
| POST   | create()           |
| PUT    | update()           |
| PATCH  | partial_update()   |
| DELETE | destroy()          |

"""