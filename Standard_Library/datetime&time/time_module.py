

# 1. time কী?
"""
time module মূলত:

Delay
Execution time measure
Unix timestamp

এর জন্য ব্যবহার হয়।

Import:

import time

"""


# 2. Current Timestamp
import time 

timestamp = time.time()
print(timestamp)
"""
Output:

1783773025.55

এটা হলো:
Unix Timestamp

মানে:
1 January 1970 থেকে এখন পর্যন্ত কত second পার হয়েছে।

Backend এ ব্যবহার:

Token expiry
Cache expiration
Performance measurement
"""

# 3. Program Delay করা
import time 

print("Start")

time.sleep(3)

print("End")



# 4. Code Execution Time Measure
import time 

start = time.time()

for i in range(100000):
   pass 

end = time.time()
print(end-start)
# Backend Optimization এ ব্যবহার হয়।


# Datetime vs time
"""
| datetime                | time               |
| ----------------------- | ------------------ |
| Date + Time নিয়ে কাজ    | Timestamp + Delay  |
| Human readable          | Machine readable   |
| Birthday, Order Date    | Timer, Performance |
| Django model timestamps | System timing      |

"""



### Problem: Function Execution Time Measure
import time 

def execution_time(func):

   def wrapper():
   
      start = time.time()

      func()

      end = time.time()

      print(
         "Execution Time:",
         end - start,
         "seconds"
      )

   return wrapper

@execution_time
def test_function():

   for i in range(100000):
      pass 

test_function()



