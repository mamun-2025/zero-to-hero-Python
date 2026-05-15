
# Python keywords
# Keywords in Python are special resrved words that are part of the language itself.
# They define the rules and structure of Python programs which means you cannot use them as names for your variables, functions, classes or any other identifiers.

# 1. Getting List of all Python Keywords
import keyword
print("The list of keywords are: ")
print(keyword.kwlist)
print(keyword.softkwlist)

# 2. Identify Python keywords
# with Syntax Highlighting: Most of IDEs provide syntax-highlight feature. You can see keywords appearing in different color or style.
# Look for SyntaxError: This error will encounter if you have used any keyword incorrectly. Keywords cannot be used as identifiers like variable or a funtion name.

# 3. Keywords as Variables Names
# If we attempt to use a keyword as a variable, Python will raise a SyntaxError. Let's look at an example: 
# for = 10
# print(for)