

# 1. Cookies কী?
"""
Definition:
Cookie হলো ছোট একটি data file যা Client (Browser) নিজের কাছে store করে।

সহজ ভাষায়:
Server Client-এর browser-এ কিছু তথ্য রেখে দেয়, পরে Client সেই তথ্য আবার পাঠায়।

Flow:
Client (Browser)

        |
        | Login Request
        ↓

Django Server

        |
        | Create Cookie
        ↓

Browser stores Cookie

পরের request:

Browser
Cookie সহ Request

        ↓

Server

Example:
তুমি একটি website-এ login করলে:

Server:
Set-Cookie:
sessionid=abc123

Browser save করে:
Cookie:
sessionid=abc123

"""

# 2. Cookie কেন দরকার?
"""
HTTP হলো Stateless:

Request 1
Login

↓

Request 2
Profile

Server জানে না:
"এই user কে?"

Cookie সাহায্য করে:
Login

↓

Cookie তৈরি

↓

Next Request

↓

Server User চিনে

"""

# 3. Cookie Example
"""
HTTP Response:

HTTP/1.1 200 OK

Set-Cookie:
user_id=10

Browser:
Cookie Storage
user_id=10


Next Request:
GET /profile

Cookie:
user_id=10

"""

# 4. Cookie-এর Types
"""
1. Session Cookie
Browser বন্ধ করলে delete হয়।

Example:
Temporary login

2. Persistent Cookie
নির্দিষ্ট সময় থাকে।

Example:
Remember Me

3. Secure Cookie
শুধু HTTPS-এ যায়।
Secure=True

4. HttpOnly Cookie ⭐
JavaScript access করতে পারে না।
Security বাড়ায়।

Example:
HttpOnly=True

"""

# 5. Django Cookie Example
"""
Set Cookie:
from django.http import HttpResponse

def set_cookie(request):

   response = HttpResponse(
      "Cookie Set"
   )

   response.set_cookie(
      "username",
      "Mamun"
   )

   return response

Read Cookie:
username = request.COOKIES.get(
   "username"
)
"""

# 6. Sessions কী?
"""

Session হলো Server-side storage যেখানে user-এর information রাখা হয়।
Cookie শুধু ID রাখে।

Architecture:
Browser

Cookie:
session_id=abc123


        ↓


Django Server

Session Database:

abc123:
{
 user_id:10
}

Cookie vs Session
| Cookie            | Session          |
| ----------------- | ---------------- |
| Client side       | Server side      |
| ছোট data          | বেশি data        |
| Less secure       | More secure      |
| Browser store করে | Server store করে |

"""

# 7. Django Session Flow ⭐
"""
Login:
User

username/password

        ↓

Django

Check Database

        ↓
Create Session

        ↓
Send session_id cookie

        ↓
Browser


Next request:
GET /profile


Cookie:
session_id=abc123


        ↓
Django Session Table


        ↓
User Found

"""

# 8. Django Session Example
"""
Set:
request.session["user_id"] = 10

Get:
user_id = request.session.get(
    "user_id"
)

Delete:
request.session.flush()

"""

# 9. Authentication কী?
"""
Authentication মানে:
User কে verify করা।

Question:
তুমি কে?

Example:
Login:

Email:
mamun@gmail.com

Password:
12345

Server:
Database check

↓

User valid

↓

Authentication Success

Authentication Methods:
Session Authentication
Token Authentication
JWT Authentication
OAuth

"""

# 10. Authorization কী?
"""
Authorization মানে:
User কী করতে পারবে সেটা নির্ধারণ করা।

Question:
তোমার permission কী?

Example:
Authentication:
User is Mamun

Authorization:
Can Mamun delete products?

Yes/No

Difference:
Authentication	         Authorization
Who are you?	         What can you do?
Login	                  Permission
Identity	               Access

Example:
Admin:
Create Product
Delete Product
Update Product

Normal User:
View Product
Buy Product

"""

# 11. JWT কী?
"""
JWT:
JSON Web Token
এটি একটি token-based authentication system।

Traditional Session:
Server remembers user

JWT:
Client keeps token
Server verifies token

JWT Structure:

একটি JWT:
xxxxx.yyyyy.zzzzz

৩টি অংশ:
Header.Payload.Signature

"""

# 12. JWT Flow ⭐
"""
Step 1: Login

Client:
POST /login

Body:
{
"email":"mamun@gmail.com",
"password":"12345"
}

Server:
Check user:
Valid User

Generate JWT:
eyJhbGciOiJIUzI...

Response:
{
"access":"token123"
}


Step 2: Client stores token

Example:
Local Storage
access_token=token123


Step 3: Next Request

Client:
GET /profile


Authorization:
Bearer token123

Server:
Decode Token

↓

Find User

↓

Allow Request

"""

# 13. JWT Example in Django REST Framework
"""
Install:
pip install djangorestframework-simplejwt

settings.py:
REST_FRAMEWORK = {

"DEFAULT_AUTHENTICATION_CLASSES":[

"rest_framework_simplejwt.authentication.JWTAuthentication"

]
}

Login API:

POST
/api/token/

Response:
{
"access":"xxxxx",
"refresh":"yyyyy"
}

"""


# 14. Access Token vs Refresh Token
"""
Access Token
Short time:

Example:
5 minutes
API access-এর জন্য।

Refresh Token
Long time:

Example:
7 days
নতুন access token তৈরি করে।

Flow:
Refresh Token

        ↓

New Access Token

        ↓

API Request

"""


# 15. CSRF কী?
"""
CSRF:
Cross-Site Request Forgery
এটি একটি security attack যেখানে অন্য website user-এর permission ব্যবহার করে unwanted request পাঠানোর চেষ্টা করে।

Example:

User:
Bank.com এ Login

তারপর:
Malicious Website

একটি hidden request পাঠানোর চেষ্টা করে।

Problem:
Browser automatically cookie পাঠায়।

Solution:
CSRF Token।

"""


# 16. Django CSRF Protection
"""

Django Form:

<form method="POST">
{% csrf_token %}
<input name="username">
</form>

Django:
Request-এর সাথে token মিলিয়ে দেখে।

Valid হলে:
Allow

না হলে:
403 Forbidden

JWT vs Session Authentication
| Session               | JWT                 |
| --------------------- | ------------------- |
| Server stores session | Client stores token |
| Cookie based          | Header based        |
| Traditional web       | Modern API          |
| Django default        | Mobile/API friendly |


Real Backend Example
E-commerce Login:
User

POST /login


        ↓


Django


        ↓


Check User


        ↓


Generate JWT


        ↓


Return Token


        ↓


Mobile App


        ↓


GET /orders


Authorization:
Bearer token


        ↓


Django verifies


        ↓


Return Orders




Backend Developer Flow:
User Login

↓

Authentication

↓

JWT / Session Created

↓

Request with Identity

↓

Authorization Check

↓

Access Resource
"""