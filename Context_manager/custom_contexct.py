


# ##### Part 1 — with Statement

# # Step 1 — Problem
# file = open("source.txt", "r")
# print(file.read())
# file.close()

# file = open("source.txt", "r")
# # print(10/0)
# # file.close()
# # তাহলে
# # file.close() আর চলবে না।
# # File Open-ই থেকে যাবে।
# # Resource Leak হতে পারে।


# # Step 2 — পুরনো সমাধান
# file = open("source.txt", "r")
# try:
#    print(file.read())
# finally:
#    file.close()

# # এখানে finally নিশ্চিত করে যে File বন্ধ হবে।
# # কিন্তু Code বড় হয়ে যায়।


# # Step 3 — with Statement
# # Python আমাদের জন্য আরও সহজ উপায় দিয়েছে।
# with open("source.txt", "r") as file:
#    print(file.read())

# # কাজ শেষ হলেই File Automatic Close হয়ে যায়।
# # তোমাকে close() লিখতে হয় না।


# # Step 4 — as
# """
# with open("data.txt") as file:

# এখানে

# open()

# ↓

# File Object

# ↓

# file Variable

# অর্থাৎ

# file.read()

# করতে পারছ কারণ File Object file Variable-এ রাখা হয়েছে।
# """


# # Step 5 — বাস্তব উদাহরণ
# # without with
# file = open("hello.txt", "w") 
# file.write("Hello Mamun")
# file.close()

# # with 
# with open("hello.txt", "w") as file:
#    file.write("Hello Nondita")

# # একই কাজ
# # কিন্তু অনেক Safe।


# # Step 6 — একাধিক File
# with open("hello.txt") as file1, open("source.txt") as file2:
#    print(file1.read())
   
#    print(file2.read())

# # দুটো File-ই Automatic Close হবে।


# # Step 7 — Exception হলেও Close হবে
# with open("hello.txt") as file:
   
#    print(file.read())

#    print(10/0)
   
# # এখানে ZeroDivisionError হবে।
# # তবুও File Close হবে।
# # এটাই with-এর সবচেয়ে বড় সুবিধা।


# # Step 8 — Backend Example
# """
# ধরো User Data Save করছ।

# with open("users.json", "w") as file:

#     file.write(data)

# File ঠিকমতো Close হবে।

# """


# # Step 9 — Django Connection
# """
# Django-তে File Upload Handle করার সময়ও একই ধারণা কাজ করে।

# with open("image.jpg", "wb") as file:
#     ...

# এছাড়া Database Transaction-এও Context Manager-এর ধারণা ব্যবহৃত হয়।

# """


# # Step 10. with আসলে কী করে?
# """
# তুমি লিখো
# with something as obj:
#     ...

# Python ভিতরে ভিতরে এই কাজ করে:
# something.__enter__()

# ↓

# Code Execute

# ↓

# something.__exit__()

# অর্থাৎ with Statement-এর পেছনে __enter__() এবং __exit__() Method কাজ করে।


# অর্থাৎ,

# with

# ↓

# __enter__()

# ↓

# Code Execute

# ↓

# __exit__()
# """
# with open("hello.txt") as file:
#    print(file.read())


# obj = open("hello.txt")
# file = obj.__enter__()
# try:
#    print(file.read())
# finally:
#    obj.__exit__(None, None, None)



# # Step 11: __enter__()
# class MyContext:

#    def __enter__(self):
#       print("Enter Method Called.")
#       return self 
   
#    def __exit__(self, exc_type, exc_value, tracebacke):
#       print("Exit Method Called.")

# with MyContext() as obj:
#    print("Inside with block.")



# # Step 12 — অন্য Object Return করা যায়
# class Demo:

#    def __enter__(self):
#       return "Hello Mamun"
   
#    def __exit__(self, exc_type, exc, tb):
#       print("Finished")

# with Demo() as text:
#    print(text)



# # Step 13 — __exit__()
# """
# def __exist__(self, exe_type, exe_value, traceback):

# এই তিনটি Parameter Exception-এর Information বহন করে।

# Parameter	         Meaning
# exc_type	            কোন ধরনের Exception
# exc_value	         Exception-এর Message
# traceback	         Error কোথায় হয়েছে
# """


# # Step 14 — Exception ছাড়া
# class Demo:

#    def __enter__(self):

#       print("Open")

#       return self
   
#    def __exit__(self, exc_type, exc, tb):
#       print("Close")

# with Demo():
#    print("Working")

# with Demo() as file:
#    print(file)



# # Step 15 — Exception হলে
# class Demo:

#    def __enter__(self):

#       print("Open")

#       return self 
   
#    def __exit__(self, exc_type, exc_value, tb):
#       print(exc_type)
#       print(exc_value)
#       print("Close")

# with Demo():
#    print(10/0)

# # দেখো,
# # Error হলেও __exit__() Call হয়েছে।


# # Step 16: Exception Suppress করা
# """
# যদি
# __exit__()
# এর শেষে

# return True

# দাও
# তাহলে Exception বাইরে যাবে না।
# """
# class Demo:

#    def __enter__(self):

#       return self 

#    def __exit__(self, exc_type, exc, tb):
#       print("Error Handled.")
#       return True
   
# with Demo():
#    print(10 / 0)
# print("Program Continues")

# # এখানে ZeroDivisionError বাইরে আর দেখাবে না।
# # ⚠️ বাস্তবে return True শুধু তখনই ব্যবহার করবে যখন সত্যিই Exception Handle করতে চাও।


# # Step 17: Real Backend Example 
# class Database:

#    def __enter__(self):

#       print("Database Connected")

#       return self 
   
#    def __exit__(self, exc_type, exc, tb):
#       print("Database Closed.")

# with Database():
#    print("Fetching Users.")



# # Step 18: File-এর ভিতরে কী হয়?
# """
# যখন তুমি লিখো

# with open("users.txt") as file:

# আসলে

# open()

# ↓

# __enter__()

# ↓

# File Object

# ↓

# Read / Write

# ↓

# __exit__()

# ↓

# File Close

# """


# # Step 19: Backend Examples
# """
# Database

# with Database():
#     ...

# Redis

# with RedisConnection():
#     ...

# API Client

# with APIClient():
#     ...

# File

# with open("users.json") as file:
#     ...
# """



# ##### 🎯 ছোট Practice (নিজে করার জন্য)
# # FileManager Class বানাও।
# # DatabaseConnection Class বানাও।
# # Logger Class বানাও, যেখানে __enter__()-এ "Start" এবং __exit__()-এ "End" Print হবে।
# # Timer Class বানাও, যেখানে __enter__()-এ Start Time এবং __exit__()-এ End Time Print করবে।


# ##########################################################################################
# ##########################################################################################

# ##### Problem 1: Custom Context Manager Structure
# # প্রায় সব Context Manager-এর Structure এমন হয়।
# class MyCotext:

#    def __enter__(self):

#       print("Resource Open")

#       return self 
   
#    def __exit__(self, exc_type, exc, tb):
      
#       print("Resource Closed.")

# with MyCotext():
#    print("Working....")


# ##### Problem 2: File Manager
# class FileManager:

#    def __init__(self, filename, mode):

#       self.filename = filename
#       self.mode = mode 

#    def __enter__(self):
      
#       print("Open file.")

#       self.file = open(self.filename, self.mode)

#       return self.file
   
#    def __exit__(self, exc_type, exc, tb):
      
#       print("Closing file.")

#       self.file.close()


# with FileManager("context_manager.txt", "w") as file:

#    file.write("Hello mamun")
   


# ##### Problem 3: Database Context Manager
# class Database:

#    def __enter__(self):

#       print("Database Connected.")

#       return self 
   

#    def query(self):
      
#       print("Running query")


#    def __exit__(self, exc_type, exc, tb):
      
#       print("Database closed.")

# with Database() as db:

#    db.query()


# ##### Problem 4: Logger
# class Logger:

#    def __enter__(self):

#       print("====== START =====")

#       return self 

#    def log(self, message):

#       print(message)

#    def __exit__(self, exc_type, exc, tb):
      
#       print("====== END ======")

# with Logger() as logger:

#    logger.log("User Login")

#    logger.log("User Logout.")



# ##### Problem 5: Timer
# import time 
# class Time:

#    def __enter__(self):

#       self.start = time.time()

#       return self 
   
#    def __exit__(self, exc_type, exc, tb):
      
#       end = time.time()

#       print("Execution Time:", end - self.start)


# with Time():

#    time.sleep(2)



# ##### Problem 6: API Client
# class APIClient:

#    def __enter__(self):
      
#       print("API Connected.")

#       return self 
   
#    def get_users(self):

#       print("Fetching Users.")


#    def __exit__(self, exc_type, exc, tb):
      
#       print("API Closed.")

# with APIClient() as api:

#    api.get_users()



# ##### Problem 7: Exception Handling Example
# class Demo:

#    def __enter__(self):
       
#        print("Open")

#        return self 
   
#    def __exit__(self, exc_type, exc, tb):
      
#       print("Close")

#       if exc_type:
#          print("Error:", exc_type.__name__)

#       # print("Error:", exc_type)
#       # print(exc)
#       # return True
   
      

# with Demo():

#    print(10 / 0)



# ##### Backend Examples
# """
# 1.File Upload
# with open("photo.jpg", "wb") as file:
#     file.write(data)

    
# 2.Database
# with Database():

#     save_user()


# 3.Logger
# with Logger():

#     create_order()


# 4.Timer
# with Timer():

#     generate_report()


# 5.API
# with APIClient():

#     get_products()

# """



# ##### Django-তে কোথায় ব্যবহার হয়?
# """
# Django-তে Context Manager-এর ধারণা অনেক জায়গায় ব্যবহৃত হয়, যেমন:

# from django.db import transaction

# with transaction.atomic():
#     # Database operations
#     ...

# এখানে transaction.atomic() একটি Context Manager। 
# যদি Block-এর মধ্যে কোনো Exception হয়, Transaction Rollback হবে। 
# যদি সব ঠিক থাকে, Commit হবে।

# """


#########################################################################################################
#########################################################################################################

##### Step 1 — সমস্যা
"""
আগে আমরা Context Manager বানাতাম এভাবে
class FileManager:

   def __enter__(self):

      ...

   def __exit__(self, exc_type, exc, tb):

      ...

ছোট কাজের জন্য এটাতে অনেক Code লিখতে হয়।

"""


##### Step 2 — contextlib and contexmanager
"""
Python-এর contextlib Module আমাদের সহজভাবে Context Manager বানাতে সাহায্য করে।

from contextlib import contextmanager


@contextmanager = এটি একটি Decorator।
এটি একটি সাধারণ Generator Function-কে Context Manager বানিয়ে দেয়।

"""
from contextlib import contextmanager

@contextmanager
def my_context():
   
   print("Open")

   yield 

   print("Close")

with my_context():
   print("Working...")

"""
ভিতরে কী হচ্ছে?
with

↓

Open

↓

yield

↓

Pause

↓

Working...

↓

Resume

↓

Close

এখানে yield ঠিক সেই জায়গা যেখানে with Block-এর Code Execute হয়।

"""


##### Step 3 — yield-এর আগে ও পরে
from contextlib import contextmanager

@contextmanager
def demo():

   print("Before")

   yield

   print("After")

with demo():

   print("Inside")



###### Step 4: Object Return 
"""
আগে Class-এ

return self

করতাম।

এখানে

yield object

করব।

"""
from contextlib import contextmanager

@contextmanager
def database():

   db = {
      "status": "Connected"
   }

   yield db 

   print("Disconnected")

with database() as db:
   print(db)



##### Step 5 — File Example
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
   file = open(filename, mode)

   yield file

   file.close()

with open_file("hello.txt", "w") as file:

   file.write("Hello contextlib and contextmanager")

# এটি Class Version-এর মতোই কাজ করে।




##### Step 6 — Exception Handle করা
from contextlib import contextmanager

@contextmanager
def demo():

   try:
      print("Open")
      yield
   except Exception as e:
      print("Error:", e)

   finally:
      print("Close")

with demo():

   print(10 / 0)



##### Step 7: Timer
import time 
from contextlib import contextmanager

@contextmanager
def timer():

   start = time.time()

   yield start

   end = time.time()

   print("Time:", end - start)

with timer():

   time.sleep(2)



##### Step 8: Nested Context Manager
from contextlib import contextmanager

@contextmanager
def first():

   print("First Open")

   yield

   print("First Close")


@contextmanager
def second():

   print("Second Open")

   yield 

   print("Second Close")


with first():
   
   with second():

      print("Working.")

"""
   Flow
First Open

↓

Second Open

↓

Working

↓

Second Close

↓

First Close

"""   



##### Step 9: All Example 
##### Backend Example 1 = Database Transaction
"""
from django.db import transaction

with transaction.Atomic():

   # Save user

   # Save profile

   # Save payment

সব সফল হলে Commit হবে।
যদি Error হয়
Rollback হবে।

"""

###### Backend Example 2 = File Uplaod
# with open("photo.jpg", "wb") as file:

#    file.write(image)


from contextlib import contextmanager

@contextmanager
def logger():

   print("Start")

   yield

   print("End")

with logger():
   print("Working")



##### Backend Example 4: API
from contextlib import contextmanager

@contextmanager
def api():

   print("Connect")

   yield

   print("Disconnected")


with api():

   print("Working")



# Class vs @contextmanager
"""
Class	                       @contextmanager
__enter__()                  লাগে	লাগে না
__exit__()                   লাগে	লাগে না
Code বেশি	                 Code কম
Complex	                    Simple
বড় Project-এর জন্য ভালো	 ছোট/মাঝারি Resource Management-এর জন্য ভালো

"""

# Context Manager কোথায় ব্যবহার করবে?
# ✅ File Handling
# ✅ Database Connection
# ✅ Database Transaction
# ✅ Timer
# ✅ Logger
# ✅ API Connection
# ✅ Lock Management
# ✅ Temporary Settings
"""
with transaction.atomic():

with open(...):

with connection.cursor() as cursor:

এগুলোর সবই Context Manager-এর ব্যবহার।
"""

# 🎯 Practice Problems (নিজে করার জন্য)
"""
1.File Context Manager
2.Database Context Manager
3.Logger Context Manager
4.Timer Context Manager
5.API Context Manager
6.JSON File Manager
7.CSV File Manager
8.Temporary Directory Context Manager
9.User Session Context Manager
10.Cache Connection Context Manager

"""