
# ayncio in Python
"""
Asyncio is a Python library that is used for concurrent programming,
including the use of async iterator in Python.
It is not multi-threading or multi-processing.
Asyncio is used as a function for multiple Python asynchornous frameworks that provide high-performance network and web servers, database connection libraries, distributed taks queues, etc.
"""

# 1. Asynchornous Programming with Asyncio in Python
"""
In the example below, we'll crate a function and make it asynchorous using the async keyword.
To achieve this, an async keyword is used.
The program will wait for 1 second after the frist print statement is executed 
and then print the next statement and so on. 
Note that we'll make it sleep (or wait) with the help of await asyncio.sleep(1) keyword,
not with time.sleep(). To run the program, we'll have to use the run() function as it is given below.
This asynchoronous approach is a fundamental concept in Python programming and is particularly useful 
when working with async iterators in Python.
"""

import asyncio

async def func():
   print("This is ")
   await asyncio.sleep(1)
   print("asynchronous programming.")
   await asyncio.sleep(1)
   print("and not multi-threading.")

asyncio.run(func())

# 2. Async Event Loop in Python
import asyncio

async def func():

   print("One")
   await asyncio.sleep(1)
   await func2()
   print("four")
   await asyncio.sleep(1)
   print("five")
   await asyncio.sleep(1)

async def func2():
   await asyncio.sleep(1)
   print("two")
   await asyncio.sleep(1)
   print("Three")

asyncio.run(func())


## Using asyncio.create_task(func())

import asyncio 

async def func():
   task = asyncio.create_task(func2())
   print("One")
   # await asyncio.sleep(1)
   # await func2()
   print("four")
   await asyncio.sleep(1)
   print("five")
   await asyncio.sleep(1)

async def func2():
   # await asyncio.sleep(1)
   print("Two")
   await asyncio.sleep(1)
   print("Three")

asyncio.run(func())


# 3. I/O-bound tasks using asyncio.sleep()
"""
In this example, the func1(), func2() and func3() functions 
are simulated I/O-bound tasks using asyncio.sleep().
They each "wait" for a different amount of time to simulate varying levels of work.

When you run this code, you'll see that the tasks start concurrently,
perform their work asynchronously, and then complete in parallel.
The order of completion might vary depending on how the asyncio event loop schedules the tasks.
This asynchronous behaviour is fundamental to understanding how to manage tasks efficiently,
especially when working with async iterators in Python.
"""
import asyncio

async def func1():
   print("function 1 started...")
   await asyncio.sleep(2)
   print("funntion 1 ended.")

async def func2():
   print("function 2 started...")
   await asyncio.sleep(3)
   print("function 2 ended.")

async def func3():
   print("function 3 started...")
   await asyncio.sleep(1)
   print("function 3 ended.")

async def main():
   result = await asyncio.gather(
      func1(),
      func2(),
      func3(),
   )
   print("Main ended..")

asyncio.run(main())





##### Python async
# Example 1:
import asyncio

async def func():
   print("Mamun: Hello, Nondita!")
   await asyncio.sleep(2)
   print("Nondita: Hi, Mamun! ")
   await asyncio.sleep(2)
   print("Mamun: How are you today!")
   await asyncio.sleep(1)
   print("Nondita: I'm good today and You?")
   await asyncio.sleep(1)
   print("Mamun: I'm also fine.")

asyncio.run(func())

# Syntax:
# async def function_name():
#     await some_async_function()


# Running Multiple Tasks Simultaneously
# Example 2:
import asyncio

async def task1():
   print("Task 1 created.")
   await asyncio.sleep(3)
   print("Task 1 finished.")

async def task2():
   print("Task 2 created.")
   await asyncio.sleep(1)
   print("Task 2 finished.")

async def main():
   await asyncio.gather(
      task1(),
      task2()
   )

asyncio.run(main())


# Using Async with File I/O
# Example 3:
import asyncio
import aiofiles

async def write():
    async with aiofiles.open("file.txt", "w") as file:
        await file.write("Hello from Geeks for Geeks!")

async def read():
    async with aiofiles.open("file.txt", "r") as file:
        content = await file.read()
        print(content)

asyncio.run(write())
asyncio.run(read())