# Indentation is used to define blocks of code. It indicates to the Python interpreter that a group of statements belongs to the same block.
# 1. All statements with the same level of indentation are treated as part of the same code blcok.
# 2. Indentation is created using tabs or spaces and the commonly accepted convention is to use four spaces.
# 3. Python expects the indentation level to be consistent within the same block. This inconsistency causes an IndentationError as shown in the below code.
print("I have no Indentation.")
#   print("I have tab Indentation")

# Explanation:
# 1. The first print statement has no indentation, so it is correctly executed.
# 2. The second print statement has tab indentation, but it doesn't belong to a new block of code, that's why it throws IndentationError.

# 1. Indentation in Conditional Statements
# All statements in a conditional block should have same alignment.
# The code below demonstrate how we use indentation to define seperate scopes of if-else statement:
a = 20 
if a >= 18:
   print("GeeksforGeeks....")
else:
   print("retype the URL.")
print("All set !")
# The statements under if and else are indented, forming two distinct blocks. Only one block executes based on the condition. The final print("Done") is outside the conditional structure, so it runs regardless of the condition

# 2. Indentation in Loops
# Indentation defines the set of statements that are executed repeatedly inside a loop. 
j = 1
while(j <= 5):
   print(j)
   j = j + 1 
# Both print(j) and j += 1 are indented and belong to the loop block which executes in each iteration until the condition becomes false.

