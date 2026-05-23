
# Sequence Data Types
"""
A sequence is an ordered collection of items, which can be of similar or different data types.
Elements in a sequence can be accessed using indexing.
"""

## 1. String
"""
Strings are used to store text data. A string is represented using the str class and can be crated using single, double or triple quotes.
"""
stirng = 'Welcome to the Geeks World'
print(stirng)
print(type(stirng))

# access string with index
print(stirng[0])
print(stirng[-1])

## 2. List
"""
Lists are ordered and mutable collections used to store multiple intems in a single variable.
Elements in a list can be of different data types and are accessed using indexing.
"""
list1 = [1, 2, 3]
print(list1)

list2 = ["Geeks", "for", "Geeks", 4, 5]
print(list2[0])
print(list2[-1])

## Tuple
"""
Tuples are ordered and immutable collections used to store multiple items in a single variable.
Once created, tuple elements cannot be modified and are accessed using indexing.
"""
tuple1 = (1, )
print(tuple1)
print(type(tuple1))

tuple2 = ("Geeks", "for", "Geeks", 1, 2)
print(tuple2[0])
print(tuple2[-1])
