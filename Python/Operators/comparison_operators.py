
# Comparison(or Relational) operators compares values. It either returns True or False according to the condition.
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Python Object comparison: "is" vs "=="
# In python, both is and == are used for comparison, but they serve different purposes.
# ==(Equality Operator) = Compares values of two objects.
# is(Identity Operator) = Compares memory location of two objects
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
# a and b are separate list objects with identical values[1, 2, 3]. 
# == checks value equlity and returns True, while memory identity and returns False.


"""
The 'is operator' checks if two variables refer to the same object in memory, rather than just having equal values.
It returns True only if both variables point to the exact same object in memory.
"""
x = [10, 20, 30]
y = x 
print(x is y)
# y is assigned x, meaning both x and y now reference the same object in memory.
# x is y returns True because x and y share the same identity.

"""
The '== operator' checks if two objects contain the same values, 
regardless of whether they are stored in the same memory location.
"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # same values
# a and b are both lists containing [1,2,3], but they are separate objects in memory
# a == b returns True because their values are the same.


"""
is vs == Summary Table

Parameter                            == operator                                    is operator
___________________________________________________________________________________________________________________________________________________________
Name                                 Equality operator                           Identity operator

Functionality                        Checks if values of                         Checks if memory addresses of 
                                     two objects are equal.                      two objects are the same.

Use Case                             Used when we want to compare                Used when we want to check whether two variables 
                                     data stored in objects.                     point to the same object in memory.

Mutable Objects                      Returns True if contents are the same,      Returns False unless both variables point to the same memory location.
(lists, dicts, sets, etc.)           even if they are different objects.

Immutable Objects                    Returns True if values are equal.           May return True due to Python's internal object caching (interning).
(ints, strings, tuples, etc.)


Example 1
[1,2,3] == [1,2,3] → True
[1,2,3] is [1,2,3] → False

Example 2
"hello" == "hello" → True
"hello" is "hello" → True

"""













