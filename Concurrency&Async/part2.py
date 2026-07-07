
from concurrent.futures import ThreadPoolExecutor

def square(n):
   return n * n 

with ThreadPoolExecutor() as executor:
   future = executor.submit(square, 5)

print(future.result())