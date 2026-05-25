
## Python Sets
"""
Set is used to store a collection of items with the following properties.

No duplicate elements. If you try to insert the same item again, it is ignored because sets store only unique values.
An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.
"""
a = set()
print(a)
print(type(a))

s = {10, 50, 20}
print(s)
print(type(s))
# There is no specifc order for set elements to be printed.

## 1. Type Casting
# set() method is used to  convert other data types, such as lists or tuples, into sets.
# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# adding element to the set 
s.add("d")
print(s)

## 2. set() Function in Python
# Syntax: set(iterable)
#Parameters: iterable (optional) - An iterable like list, tuple, string, range or dictionary. If not provided, it creates an empty set.
# Returns: Returns a new set with unique elements.
# Example: In this example, set() is used to create a set from a list containing duplicate values.
num = [1, 2, 2, 3]
s = set(num)
print(s)

num2 = (1, 1, 2, 3)
s = set(num2)
print(s)

s = set(range(1, 8))
print(s)

d = {"x": 1, "y": 2, "z": 3}
s = set(d)
print(s)



## 3. Check unique and Immutable
# Sets cannot have duplicate values. While you cannot modifty the individual elements directly, You can still add or remove elements from the set.
# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
# s[1] = "Hello"
# print(s) - TypeError: 'set' object does not support item assignment



## 4. Frozen Sets
"""
Frozenset is an immutable version of a set. 
Its elements cannot be changed after creation,
but you can perform operations like union, 
intersection and difference. Use frozenset() to create one."""
# Normal set(mutable)
s = set(["a", "b", "c"])
print("Normal set: ", s) 

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen set: ", fs)
"""
Note: Frozensets are immutable, so methods like add() or remove() cannot be used. 
They are also hashable, which allows them to be used as dictionary keys.
"""

# example1:
a = frozenset(["cat", "dog", "lion"])
print("cat" in a)
print("elephang" in a)
"""
Explanation:

frozenset([...]) creates an immutable set and "cat" in 'a' checks membership.
Duplicate values (if any) are automatically removed.
Syntax 
frozenset(iterable)

Parameters: iterable - Any iterable object like list, tuple, set, string or dictionary.
Return Value: Returns a frozenset object.
"""

# example2:
# f = frozenset(["apple", "banana", "orange"])
# print(f)
# f.add("grape") - AttributeError: 'frozenset' object has no attribute 'add'


# example3:
a = ()
f1 = frozenset(a)
print(f1)

b = ["Geeks", "for", "Geeks"]
f2 = frozenset(b)
print(f2)

"""
Explanation:
frozenset(a) creates an empty frozenset.
frozenset(b) removes duplicate "Geeks".
"""

# exmaple4:
d = {"name": "Mamun", "age": 26}
f = frozenset(d)
print(f)
"""
Explanation: frozenset(d) stores only dictionary keys. 
Values are not included in the frozenset.
"""

# example5:
"""
A frozenset supports common set operations such as union, intersection, difference and symmetric difference. 
Although it is immutable, these operations return new frozenset objects without modifying the original sets.
"""
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

c = a.copy()
print(c)

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


# example6:
# Heterogeneous Element
""" 
Sets can store heterogeneous elements in it, i.e, a set can store a mixture of string, integer, boolean, etc datatypes.
"""
s = {"Geeks", "for", 10, 52.7, True}
print(s)






## 5. Methods for Sets
"""
1. Adding elements to Sets: add()
2. Union of Sets: union()
3. Intersection of Sets: intersection()
4. Difference of Sets: difference()
5. Clearing a Set: clear()
"""

#####
#  1. Set add() method in Python
# Syntax: set_name.add(element)
# example1
a = set()
a.add("s")
print(a)

# example2
a = {"apple", "banana", "carrot"}

a.add("Orange")
print(a)

a.add("Orange")
print(a)

"""
Explanation: a.add('s') adds 's' to the set and calling a.add('s') again does not change the set.
"""

# example3
a = {5, 0, 3}

a.add(1)
print(a)

a.add(0)
print(a)
"""
Explanation: a.add(1) inserts 1 into the set and a.add(0) does not change the set because 0 already exists.
"""

# example4
s = {"g", "e", "e", "k", "s"}
t = ("f", "o")
l = ["a", "e"]

s.add(t)
s.update(l)
print(s)
"""
Explanation:
Duplicate 'e' is removed when creating the set and s.add(t) adds the tuple ('f', 'o') as a single element
s.update(l) adds elements of list l individually and duplicate 'e' from l is ignored.
"""





#####
# Union() Function in Set Python
"""
The set.union() method in Python returns a new set containing all unique elements from two or more sets. 
It combines the given sets and automatically removes duplicate values. 
The original sets remain unchanged.
"""
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
"""
Explanation: a.union(b) merges both sets.
Duplicate element 3 appears only once.
Syntax: set1.union(set2, set3)
Parameters: One or more sets to be merged. If no argument is given, it returns a copy of the original set.
Returns: Returns a new set containing all unique elements.
"""
# example1:
a = {2, 4, 5, 6}
b = {4, 6, 7, 8}
c = {7, 8, 9, 10}

print(a.union(b).union(c))
print(a.union(b, c))

# example2:
a = {2, 4, 5, 6}
b = {4, 6, 7, 8}
c = {7, 8, 9, 10}

print(a | b)
print(a | b | c)
"""
Explanation:
a | b performs union of two sets.
a | b | c merges all three sets.
The | operator works the same as union().
"""

# example3:
a = {"ab", "ba", "cd", "dz"}
b = {"cd", "ab", "dd", "za"}
print(a.union(b))
"""
Explanation:
a.union(b) combines both sets.
Common elements 'ab' and 'cd' appear only once.
The result contains all unique strings.
"""


#####
# Intersection() function Python
#####
# Python Set difference()
#####
# Python Set update()


