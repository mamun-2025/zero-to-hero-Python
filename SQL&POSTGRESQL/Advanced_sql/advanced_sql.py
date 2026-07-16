

# 1. Index ⭐⭐⭐
"""
একটি গল্প দিয়ে বুঝি

ধরো তোমার কাছে ১০,০০০ পৃষ্ঠার একটি বই আছে।

তুমি খুঁজতে চাও:

"Django"

দুইভাবে খুঁজতে পারো।

Method 1

প্রথম পৃষ্ঠা থেকে পড়া শুরু করলে

Page 1
↓

Page 2
↓

Page 3
↓

...

↓

Page 9000

অনেক সময় লাগবে।

Method 2

বইয়ের Index দেখলে

Django → Page 8234

সরাসরি Page 8234-এ চলে গেলে।

এক সেকেন্ডও লাগবে না।

Database-এও ঠিক একই ঘটনা ঘটে।

Table:

id	name	email
1	A	a@gmail.com
2	B	b@gmail.com
...	...	...
1000000	Mamun	mamun@gmail.com

তুমি Query করলে:

SELECT *
FROM users
WHERE email='mamun@gmail.com';
Index না থাকলে

Database করবে:

Row 1

↓

Row 2

↓

Row 3

↓

...

↓

Row 1000000

এটাকে বলে

Full Table Scan

খুব Slow।

Index থাকলে

Database আগে Index দেখবে।

mamun@gmail.com

↓

Row 1000000

সরাসরি Data পেয়ে যাবে।

Index কী?

Definition:

Index হলো Database-এর একটি বিশেষ Data Structure যা Search দ্রুত করে।

Index Example
CREATE INDEX idx_email

ON users(email);

এখন

SELECT *

FROM users

WHERE email='abc@gmail.com';

অনেক দ্রুত হবে।

কোথায় Index দেব?

যে Column-এ বেশি Search হয়।

Example:

email

username

phone

product_id

user_id

created_at
কোথায় Index দেব না?

যে Column-এ

খুব কম Search হয়
বারবার Update হয়

কারণ Index-ও Update করতে হয়।

Django
email = models.EmailField(
    unique=True,
    db_index=True
)

"""


# 2. Transactions ⭐⭐⭐
"""
বাস্তব উদাহরণ

তুমি ATM থেকে টাকা তুলছো।

Process:

Balance:

10000

Step 1

10000 - 5000

Step 2

ATM টাকা বের করবে।

যদি Step 1 হয়ে যায়

কিন্তু

Step 2 Fail করে?

তাহলে?

Balance:

5000

কিন্তু টাকা পাওনি।

এটি বড় সমস্যা।

এজন্য Transaction।

Transaction কী?

একাধিক SQL Query-কে

একটি Unit হিসেবে Execute করে।

সব হবে

অথবা

কিছুই হবে না

এটাকে বলে

All or Nothing

Example

Bank Transfer

Mamun

↓

-5000

↓

Rahim

+5000

দুটি Query:

UPDATE accounts

SET balance=balance-5000

WHERE id=1;
UPDATE accounts

SET balance=balance+5000

WHERE id=2;

দুটোই Successful হতে হবে।

ACID Properties ⭐⭐⭐⭐⭐

Interview-এ খুব জিজ্ঞাসা করে।

Transaction-এর ৪টি Rule।

A = Atomicity

All অথবা Nothing

C = Consistency

Database সবসময় Valid থাকবে।

I = Isolation

এক Transaction অন্য Transaction-কে Disturb করবে না।

D = Durability

Commit হয়ে গেলে Data আর হারাবে না।

"""


# 3. COMMIT
"""
Commit মানে

Permanent Save।

Example

BEGIN;
UPDATE accounts

SET balance=balance-1000

WHERE id=1;
COMMIT;

এখন Data Permanently Save।

"""



# 4. ROLLBACK
"""
Rollback মানে

আগের অবস্থায় ফিরে যাও।

Example

BEGIN;
UPDATE users

SET salary=100;

দেখলে ভুল হয়েছে।

ROLLBACK;

সব আগের মতো হয়ে যাবে।

Transaction Flow
BEGIN

↓

SQL Query

↓

Success?

↓

Yes

↓

COMMIT

↓

Permanent

Fail হলে

ROLLBACK

↓

Previous State
Django Transaction
from django.db import transaction

with transaction.atomic():

    sender.balance -= 5000

    sender.save()

    receiver.balance += 5000

    receiver.save()

যদি মাঝখানে Error হয়

সব Rollback হবে।

"""



# 5. CONSTRAINTS ⭐⭐⭐⭐⭐
"""
Constraint মানে

Database-এর Rules।

Primary Key
id SERIAL PRIMARY KEY

Unique হবে।

NOT NULL
name VARCHAR(100)

NOT NULL

Name Empty হতে পারবে না।

UNIQUE
email VARCHAR(100)

UNIQUE

একই Email দুইবার থাকবে না।

CHECK
age INT

CHECK(age>=18)

১৮-এর কম হলে Insert হবে না।

DEFAULT
status VARCHAR(20)

DEFAULT 'Pending'

Value না দিলে

নিজে থেকেই

Pending হবে।

Foreign Key
user_id

REFERENCES users(id)

Relationship তৈরি করবে।

Django Constraint
email = models.EmailField(
    unique=True
)
name = models.CharField(
    max_length=100,
    null=False
)

"""


# 6. VIEWS ⭐⭐⭐⭐
"""
View হলো

Virtual Table।

Data Copy করে না।

ধরো

Employees

name	salary
Mamun	50000
Rahim	40000

তুমি শুধু IT Department দেখতে চাও।

বারবার Query না লিখে

View বানালে

CREATE VIEW it_employees

AS

SELECT *

FROM employees

WHERE department='IT';

এখন

SELECT *

FROM it_employees;

হলেই হবে।

View-এর সুবিধা

Query ছোট হয়
Security বাড়ে
Reusable

"""


# 7. Normalization ⭐⭐⭐
"""
📘 Normalization (Deep Understanding)
প্রথমে একটা প্রশ্ন।

ধরো তুমি একটি E-commerce Website বানাচ্ছ।

একজন User ১০০টি Order করল।

তুমি কি প্রতিটি Order-এর মধ্যে User-এর Name, Email, Phone বারবার লিখবে?

❌ Design 1
Order ID	User Name	Email	Phone	Product
101	Mamun	mamun@gmail.com	01711111111	Laptop
102	Mamun	mamun@gmail.com	01711111111	Mouse
103	Mamun	mamun@gmail.com	01711111111	Keyboard

দেখো এখানে একই তথ্য বারবার আছে।

সমস্যা ১ — Storage Waste

একজন User যদি ১০০০টা Order করে?

তাহলে Email ১০০০ বার Save হবে।

mamun@gmail.com
mamun@gmail.com
mamun@gmail.com
mamun@gmail.com
...

অপ্রয়োজনীয়ভাবে Storage নষ্ট হচ্ছে।

সমস্যা ২ — Update Problem

ধরো Mamun Email পরিবর্তন করল।

নতুন Email:

mamun@yahoo.com

এখন তোমাকে ১০০০টি Row Update করতে হবে।

যদি ৯৯৯টি Update হয়, আর ১টি না হয়?

তাহলে Database-এ দুই রকম Email থাকবে।

Order	Email
101	mamun@yahoo.com
102	mamun@yahoo.com
103	mamun@gmail.com

এটাকে Data Inconsistency বলে।

সমস্যা ৩ — Delete Problem

ধরো Mamun-এর শেষ Order Delete করলে User-এর তথ্যও হারিয়ে যেতে পারে, কারণ User-এর আলাদা Table নেই।

তাহলে সমাধান কী?

Database-কে ছোট ছোট Related Table-এ ভাগ করো।

এটাই Normalization।

✅ Good Design

Users Table

id	name	email	phone
1	Mamun	mamun@gmail.com	01711111111

Orders Table

id	user_id	product
101	1	Laptop
102	1	Mouse
103	1	Keyboard

এখন User-এর তথ্য একবারই রাখা হয়েছে।

Orders শুধু user_id রাখছে।

সুবিধা

Storage কম লাগছে।

Email একবারই Save হচ্ছে।

Update একবারই করতে হবে।

Relationship সুন্দর হয়েছে।

এবার Normal Forms বুঝি
⭐ First Normal Form (1NF)
Rule

একটি Cell-এ শুধুমাত্র একটি Value থাকবে।

ধরো Student Table।

❌ Wrong
id	Name	Skills
1	Mamun	Python, Django, SQL

এখানে একটি Cell-এ ৩টি Value আছে।

এটি 1NF ভঙ্গ করছে।

✅ Correct

Option 1 (আলাদা Row)

id	Name	Skill
1	Mamun	Python
1	Mamun	Django
1	Mamun	SQL

বাস্তবে আরও ভালো Design হলো:

Students

id	Name
1	Mamun

Skills

id	name
1	Python
2	Django
3	SQL

StudentSkills

student_id	skill_id
1	1
1	2
1	3

এটি Many-to-Many Relationship।

1NF-এর মূল কথা

একটি Cell = একটি Value।

⭐ Second Normal Form (2NF)

এটি বুঝতে হলে Composite Primary Key জানতে হবে।

ধরো:

Enrollment Table

Student ID	Course ID	Student Name
1	101	Mamun
1	102	Mamun

Primary Key:

(Student ID, Course ID)

এটি Composite Key।

কিন্তু সমস্যা হলো:

Student Name শুধু Student ID-এর উপর নির্ভর করছে।

Course ID-এর উপর নয়।

এটাকে বলে Partial Dependency।

Solution

Students

id	Name
1	Mamun

Enrollment

student_id	course_id
1	101
1	102

এখন Student Name এক জায়গায় আছে।

2NF-এর মূল কথা

Non-key Column পুরো Primary Key-এর উপর নির্ভর করবে।

Partial Dependency থাকবে না।

⭐ Third Normal Form (3NF)

এটি সবচেয়ে গুরুত্বপূর্ণ।

Rule:

Non-key Column অন্য Non-key Column-এর উপর নির্ভর করবে না।

ধরো Employee Table।

❌ Wrong
id	Name	Department	Department Phone
1	Mamun	IT	12345
2	Rahim	IT	12345

সমস্যা:

Department Phone আসলে Department-এর Property।

Employee-এর নয়।

যদি IT Department-এর Phone বদলায়?

তাহলে সব Employee Update করতে হবে।

Solution

Departments

id	Name	Phone
1	IT	12345

Employees

id	Name	department_id
1	Mamun	1
2	Rahim	1

এখন Phone এক জায়গায় আছে।

3NF-এর মূল কথা

একটি Non-key Column আরেকটি Non-key Column-এর উপর নির্ভর করবে না।

মনে রাখার সহজ Trick
1NF
One Cell
↓

One Value
2NF
Every Column

↓

Depends on Whole Primary Key
3NF
Column

↓

Depends Only on Primary Key

NOT Another Column
বাস্তব Django Example

ধরো তুমি এমন Model লিখলে:

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)

এটি Normalized নয়।

সঠিক Design:

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

এখন User-এর তথ্য একবারই রাখা হচ্ছে।

Interview Answer (১ মিনিটে)

Normalization কী?

Normalization is the process of organizing data into multiple related tables to reduce redundancy, improve consistency, and maintain data integrity.

1NF: একটি Cell-এ একটি Value থাকবে।

2NF: সব Non-key Column পুরো Primary Key-এর উপর নির্ভর করবে।

3NF: কোনো Non-key Column অন্য Non-key Column-এর উপর নির্ভর করবে না।

"""


# 8. EXPLAIN ⭐⭐⭐⭐⭐
"""
Interview-এ খুব গুরুত্বপূর্ণ।

ধরো

SELECT *

FROM users

WHERE email='abc@gmail.com';

তুমি জানতে চাও

Database কীভাবে Query Execute করছে।

EXPLAIN

SELECT *

FROM users

WHERE email='abc@gmail.com';

Output

Index Scan

অথবা

Seq Scan
Seq Scan

মানে

পুরো Table Scan করছে।

Slow।

Index Scan

মানে

Index ব্যবহার করছে।

Fast।

Production-এ Slow Query খুঁজতে

EXPLAIN ব্যবহার করা হয়।

Django ORM Performance Tips ⭐⭐⭐⭐⭐
❌ খারাপ
for order in Order.objects.all():
    print(order.user.name)

এখানে N+1 Query Problem হতে পারে।

✅ ভালো
orders = Order.objects.select_related(
    "user"
)

একটি JOIN Query হবে।

ManyToMany

Course.objects.prefetch_related(
    "students"
)






Database Query কীভাবে Execute করবে তা দেখায়।

Example:

EXPLAIN

SELECT *

FROM users

WHERE email='mamun@gmail.com';

Output (সরলভাবে):

Index Scan

অথবা

Seq Scan
Seq Scan
Row 1

↓

Row 2

↓

Row 3

↓

...

সব Row দেখছে।

Slow.

Index Scan
Index

↓

Direct Row

Fast.

Production-এ Slow Query খুঁজতে EXPLAIN খুব গুরুত্বপূর্ণ।

Real Backend Example

ধরো:

User.objects.get(
    email="mamun@gmail.com"
)

ORM SQL বানায়:

SELECT *

FROM users

WHERE email='mamun@gmail.com';

যদি Email-এ Index থাকে:

Index Scan

না থাকলে:

Sequential Scan

"""



# Django Mapping ⭐⭐⭐
"""
| SQL Concept | Django                                         |
| ----------- | ---------------------------------------------- |
| Index       | `db_index=True`                                |
| Transaction | `transaction.atomic()`                         |
| COMMIT      | `atomic()` সফল হলে                             |
| ROLLBACK    | Exception হলে                                  |
| Constraints | `unique=True`, `null=False`, `CheckConstraint` |
| View        | Raw SQL / Database View                        |
| EXPLAIN     | `QuerySet.explain()`                           |



Django Index:
email = models.EmailField(
    db_index=True
)

Django EXPLAIN:
User.objects.filter(
    email="mamun@gmail.com"
).explain()

"""