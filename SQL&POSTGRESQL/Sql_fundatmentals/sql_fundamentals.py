

# 1. Database কী?
"""
Definition:
Database হলো এমন একটি জায়গা যেখানে data সংগঠিতভাবে সংরক্ষণ (store), manage এবং retrieve করা হয়।

সহজ ভাষায়:
Database হলো application-এর memory যেখানে সব গুরুত্বপূর্ণ তথ্য থাকে।

Example:
E-commerce Website:

User data:
Name:
Mamun

Email:
mamun@gmail.com


Product data:
Product:
Laptop

Price:
50000


Order data:
Order ID:
101

Customer:
Mamun

Product:
Laptop
এগুলো Database-এ থাকে।


Without Database:
Application বন্ধ

↓

সব data হারিয়ে যাবে


With Database:
Application বন্ধ

↓

Data নিরাপদ থাকে



Real Backend Example
Django Application:

User Registration

        ↓

Save User

        ↓

PostgreSQL Database


Database:
users table

id | name | email
------------------
1  | Mamun| gmail

"""


# 2. DBMS কী?
"""
DBMS:

Database Management System
এটি Database manage করার software।

কাজ:
Data store করা
Data update করা
Data delete করা
Security দেওয়া

Examples:
MySQL
PostgreSQL
Oracle
SQLite

Flow:
Application

↓

DBMS

↓

Database

"""


# 3. RDBMS কী?
"""
RDBMS:
Relational Database Management System
এটি DBMS-এর advanced version।

এখানে data table এবং relationship আকারে থাকে।

Example:
একটি E-commerce Database:

Users Table
id	                  name
1	                  Mamun


Orders Table
id	                  user_id
101	               1

এখানে:
User এবং Order-এর relationship আছে।

Popular RDBMS:
✅ PostgreSQL
✅ MySQL
✅ Oracle
✅ SQL Server

DBMS vs RDBMS
DBMS	                           RDBMS
Data সাধারণত simple form	      Data table form
Relationship নেই	               Relationship আছে
Small system	                  Large system
Less security	                  More security

"""


# 4. Table কী?
"""
RDBMS-এ data Table আকারে থাকে।

Table হলো:
Related data-এর collection।

Example:
User Table:
| id | name  | email                             |
| -- | ----- | --------------------------------- |
| 1  | Mamun | [a@gmail.com](mailto:a@gmail.com) |
| 2  | Rahim | [b@gmail.com](mailto:b@gmail.com) |


একটি Django Model:
class User(models.Model):

   name = models.CharField()

   email = models.EmailField()

এটি Database-এ Table তৈরি করবে।

"""


# 5. Row কী?
"""
Row = একটি complete record।

Example:
Users Table:

id	         name	            email
1	         Mamun	            a@gmail.com

পুরো line:
1 | Mamun | a@gmail.com

এটি একটি Row।


মানে:
একজন User = One Row

"""


# 6. Column কী?
"""
Column হলো একটি attribute বা field।

Example:

Users Table:

id	            name	            email

এখানে:
id
name
email

সবগুলো Column।

Django:
name
email
password

সব Column হবে।

"""


# 7. Primary Key ⭐
"""
Primary Key হলো:
একটি Table-এর প্রতিটি Row-কে uniquely identify করার field।

Example:
Users:
id	         name
1	         Mamun
2	         Rahim

এখানে:
id
Primary Key।

Rules:
Primary Key:
✅ Unique হবে
✅ NULL হবে না
✅ একটি Table-এ সাধারণত একটি থাকে


Django:

id = models.AutoField(
primary_key=True
)

Example:
User:
id = 101

এই ID দিয়ে User খুঁজে পাওয়া যাবে।

"""


# 8. Foreign Key ⭐
"""
Foreign Key হলো:
একটি Table-এর Primary Key অন্য Table-এ reference করলে সেটি Foreign Key।

Example:

Users:
id	            name
1	            Mamun

Orders:
id	         user_id
101	         1

এখানে:
user_id
হলো Foreign Key।

Relationship:

User

1

|

|

Many
Orders

একজন User অনেক Order করতে পারে।

Django:
class Order(models.Model):

   user = models.ForeignKey(
      user,
      on_delete=models.CASCADE
   )

"""


# 9. SQL কী?
"""
SQL:
Structured Query Language
Database-এর সাথে কথা বলার ভাষা।

Application:
"আমাকে সব user দাও"

SQL:
SELECT * FROM users;

Database:
"এই নাও users"

SQL দিয়ে:
Create data
Read data
Update data
Delete data
করা হয়।

CRUD SQL:
| Operation | SQL    |
| --------- | ------ |
| Create    | INSERT |
| Read      | SELECT |
| Update    | UPDATE |
| Delete    | DELETE |

# Example:
Create(INSERT):

INSERT INTO users
(name, email)

VALUES
("Mamun", "mamun@gmail.com)

______________________________
Read(SELECT):

SELECT * FROM
users;

_______________________________
update(UPDATE):

UPDATE users
SET name="Habib"
WHERE id=1;

______________________________
delete(DELETE):

DELETE FROM users
WHERE id=1;

"""


# 10. PostgreSQL Introduction ⭐
"""
PostgreSQL হলো একটি powerful open-source RDBMS।

Backend industry-তে অনেক জনপ্রিয়।
Features:
✅ Open Source
✅ Powerful
✅ Large Data Support
✅ ACID Transaction
✅ JSON Support
✅ Django Friendly

Real Companies ব্যবহার করে:
Large SaaS applications
Financial systems
E-commerce platforms


PostgreSQL কেন Django-এর সাথে ব্যবহার করি?

Django default:
SQLite
Development-এর জন্য ভালো।

কিন্তু Production:
PostgreSQL বেশি ব্যবহার হয়।

"""


# Django settings:
"""
DATABASES = {

'default': {

'ENGINE':
'django.db.backends.postgresql',

'NAME':
'mydatabase',

}

}

"""


# Database Structure Example (E-commerce)
"""
Database: ecommerce


Tables:

users

id
name
email


products

id
name
price


orders

id
user_id
total


payments

id
order_id
amount



Relationship:

User

 |
 |
Many

Orders

 |
 |
One

Payment

"""


# Backend Developer Mindset
"""
Frontend:
Show Data

Backend:
Process Data

Database:
Store Data



Complete Flow:
User Registration

↓

HTTP POST Request

↓

Django View

↓

ORM

↓

SQL Query

↓

PostgreSQL

↓

Save User

↓

Response

"""