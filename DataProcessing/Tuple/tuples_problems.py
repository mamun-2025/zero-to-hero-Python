

## (1). Basic Tuple
# Problem 1:
t = (10, 20, 30, 40, 50)
print(t[0])

# Problem 2:
t = (10, 20, 30, 40, 50)
print(t[-1])

# Problem 3:
t = (10, 20, "index", 40, 50)
print(t[2])

# Problem 4:
t = (10, 20, 30, 40, 50)
print(len(t))

# Problem 5:
t = (100,)
print(type(t))

# Problem 6:
t = tuple("Python")
print(t)

# Problem 7:
li = [1, 2, 3, 4, 5]
result = tuple(li)
print(result)

# Prolem 8:
t = ("Mamun", 25, 5.0, True, [1, 2, 3], {"name": "Mamun"})
print(t)

# Problem 9:
t = ()
print(t)

# Problem 10:
t = (1, 2, 3)
print(type(t))





## (2). Indexing & Slicing
# Problem 11:
t = (10, 20, 30, 40, 50)
print(t[:3])

# Problem 12:
t = (10, 20, 30, 40, 50)
print(t[3:])

# Problem 13:
t = (10, 20, 30, 40, 50)
print(t[1:4])

# Problem 14:
t = (10, 20, 30, 40, 50)
print(t[::-1])

# Problem 15:
t = (10, 20, 30, 40, 50)
print(t[::2])

# Problem 16:
t = ("Python", "Django", "FastAPI")
print(t[-1])

# Problem 17:
t = tuple("Bangladesh")
res = t[0:6]
print(res)

# Problem 18:
t = tuple("Hello")

# Slice from the third last to the end
print(t[-3:]) 
print(t[-1:]) 
print(t[-4:])

# Slice from the beginning to the third last
print(t[:-3]) #

# Slice from the third last to the second last
print(t[-3:-1])




## (3). Tuple Methods
# Problem 19:
t = (1, 2, 2, 2, 3, 4, 5)
print(t.count(2))

# Problem 20:
t = (10, 20, 30, 40)
print(t.index(30))

t = ("A", "B", "C")
print(t.index("B"))

# Problem 21:
t = ("apple", "banana", "apple", "grape", "apple")
print(t.count("apple"))




## (4). Tuple Unpacking
# Problem 22:
t = ("Mamun", 25)
a, b = t
print(a)
print(b)

# Problem 23:
t = (10,20,30)
a, b, c = t 
print(a)
print(b)
print(c)

# Problem 24:
t = (1, 2, 3, 4, 5)
a, *b, c = t 
print(a)
print(b)
print(c)

# Problem 25:
t = ("Mamun", 25, "Python", "Django")
name, age, *skills = t 
print(name)
print(age)
print(skills)

# Problem 26:
def get_user():
   return ("Mamun", 25)

a, b = get_user()
print(a)
print(b)

# Problem 27:
users = [
   (1, "Mamun"),
   (2, "Rahim"),
   (3, "Karim")
]

for user in users:
   print(user[1])

# Problem 28:
products = (
   ("Pen", 10),
   ("Book", 50),
   ("Bag", 100)
)

total = 0

for product in products:
   total += product[1]

print(total)