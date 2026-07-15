

"""

# 1. Create Database:
CREATE DATABASE ecommerce;
CREATE DATABASE school;
CREATE DATABASE hospital;
CREATE DATABASE library;


_____________________________________
2. CREATE TABLE:
CREATE TABLE userS(
   id SERIAL PRIMARY KEY,
   
   name VARCHAR(100),
   
   email VARCHAR(100)
   
);

_____________________________________
3. INSERT(data add)
INSERT INTO users
(name, email)

VALUES
("Mamun", "mamun@gmail.com)
("Habib", "habib@gmail.com)
("Rudro", "rudro@gmail.com)

____________________________________
4. SELECT 
All data read:
SELECT * 
FROM users;

One column data read:
SELECT name
FROM users;

Multiple column data read:
SELECT name, email
FROM users;


____________________________________
5. WHERE(Data filter by condition)
SELECT *
FROM users
WHERE id=1;

SELECT *
FROM users
WHERE name="Mamun";

SELECT *
FROM products
WHERE price > 50000;

SELECT *
FROM users
WHERE age > 18 
AND city="Dhaka";

SELECT *
FROM users
WHERE city="Dhaka"
OR city="Madaripur";


___________________________________
6. ORDER BY (Data sort)
SELECT *
FROM users
ORDER BY name;

SELECT *
FROM products
ORDER BY price ASC;

SELECT *
FROM products
ORDER BY price DESC;


_______________________________________
7. LIMIT(Define Row)
SELECT *
FROM users
LIMIT 5;

TOP PRODUCT:
SELECT *
FROM products
ORDER BY price DESC
LIMIT 1;

LASTED ORDERS:
SELECT *
FROM orders
ORDER BY created_at DESC;
LIMIT 10;


___________________________________
8. DISTINCT(Duplicate value delete)
SELECT DISTINCT city
FROM users;

SELECT DISTINCT category
FROM products;


__________________________________________________________________________
Django ORM Mapping ⭐
SQL                              DJANGO ORM
SELECT *                         User.objects.all()
FROM users

WHERE id=1                       User.objects.get(id=1)

WHERE price > 50000              Product.objects.filter(price__gt=50000)

ORDER BY price                   Product.objects.order_by("price")

ORDER BY pirce DESC              Product.objects.order_by("-price")

LIMIT 5                          User.objects.all()[:5]

DISTINCT                         User.objects.values("city").distinct()


____________________________________________________________________________
Complete Backend Flow

ধরো Frontend থেকে Request এলো:
GET /products?category=laptop

Django View:

products = Product.objects.filter(
    category="laptop"
)


ভিতরে ORM SQL তৈরি করবে:

SELECT *
FROM products
WHERE category='laptop';

তারপর PostgreSQL Data ফেরত দেবে।

"""


# SQL কীভাবে কাজ করে?
"""

মনে করো তোমার PostgreSQL Server চালু আছে।
Your Application
       │
       ▼
    SQL Query
       │
       ▼
 PostgreSQL Database
       │
       ▼
   Result

Django ORM-ও ভিতরে ভিতরে SQL Query-ই তৈরি করে।

Step 1: CREATE DATABASE
Database তৈরি করার জন্য ব্যবহার করা হয়।

Syntax:
CREATE DATABASE ecommerce;

এখানে:
Database Name:
ecommerce

Example:
CREATE DATABASE school;

Database তৈরি হবে:
school

একটি PostgreSQL Server-এ একাধিক Database থাকতে পারে।

PostgreSQL
├── ecommerce
├── school
├── hospital
└── library

"""



# Step 2: CREATE TABLE
"""
Database-এর ভিতরে Table তৈরি করা হয়।

Syntax:
CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    email VARCHAR(100)

);

এখানে:
Table Name:
users

Columns:
id

name

email

Result:
id	         name	            email

এখনও কোনো data নেই।


Data Type বুঝি
INTEGER
age INTEGER

Example:
25
40
60
VARCHAR

String রাখার জন্য।
name VARCHAR(100)

মানে:
সর্বোচ্চ 100 character।

TEXT
বড় লেখার জন্য।
description TEXT


BOOLEAN
is_active BOOLEAN

Values:
TRUE
FALSE


DATE
created_at DATE

Example:
2026-07-15


SERIAL কী?
id SERIAL PRIMARY KEY

SERIAL automatically number দেয়।

Example:
id
1
2
3
তোমাকে manually id দিতে হবে না।

"""


# Step 3: INSERT
"""
Table-এ data যোগ করা।

Syntax:

INSERT INTO users
(name,email)

VALUES
('Mamun','mamun@gmail.com');


আরও Data:

INSERT INTO users
(name,email)

VALUES
('Rahim','rahim@gmail.com');

Result:
id	         name	         email
1	         Mamun	         mamun@gmail.com
2	         Rahim	         rahim@gmail.com


একসাথে অনেকগুলো row insert:

INSERT INTO users (name, email)
VALUES
('Karim', 'karim@gmail.com'),
('Sakib', 'sakib@gmail.com'),
('Nusrat', 'nusrat@gmail.com');

"""



# Step 4: SELECT
"""
Database থেকে Data পড়া।

সব data:
SELECT *

FROM users;

Output:
id	name	email
1	Mamun	mamun@gmail.com
2	Rahim	rahim@gmail.com


শুধু একটি Column:

SELECT name
FROM users;

Output:
name
Mamun
Rahim


একাধিক Column:

SELECT
name,
email

FROM users;


SELECT * মানে কী?
SELECT *
* মানে:
সব Column।

"""



# Step 5: WHERE
"""
Condition দিয়ে Data filter করা।

Example:
SELECT *
FROM users
WHERE id=1;

Output:
id	name
1	Mamun


আরও Example:
SELECT *

FROM users

WHERE name='Rahim';


Number Comparison:
SELECT *

FROM products

WHERE price > 50000;


Multiple Conditions:
SELECT *
FROM users
WHERE age > 18
AND city='Dhaka';



SELECT *
FROM users
WHERE city='Dhaka'
OR city='Khulna';

"""



# Step 6: ORDER BY
"""
Data Sort করার জন্য।
Ascending:

SELECT *
FROM products
ORDER BY price ASC;

Result:
1000
5000
10000
50000

Descending:
SELECT *
FROM products
ORDER BY price DESC;

Result:
50000
10000
5000
1000

Sort by Name:
SELECT *
FROM users
ORDER BY name;
Alphabetical order হবে।

"""



# Step 7: LIMIT
"""
কতটি Row চাই সেটা নির্ধারণ করে।

Example:
SELECT *
FROM users
LIMIT 5;

মানে:
প্রথম ৫টি Row।

Top Product:
SELECT *
FROM products
ORDER BY price DESC
LIMIT 1;

Result:
সবচেয়ে দামি Product।

Latest Orders:
SELECT *
FROM orders
ORDER BY created_at DESC
LIMIT 10;



Step 8: DISTINCT

Duplicate value বাদ দেয়।

ধরো:
city
Dhaka
Dhaka
Khulna
Rajshahi
Khulna

Query:
SELECT DISTINCT city
FROM users;

Output:
city
Dhaka
Khulna
Rajshahi

"""



# Real E-commerce Examples:
"""
সব Product দেখাও
SELECT *
FROM products;

Price 50000-এর বেশি
SELECT *
FROM products
WHERE price > 50000;

Cheapest Product
SELECT *
FROM products
ORDER BY price ASC
LIMIT 1;

Most Expensive Product
SELECT *
FROM products
ORDER BY price DESC
LIMIT 1;

সব Category
SELECT DISTINCT category
FROM products;

"""