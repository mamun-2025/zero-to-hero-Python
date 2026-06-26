

##### Group 1: Object and Type Checking
#______________________________________

## 1. len()
# যেকোনো সিকোয়েন্স (যেমন: string, list, tuple) বা কালেকশনের 
# মোট উপাদানের সংখ্যা (দৈর্ঘ্য) বের করার জন্য এটি ব্যবহার করা হয়।
print(len("Python"))

fruits = ["apple", "mango", "cherry"]
print(len(fruits))

data = {"name": "mamun",
        "age": 25
}
print(len(data))


numbers = [1, 2, 3, 4]
print(len(numbers))


## 2. type()
# যেকোনো অবজেক্ট বা ভেরিয়েবলটি কোন ডাটা টাইপের (যেমন: int, str, list) 
# তা জানার জন্য এটি ব্যবহার করা হয়।
print(type(10))
print(type("mamun"))
print(type(True))
print(type([1, 2, 3]))
print(type((1, 2, 3, 4)))
print(type({1, 2, 3}))
print(type({"name": "Mamun", "age": 25}))


## 3. isinstance()
# কোনো অবজেক্ট নির্দিষ্ট কোনো ডাটা টাইপ বা ক্লাসের অংশ কিনা তা পরীক্ষা করে True অথবা False রিটার্ন করে। 
# এটি অবজেক্ট অরিয়েন্টেড প্রোগ্রামিংয়ে টাইপ চেকিংয়ের জন্য নিরাপদ।
x = 12
print(isinstance(x, int))

y = "Dhaka"
print(isinstance(y, (int, str, bool)))

z = {"name": "Mamun", "age": 25}
print(isinstance(z, (str, int, bool, set, tuple, list)))

a = [1, 2, 3]
print(isinstance(a, list))






##### Group 2: Type Casting
## 4. int()
# অন্য কোনো ডাটা টাইপকে (যেমন: float বা উপযুক্ত string) পূর্ণসংখ্যায় (Integer) রূপান্তর করে।
x = 10.7
print(int(x))

y = "450"
print(int(y) + 50)


## 5. float()
# পূর্ণসংখ্যা বা উপযুক্ত স্ট্রিং-কে দশমিকে (Floating-point number) রূপান্তর করে।
x = 50
print(float(x))

y = "3.1416"
print(float(y))


## 6. str()
# যেকোনো অবজেক্ট বা সংখ্যাকে স্ট্রিং-এ (Text) রূপান্তর করে।
age = 25
print("My age " + str(age))

my_list = [1, 2]
print(type(str(my_list)))


## 7. bool()
# যেকোনো মানকে Boolean (True বা False)-এ রূপান্তর করে। পাইথনে খালি মান (যেমন: 0, "", [], None) সর্বদা False দেয়, বাকি সব True দেয়।
x = []
print(bool(x))

y = ""
print(bool(y))

z = 0
print(bool(z))

a = None
print(bool(a))

b = -5
print(bool(b))

c = "Python"
print(bool(c))






##### Group 3: Data Structures
## 8. list()
a = (1, 2, 3)
print(list(a))

b = {1, 2, 3}
print(list(b))

c = {"name": "Mamun", "age": 25}
print(list(c))
print(list(c.keys()))
print(list(c.items()))

d = "Mamun" 
print(list(d))

e = (10, 10.5, True, "Python", (1, 2, 3), {1, 2, 3}, {"name": "mamun", "age": 25})
print(list(e))


## 9. tuple()
# একটি নতুন টাপল তৈরি করে (যা পরিবর্তন অযোগ্য বা Immutable)।
num1 = [10, 20, 30]
print(tuple(num1))

num2 = {10, 20, 30}
print(tuple(num2))

num3 = {"name": "mamun", "age": 25}
print(tuple(num3))
print(tuple(num3.keys()))
print(tuple(num3.items()))

num4 = {}
print(tuple(num4))

num5 = "mamun"
print(tuple(num5))

num6 = []
print(tuple(num6))

num7 = ["python", 10, 10.5, (1, 2, 3), {1, 2, 3}, {"name": "mamun", "age": 25}]
print(tuple(num7))


## 10. set()
# একটি নতুন সেট তৈরি করে। সেট ডুপ্লিকেট বা বারবার থাকা মানগুলো স্বয়ংক্রিয়ভাবে বাদ দিয়ে দেয় এবং ইউনিক মান রাখে।
numbers = [1, 2, 3, 2, 2, 4, 5]
print(set(numbers))

numbers2 = {1, 2, 3, 4, 2, 2, 2, 1, 5}
print(set(numbers2))

numbers3 = {"name": "Mamun", "age": 25, "name": "Habib"}
print(set(numbers3))

x = "hello"
print(set(x))


## 11. dict()
# একটি নতুন ডিকশনারি (Key-Value Pair) তৈরি করে।
user = dict(name = "Mamun", age=22)
print(user)

user2 = [("name", "Nondita"), ("age", 25)]
print(user2)

user3 = {("name","mamun")}
print(dict(user3))






##### Group 4: Loops & Sequences
## 12. range()
print(list(range(11)))
print(list(range(1, 11)))
print(list(range(1, 11, 2)))
print(list(range(1, 11, 3)))


## 13. enumerate()
languages = ["Python", "Java", "C++"]
for index, element in enumerate(languages):
   print(f"{index} of element: {element}")


for index, element in enumerate(languages, start=1):
   print(f"{index}:{element}") # ১ থেকে ইনডেক্স শুরু করা


## 14. zip()
# একাধিক লিস্ট বা কালেকশনকে সমান্তরালভাবে জোড়া লাগিয়ে একটি টাপলের সিকোয়েন্স তৈরি করে।
names = ["Rohit", "Sakib", "Tamim"]
rolls = [1, 2, 3]
print(dict(zip(names, rolls)))
print(list(zip(names, rolls)))
print(tuple(zip(names, rolls)))

for name, roll in zip(names, rolls):
   print(f"{name} of roll: {roll}")






##### Group 5: Data & Math operations, Data Analysis and Sorting
## 15. max()
# কোনো কালেকশন বা একাধিক আর্গুমেন্টের মধ্যে সবচেয়ে বড় (সর্বোচ্চ) মানটি বের করে।
numbers = [1, 11, 34, 75, 100]
print(max(numbers))

print(max(1, 11, 32, 53, 35))


## 16. min()
# কোনো কালেকশন বা একাধিক আর্গুমেন্টের মধ্যে সবচেয়ে ছোট (সর্বনিম্ন) মানটি বের করে।
numbers = [1, 11, 34, 75, 100]
print(min(numbers))

print(min([1, 11, 34, 75, 100]))


## 17. sum()
# একটি লিস্ট বা কালেকশনের সমস্ত সংখ্যার যোগফল নির্ণয় করে।
numbers = [1, 11, 34, 75, 100]
print(sum(numbers))

print(sum(numbers, 10))


## 18. sorted()
# মূল লিস্ট বা কালেকশন অপরিবর্তিত রেখে, তার উপাদানগুলোকে ছোট থেকে বড় ক্রমে (Ascending order) সাজিয়ে একটি নতুন লিস্ট তৈরি করে।
unordered = [5, 6, 9, 1]
print(sorted(unordered))

unordered = [5, 6, 9, 1]
print(sorted(unordered, reverse=True))






##### Group 6: Logical Conditional Checking
## 19. any()
# কোনো কালেকশনের যেকোনো একটি উপাদান যদি True হয়, তবে এটি True দেয়। 
# সব উপাদান False হলে এটি False দেয়।
numbers = [1, 3, 5, 8]
print(any(n % 2 == 0 for n in numbers))

flags = [False, False, False, True]
print(any(flags))


## 20. all()
# কোনো কালেকশনের সবগুলো উপাদানকে True হতে হবে, তবেই এটি True দিবে। 
# একটি উপাদানও False হলে আউটপুট হবে False।
flags = [True, True, False]
print(all(flags))

numbers = [4, 7, 12, 5]
print(all(n > 0 for n in numbers))






##### Group 7: Functional Programming
## 21. map()
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

str_nums = ["10", "20", "30"]
int_nums = list(map(int, str_nums))
print(int_nums)


## 22. filter()
# একটি নির্দিষ্ট শর্ত বা ফাংশন ব্যবহার করে কোনো কালেকশন থেকে 
# শুধু সঠিক (True) উপাদানগুলোকে ছেঁকে (Filter) আলাদা করে।
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, nums))

names = ["Mamun", "Nondita", "Habib", "Rajib", "Rudro", "Sanjib"]
last_word = list(filter(lambda word: word.endswith("b"), names))
print(last_word)

long_names = list(filter(lambda name: len(name) > 5, names))
print(long_names)






##### Group 8: File Handling
## 23. open()
file = open("test.txt", "w") # ফাইলে নতুন কিছু লেখা ('w' mode)
file.write("Hello Python")
file.close() # # কাজ শেষে ফাইল বন্ধ করা জরুরি


# ফাইল থেকে ডেটা পড়া ('r' mode) - নিরাপদ পদ্ধতি (with)
with open("test.txt", "r") as file:
   content = file.read()
   print(content)






##### Group 9: Iterators(Iter control)
## 24. iter()
# যেকোনো ইটারেবল অবজেক্টকে (যেমন: list, tuple) একটি Iterator অবজেক্টে রূপান্তর করে, 
# যাতে next() দিয়ে এক এক করে উপাদান নেওয়া যায়।

fruits = ["apple", "mango", "cherry"]
my_iterator = iter(fruits)
print(type(my_iterator))


## 25. next()
# একটি ইটারেটরের পরবর্তী উপাদানটি তুলে আনে। 
# যদি কোনো উপাদান বাকি না থাকে, তবে এটি StopIteration এরর দেয় (যদি না কোনো ডিফল্ট মান সেট করা থাকে)।
fruits = ["apple", "mango", "cherry"]
my_iterator = iter(fruits)

# next() ব্যবহার করে ডাটা তোলা
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator)) আবার কল করলে Error দিবে!

# এরর এড়াতে default মান ব্যবহার করা
print(next(my_iterator, "banana")) # StopIteration (If not default value )






##### Group 10: Code Inspection and help
## 26. dir(
# কোনো অবজেক্ট, ক্লাস বা মডিউলের ভেতরে কী কী মেথড, ফাংশন বা অ্যাট্রিবিউট আছে, 
# তার একটি তালিকা দেখার জন্য এটি ব্যবহৃত হয়।
text = "Python"
print(dir(text)[:3])

# উদাহরণ ১: একটি স্ট্রিং অবজেক্টের সব মেথড দেখা
text = "hello"
# প্রিন্ট করলে upper(), lower(), split() সহ সব মেথডের লিস্ট দেখাবে
print(dir(text)[:3])  # শুরুর ৩টি মেথড দেখাবে বোঝার জন্য


## 27. help()
# পাইথনের যেকোনো ফাংশন, মডিউল বা ক্লাসের অফিশিয়াল ডকুমেন্টেশন বা এটি কীভাবে কাজ করে 
# তা বিস্তারিত জানার জন্য ব্যবহৃত হয়।
# উদাহরণ ১: print ফাংশনের কাজ ও নিয়ম জানা
# help(print) 

# উদাহরণ ২: list এর কাজ জানা
# help(list) # এটি রান করলে ইন্টারাক্টিভ হেল্প গাইড চালু হবে







##### Group 11: Dynamic Attribute Handling
## 28. getattr()
# কোনো অবজেক্টের ভেতরের কোনো অ্যাট্রিবিউট বা ভেরিয়েবলের মান 
# ডাইনামিকভাবে (নাম স্ট্রিং হিসেবে দিয়ে) তুলে আনার জন্য ব্যবহৃত হয়।
class Person:
   name = "Siam"

p1 = Person()
print(getattr(p1, "name"))

# কোনো অ্যাট্রিবিউট না থাকলে এরর এড়াতে ডিফল্ট মান রাখা
# print(getattr(p1, "age"))  আউটপুট: Age পাওয়া যায়নি


## 29. setattr()
# কোনো অবজেক্টের কোনো অ্যাট্রিবিউটের মান ডাইনামিকভাবে সেট বা পরিবর্তন করার জন্য ব্যবহৃত হয়। অ্যাট্রিবিউটটি আগে থেকে না থাকলে নতুন তৈরি হয়।
class Car:
   brand = "Toyota"

# বিদ্যমান মান পরিবর্তন করা
c1 = Car()
setattr(c1, "brand", "BMW")
print(c1.brand)

# নতুন অ্যাট্রিবিউট যোগ করা
setattr(c1, "color", "Red")
print(c1.color)


## 30. hasattr()
# কোনো অবজেক্টের ভেতরে নির্দিষ্ট নামের কোনো অ্যাট্রিবিউট বা মেথড আছে কিনা 
# তা পরীক্ষা করে True/False দেয়।
class Laptop:
   ram = "`16GB"

l1 = Laptop()
print(hasattr(l1, "ram"))

print(hasattr(l1, "price"))






##### Group 12: OOP Decorator and Method
## 31. @property
# কোনো ক্লাসের মেথডকে সাধারণ ভেরিয়েবল বা অ্যাট্রিবিউটের মতো করে অ্যাক্সেস করার সুবিধা দেয় (ব্র্যাকেট () ছাড়াই মেথড কল করা যায়)। 
# একে Getter-ও বলা হয়।


## 32. @classmethod
# এই ডেকোরেটর দিয়ে তৈরি মেথড সরাসরি ক্লাসের সাথে যুক্ত থাকে (অবজেক্টের সাথে নয়)। 
# এর প্রথম প্যারামিটার হিসেবে অবজেক্ট (self) এর পরিবর্তে ক্লাস নিজে (cls) পাস হয়। 
# এটি দিয়ে মূলত ফ্যাক্টরি মেথড বা বিকল্প কনস্ট্রাক্টর বানানো হয়।


## 33. @staticmethod
# এই মেথডগুলো ক্লাসের ভেতরে থাকে ঠিকই, 
# কিন্তু এরা ক্লাস (cls) বা অবজেক্ট (self) কোনোটার কোনো ডেটাই অ্যাক্সেস বা পরিবর্তন করতে পারে না। 
# এটি একটি সাধারণ ফাংশনের মতো, যা লজিক্যালি ক্লাসের সাথে সম্পর্কিত বলে ভেতরে রাখা হয়।


## 34. super()
# ইনহেরিটেন্স (Inheritance)-এর ক্ষেত্রে চাইল্ড বা সাব-ক্লাস থেকে প্যারেন্ট বা মাদার-ক্লাসের মেথড বা কনস্ট্রাক্টর (__init__) কে কল করার জন্য super() ব্যবহার করা হয়।
