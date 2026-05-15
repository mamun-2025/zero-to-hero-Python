

# Python None keyword:
"""
None is used to define a null value or Null obeject in Python.
It is not the same as an empty string, a False, or a zero.
It is a data type of the class NoneType object.
"""

# 1. None in Python
def check_return():
   pass 
print(check_return())

# 2. Null Vs None in Python
"""
None- None is asn instance of the NoneType object type.
And it is a particular variable that has no objective value.
While new NoneType objects cannot be generated, None can be assigned to any varaiable.

Null- There is no null in Python, we can use None instead of using null values.
"""

print(type(None))
# print(type(Null))

# 3. Referring to the null object in Python
print(type(None))

# Declaring a varialbe as None:
var = None

if var is None:
   print("Var has a value of None")
else:
   print("Var has a value")