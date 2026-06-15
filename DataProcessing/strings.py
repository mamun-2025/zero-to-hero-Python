

"""
Backend Developer-এর জন্য Top 15 String Methods:
এই ১৫টা সবচেয়ে গুরুত্বপূর্ণ:

len()
lower()
upper()
strip()
replace()
split()
join()
find()
count()
startswith()
endswith()
isdigit()
isalpha()
isalnum()
f-string

"""
"""
Strings are sequence of characters written inside quotes. 
It can include letters, numbers, symbols and spaces.
Python does not have a separate character type.
- A single character is treated as a string of length one.
- Strings are commonly used for text handling and manipulation.

"""

# Step 1: String কী?
# String = Characters-এর Collection

name = "Mamun"
print(name)
"""
Memory:

M  a  m  u  n

এগুলো একসাথে মিলে String।

"""
# String-এর Data Type
name = "Mamun" 
print(type(name))


# Step 2: String Create করা
# single quote
a = 'GFG'

# double quote
b = "GeeksForGeeks"
print(a)
print(b)

# single quote and double quote explanation
text = "I'm Mamun."

# text = 'I'm Mamun' 
# Error , Because Python ভাববে: 'I' এখানেই String শেষ।


# Step 3: Multi Line String
msg = """

Hello
I am Mamun.
Learning Python.

"""
print(msg)

str = '''

I am learning 
Python string on GeeksforGeeks.

'''
print(str)


# Step 4: Indexing 
# Most Important
# Every character have number of python string.
s = "Python"
"""
Character

P  Y  T  H  O  N

Index

0  1  2  3  4  5

"""

# Accessing Character
# Positive Indexing Character
s = "Python"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

# Negative Indexing Character
"""
ডান দিক থেকে গণনা।

P  Y  T  H  O  N

-6 -5 -4 -3 -2 -1

"""
s = "Python"
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])

# Indexing Error
s = "Python"
# print(s[10])
# IndexError : string index out of range 
# কারণ Index 10 নেই।


# Step 5: String Slicing 
# Syntax: string[start:end]
s = "Python"
print(s[1:4])
"""
Memory

P Y T H O N
0 1 2 3 4 5

Python নেয়:
Start = 1

Y
T
H

Stop before 4
Output: YTH

Rule: Start Included / End Excluded

"""
s = "PYTHON"
print(s[0:3])

# Slicing Shortcuts
s = "PYTHON"
print(s[:3]) # (s[0:3]) Equivalent 

s = "PYTHON"
print(s[2:]) # (s[2:End]) = (s[2:6]) = Equivalent


# Step 6: Reverse String
s = "PYTHON"
t = "GEEKSFORGEEKS"
print(s[::-1])
print(t[::-1])
 
"""
Start = End
Step = -1
Move Backward

"""


# Step 7: Loop Through String
t = "Python"
for char in t:
   print(char)

s = "ABCDE"
for char in s:
   print(s)


# Step 8: String Immutable
# Most Important Concept
# String পরিবর্তন করা যায় না।

"""
s = "ABC"
s[0] = "X"
print(s) 

TypeError: String object does not support item assignment

"""
# Correct Way
s = "ABC"
s = "X" + s[1:]
print(s)

# List mutable 
# List পরিবর্তন করা যায়
l = [1, 2, 3, 4, 5]
l[0] = 15
print(l)


# Step 9: Len()
length = "GeeksForGeeks"
print(len(length))


# Step 10: upper() lower()
u = "python"
print(u.upper())

l = "PYTHON"
print(l.lower())


# Step 11: strip()
# Extra Space Remove
s = "   Python   "
print(s)
print(s.strip())


# Step 12: replace()
t = "My name is Mamun."
print(t.replace("Mamun", "Nondita"))

r = "I lvoe Java."
print(r.replace("Java", "Python"))


# Step 13: Concatenation
# String Join করা।
s1 = "Mamun"
s2 = "Bepari"

print(s1 + " " + s2)


# Step 14: Repetition
rep = "Hello "
print(rep * 5)
print("Hi " * 3)


# Step 15: f-strings
# Backend huge use.
name = "Mamun"
age = 25

print(f"My name is {name}. And I'm {age} years old.")


# step 16: format()
# Syntax: string.format(value1, value2, ...)

# single placeholder
a = "Python"
msg = "{} is a easy programming language.".format(a)
print(msg)

b = 25
print("Hello, I am {} years old.".format(b))

print("{}, a platform for coding enthusiasts.".format("GeeksforGeeks"))

# multiple placeholder
# Syntax: "{} {}".format(value1, value2, ...)
a = "Mamun"
b = 25

msg = "My name is {0} and I am {1} years old.".format(a, b)
print(msg)

str = "{} is a {} science portal for {}".format("GeeksforFGeeks", "computer", "geeks.")
print(str)

print("This is {} {} {} {}.".format("One", "two", "three", "four"))



# Step 17: split()
text = "Python Django FastAPI"
print(text.split())
# Backend-এ JSON, CSV, User Input parse করতে খুব লাগে।



# Step 18: join()
# Syntax: separator.join(iterable)
words = ["Python", "is", "awesome."]
print(" ".join(words))

t = ("Learn", "Python", "Fast")
print("-".join(t))

# sets are unordered, the result string may appear in any order, such as "fun is Python" or "Python is fun" etc.
s = {"Python", "is", "fun"}
res = " ".join(s)
print(res) 

# "
d = {"Geek": 1, "for": 2, "Geeks": 3}
res = "_".join(d)
print(res)



# Step 19: find()
# Syntax: text.find(substring, start, end))

text = "Hello Python"
res = text.find("Python")
print(res)

s = "Welcome to GeekforGeeks!"
index = s.find("GeekforGeeks")
print(index)

t = "abc  abc  abc"
res = t.find("abc")
print(res)


# find() vs index()
# find() returns the index or -1 if not found.
# index() same as find(), but raises a ValueError if not found.
text = "Python is fun"
print(text.find("python"))

text = "Python is fun"
# print(text.index("python"))


# Step 20: starswith()
"""
Syntax
string.startswith(prefix[, start[, end]])

Parameters:

prefix: A string or a tuple of strings to check at the start.
start (optional): Index to start checking from.
end (optional): Index to stop checking.
Return Type: The method returns a Boolean:

True if the string starts with the specified prefix.
False if it does not.

"""
# Basic Prefix
email = "admin@gmail.com"
print(email.startswith("admin"))
print(email.startswith("@gmail"))

# Using start Parameter
s = "GeeksforGeeks"
res = s.startswith("for", 5)
print(res)

# Using start and end Parameters 
s = "GeeksforGeeks"
print(s.startswith("for", 5, 8))

# Checking Multiple Prefixes
s = "GeeksforGeeks"
res = s.startswith(("Geeks", "G"))
print(res) 


# Step 21: endswith()
"""
Syntax of endswith() Method
str.endswith(suffix, start, end)

Parameters: 
suffix: Suffix is nothing but a string that needs to be checked. 
start: Starting position from where suffix is needed to be checked within the string. 
end: Ending position + 1 from where suffix is needed to be checked within the string.
Return:
Returns True if the string ends with the given suffix otherwise return False.
Note: If start and end index is not provided then by default it takes 0 and length -1 as starting and ending indexes where ending index is not included in our search.
"""
s = "Geeksforgeeks"
res = s.endswith("geeks")
print(res)

# Using endswith() with Tuple of Substrings
s = "geeksforgeeks"
res = s.endswith(("geeks", "com", "org"))
print(res) # This will print True because 'geeks' is one of the options.

# Using endswith() with Start and End Parameters
s = "geeksforgeeks"
res = s.endswith("geeks", 5, 15)
print(res) # This will print True because 'geeks' is found between position 5 and 15.

# Validating File Extensions
f = "Profile_picture.jpg"
if f.endswith((".jpg", ".png")):
   print("File is valid")
else:
   print("Invalid file type!")


# Step 22: count()
text = "banana"
print(text.count("a"))

# Finding Character Frequency in String
s = "GeeksforGeeks"
res = s.count("e")
print(res)

# Counting Words in String
s = "Python is fun and Python is easy and Python is powerful."
print(s.count("Python"))

# Count Substring Occurrences with Start and End parameter
s = "apple banana apple grape apple"
substring = "apple"

res = s.count(substring, 1, 20)
print(res)



# Step 23: isdigit()
age = "25"
print(age.isdigit())



# Step 24: isalpha()
name = "@hello"
print(name.isalpha())



# Step 25: isalnum()
# Empty String
s = ""
res = s.isalnum()
print(res)

# String with Non-Alphanumeric characters
n = "1234 mmm"
print(n.isalnum())

# String with Only Letters
username = "mamun"
print(username.isalnum())

