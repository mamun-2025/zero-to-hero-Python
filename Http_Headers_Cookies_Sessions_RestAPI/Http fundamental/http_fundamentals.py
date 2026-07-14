

##### 🌐 Part 1 — HTTP Fundamentals

# 1. Internet কীভাবে কাজ করে?
"""
Internet কী?

Internet হলো পৃথিবীর কোটি কোটি computer/device-এর একটি বিশাল network।

সহজ ভাষায়:
Your Computer
        |
        |
     Internet
        |
        |
   Server Computer

তুমি যখন browser-এ লিখো:

youtube.com

তখন:
তোমার Browser

↓

Internet

↓

YouTube Server

↓

Response ফিরে আসে



Example:
তুমি Google-এ search করলে:
তুমি:
"Python tutorial"

↓

Browser request পাঠায়

↓

Google Server search করে

↓

Result পাঠায়

↓

Browser দেখায়

"""



# 2. Client vs Server
"""
Backend বুঝতে হলে Client এবং Server বুঝতে হবে।

Client কী?
যে device/service request পাঠায় তাকে Client বলে।

Example:

Browser
Mobile App
Frontend Application

Example:
Chrome Browser

Request পাঠাচ্ছে

↓

Server


Server কী?
যে computer request গ্রহণ করে এবং response দেয় তাকে Server বলে।

Example:
Django Server
Database Server
API Server

Flow:
Client

"Give me products"

        ↓

Server

"Here are products"

        ↓

Client


Real E-commerce Example
তুমি Daraz App খুললে:

Client:
Mobile App

Request:
Give me products

Server:
Django Backend

Response:
[
 {
  "name":"Laptop",
  "price":50000
 }
]

"""


# 3. HTTP কী?
"""
HTTP এর পূর্ণরূপ:
HyperText Transfer Protocol

সহজ ভাষায়:
HTTP হলো Client এবং Server-এর মধ্যে communication rule।

মানে:
"কীভাবে request এবং response পাঠানো হবে"
তার নিয়ম।

Example:

Client:
GET /products

Server:
200 OK

[
Laptop,
Mobile
]

এই communication HTTP দিয়ে হয়।

HTTP ছাড়া কী সমস্যা?
ধরো তুমি server-এ message পাঠালে:
Give product

Server বুঝবে কীভাবে?

HTTP বলে দেয়:

GET = data চাই
POST = data পাঠাও
DELETE = data মুছে ফেলো

"""


# 4. HTTPS কী?
"""
HTTPS:
HTTP Secure
HTTP + Encryption

HTTP:
Client

username=password

        ↓

Internet

        ↓

Server

সমস্যা:
মাঝখানে কেউ data দেখতে পারে।

HTTPS:
Client

Encrypted Data

        ↓

Internet

        ↓

Server

Decrypt

Example:
Bank website:
https://bank.com

এখানে HTTPS ব্যবহার হয়।

HTTP vs HTTPS
| HTTP           | HTTPS         |
| -------------- | ------------- |
| Not encrypted  | Encrypted     |
| Less secure    | Secure        |
| Port 80        | Port 443      |
| Normal website | Banking/Login |

"""


# 5. URL Structure
"""
URL:

https://www.example.com/products?id=10

এখানে অংশগুলো:

1. Protocol
https://

Communication method।

2. Domain
example.com

Website address।

3. Path
/products

Server-এর কোন resource চাই।

4. Query Parameter
?id=10

Extra information।

Full Structure:
Protocol
   |
   |
https://example.com/products?id=10
          |
          |
        Domain

                  |
                  |
                Path

                         |
                         |
                    Query



Django Example

URL:

https://api.shop.com/products/10

Django:

path(
   "products/<id>",
   view
)
"""


# 6. Domain and DNS
"""
Domain কী?
IP address মনে রাখা কঠিন।

Example:

Server IP:
142.250.183.14

মানুষের জন্য কঠিন।

তাই:google.com ব্যবহার করি।

DNS কী?
DNS:
Domain Name System
এটি Domain কে IP address-এ convert করে।

Flow:
Browser

google.com

↓

DNS Server

↓

142.250.xxx.xxx

↓

Google Server


Real Example
তুমি লিখলে:

facebook.com

DNS খুঁজে বের করে:
Facebook Server IP

তারপর connect করে।

"""

# 7. Request and Response
"""
HTTP-এর মূল দুইটি অংশ:
Request
Response
Request

Client থেকে Server-এ যায়।
Example:

GET /products

Request contains:

Method
URL
Headers
Body

Example:
GET /users

Header:
Authorization: token123

Response
Server থেকে Client-এ আসে।

Example:
200 OK

Body:
{
"name":"Mamun"
}

Flow:
CLIENT

Request
   |
   |
   ↓

SERVER

Response
   |
   |
   ↓

CLIENT

"""


# 8. Stateless Protocol
"""
HTTP হলো Stateless।

মানে:
Server প্রতিটি request আলাদা হিসেবে দেখে।

Example:
First Request:

User login

username:
mamun

password:
12345

Server:
Login successful

Next Request:
GET /profile

Server চিনবে না যে আগে login করেছিল।
কারণ HTTP কিছু মনে রাখে না।

Solution:
আমরা ব্যবহার করি:

Cookies

Sessions

JWT Token

যাতে server user চিনতে পারে।


Real Django Example

Without session:
Request 1:
Login

Server:
OK

Request 2:
Profile

Server:
Who are you?


With session:
Login

↓

Create Session ID

↓

Cookie save

↓

Next request

↓

User identified

"""

# Backend Developer হিসেবে মনে রাখবে:
"""
Frontend
   |
   | HTTP Request
   ↓

Django Backend

   |
   | Database Query
   ↓

PostgreSQL

   |
   | HTTP Response
   ↓

Frontend

"""
