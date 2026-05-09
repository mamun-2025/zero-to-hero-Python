
print("Hello, World!")

# 1.Indentation 
print("I have no Indentation.")
#   print("I have tab Indentation.")

# 2. Indentation in Conditional Statements
a = 20 
if a >= 18:
   print("GeeksforGeeks")
else:
   print("retype the URL")
print("All Set!")

# 3. Indentation in Loops
j = 1
while(j <= 5):
   print(j)
   j = j + 1 

# 4. Python Comments
# Single Line Comments 
# sample comment
name = "GeeksforGeeks"
print(name) 

# Multiline comment 
# This is a multiline comment 
# Each starts with # 
# This method is efficient and preferred
print("Geeks for Geeks") # Inline comment

# Triple single(''' ''') and triple double(""" """)
'''
This is a multiline comment using triple single quotes
It is commonly used as a workaround.
'''

print("Triple single and double quotes.")

"""
This is another multiline comment 
using triple double quotes.
"""

# 5. Python docstrings()
def docstring():
   """This is a docstring.
   It describes what the function does.
   """
   print("Geeks for geeks tutorial.")

print(docstring.__doc__) # Access the docstring