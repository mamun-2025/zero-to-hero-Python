

# 1. HTTP Response কী?
"""
যখন Client Server-এ request পাঠায়, Server তার উত্তর দেয়।
এই উত্তরকে বলে HTTP Response।

Flow:
Client

HTTP Request
      |
      |
      ↓

Django Server

HTTP Response
      |
      |
      ↓

Client


Example:

Client:
GET /products

Server Response:
HTTP/1.1 200 OK

[
 {
  "name":"Laptop",
  "price":50000
 }
]


একটি HTTP Response-এর অংশ:

HTTP Response
|
|-- Status Code
|
|-- Headers
|
|-- Body

Example:

HTTP/1.1 200 OK
Content-Type: application/json
{
"name":"Laptop"
}


"""


# 2. HTTP Status Code কী?
"""
Status Code হলো 3 digit number যা বলে:

Request সফল হয়েছে কিনা অথবা সমস্যা কোথায়।

Example:

200 OK
404 Not Found
500 Server Error

Status Code Category:
| Range   | Meaning      |
| ------- | ------------ |
| 100-199 | Information  |
| 200-299 | Success      |
| 300-399 | Redirection  |
| 400-499 | Client Error |
| 500-599 | Server Error |


Part 1: 1xx Informational
এগুলো শুধু information দেয়।
সাধারণ API development-এ কম দেখা যায়।

100 Continue
Meaning:
Client request পাঠানো চালিয়ে যেতে পারে।

Example:
Large file upload:

Client:
Can I upload?

Server:
100 Continue


101 Switching Protocols
Protocol change হচ্ছে।

Example:
HTTP থেকে WebSocket।




Part 2: 2xx Success Codes ⭐
সবচেয়ে বেশি ব্যবহার হয়।

1. 200 OK
সবচেয়ে common।

Meaning:
Request সফল হয়েছে।

Example:
GET /products

Response:
200 OK

Body:
[
{
"name":"Laptop"
}
]

Django:
return Response(
    data,
    status=200
)
201 Created ⭐

নতুন resource তৈরি হয়েছে।

Example:
User Registration:

Request:
POST /users

Response:
201 Created

Body:
{
"id":1,
"name":"Mamun"
}


Django REST Framework:
return Response(
    serializer.data,
    status=201
)




2. 202 Accepted
Request গ্রহণ করা হয়েছে কিন্তু এখনো complete হয়নি।

Example:
Large video processing:

Upload Video

↓

202 Accepted

↓

Processing

Real Backend:
Celery background job:
User uploads file

↓

Task Queue

↓

Processing



3. 204 No Content
Request সফল কিন্তু কোনো body নেই।

Example:
DELETE:
DELETE /users/10

Response:
204 No Content



Part 3: 3xx Redirection
Client-কে অন্য জায়গায় পাঠায়।

4. 301 Moved Permanently
Resource permanently অন্য URL-এ গেছে।

Example:
Old:
example.com

New:
newexample.com



5. 302 Found
Temporary redirect।
Example:
Login না করলে:

/profile

↓

/login




6. 304 Not Modified
Browser cache ব্যবহার করতে বলে।
Example:
Browser আগে image download করেছে।

পরের বার:
304
Use cached version




Part 4: 4xx Client Error ⭐
Client-এর request-এ সমস্যা।

7. 400 Bad Request
Request format ভুল।
Example:

API:
{
"name":123
}


কিন্তু দরকার:
{
"name":"Mamun"
}

Response:
400 Bad Request

Django:
return Response(
{
"error":"Invalid data"
},
status=400
)



8. 401 Unauthorized ⭐
Authentication নেই।

Example:
API:
GET /profile
কিন্তু token নেই।

Response:
401 Unauthorized

Example:
User

↓

Login required

↓

Token নেই

↓

401



9. 403 Forbidden ⭐

User authenticated কিন্তু permission নেই।
Difference:

401:
"তুমি কে?"

403:
"তুমি কে জানি, কিন্তু তোমার permission নেই।"

Example:
Admin API:
Normal User

↓

DELETE /users

↓

403 Forbidden

Django:
permission_classes=[
IsAdminUser
]
404 



10. Not Found ⭐
Resource পাওয়া যায়নি।
Example:
Request:

GET /products/999

কিন্তু product নেই।

Response:
404 Not Found

Django:
get_object_or_404(
Product,
id=999
)



11. 405 Method Not Allowed
Method ভুল।
Example:
API:

/products
শুধু GET allow।

কেউ:
DELETE /products
পাঠালো।

Response:
405




12. 429 Too Many Requests
অনেক বেশি request।

Example:
Brute force attack:

1000 login requests

Response:
429




Part 5: 5xx Server Error ⭐
Server-এর সমস্যা।

13. 500 Internal Server Error
সবচেয়ে common server error।
Example:

Django code:
x = 10 / 0

Error:
ZeroDivisionError

Response:
500 Internal Server Error



14. 502 Bad Gateway
Server অন্য server থেকে ভুল response পেয়েছে।

Example:
Nginx

↓

Gunicorn

↓

Django

Django down হলে:
502



15. 503 Service Unavailable
Server বর্তমানে available না।

Example:
Maintenance:

Website under maintenance




16. 504 Gateway Timeout
Server সময়ের মধ্যে response দেয়নি।

Example:
Nginx
waits
Django slow
timeout


Important Status Code Cheat Sheet ⭐
| Code | Meaning            | Use                  |
| ---- | ------------------ | -------------------- |
| 200  | OK                 | Data fetch           |
| 201  | Created            | Create object        |
| 204  | No Content         | Delete success       |
| 301  | Permanent Redirect | URL change           |
| 302  | Temporary Redirect | Login redirect       |
| 400  | Bad Request        | Invalid input        |
| 401  | Unauthorized       | No login             |
| 403  | Forbidden          | No permission        |
| 404  | Not Found          | Resource missing     |
| 405  | Method Not Allowed | Wrong method         |
| 429  | Too Many Requests  | Rate limit           |
| 500  | Server Error       | Bug                  |
| 502  | Bad Gateway        | Server communication |
| 503  | Unavailable        | Maintenance          |
| 504  | Timeout            | Slow server          |



Django REST Framework Example:

Create User
Request:
POST /api/users/

Success:
201 Created

 

Get User
GET /api/users/1

Success:
200 OK



Wrong ID
GET /api/users/999

Response:
404 Not Found



No Token
GET /api/profile

Response:
401 Unauthorized



No Permission
DELETE /api/users/1

Response:
403 Forbidden

"""