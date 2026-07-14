

# 1. REST কী?
"""
REST:
Representational State Transfer
এটি একটি software architecture style যা Client এবং Server-এর মধ্যে communication design করার নিয়ম দেয়।

সহজ ভাষায়:
REST বলে API কীভাবে design করলে clean, scalable এবং understandable হবে।

Example:
একটি E-commerce system:

Resources:
User
Product
Order
Payment

REST অনুযায়ী:
Resource-এর জন্য URL থাকবে।

Example:
/products
/users
/orders


REST-এর মূল Principles
1. Client-Server Separation
Frontend এবং Backend আলাদা থাকবে।

Frontend
React / Mobile App

        |

        HTTP

        |

Backend

Django API


2. Stateless
প্রতিটি request নিজে complete information বহন করবে।

Example:

JWT:
GET /orders

Authorization:
Bearer token123

Server token দেখে user চিনবে।


3. Resource Based URL
REST এ action নয়, resource ব্যবহার করা হয়।

❌ Bad:
/getAllProducts
/createProduct
/deleteProduct

✅ Good:
GET /products
POST /products
DELETE /products/10

"""

# 2. REST API কী?
"""
REST API হলো এমন API যা REST principles follow করে।

Example:

Frontend:
Mobile App

Request:
GET /api/products

Django:
Find products

↓

Database

Response:
[
 {
  "id":1,
  "name":"Laptop"
 }
]

"""


# 3. REST API URL Design ⭐
"""
ধরো একটি Blog System:

Resource:

Posts
Get all posts

Request:
GET /api/posts

Response:
[
 {
 "id":1,
 "title":"Django"
 }
]


Get single post
GET /api/posts/1


Create post
POST /api/posts
Body:

{
"title":"REST API",
"content":"Learning"
}


Update post
Full update:
PUT /api/posts/1



Partial update:
PATCH /api/posts/1


Delete post
DELETE /api/posts/1

"""


# 4. CRUD কী?
"""
CRUD হলো Database-এর চারটি basic operation।

C = Create
R = Read
U = Update
D = Delete

REST Mapping:
| CRUD   | HTTP Method |
| ------ | ----------- |
| Create | POST        |
| Read   | GET         |
| Update | PUT/PATCH   |
| Delete | DELETE      |


Example:
Product System:

Create
POST /products

Read
GET /products

Update
PATCH /products/5

Delete
DELETE /products/5

"""


# 5. HTTP in Django
"""
Django নিজে HTTP Request handle করে।

Flow:
Browser

HTTP Request

        ↓

Django URL Router

        ↓

View Function

        ↓

Database

        ↓

HTTP Response

        ↓

Browser


Django Request Object

Example:
def product_view(request):

    print(request.method)


Output:
GET

Request Data:
request.GET


Query Parameter:
Example:
/products?category=mobile


Django:
category = request.GET.get(
    "category"
)

POST Body:
request.POST

Headers:
request.headers

"""


# 6. Django Response
# Django Response
from django.http import HttpResponse

def home(request):

   return HttpResponse(
      "Hello Backend"
   )


# JSON Response:
from django.http import JsonResponse

def user(request):

   data = {
      "name": "Mamun",
      "skill": "Django"
   }

   return JsonResponse(data)


# Response:
{
"name":"Mamun",
"skill":"Django"
}


# 7. HTTP Methods in Django View
from django.http import JsonResponse

def user_view(request):

   if request.method == "GET":

      return JsonResponse(
         "message": "Get User"
      )
   
   elif request.method == "POST":

      return JsonResponse(
         "message": "Create User"
      )
   

# 8. HTTP in Django REST Framework (DRF)
"""
DRF Django-কে API framework বানায়।

Install:
pip install djangorestframework

Architecture:
Client

JSON Request

↓

DRF Serializer

↓

Django Model

↓

Database

↓

JSON Response

"""


# 9. DRF Serializer
"""
Serializer:
Python Object ↔ JSON convert করে।

Example:
Model:

class Product(models.Model):

    name = models.CharField(
        max_length=100
    )

    price = models.IntegerField()



Serializer:
from rest_framework import serializers

class ProductSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Product

        fields = "__all__"

"""


# 10. DRF APIView Example
# GET + POST
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductAPI(APIView):

   def get(self, request):
      return Response(
         {
            "message":
            "All products"
         }
      )
   
   def post(self, request):
      data = request.data 

      return Response(
         data
      )
"""
GET:
GET /api/products

Response:
{
"message":"All products"
}

POST:
POST /api/products

Body:
{
"name":"Laptop"
}

"""


# 11. Real Backend Example: E-commerce Order API ⭐
"""
Create Order
Request:
POST /api/orders

Body:
{
"product_id":10,
"quantity":2
}

Django:
class OrderAPI(APIView):


    def post(self,request):

        product_id = request.data[
            "product_id"
        ]

        quantity = request.data[
            "quantity"
        ]


        order = Order.objects.create(
            product_id=product_id,
            quantity=quantity
        )


        return Response(
            {
            "message":
            "Order Created"
            },
            status=201
        )

        
Response:
{
"message":"Order Created"
}    

"""


# 12. Complete Backend Flow
"""
একটি real request:

User:
Mobile App

Request:
POST /api/orders

Authorization:
Bearer token

{
product_id:10
}

Django:
Step 1:
URL Routing

Step 2:
JWT Authentication

Step 3:
Permission Check

Step 4:
Serializer Validation

Step 5:
Database Save

Step 6:
JSON Response

"""

# Backend Engineer Complete Flow
"""
Client
(Mobile/Web)

        |
        |
     HTTP Request

        |
        ↓

Django REST Framework

        |
        |
 Authentication
 Authorization
 Serializer

        |
        ↓

Django ORM

        |
        ↓

PostgreSQL

        |
        ↓

HTTP Response(JSON)

        |
        ↓

Client

"""