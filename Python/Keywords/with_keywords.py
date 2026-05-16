

# with statement in Python
# Save file handling

## Resource Management Using "with" Statement
# 1. Without "with" (Manual closing)
file = open("example.txt", "r")
try: 
   content = file.read()
   print(content)
finally:
   file.close()
# Note: This code opens "example.txt" in read mode, reads its content, prints it and ensures file is closed using a finally block.

# 2. Using "with" (Automatic closing) - (Reading a file)
with open("example.txt", "r") as file: 
   content = file.read()
   print(content)

# Writing to a file
with open("example.txt", "w") as file:
   file.write("Hello, Python with statement!")



## Replacing Try-Except finally with "with" statement
# 1. Without using "with"
file = open("example2.txt", "w")
try:
   file.write("Hello, Python!")
finally:
   file.close() # Ensure file is closed

# Note: This code opens example.txt in write mode("w"), creating or clearing it. The try block writes "Hello, Python!" and finally ensures the file closes, preventing resource leaks.



## Context Managers and "with" statement
"""
The with statment relies on context managers,
which manage resource allocation and deallocation using two special methods:
- __enter__(): Acquires the resource and returns it.
- __exit__(): Releases the resource when the block exits.
"""
# 1. Custom context manager for file writing
class FileManager:
   def __init__(self, filename, mode):
      self.filename = filename
      self.mode = mode

   def __enter__(self):
      self.file = open(self.filename, self.mode)
      return self.file 
   
   def __exit__(self, exc_type, exc, tb):
      self.file.close()


with FileManager("example3.txt", "w") as file:
   file.write("Hello, custom context manager!")


## Using contextlib Module
# Instead of creating a full class, Python provides the contextlib module to create context managers using functions.
# Function-Based Context Manager
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
   file = open(filename, mode)
   try:
      yield file 
   finally:
      file.close()
      
# Using the generator-based context manager
with open_file("example4.txt", "w") as file:
   file.write("Hello, Mamun!")

# Note: @contextemanager, where open_file() opens a file and yields it for use.
# Ensures automatic file closure with a finally block, even if an exception occurs.
# Writes "Hello, World!" to "file.txt" and the file closes automatically afe4r the block.


## Database Connection Management
import sqlite3

with sqlite3.connect("example.db") as conn:

  cursor = conn.cursor()

  cursor.execute("""SELECT name 
                 FROM sqlite_master 
                 WHERE type='table' AND name = 'users'
               """)
  
  res = cursor.fetchone()

  print("Table Create successfully!" if res else "Table not found")