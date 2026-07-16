

# কেন Relationship দরকার?
"""

ধরো তুমি একটি E-commerce Website বানাচ্ছ।
তুমি কি Order Table-এর মধ্যে User-এর সব তথ্য বারবার রাখবে?

❌ খারাপ Design:
OrderID	         User Name	Email	            Phone	   Product
101	            Mamun	      mamun@gmail.com	017...	Laptop
102	            Mamun	      mamun@gmail.com	017...	Mouse

এখানে একই User-এর তথ্য বারবার লেখা হচ্ছে।
এটাকে Data Redundancy বলে।

ভালো Design:
Users Table
id	name
1	Mamun

Orders Table
id	   user_id	   product
101	1	         Laptop
102	1	         Mouse

এখন শুধু user_id রাখা হয়েছে।
এটাই Relationship-এর কাজ।

"""


# 1. One-to-One Relationship
"""
একটি Row ↔ একটি Row
User
  │
  │
  │
Profile

Example:
একজন User-এর একটি Profile।

Users
id	name
1	Mamun

Profiles
id	   user_id	   phone
1	   1	         017xxxxxxxx

একজন User-এর একটিই Profile।

Django:
class Profile(models.Model):
   user = models.OneToOneField(
      User,
      on_delete=models.CASCADE
   )

Real Examples:
User ↔ Profile
User ↔ Passport
Student ↔ Student ID Card

"""


# 2. One-to-Many Relationship ⭐
"""
সবচেয়ে বেশি ব্যবহৃত Relationship।
একজন Parent-এর অনেক Child থাকতে পারে।

User

   │
   ├──────── Order
   ├──────── Order
   └──────── Order

Users
id	name
1	Mamun
2	Rahim

Orders
id	   user_id	   product
101	1	         Laptop
102	1	         Keyboard
103	2	         Mouse

একজন User-এর অনেক Order।

কিন্তু
একটি Order শুধু একজন User-এর।

Django:
class Order(models.Model):
   user = models.ForeignKey(
      User,
      on_delete=models.CASCADE
   )

আরও Examples
Customer → Orders
Category → Products
Teacher → Students
Department → Employees

"""


# 3. Many-to-Many Relationship ⭐
"""
উভয় দিকেই অনেক।
Student

   │

Many

   │

Course

Many
Students

id	name
1	Mamun
2	Rahim

Courses
id	title
1	Python
2	Django

Enrollment Table
student_id	course_id
1	            1
1	            2
2	            1

Mamun:

Python
Django

Rahim:

Python

Django:
class Course(models.Model):
   students = models.ManyToManyField(
      Student 
   )

Real Examples
Students ↔ Courses
Products ↔ Tags
Movies ↔ Actors
Users ↔ Roles


Relationship Summary:
| Relationship | Example          |
| ------------ | ---------------- |
| One-to-One   | User → Profile   |
| One-to-Many  | User → Orders    |
| Many-to-Many | Student ↔ Course |

"""


# JOIN কী?
"""
Relationship থাকলেই JOIN দরকার।
JOIN একাধিক Table-এর Data একসাথে আনে।

Example
Users

id	name
1	Mamun
2	Rahim

Orders
id	   user_id	product
101	1	      Laptop
102	1	      Mouse
103	2	      Keyboard


আমরা চাই:
User	Product
Mamun	Laptop
Mamun	Mouse
Rahim	Keyboard

এজন্য JOIN ব্যবহার করি।



4. INNER JOIN ⭐

শুধুমাত্র Matching Row ফেরত দেয়।

SQL:
SELECT
users.name,
orders.product

FROM users

INNER JOIN orders

ON users.id = orders.user_id;

Result
name	product
Mamun	Laptop
Mamun	Mouse
Rahim	Keyboard

Visualization
Users      Orders

  ○────────○
Only Matching Area



5. LEFT JOIN

বাম Table-এর সব Row ফেরত দেয়।
Matching না থাকলেও।

Example
Users

id	name
1	Mamun
2	Rahim
3	Karim

Orders
user_id	product
1	      Laptop
2	      Mouse

SQL
SELECT
users.name,
orders.product

FROM users

LEFT JOIN orders

ON users.id = orders.user_id;

Result
name	product
Mamun	Laptop
Rahim	Mouse
Karim	NULL

Visualization
Users      Orders

███████
Matching
Users-এর সব Row থাকবে।



6. RIGHT JOIN

ডান Table-এর সব Row ফেরত দেয়।

SQL
SELECT *

FROM users

RIGHT JOIN orders

ON users.id = orders.user_id;

Visualization
Users      Orders

Matching
███████
Orders-এর সব Row থাকবে।




7. FULL JOIN

দুই Table-এর সব Row ফেরত দেয়।
Matching না থাকলেও।

SELECT *

FROM users

FULL JOIN orders

ON users.id = orders.user_id;

Visualization
Users      Orders

████████████
সব Row।

JOIN Comparison
JOIN	কী ফেরত দেয়
INNER	শুধু Matching
LEFT	Left-এর সব
RIGHT	Right-এর সব
FULL	দুই Table-এর সব



8. SELF JOIN

একই Table নিজের সাথে JOIN করে।
Example
Employees

id	name	      manager_id
1	CEO	      NULL
2	Manager	   1
3	Developer	2

Query
SELECT
e.name,
m.name

FROM employees e

LEFT JOIN employees m

ON e.manager_id = m.id;

Result
Employee	Manager
CEO	NULL
Manager	CEO
Developer	Manager

"""


# Django ORM Mapping ⭐
"""
One-to-One
Profile.objects.select_related(
    "user"
)
One-to-Many
Order.objects.select_related(
    "user"
)
Many-to-Many
Course.objects.prefetch_related(
    "students"
)
SQL vs Django ORM:
| SQL               | Django ORM                               |
| ----------------- | ---------------------------------------- |
| INNER JOIN        | `select_related()` (ForeignKey/OneToOne) |
| LEFT JOIN         | ORM relation lookup (depending on query) |
| Many-to-Many JOIN | `prefetch_related()`                     |
| Foreign Key       | `models.ForeignKey()`                    |
| One-to-One        | `models.OneToOneField()`                 |
| Many-to-Many      | `models.ManyToManyField()`               |

"""


# Real Backend Example
"""

ধরো Frontend থেকে Request এসেছে:
GET /api/orders
তুমি Response-এ Order-এর সাথে User-এর নামও দেখাতে চাও।

ORM:
orders = Order.objects.select_related(
    "user"
)

ভিতরে Django একটি SQL JOIN চালাবে।

SQL (সরলভাবে):
SELECT
orders.id,
orders.product,
users.name

FROM orders
INNER JOIN users

ON users.id = orders.user_id;

তারপর Response:

[
  {
    "id": 101,
    "product": "Laptop",
    "user": "Mamun"
  }
]

"""





"""
আমরা একটা E-commerce Database বানাবো এবং পুরো SQL + পরে Django ORM শিখব।

Project: E-commerce Database

আমাদের ৪টি Table থাকবে।

users
│
├── orders
│
├── products
│
└── order_items

Relationship:

Users
  │
  │ 1
  │
  ▼
Orders
  │
  │ 1
  │
  ▼
Order Items
  ▲
  │
  │
Products
Step 1: Users Table
CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    email VARCHAR(100)

);
Step 2: Products Table
CREATE TABLE products (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    price INT

);
Step 3: Orders Table
CREATE TABLE orders (

    id SERIAL PRIMARY KEY,

    user_id INT REFERENCES users(id),

    order_date DATE

);

এখানে প্রথম Foreign Key দেখলে।

orders.user_id
        │
        ▼
users.id

মানে Order একজন User-এর।

Step 4: Order Items Table
CREATE TABLE order_items (

    id SERIAL PRIMARY KEY,

    order_id INT REFERENCES orders(id),

    product_id INT REFERENCES products(id),

    quantity INT

);

Relationship

order_items.order_id
            │
            ▼
orders.id

order_items.product_id
            │
            ▼
products.id
এবার Data Insert
Users
INSERT INTO users (name,email)

VALUES

('Mamun','mamun@gmail.com'),

('Rahim','rahim@gmail.com'),

('Karim','karim@gmail.com');
Products
INSERT INTO products (name,price)

VALUES

('Laptop',80000),

('Mouse',1200),

('Keyboard',2500),

('Monitor',18000);
Orders
INSERT INTO orders (user_id,order_date)

VALUES

(1,'2026-07-12'),

(2,'2026-07-13');
Order Items
INSERT INTO order_items

(order_id,product_id,quantity)

VALUES

(1,1,1),

(1,2,2),

(2,3,1);
এখন Database Structure
Users

1 Mamun
2 Rahim
3 Karim

↓

Orders

1 -> User 1
2 -> User 2

↓

Order Items

Order 1
    Laptop
    Mouse

Order 2
    Keyboard
Lesson 1 — INNER JOIN

প্রশ্ন:

কে কোন Product কিনেছে?

SELECT

users.name,

products.name,

order_items.quantity

FROM users

INNER JOIN orders

ON users.id = orders.user_id

INNER JOIN order_items

ON orders.id = order_items.order_id

INNER JOIN products

ON products.id = order_items.product_id;

Output

User	Product	Quantity
Mamun	Laptop	1
Mamun	Mouse	2
Rahim	Keyboard	1
এটা কীভাবে কাজ করল?

ধাপে ধাপে:

users
   │
   ▼
orders

প্রথম JOIN:

Mamun ---- Order 1

Rahim ---- Order 2

তারপর:

orders
      │
      ▼
order_items

হলো:

Order 1

Laptop

Mouse

Order 2

Keyboard

শেষে:

products

থেকে Product-এর নাম নিয়ে এল।

Django ORM-এ একই Query

পরে আমরা এটা লিখব:

OrderItem.objects.select_related(
    "order__user",
    "product"
)

এবং Django ORM নিজে JOIN query তৈরি করবে।

"""




# আগে ধরে নিচ্ছি তোমার এই ৪টি table আছে:
"""
users
-----
id | name
1  | Mamun
2  | Rahim
3  | Karim


products
---------
id | name      | price
1  | Laptop    | 80000
2  | Mouse     | 1200
3  | Keyboard  | 2500
4  | Monitor   | 18000


orders
------
id | user_id | order_date
1  | 1       | 2026-07-12
2  | 2       | 2026-07-13


order_items
-----------
id | order_id | product_id | quantity
1  | 1        | 1          | 1
2  | 1        | 2          | 2
3  | 2        | 3          | 1



1. 3 Table JOIN ⭐
Question

কে কোন Order করেছে?

SELECT
    users.name,
    orders.id,
    orders.order_date

FROM users

INNER JOIN orders
ON users.id = orders.user_id;

Output

User	Order ID	Date
Mamun	1	2026-07-12
Rahim	2	2026-07-13
এবার 3 Table

কে কোন Product কিনেছে?

SELECT

users.name,

orders.id,

products.name

FROM users

INNER JOIN orders
ON users.id = orders.user_id

INNER JOIN order_items
ON orders.id = order_items.order_id

INNER JOIN products
ON products.id = order_items.product_id;

Output

User	Order	Product
Mamun	1	Laptop
Mamun	1	Mouse
Rahim	2	Keyboard
2. 4 Table JOIN ⭐⭐⭐
এবার Quantity-ও দেখাও।
SELECT

users.name,

orders.id,

products.name,

order_items.quantity

FROM users

INNER JOIN orders
ON users.id = orders.user_id

INNER JOIN order_items
ON orders.id = order_items.order_id

INNER JOIN products
ON products.id = order_items.product_id;

Output

User	Order	Product	Qty
Mamun	1	Laptop	1
Mamun	1	Mouse	2
Rahim	2	Keyboard	1

এখানে ৪টি table একসাথে JOIN হয়েছে।

3. Aggregate + JOIN ⭐⭐⭐
Question

প্রতিটি User মোট কতটি Product কিনেছে?

SELECT

users.name,

SUM(order_items.quantity) AS total_products

FROM users

INNER JOIN orders
ON users.id = orders.user_id

INNER JOIN order_items
ON orders.id = order_items.order_id

GROUP BY users.name;

Output

User	Total Products
Mamun	3
Rahim	1
Question

প্রতিটি User কত টাকা spend করেছে?

SELECT

users.name,

SUM(products.price * order_items.quantity)
AS total_spent

FROM users

INNER JOIN orders
ON users.id = orders.user_id

INNER JOIN order_items
ON orders.id = order_items.order_id

INNER JOIN products
ON products.id = order_items.product_id

GROUP BY users.name;

Calculation

Mamun

Laptop
80000 × 1

Mouse
1200 × 2

Total

82400

Output

User	Total Spent
Mamun	82400
Rahim	2500
4. GROUP BY + JOIN ⭐⭐⭐
প্রতিটি Product কতবার বিক্রি হয়েছে?
SELECT

products.name,

SUM(order_items.quantity) AS total_sales

FROM products

INNER JOIN order_items
ON products.id = order_items.product_id

GROUP BY products.name;

Output

Product	Sold
Laptop	1
Mouse	2
Keyboard	1
প্রতিটি User কতটি Order করেছে?
SELECT

users.name,

COUNT(orders.id) AS total_orders

FROM users

LEFT JOIN orders
ON users.id = orders.user_id

GROUP BY users.name;

Output

User	Orders
Mamun	1
Rahim	1
Karim	0

এখানে LEFT JOIN ব্যবহার করেছি, তাই Karim-এর কোনো order না থাকলেও result-এ এসেছে।

5. HAVING + JOIN ⭐⭐⭐⭐
যেসব User ১টির বেশি Product কিনেছে
SELECT

users.name,

SUM(order_items.quantity) AS total_products

FROM users

INNER JOIN orders
ON users.id = orders.user_id

INNER JOIN order_items
ON orders.id = order_items.order_id

GROUP BY users.name

HAVING SUM(order_items.quantity) > 1;

Output

User	Total Products
Mamun	3
যেসব Product-এর Total Sale ১টির বেশি
SELECT

products.name,

SUM(order_items.quantity) AS sold

FROM products

INNER JOIN order_items
ON products.id = order_items.product_id

GROUP BY products.name

HAVING SUM(order_items.quantity) > 1;

Output
Product	Sold
Mouse	   2


"""