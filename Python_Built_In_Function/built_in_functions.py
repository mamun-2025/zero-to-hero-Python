

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