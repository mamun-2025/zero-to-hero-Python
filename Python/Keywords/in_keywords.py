
# Python in Keyword
"""
The in keyword in Python is a powerful operator used for membership 
testing and iteration.
It helps determine whether an element exists within a given sequence,
such as a list, string, tuple, set or dictionary.
"""

s = "Geeks for geeks"

if "for" in s:
   print("found")
else:
   print("Not found.")


# Purpose of the in keyword
"""
The in keyword in PYthon serves two primary purposes:
- Membership Testing: To check if a value exists in a sequence 
such as a list, tuple, set, range, dictionary or string.
- Iteration: To iterate through elements of a sequence in a for loop.
"""

# 1. in keyword with if statement
a = ["php", "python", "java"]

if "php" in a:
   print(True)

# 2. in keyword in a for loop
s = "geeksforgeeks"

for char in s:
   if char == "f":
      break
   print(char)

# 3. in keyword with dictionaries
d = {"Mamun": 98,
     "Habib": 95}

if "Mamun" in d:
   print("Mamun's marks are:", d["Mamun"])

# 4. in keyword with sets
vowel = {'a', 'e', 'i', 'o', 'u'}

print('e' in vowel)