
## Python Dictionary Data Types
"""
Dictionary is a data structure that stores information in key-value paris.
While keys must be unique and immutable (like strings, numbers, or tuples), 
values can be of any data type and can be duplicated.
This makes dictionaries ideal for accessing data by a 
specific name rather than a numeric position like in lists or tuples.
Dicitionaries are used curly braces {} and key-value paris are separated by a colon : and each pair is separated by a comma.
"""

data = { "name": "Mamun", "age": 26, "city": "Dhaka"}
print(data)

# 1. Creating a Dictionary
a = {"name": "Habib", "age": 30, "city": "New York"}
print(a)

# dict() function can also be used to create a dictionary
"""
Syntax
dict()
dict(mapping)
dict(iterable)
dict(**kwargs)
dict(mapping, **kwargs)
"""
b = dict(name="Habib", age=30, city="New York")
print(b)

c = dict(One="1", two="2", three="3")
print(c)

# Using a iterable of key-value pairs to create a dictionary using dict() function 
d = dict([("name", "Habib"), ("age", 30), ("city", "New York")])
print(d)


# 2. Accessing Dictionary Items 
