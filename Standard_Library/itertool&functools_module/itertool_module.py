


### 1. itertools কী?
"""
itertools হলো Python-এর built-in module, যেখানে অনেক iterator building tools আছে।

সহজ ভাষায়:

বড় data efficiently process করার জন্য itertools ব্যবহার করি।

এটা memory efficient কারণ অনেক ক্ষেত্রে এটি একসাথে সব data তৈরি করে না, প্রয়োজন অনুযায়ী দেয়।

"""
# import 
import itertools



### 1. count()
# count কী?
# Count একটি infinite counter তৈরি করে।

from itertools import count

counter = count()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# starting value
counter = count(10)

print(next(counter))
print(next(counter))
print(next(counter))


# Order ID generate করতে হবে:
from itertools import count

order_id = count(1000)

print(next(order_id))
print(next(order_id))





### 2. cycle()
# cycle কী?
# কোনো iterable বারবার repeat করে।
from itertools import cycle

colors = cycle(
   ["Red", "Green", "Blue"]
)

print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))


# Backend Example: Round Robin System
"""
Round Robin হলো একটি load balancing algorithm 
যেখানে incoming request গুলো একটার পর একটা করে 
বিভিন্ন server-এর মধ্যে ভাগ করে দেওয়া হয়।

সহজ ভাষায়:
একাধিক server থাকলে সব request যেন একটি server-এর উপর চাপ না ফেলে, 
এজন্য request গুলো পালাক্রমে (turn by turn) distribute করা হয়।
"""
# simple round robin system
from itertools import cycle

servers = [
   "server-1",
   "server-2",
   "server-3"
]

server_cycle = cycle(servers)

requests = [
   "request-1",
   "request-2",
   "request-3",
   "request-4",
   "request-5",
   "request-6",
   "request-7",
   "request-8"
]

for requset in requests:
   server = next(server_cycle)

   print(
      requset,
      "➡️ ",
      server
   )

# Real Mini Load Balancer Class
from itertools import cycle


class LoadBalancer:

    def __init__(self, servers):

        self.servers = cycle(servers)


    def get_server(self):

        return next(self.servers)



servers = [
    "Django-Server-1",
    "Django-Server-2",
    "Django-Server-3"
]


lb = LoadBalancer(servers)


for i in range(10):

    server = lb.get_server()

    print(
        f"Request {i+1} handled by {server}"
    )




### 3. repeat()
# repeat কী?
# একই value বারবার দেয়।
from itertools import repeat

for item in repeat("Mamun is a profession Software Engineer.", 5):
   print(item)

for item in repeat("USER", 5):
   print(item)





### 4. chain()
# chain কী?
# একাধিক iterable একসাথে যুক্ত করে।


from itertools import chain

a = [1, 2, 3]
b = [4, 5, 6]

result = chain(a, b)
print(list(result))

# active users
from itertools import chain
active_users = [
   "Mamun",
   "Rahim"
]

inactive_users = [
   "Karim"
]

all_users = chain(
   active_users,
   inactive_users
)
print(list(all_users))





### 5. combinations()
# combinations কী?
# Order matter করে না।
# Example 1:
# 3 জন থেকে 2 জন নির্বাচন:
from itertools import combinations

team = [
   "A",
   "B",
   "C"
]

result = combinations(
   team,
   2
)

print(list(result))

# example 2:
from itertools import combinations
product = [
   "Laptop",
   "Mouse",
   "Bag"
]

product_bundle = combinations(
   product,
   2
)

print(list(product_bundle))





### 6. Permutations()
# permutations কী?
# Order matter করে।
from itertools import permutations

items = [
   "A",
   "B",
   "C"
]

result = permutations(
   items,
   2
)

print(list(result))




### 7. product()
# product কী?
# সব possible combination তৈরি করে।
from itertools import product

colors = [
   "Red",
   "Blue"
]

sizes = [
   "M",
   "L"
]

result = product(
   colors,
   sizes
)

print(list(result))




### 8. accumulate()
# accumulate কী?
# Running calculation করে।
from itertools import accumulate

numbers = [
   1, 2, 3, 4
]

result = accumulate(numbers)
print(list(result))

##
sales = [
   100,
   200,
   300,
   400
]
print(list(accumulate(sales)))