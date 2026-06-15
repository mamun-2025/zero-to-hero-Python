

## (1).String Comparison Problems
# Problem 1: Equal কিনা
s1 = "apple"
s2 = "apple"

result = s1 == s2
print(result)

# Problem 2: Case-Sensitive Comparison
s1 = "Python"
s2 = "python"

print(s1 == s2)

# Problem 3: Case-Insensitive Comparison
s1 = "Python"
s2 = "python"

print(s1.lower() == s2.lower())

# Problem 4: Lexicographical Comparison
s1 = "abc"
s2 = "abd"

print(s1 < s2)




## (2).Type Conversion Problems
# Problem 5: Number to String
num = 123

s = str(num)

print(s)
print(type(s))

# Problem 6: String Concatenation
num = 123

result = "Number: " + str(num)
print(result)

# Problem 7: String to Integer
text = "123"
result = int(text)

print(result)
print(type(result))

# Problem 8: Sum of Numeric Strings
a = "200"
b = "300"

result = int(a) + int(b)
print(result)



## (3).String to List
# Problem 9: String to list
text = "Python"
chars = list(text)
print(chars)

# Problem 10: Count Characters
text = "GeeksForGeeks"
print(text.count("e"))
print(list(text))
print(len(list(text)))

# Problem 11: Split String
text = "Python Django FastAPI"
words = text.split()

print(words)

# Problem 12: List to sting
text = ["I", "Love", "Coding."]
sentence = " ".join(text)

print(sentence)



## (4). Character Frequency
# Problem 13: Count "a"
text = "banana"
print(text.count("a"))

# Problem 14: Count All Characters
text = "banana"

freq = {}

for char in text:
   freq[char] = freq.get(char, 0) + 1

print(freq)



## (5). String Searching
# Problem 15: First Occurrence
text = "banana"
print(text.find("a"))

# Problem 16: Last Occurrence
text = "banana"
print(text.rfind("a"))

# Problem 18: Word Search
text = "I love Python"
print("Python" in text)



## (6). String Validation
# Problem 19: Email Validation
email = "mamun@gmail.com"

if "@" in email and "." in email:
   print("Valid")
else:
   print("Invalid")

# Problem 20: Username Validation
username = "mamun123"
print(username.isalnum())

# Problem 21: Phone Number Validation
phone = "01964766244"
print(phone.isdigit())

# Problem 22: Password Length Check
password = "abc12345"
if len(password) >= 8:
   print(True)
else:
   print(False)



## (7). String Modification
# Problem 23: Replace Character
text = "banana"
print(text.replace("a", "*"))

# Problem 24: Remove Spaces
text = "I Love Python"
print(text.replace(" ", ""))

# Problem 25: Remove Vowels
text = "Python Programming"

vowels = "aeiou"

result = ""

for char in text:
   if char not in vowels:
      result += char 

print(result)


## (8). String Reversal
# Problem 26: sting reverse
text = "Python"
print(text[::-1])

# Problem 27: Palindrome
text = "madam"
print(text == text[::-1])

# Problem 28: Anagram
s1 = "listen"
s2 = "silent"

print(sorted(s1) == sorted(s2))



## (9). Word Based Problems
# Problem 29: Count Words
text = "I love Python"
print(len(text.split()))

# Problem 30: Longest Word
text = "Python is very powerful language"

words = text.split()

print(max(words, key=len))










# Problem 31: Reverse Word Order
# text = "I love Python"

# words = text.split()

# print(" ".join(words[::-1]))

# Output:

# Python love I
# 12. Pattern Matching
# Problem 32: Starts With
# email = "hello@gmail.com"

# print(email.startswith("hello"))
# Problem 33: Ends With
# email = "hello@gmail.com"

# print(email.endswith(".com"))
# Problem 34: Contains
# text = "Python Django"

# print("Django" in text)
# 13. String Formatting
# Problem 35
# name = "Mamun"
# age = 22

# print(f"My name is {name} and I am {age} years old.")
# Problem 36
# name = "Mamun"
# age = 22

# print("My name is {} and I am {} years old.".format(name, age))
# 14. ASCII Problems
# Problem 37
# print(ord("A"))

# Output:

# 65
# Problem 38
# print(chr(65))

# Output:

# A
# Problem 39: Uppercase → Lowercase Manually
# ch = "A"

# lower = chr(ord(ch) + 32)

# print(lower)

# Output:

# a
# Problem 40: Lowercase → Uppercase Manually
# ch = "a"

# upper = chr(ord(ch) - 32)

# print(upper)

# Output:

# A