

# 1. HTTP Headers কী?
"""
HTTP Header হলো additional information যা Client এবং Server একে অপরকে পাঠায়।

সহজ ভাষায়:
Header বলে দেয় request/response সম্পর্কে extra তথ্য।

HTTP Structure:

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
Authorization: Bearer token123
Content-Type: application/json

এখানে:
Host
Authorization
Content-Type

এগুলো Header।

"""

# 2. Request Headers
"""
2. Request Headers

Request Header Client → Server যায়।
মানে Client Server-কে extra information দেয়।

Example:

GET /profile

Authorization: Bearer abc123

Accept: application/json

Common Request Headers:
| Header        | কাজ                   |
| ------------- | --------------------- |
| Authorization | User identity/token   |
| Content-Type  | Data type             |
| Accept        | কী ধরনের response চাই |
| User-Agent    | Client information    |
| Cookie        | User session data     |

"""

# 3. Authorization Header ⭐
"""
Authentication-এর জন্য ব্যবহার হয়।

Example:
GET /profile


Authorization:
Bearer eyJhbGciOiJIUzI1

Flow:
User Login

↓

Server creates token

↓

Client saves token

↓

Every request:

Authorization Header

↓

Server verifies

Django REST Framework:
request.headers.get(
    "Authorization"
)

"""

# 4. Content-Type Header
"""
Request body-এর data type বলে।

Example:
JSON পাঠালে:

Content-Type:
application/json

Form data:
Content-Type:
multipart/form-data

Example:
User Create:

POST /users

Content-Type: application/json


{
"name":"Mamun"
}

"""


# 5. Accept Header
"""
Client কী ধরনের response চায় সেটা বলে।

Example:

Accept:
application/json

মানে:

"আমাকে JSON format-এ response দাও"

"""


# 6. Response Headers
"""
Server → Client পাঠায়।

Example:
HTTP/1.1 200 OK

Content-Type: application/json

Cache-Control: max-age=3600

Common Response Headers:
| Header        | কাজ                |
| ------------- | ------------------ |
| Content-Type  | Response type      |
| Set-Cookie    | Cookie তৈরি        |
| Cache-Control | Cache rules        |
| Server        | Server information |


"""

# 7. Query Parameters
"""
URL-এর শেষে ? এর পরে যে data পাঠানো হয়।

Example:
GET /products?category=mobile

এখানে:
category=mobile
Query Parameter।

Multiple Query:
GET /products?category=mobile&price=20000

Structure:
/products

?

category=mobile

&

price=20000


Backend Example
E-commerce:

User search:

GET /products?search=laptop

Response:
[
{
"name":"Gaming Laptop"
}
]

Django:
def products(request):

    search = request.GET.get(
        "search"
    )

"""


# 8. Path Parameters
"""
URL-এর অংশ হিসেবে data পাঠানো হয়।

Example:
GET /products/10

এখানে:
10
হলো Path Parameter।


Query vs Path:

Query Parameter:
/products?id=10

মানে:
Filter/Search

Path Parameter:
/products/10

মানে:
Specific resource

Example:
User:

GET /users/5

মানে:
User যার ID = 5

Django:
path(
"users/<int:id>",
user_detail
)

"""

# 9. Request Body
"""
Client যখন Server-এ data পাঠায়, সেই data Body-তে থাকে।

সাধারণত:
POST
PUT
PATCH
এ ব্যবহার হয়।

Example:
User Registration:

POST /users

{
"name":"Mamun",
"email":"mamun@gmail.com",
"password":"12345"
}

এই JSON অংশটি Body।

GET সাধারণত:
No Body

"""

# 10. JSON কী?
"""
JSON:
JavaScript Object Notation
এটি data exchange format।

Frontend এবং Backend-এর মধ্যে data পাঠানোর সবচেয়ে common format।

Example:
{
"name":"Mamun",
"age":25,
"skill":"Python"
}


JSON Rules:
1. Key সবসময় double quote:

Correct:
{
"name":"Mamun"
}

Wrong:
{
'name':'Mamun'
}


2. Data Types:
JSON support করে:
String
Number
Boolean
Array
Object
Null

Example:
{
"name":"Mamun",
"age":25,
"active":true,
"skills":[
"Python",
"Django"
]
}

"""


# 11. JSON এবং Python Conversion
"""
Python Dictionary:

user = {

"name": "Mamun",
"age": 25

}

JSON:
import json

data = json.dumps(user)

print(data)

Output:
JSON:
{
"name": "Mamun",
"age": 25
}


JSON - Python:

json_string = '{
"name": "Mamun",
"age": 25
}'

data = json.loads(
      json_string
)

print(data)

"""


# 12. Real API Example
"""
User Registration API

Request:
POST /api/register

Headers:
Content-Type:
application/json


Body:
{
"username":"mamun",
"password":"12345"
}

Server:
Django:

username = request.data["username"]

password = request.data["password"]

Response:
201 Created

{
"id":1,
"username":"mamun"
}

"""


# 13. Complete HTTP Request Example
"""
POST /api/orders HTTP/1.1


Host: shop.com

Authorization: Bearer token123

Content-Type: application/json


{
"product_id":10,
"quantity":2
}


এখানে:

Method:
POST

Path:
/api/orders

Headers:
Authorization
Content-Type

Body:
{
"product_id":10,
"quantity":2
}

"""


# Django REST Framework Mapping
"""
Headers:
request.headers

Query Parameter:
request.query_params

Example:
request.query_params.get(
"search"
)

Path Parameter:
def get(self, request, id):
   
Body:
request.data

"""