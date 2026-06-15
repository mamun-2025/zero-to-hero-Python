

# Problem 1: Length
name = "mamun"
print(len(name))


# Problem 2: Uppercase
text = "geeksforgeeks"
print(text.upper())


# Problem 3: Lowercase
text = "GEEKSFORGEEKS"
print(text.lower())


# Problem 4: Remove Spaces
text = "  Python  "
print(text.strip())


# Problem 5: Replace Word
text = "I love Java."
print(text.replace("Java", "Python"))


# Problem 6: Count Character
text = "madam"
print(text.count("a"))


# Problem 7: Find Position
text = "Hello Python"
print(text.find("Python"))


# Problem 8: Check Start
email = "admin@gmail.com"
print(email.startswith("admin"))


# Problem 9: Check End
file = "profile_picture.jpg"
print(file.endswith("jpg"))


# Problem 10: Split Words
programming = "Python Java C++ JavaScript"
print(programming.split())


# Problem 11: Join Words
words = ["I", "Love", "Python"]
print("-".join(words))


# Problem 12: Is Digit
age = "25"
print(age.isdigit())


# Problem 13: Is Alpha
name = "Mamun"
number = "12345"
print(name.isalpha())
print(number.isalpha())


# Problem 14: Is Alphanumeric
username = "admin123"
print(username.isalnum())


# Problem 15: f-string
name = "mamun"
age = 25
print(f"My name is {name}. And I'm {age} years old.")


# Problem 16: Count Specific Word
text = "Python is very easy and Python is powerful.Python syntax is easy."
print(text.count("Python"))


# Problem 17: Count Spaces
text = "I love Python"
print(text.count(" "))


# Problem 18: Email validator
email = "mamun@gmail.com"
print("@" in email)


# Problem 19: Username Validator
username = "mamun123"
print(username.isalnum())


# Problem 20: Count Words
text = "Python"
print(text.split())
print(len(text))


# Problem 21: Initials
name = "Python is easy to learn."
print(name.split())


# Problem 22: Reverse Word Order
text = "I love Python"
s = text.split()
res = " ".join(s[::-1])
print(res)

name = "Python"
print(name[::-1])



# Problem 23: Hide Gmail.com
email = "mamun@gmail.com"
print(email.replace("mamun", "*****"))



# Problem 24: Title Case
text = "python backend engineer"
print(text.title())



# Problem 25: Username Generator
first = "Mamun"
last = "Bepari"
username = first.lower() + "_" + last.lower()
print(username)


# Problem 26: Check Palindrome
text = "madam"

if text == text[::-1]:
   print(True)
else:
   print(False)

text = "madam"
print(text == text[::-1])


# Problem 27: Count Vowels
text = "Nondita"

count = 0

for char in text:
   if char in "aeiou":
      count += 1

print(count)

# Using sum()
text = "geeksforgeeks"
count = sum(1 for char in text if char in "aeiou")
print(count)



# Problem 28: Count Consonants 
text = "geeksforgeeks"
count = 0

for char in text:
   if char.isalpha() and char not in "aeiou":
      count += 1

print(count)


# Problem 29: Remove All Spaces
text = "  I    love    Python  "
res = text.replace(" ", "")
print(res)

# Alternative
text = "I love Python"
result = "".join(text.split())
print(result)


# Problem 30: Find Longest Word
text = "Python is a easy programming language."

words = text.split()

longest = words[0]

for word in words:
   if len(word) > len(longest):
      longest = word


print(longest)


# Using max(), min()
text = "Python is a easy programming language."

words = text.split()

longest = max(words, key=len)
longest = min(words, key=len)
print(longest)
