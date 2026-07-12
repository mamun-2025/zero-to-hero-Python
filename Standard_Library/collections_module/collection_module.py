


"""
প্রথমে বুঝি: collections কী?

Python-এর built-in data structure আছে:

list
tuple
dict
set

কিন্তু অনেক real-world problem এ এগুলো দিয়ে কাজ করা কঠিন হয়।

তখন Python-এর collections module আমাদের specialized data structures দেয়।

সহজ ভাষায়:

collections module হলো Python-এর এমন একটি toolbox যেখানে সাধারণ list/dict-এর চেয়ে powerful কিছু data structure পাওয়া যায়।

Import:

import collections

অথবা নির্দিষ্ট জিনিস:

from collections import Counter

"""
# simple
letters = [
   "a",
   "b",
   "a",
   "c",
   "a"
]

Count = {}

for letter in letters:
   if letter in Count:
      Count[letter] += 1
   else:
      Count[letter] = 1

print(Count)






##### 1.Counter
"""
Counter কী?

Counter কোনো iterable-এর element কতবার এসেছে সেটা গুনে দেয়।

যেমন:
তোমার কাছে:

letters = [
    "a",
    "b",
    "a",
    "c",
    "a"
]

তুমি জানতে চাও:
a কতবার?
b কতবার?
c কতবার?

Counter ব্যবহার হয়:
Product popularity
Word frequency
Log analysis
User activity count
Analytics

"""
from collections import Counter

letters = [
   "a",
   "b",
   "a",
   "c",
   "a"
]

result = Counter(letters)
print(result)
print(result["a"])
print(result["d"])
# Counter আসলে কী return করে?
# এটা dictionary-এর মতো।




# Example 1: Product Sale Count
from collections import Counter

orders = [
   "Laptop",
   "Mobile",
   "Laptop",
   "Laptop",
   "Mouse"
]

sales = Counter(orders)

print(sales)
print(sales.most_common(2))


# Example 2: এই list থেকে count বের করো:
skills = [
   "Python",
   "Django",
   "Python",
   "SQL",
   "Django",
   "Python"
]

result = Counter(skills)
print(result)
print(f"Highest Course: {result.most_common(1)}")





##### 2. Defualtdict
"""
সাধারণ dictionary:

users = {}

users["Mamun"].append("Python")

Error:

KeyError

কারণ "Mamun" key এখনো নেই।

"""
# defaultdict
from collections import defaultdict

users = defaultdict(list)

users["Mamun"].append("Python")

print(users)


# বিভিন্ন default value
# int
count = defaultdict(int)

count["Python"] += 1

print(count)

# list
group = defaultdict(list)

group["Backend"].append("Mamun")

print(group)

# set
data = defaultdict(set)

data["Python"].add("Django")

print(data)


# Backend Example:Group Users
users = [
   ("Dhaka", "Mamun"),
   ("Dhaka", "Rahim"),
   ("Chittagong", "Karim")
]

from collections import defaultdict

cities = defaultdict(list)

for city, user in users:
   cities[city].append(user)

print(cities)

# Backend Example:এই data group করো
products = [
   ("Mobile", "iphone"),
   ("Mobile", "Samsung"),
   ("Laptop", "HP")
]

from collections import defaultdict

product = defaultdict(list)

for p, n in products:
   product[p].append(n)
   
print(product)

# Backend Use Case

# defaultdict:
# Grouping data
# API response formatting
# Category wise products
# User permissions





##### 3. deque
"""
deque কী?

deque = Double Ended Queue

মানে:
দুই দিক থেকে data add/remove করা যায়।

List-এ:

শেষে add fast:
list.append()

কিন্তু শুরুতে:
list.insert(0)
slow।

deque এ দুই দিক fast।

"""
from collections import deque

queue = deque()

queue.append("User1")
queue.append("User2")

print(queue)

# left side add
queue.appendleft("Admin")
print(queue)

# right remove
queue.pop()
print(queue)

# left remove
queue.popleft()
print(queue)


# Backend example: Queue System
from collections import deque

email_queue = deque()

email_queue.append("user1@gmail.com")
email_queue.append("user2@gmail.com")

while email_queue:
   email = email_queue.popleft()
   print(email)

# Backend Use Case

# deque:
# Task Queue
# Message Queue
# Browser History
# Cache
# BFS Algorithm


# Backend example: একটি queue বানাও:
from collections import deque

order_queue = deque()

order_queue.append("Order1")
order_queue.append("Order2")
order_queue.append("Order3")

while order_queue:
   order = order_queue.popleft()
   print(order)





##### 4. namedtuple
# simple tuple 
user = (
   "Mamun",
   25,
   "Backend tuple"
)

print(user)
print(user[0])

# namedtuple
from collections import namedtuple

User = namedtuple(
   "User",
   [
      "name",
      "age",
      "role"
   ]
)

user = User(
   "Mamun",
   25,
   "Jr Software Engineer"
)

print(user)
print(user.name)
print(user.age)
print(user.role)


# Backend example: Dashboard record
Product = namedtuple(
   "Product",
   [
      "id",
      "name",
      "price"
   ]
)

product = Product(
   1, 
   "Laptop",
   40000
)

print(product)
print(product.name)
print(product.price)

# namedtuple Use Case
# Read-only data
# Database result
# API response structure
# Configuration object


# Collections Summary
"""
| Tool        | কাজ                | Backend Example  |
| ----------- | ------------------ | ---------------- |
| Counter     | Count করা          | Product sales    |
| defaultdict | Auto default value | Group data       |
| deque       | Queue              | Email/task queue |
| namedtuple  | Structured tuple   | Data record      |


"""


### Problem 1: একটি website-এর visitor log:
vistitors = [
   "Django",
   "Python",
   "Django",
   "SQL",
   "Python",
   "Django",
   "Python"
]

from collections import Counter

result = Counter(vistitors)

print(f"Highest visitors: {result}")
print(result.most_common(1))




### Problem 2: একটি order list
orders = [
   ("Food", "Burger"),
   ("Food", "Pizza"),
   ("Drink", "Coffee")
]
\
from collections import defaultdict

order = defaultdict(list)

for key, value in orders:
   order[key].append(value)
   print(order)


### Problem 3: একটি task queue বানাও:
from collections import deque

task_queue = deque()

task_queue.append("Task1")
task_queue.append("Task2")
task_queue.append("Task3")

while task_queue:
   task = task_queue.popleft()
   print(task)



### 4: একটি User record namedtuple দিয়ে তৈরি করো।
from collections import namedtuple

Users = namedtuple(
   "User_record",
   [
      "id",
      "username",
      "email"
   ]
)

user = Users(
   101,
   "Habib Mamun",
   "habib@gmail.com"
)

print(user)



### Problem 5 (Mini Backend): Task Processing System
from collections import Counter, deque, defaultdict

class TaskManager:

   def __init__(self):
      # queue
      self.queue = deque()

      # Task count
      self.task_count = Counter()

      # Category group
      self.categories = defaultdict(list)


   # Add task
   def add_task(self, task_name, category):
      task = {
         "name": task_name,
         "category": category
      }

      # Queue add
      self.queue.append(task)

      # Count update
      self.task_count[category] += 1 

      # Category group
      self.categories[category].append(task_name)

      print("Task Added:", task_name)

   
   # Queue to task process
   def process_task(self):

      if self.queue:

         task = self.queue.popleft()

         print(
            "Processing:",
            task["name"]
         )
      else:
         print("No task available")

   
   # Total task count 
   def show_count(self):
      print("\nTask Count:")

      for category, count in self.task_count.items():
         print(category, ":", count)

   
   # Category wise task
   def show_category(self):
      print("\nCategory Group:")

      for category, tasks in self.categories.items():

         print(
            category,
            "=>",
            tasks
         )



# Object Create
manager = TaskManager()


manager.add_task(
   "Send Email",
   "Email"
)

manager.add_task(
   "Generate Report",
   "Report"
)

manager.add_task(
   "Backup Database",
   "Database"
)

manager.add_task(
   "Send OTP",
   "Email"
)

# Show Queue
print("\nQueue")

print(manager.queue)


# Process Task
manager.process_task()


# Count
manager.show_count()


# Category
manager.show_category()