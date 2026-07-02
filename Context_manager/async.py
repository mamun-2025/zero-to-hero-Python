

####### 1. Therading Basics
import time 

def task():
   print("Start")
   time.sleep(5)
   print("End")


task()
task()

# Thread Use
import threading
import time 

def task():
   print("Start")
   time.sleep(5)
   print("End")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
# two task running together

# t1.join()
# t2.join()


import threading
import time 

def worker():
   for i in range(5):
      print(i)
      time.sleep(2)

t1 = threading.Thread(target=worker)
t1.start()
t2 = threading.Thread(target=worker)
t2.start()



##### 2. ThreadpoolExecutor
from concurrent.futures import ThreadPoolExecutor
import time 

def task(n):
   time.sleep(2)
   return n * 2

with ThreadPoolExecutor(max_workers=3) as executor:
   results = executor.map(
      task,
      [1,2,3,4,5]
   )
   print(list(results))




###### 3. Multiprocessing Basics
from multiprocessing import Process

def task():
   print("Running")

p1 = Process(target=task)
p2 = Process(target=task)

p1.start()
p2.start()

p1.join()
p2.join()


##### 4. ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor
def square(n):
   return n * n

with ProcessPoolExecutor() as e:
   result = e.map(
      square,
      range(10)
   )
   print(list(result))