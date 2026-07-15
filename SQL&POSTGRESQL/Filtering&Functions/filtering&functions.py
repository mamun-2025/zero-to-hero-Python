


# আমাদের Sample Table
# ধরো আমাদের employees নামে একটি Table আছে।
"""
| id | name   | department | salary | city     | bonus |
| -: | ------ | ---------- | -----: | -------- | ----: |
|  1 | Mamun  | IT         |  50000 | Dhaka    |  5000 |
|  2 | Rahim  | HR         |  35000 | Khulna   |  NULL |
|  3 | Karim  | IT         |  60000 | Dhaka    |  3000 |
|  4 | Sakib  | Sales      |  45000 | Rajshahi |  NULL |
|  5 | Nusrat | HR         |  40000 | Dhaka    |  2000 |


Table তৈরি:
CREATE TABLE employees (

id SERIAL PRIMARY KEY,

name VARCHAR(100),

department VARCHAR(50),

city VARCHAR(100),

salary INT,

bonus INT

);


Data Insert:
INSERT INTO employees
(name, department, salary, city, bonus)

VALUES

('Mamun','IT',50000,'Dhaka',5000),

('Rahim','HR',35000,'Khulna',NULL),

('Karim','IT',60000,'Dhaka',3000),

('Sakib','Sales',45000,'Rajshahi',NULL),

('Nusrat','HR',40000,'Dhaka',2000);

"""


# 1. UPDATE
"""

Data পরিবর্তন করার জন্য UPDATE ব্যবহার করা হয়।

Syntax:
UPDATE table_name
SET column = value
WHERE condition;

Example:
Rahim-এর salary বাড়াও।

UPDATE employees
SET salary = 38000
WHERE id = 2;

Result:
id	name	salary
2	Rahim	38000

একাধিক Column Update:
UPDATE employees
SET
salary = 55000,
city = 'Chattogram'
WHERE id = 1;


⚠️ খুব গুরুত্বপূর্ণ
WHERE না দিলে?

UPDATE employees
SET salary = 10000;

ফলাফল:
সব Employee-এর salary 10000 হয়ে যাবে।

Django ORM
Employee.objects.filter(id=2).update(
    salary=38000
)

"""


# 2. DELETE
"""
Row মুছে ফেলার জন্য।

Syntax:
DELETE FROM table_name
WHERE condition;

Example:
DELETE FROM employees
WHERE id = 4;

Employee ID 4 delete হবে।


⚠️ WHERE না দিলে
DELETE FROM employees;

Result:
পুরো Table-এর সব Row delete হয়ে যাবে।

Django ORM:
Employee.objects.filter(id=4).delete()

"""


# 3. LIKE
"""
Pattern Matching করার জন্য।

ধরো:
name
Mamun
Mahin
Rahim
Karim
%
যে কোনো সংখ্যক Character।

Example:

SELECT *
FROM employees
WHERE name LIKE 'Ma%';

Result:
name
Mamun
Mahin


শেষে im
SELECT *
FROM employees
WHERE name LIKE '%im';

Result:
name
Rahim
Karim


মাঝখানে mu
SELECT *
FROM employees
WHERE name LIKE '%mu%';

Result:
name
Mamun
_

একটি মাত্র Character।
Example:

SELECT *
FROM employees
WHERE name LIKE 'M____';

এটি ৫ অক্ষরের M দিয়ে শুরু হওয়া নাম খুঁজবে।


Django ORM
Employee.objects.filter(
   name__startswith="Ma"
)

"""


# 4. IN
"""
একাধিক Value-এর মধ্যে খুঁজতে।

Example:
SELECT *
FROM employees
WHERE city IN (
'Dhaka',
'Khulna'
);

Result:
Dhaka অথবা Khulna-এর Employee।

Django ORM:
Employee.objects.filter(
   city__in=[
      "Dhaka",
      "Khulna"
   ]
)

"""


# 5. BETWEEN
"""
Range-এর মধ্যে Data খুঁজতে।

Example:
SELECT *
FROM employees
WHERE salary
BETWEEN 40000 AND 55000;

Result:
40000–55000-এর মধ্যে salary।

Django ORM:
Employee.objects.filter(
   salary_range=(
      400000,
      550000
   )
)

"""


# 6. IS NULL
"""
NULL Value খুঁজতে।

Example:
SELECT *
FROM employees
WHERE bonus IS NULL;

Result:
name
Rahim
Sakib

NULL না হলে:
SELECT *
FROM employees
WHERE bonus IS NOT NULL;

Django ORM:
Employee.objects.filter(
   bonus_isnull=True
)

"""



# 7. Aggregate Functions ⭐
"""
Aggregate Function অনেক Row-এর উপর Calculation করে।

COUNT()
কতটি Row আছে।

SELECT COUNT(*)
FROM employees;

Output:
5

SUM()
সব Salary যোগ।
SELECT SUM(salary)
FROM employees;


AVG()
Average Salary।

SELECT AVG(salary)
FROM employees;


MAX()
সবচেয়ে বড় Salary।
SELECT MAX(salary)
FROM employees;


MIN()
সবচেয়ে ছোট Salary।
SELECT MIN(salary)
FROM employees;

Django ORM:
from django.db.models import AVG

Employee.objects.aggregate(
   AVG("salary")
)

"""


# 8. GROUP BY ⭐
"""
8. GROUP BY ⭐
একই ধরনের Data Group করার জন্য।

ধরো:
department	salary
IT	         50000
IT	         60000
HR	         35000
HR	         40000
Sales	      45000


Department অনুযায়ী Average Salary:
SELECT
department,
AVG(salary)
FROM employees
GROUP BY department;


Output:
department	avg_salary
IT	         55000
HR	         37500
Sales	      45000

আরও Example:
Department অনুযায়ী Employee Count:

SELECT
department,
COUNT(*)
FROM employees
GROUP BY department;


Django ORM:
from django.db.models import Count

Employee.objects.values(
   "department"
).annotate(
   total=Count("id")
)

"""


# 9. HAVING ⭐
"""
WHERE Row filter করে।
HAVING Group filter করে।

Example:
যেসব Department-এ ১ জনের বেশি Employee আছে:

SELECT
department,
COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;

Output:
department
IT
HR


Difference

WHERE
Group হওয়ার আগে Filter।
SELECT *
FROM employees
WHERE salary > 40000;
HAVING



Group হওয়ার পরে Filter।
SELECT
department,
AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 45000;



Real E-commerce Examples
Price Range
SELECT *
FROM products
WHERE price
BETWEEN 10000 AND 50000;


Total Orders
SELECT COUNT(*)
FROM orders;


Total Sales
SELECT SUM(total)
FROM orders;


Most Expensive Product
SELECT MAX(price)
FROM products;


Category অনুযায়ী Product Count
SELECT
category,
COUNT(*)
FROM products
GROUP BY category;

"""

# Django ORM Mapping
"""
| SQL          | Django ORM              |
| ------------ | ----------------------- |
| `UPDATE`     | `.update()`             |
| `DELETE`     | `.delete()`             |
| `LIKE 'Ma%'` | `name__startswith="Ma"` |
| `IN (...)`   | `field__in=[...]`       |
| `BETWEEN`    | `field__range=(a, b)`   |
| `IS NULL`    | `field__isnull=True`    |
| `COUNT()`    | `Count()`               |
| `AVG()`      | `Avg()`                 |
| `SUM()`      | `Sum()`                 |
| `GROUP BY`   | `.values().annotate()`  |
| `HAVING`     | `.annotate().filter()`  |

"""


# Backend Flow
"""
Frontend
Search Products

↓

GET /products?min=10000&max=50000

↓

Django ORM

↓

SQL

SELECT *
FROM products
WHERE price
BETWEEN
10000 AND 50000;

↓

PostgreSQL

↓

JSON Response
"""
