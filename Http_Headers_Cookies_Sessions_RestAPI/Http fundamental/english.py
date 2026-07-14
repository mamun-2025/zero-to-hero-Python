

# 🌐 HTTP Fundamentals Vocabulary 
# (English → Bangla Meaning)
"""
| Vocabulary      | Bangla Meaning               | Example                     |
| --------------- | ---------------------------- | --------------------------- |
| Internet        | ইন্টারনেট, সংযুক্ত নেটওয়ার্ক | Internet connects computers |
| Network         | নেটওয়ার্ক                    | A computer network          |
| Device          | ডিভাইস / যন্ত্র              | Mobile device               |
| Client          | অনুরোধকারী পক্ষ              | Browser is a client         |
| Server          | সেবা প্রদানকারী কম্পিউটার    | Django server               |
| Request         | অনুরোধ                       | Send a request              |
| Response        | উত্তর / ফলাফল                | Server response             |
| Communication   | যোগাযোগ                      | Client-server communication |
| Protocol        | নিয়ম / পদ্ধতি                | HTTP protocol               |
| Transfer        | স্থানান্তর                   | Data transfer               |
| Secure          | নিরাপদ                       | HTTPS is secure             |
| Encryption      | ডাটা গোপন করার প্রক্রিয়া     | HTTPS encryption            |
| Domain          | ওয়েব ঠিকানা                  | google.com                  |
| Address         | ঠিকানা                       | IP address                  |
| Resource        | রিসোর্স / তথ্য               | Product resource            |
| Path            | পথ / URL-এর অংশ              | /products                   |
| Query Parameter | অতিরিক্ত তথ্য                | ?id=10                      |
| Resolve         | খুঁজে বের করা / রূপান্তর করা | DNS resolves domain         |
| Authentication  | পরিচয় যাচাই                  | User authentication         |
| Session         | সেশন / ব্যবহারকারীর অবস্থা   | Django session              |
| Cookie          | ছোট তথ্য সংরক্ষণ             | Browser cookie              |
| Token           | পরিচয়পত্রের মতো তথ্য         | JWT token                   |
| Stateless       | কিছু মনে না রাখা             | HTTP is stateless           |
| Request Method  | অনুরোধের ধরন                 | GET, POST                   |
| Header          | অতিরিক্ত তথ্য                | HTTP headers                |
| Body            | মূল ডাটা                     | JSON body                   |

"""


# 🌐 HTTP Fundamentals — 10 Questions & Answers
"""
1. What is the Internet?
= The Internet is a global network that connects millions of computers and devices around the world.


2. What is a Client?
= A client is a device or application that sends requests to a server.
  Example:
  - Browser
  - Mobile App
  - Frontend Application

  
3. What is a Server?
= A server is a computer that receives requests and sends responses.
  Example:
  - Django Server
  - Database Server
  - API Server

  
4. What is HTTP?
= HTTP stands for Hyper Text Transfer Protocol.
  It is a communication protocol between client and server.

  
5. What is HTTPS?
= HTTPS is a secure version sof HTTP.
  It encypts data between client and server.

  
6. What is a URL?
= A URL is the address of a resource on the Internet.
  Example:
  https://example.com/prodcuts?id=10
  It contains:
  - Protocol
  - Domain
  - Path
  - Query Parameter

  
7. What is DNS?
= DNS stands for Domain Name System.
  It converts domain names into IP addresses.
  Example:
  google.com ➡️ 142.xxx.xxx.xxx
      

8. What is an HTTP Request?
= An HTTP request is a message sent from to server asking for data or action.
  Example:
  GET /products

  
9. What is an HTTP Response?
= An HTTP response is the data sent from server back to client.
  Example:
  200 OK
  {
   "name": "Laptop:
  }

  
10. Why is HTTP called Stateless?
= HTTP is called stateless because the server dose not remember previous requests.
  To remember users, we use:
  - Cookies
  - Sessions
  - JWT Token

"""


# 🎤 2–3 Minutes Speaking Practice
"""
TOPIC:
"How HTTP Works"
____________________
Hello, today I will talk about how HTTP works.
The Internet is a global network that connects many computers and devices.
In Web applications, we mainly have two important parts: client and server.

The client sends a request to the server. For example, when a user opens an 
e-commerce website and wants to see products, the browser sens an HTTP
request to the backend server.

HTTP stands for HyperText Transfer Protocol. It defines how data should be transferred between client and server.

The server recieves the request, processes the information, communicates with 
the database, and sends a response back to the client.

HTTPS is the secure version of HTTP. It uses encryption to protect sensitive
information like passwords and payment data.

A URL contains different parts like protocol, domain, path and query parameters.

DNS helps us by converting domain names into IP addresses because rememberrin
IP addresses is difficult.

HTTP is a stateless protocol, which means the server does not remember 
previous requests. To solve this problem, we use sessions, cookies, and JWT tokens.

As a backend develper, understanding HTTP is very impotant because APIs. 
Django applications, and frontend-backend communication depend on HTTP.

Thank you.



"""