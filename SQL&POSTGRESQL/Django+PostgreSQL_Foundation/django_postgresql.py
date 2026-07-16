


# Part 1 — PostgreSQL + Django Configuration
"""
Step 1: PostgreSQL Driver Install
Django PostgreSQL-এর সাথে কথা বলতে psycopg ব্যবহার করে।

pip install psycopg[binary]
(আগে psycopg2-binary বেশি ব্যবহার হতো, এখন নতুন psycopg-ও জনপ্রিয়।)

Step 2: settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ecommerce",
        "USER": "postgres",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

Step 3
Migration চালাও

python manage.py makemigrations
python manage.py migrate

Flow
Django

↓

ORM

↓

PostgreSQL Driver

↓

PostgreSQL

"""


# Part 2 — Django ORM vs Raw SQL
"""
ORM = Object Relational Mapper
ORM Python Object-কে SQL-এ রূপান্তর করে।

Raw SQL
SELECT *

FROM products

WHERE price > 50000;


ORM:
Product.objects.filter(
    price__gt=50000
)


ORM ভিতরে SQL বানায়।
SELECT *

FROM products

WHERE price > 50000;


Comparison:
| ORM                               | Raw SQL                    |
| --------------------------------- | -------------------------- |
| Pythonic                          | SQL লিখতে হয়              |
| নিরাপদ (SQL Injection Protection) | সতর্ক থাকতে হয়            |
| Cross Database                    | Database-specific হতে পারে |
| Maintainable                      | Complex Query-তে ভালো      |


কখন Raw SQL?
Complex Reporting
Database View
Stored Procedure
খুব Specific Query

বাকি ৯৫% ক্ষেত্রে ORM যথেষ্ট।

"""



# Part 3 — Basic ORM Queries
"""
Model:
class Product(models.Model):
   name = models.CharField(
      max_length=100
   )

   price = models.IntegerField()

   
1. .all()
= all data

Product.objects.all()

SQL:

SELECT *
FROM product;


2. .get()
= One Row

Product.objects.get(
   id=1
)


SQL:

SELECT *
FROM product
WHERE id = 1;
যদি একাধিক Row থাকে তাহলে Exception হবে।


3. .filter()
= Condition

Product.objects.filter(
   price_gt=50000
)


SQL:
SELECT *
FROM product
WHERE price>50000;


4. .exclude()
= NOT

Product.objects.exclude(
   price_gt=50000
)


SQL:
SELECT *
FROM product
WHERE NOT price>50000;


5. .create()
= INSERT(add)

Product.objects.create(
   name="Laptop",
   price=40000
)


SQL:
INSET INTO product
(name, price)

VALUES
('Laptop', 50000)


6. .update()
= update

Product.objects.filter(
   id=1
).update(
   price=50000
)

SQL:
UPDATE product
SET price=60000
WHERE id=1;


7. .delete()
= delete

Product.object.filter(
   id=1
).delete()


SQL:
DELETE
FROM product
WHERE id=1;


8. .order_by()
= sort 

ASC:
Product.objects.order_by(
   "price"
)

DESC:
Product.objects.order_by(
   "-price"
)


SQL:
SELECT *
FROM product
ORDER BY price DESC


9. .values()
= return dictionary

Product.objects.values(
   "name",
   "price"
)

output:
[
 {
   "name":"Laptop",
   "price":50000
 }
]



10. .values_list()
= return tuple

product.objects.values_list(
   "name",
   "price"
)

[
   ("Laptop", 500000)
]


"""



# Part 4 — Relationships
"""
1. ForeignKey
class Order(models.Model):
   user = models.ForeignKey(
      User, 
      on_delete=models.CASCADE
   )

SQL:
User

1

↓

Many Orders


2. OneToOneField
class Profile(models.Model):
   user = models.OneToOneField(
      User,
      on_delete=models.CASCADE
   )

User

↓

Profile



3. ManyToManyField
class Course(models.Model):
   students = models.ManyToManyField(
      Student 
   )

Student

↕

Course

"""


# Part 5 — Performance Basics ⭐⭐⭐
"""
Problem
ধরো:

orders = Order.objects.all()

for order in orders:

    print(order.user.name)

    
ORM কী করবে?
Query 1
Orders

তারপর
Order 1
↓

User
Order 2

↓

User
Order 3

↓

User

এটাকে N+1 Query Problem বলে।


select_related()
ForeignKey-এর জন্য।

orders = Order.objects.select_related(
    "user"
)

SQL
INNER JOIN
একটি Query।

prefetch_related()
ManyToMany-এর জন্য।

Course.objects.prefetch_related(
    "students"
)
দুটি Query চালায়।
Python-এ Merge করে।



কখন কোনটি?
| Relationship       | Method             |
| ------------------ | ------------------ |
| ForeignKey         | select_related()   |
| OneToOne           | select_related()   |
| ManyToMany         | prefetch_related() |
| Reverse ForeignKey | prefetch_related() |

"""




# Real Production Example
"""
ধরো
GET /api/orders

Response
[
 {
   "id":1,
   "user":"Mamun",
   "product":"Laptop"
 }
]

ORM
orders = Order.objects.select_related(
    "user"
)

Serializer

class OrderSerializer(
    ModelSerializer
):

    class Meta:

        model = Order

        fields = "__all__"


        
Production Example 2:

Course API

Course.objects.prefetch_related(
    "students"
)

Response
{
 "course":"Python",
 "students":[
   "Mamun",
   "Rahim"
 ]
}



Backend Flow:
Frontend

↓

GET /products

↓

Django URL

↓

View

↓

ORM

↓

SQL

↓

PostgreSQL

↓

ORM Object

↓

Serializer

↓

JSON

↓

Frontend


SQL ↔ ORM Cheat Sheet ⭐
| SQL               | Django ORM            |
| ----------------- | --------------------- |
| SELECT            | `.all()`              |
| WHERE             | `.filter()`           |
| NOT               | `.exclude()`          |
| INSERT            | `.create()`           |
| UPDATE            | `.update()`           |
| DELETE            | `.delete()`           |
| ORDER BY          | `.order_by()`         |
| SELECT Columns    | `.values()`           |
| SELECT Tuple      | `.values_list()`      |
| INNER JOIN        | `.select_related()`   |
| Many-to-Many JOIN | `.prefetch_related()` |


"""