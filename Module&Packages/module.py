



#### import
import math 
print(math.sqrt(25))

import random 
print(random.randint(1, 10))



#### from import
from math import sqrt
print(sqrt(36))

from random import randint
print(randint(1, 20))



##### Multiple import
from math import sqrt, ceil, floor

print(sqrt(81))
print(pow(2, 5))
print(ceil(2.7))
print(floor(4.9))


#### import*
# It is not professional
from math import *
print(ceil(3.9))
print(pow(2, 4))
print(sqrt(49))
print(floor(5.4))



##### as keyword
import mathmatics_operations
print(mathmatics_operations.multiply(3, 4))

from mathmatics_operations import multiply
print(multiply(4, 5))

import mathmatics_operations as mo 
print(mo.multiply(5, 6))



##### Function Alias
from mathmatics_operations import multiply as mp 
print(mp(6, 7))



#############################################################################



def create_order(name):
   print(f"Order name: {name}")

if __name__ == "__main__":
   create_order("Laptop")


def connect():
   print("Database Connected.")

if __name__ == "__main__":
   connect()


def show_students(name, age):
   print(f"Name: {name}, Age: {age}")

if __name__ == "__main__":
   show_students("Mamun", 25)


def get_products(name):
   print(f"Product Name: {name}")

if __name__ == "__main__":
   get_products("Mouse")


def deposit(amount):
   print(f"Deposited {amount}tk successfully.")

if __name__ == "__main__":
   deposit("1000")


def add(a, b):
   return a + b

def subtract(a, b):
   return a - b 




import utils