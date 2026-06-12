
"""
1. Recursion কী?
Recursion হলো এমন একটি function যা নিজেকেই call করে।

def hello():
   print("Hello")
   hello()

hello()

- এটা Infinite Loop এর মতো চলতে থাকবে এবং শেষে:
RecursionError দেবে।
তাই Recursion-এ অবশ্যই Base Case থাকতে হবে।


2. Recursion-এর ২টা অংশ
1. Base Case
যেখানে recursion থেমে যাবে।
2. Recursive Case
যেখানে function নিজেকে call করবে।

Recursion in Python:
Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem. 
It is commonly used for:
- Breaking problems into smaller subproblems
- Mathmatical calculations like factorial and Fibonacci
- Tree and graph traversal and Divide-and-conquer algorithms

"""

# Example 1: 1 থেকে n পর্যন্ত যোগফল
def total(n):
   result = 0

   for item in range(1, n + 1):
      result += item 
   return result
   
print(total(5))  
# Recursive Way
def total(n):
   if n == 1:
      return 1

   return n + total(n - 1)

print(total(5)) 
"""
Dry run:
total(5)

= 5 + total(4)

= 5 + 4 + total(3)

= 5 + 4 + 3 + total(2)

= 5 + 4 + 3 + 2 + total(1)

= 5 + 4 + 3 + 2 + 1

= 15

"""


# Example 2: Factorial
def factorial(n):
   if n == 0:
      return 1
   else:
      return n * factorial(n-1)

print(factorial(5))
"""
Dry Run:
factorial(5)

= 5 * factorial(4)

= 5 * 4 * factorial(3)

= 5 * 4 * 3 * factorial(2)

= 5 * 4 * 3 * 2 * factorial(1)

= 5 * 4 * 3 * 2 * 1

= 120

"""


# Example 3: String Reverse
def reverse_string(text):
   
   if len(text) == 0:
      return ""
   
   return text[-1] + reverse_string(text[:-1])

print(reverse_string("mamun"))
"""
Dry run:
"mamun"

n + reverse("mamu")

n + u + reverse("mam")

n + u + m + reverse("ma")

n + u + m + a + reverse("m")

n + u + m + a + m

"""


# Example 4: Count Digits
def count_digits(n):
   if n < 10:
      return 1
   
   return 1 + count_digits(n // 10)

print(count_digits(12345))

# iterative version
def count_digit(n):
   count = 0

   while n > 0:
      count += 1
      n //= 10

   return count 

print(count_digit(12345678915162))
"""
Dry run:

12345

1 + count_digits(1234)

1 + 1 + count_digits(123)

1 + 1 + 1 + count_digits(12)

1 + 1 + 1 + 1 + count_digits(1)

5

"""


# Example 5: Power Function
def power(base, exp):

   if exp == 0:
      return 1
   
   return base * power(base, exp-1)

print(power(2, 5))

"""
🟢 Recursive Case
return base * power(base, exp-1)

মানে:
2^5
=
2 × 2^4

আবার:
2^4
=
2 × 2^3

এভাবে চলতে থাকবে।

🟢 Dry Run
ধরি:
power(2, 5)
Call 1
2 * power(2, 4)
Call 2
2 * power(2, 3)
Call 3
2 * power(2, 2)
Call 4
2 * power(2, 1)
Call 5
2 * power(2, 0)
Base Case
power(2, 0)


returns:
1
🟢 Return Phase
এখন stack থেকে ফিরে আসবে।

power(2, 0) = 1

↓
power(2, 1)
= 2 × 1
= 2

↓
power(2, 2)
= 2 × 2
= 4

↓
power(2, 3)
= 2 × 4
= 8

↓
power(2, 4)
= 2 × 8
= 16

↓
power(2, 5)
= 2 × 16
= 32

Recursion Call Tree:
power(2,5)
= 2 × power(2,4)
= 2 × 2 × power(2,3)
= 2 × 2 × 2 × power(2,2)
= 2 × 2 × 2 × 2 × power(2,1)
= 2 × 2 × 2 × 2 × 2 × power(2,0)
= 2 × 2 × 2 × 2 × 2 × 1
= 32

"""
# Iterative version
def power(base, exp):
   result = 1

   for _ in range(exp):
      result *= base 

   return result 

print(power(2, 5))

# Python Built-in way
print(2 ** 5)
print(pow(2, 5))



# Example 6: Fibonacci
def fibonacci(n):

   if n <= 1:
      return n
   
   return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
"""
🟢 Fibonacci Series কী?

Fibonacci Series-এ প্রতিটি সংখ্যা আগের দুইটি সংখ্যার যোগফল।

Series:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

টেবিল:
n	Fibonacci(n)
0	0
1	1
2	1
3	2
4	3
5	5
6	8

তাই:
fibonacci(6)
Output:
8

🟢 Base Case
if n <= 1:
    return n

যদি:
n = 0

তাহলে:
return 0

যদি:
n = 1

তাহলে:
return 1

এগুলোই Fibonacci-এর শুরু।


🟢 Recursive Formula

Fibonacci-এর মূল সূত্র:
F(n)=F(n−1)+F(n−2)

তোমার কোডের এই লাইনটি সেই সূত্রই:
return fibonacci(n - 1) + fibonacci(n - 2)


🟢 Dry Run: fibonacci(6)

প্রথম Call:
fibonacci(6)

হবে:
fibonacci(5) + fibonacci(4)
fibonacci(5)
fibonacci(4) + fibonacci(3)
fibonacci(4)
fibonacci(3) + fibonacci(2)
fibonacci(3)
fibonacci(2) + fibonacci(1)
fibonacci(2)
fibonacci(1) + fibonacci(0)

Base Case:
fibonacci(1) = 1
fibonacci(0) = 0

তাই:
fibonacci(2) = 1 + 0 = 1

এরপর:
fibonacci(3)
= fibonacci(2) + fibonacci(1)
= 1 + 1
= 2

fibonacci(4)
= fibonacci(3) + fibonacci(2)
= 2 + 1
= 3

fibonacci(5)
= fibonacci(4) + fibonacci(3)
= 3 + 2
= 5

fibonacci(6)
= fibonacci(5) + fibonacci(4)
= 5 + 3
= 8

🟢 Call Tree
fibonacci(6)
├── fibonacci(5)
│   ├── fibonacci(4)
│   │   ├── fibonacci(3)
│   │   └── fibonacci(2)
│   └── fibonacci(3)
└── fibonacci(4)
    ├── fibonacci(3)
    └── fibonacci(2)

"""
# Better Iterative Version
def fibonacci(n):
   a, b = 0, 1

   for _ in range(n):
      a, b = b, a + b 

   return a 

print(fibonacci(6))