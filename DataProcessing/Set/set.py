

"""

পাইথনের Set ডেটা স্ট্রাকচারটি ব্যাকএন্ড ডেভেলপমেন্ট এবং API ডিজাইনে একটি গেম-চেঞ্জার। 
ডেটা ফিল্টারিং, পারমিশন চেকিং বা ইউনিক ডেটা হ্যান্ডেল করার জন্য এটি ব্যাকএন্ড ইঞ্জিনিয়ারদের সবচেয়ে প্রিয় টুল।

"""

## 1. Set কী?
# সহজ কথায়, Set হলো ইউনিক (Unique) বা অনন্য উপাদানের একটি আনঅর্ডারড (Unordered) কালেকশন।
# List এর মতো Collection, কিন্তু ২টা বড় পার্থক্য আছে:
# list (Duplicate থাকে।)
nums = [1, 2, 2, 3, 3, 4]
print(nums)

# set (Duplicate Automatically Remove হয়ে যায়।)
nums = {1, 2, 2, 3, 3, 4}
print(nums)






## 2. Set কেন দরকার?
# কোনো ডুপ্লিকেট ডেটা রাখে না: সেটের ভেতর একই জিনিস দুবার দিলে সে অটোমেটিক একটি ডিলিট করে দেয়।
# কোনো নির্দিষ্ট ইনডেক্স বা অর্ডার নেই: লিস্টের উপাদান যেমন সাজানো থাকে (০, ১, ২ ইনডেক্স), সেটে তা থাকে না।
emails = [
   "a@gmail.com",
   "b@gmail.com",
   "b@gmail.com",
   "c@gmail.com",
   "a@gmail.com"
]
unique_emails = set(emails)
print(unique_emails)






## 3. Set তৈরি
# এটি একটি সাধারণ সেট
s = {1, 2, 3}

# ❌ ট্র্যাপ: খালি সেট তৈরি করতে গিয়ে s = {} লেখা যাবে না! 
# পাইথনে এটি একটি খালি ডিকশনারি (Dict) তৈরি করে।

# ✅ সঠিক নিয়ম:
empty_set = set()
print(type(empty_set)) # <class 'set'>

s = {1, 2, 3}
print(s)

# empty set (wrong + এটা Dictionary। )
s = {}
print(s)
print(type(s))

# empty tuple
s = ()
print(s)
print(type(s))

# empty set(✅ ঠিক )
s = set()
print(s)
print(type(s))







## 4. Set Indexing Support করে না
# list
nums = [10, 20, 30, 40, 50]
print(nums[0])

"""
set ( TypeError কারণ Set Unordered।)

ইনডেক্সিং ট্র্যাপ:
যেহেতু সেটের কোনো নির্দিষ্ট সিরিয়াল বা অর্ডার নেই, 
তাই তুমি লিস্টের মতো s[0] লিখে ডেটা অ্যাক্সেস করতে পারবে না। 
এটা করলে পাইথন TypeError দেবে।

   nums = {1, 2, 3, 4, 5}
   nums[0]
   print(nums)

"""






## 5. add()
s = {1, 2, 3}
s.add(4)
print(s)

# Duplicate Add করলে?
s = {1, 2, 3}
s.add(3)
print(s) # কিছুই হবে না।


## 6. update()
# একাধিক Item যোগ করে।
s = {1, 2, 3}
s.update([3, 4, 5, 6])
print(s)


## 7. remove()
s = {1, 2, 3}
s.remove(2)
print(s)

# যদি Item না থাকে? (KeyError)
# s.remove(100)
# print(s)


## 8. discard()
# remove এর Safe Version।
# Error হবে না।
s = {1, 2, 3}
s.discard(100)
print(s)


## 9. pop()
# Random Item Remove করে।
s = {10, 20, 30}
value = s.pop()
print(value)
print(s)
# Output যেকোনো হতে পারে।


## 10. clear()
# সব Remove।
s = {1, 2, 3}
s.clear()
print(s)

"""
ডেটা যোগ এবং বিয়োগ (CRUD Operations)
একটি সেটের উপাদান পরিবর্তন করার জন্য ব্যাকএন্ডে নিচের মেথডগুলো সবচেয়ে বেশি লাগে:

add(item): একটি উপাদান যোগ করে। ডুপ্লিকেট যোগ করলে কোনো পরিবর্তন হয় না।

update([list]): একসাথে অনেকগুলো উপাদান যোগ করার জন্য।

remove(item) বনাম discard(item) (খুব ইম্পর্টেন্ট):

remove() ব্যবহার করলে উপাদানটি সেটে না থাকলে কোড ক্র্যাশ করবে (KeyError)।

discard() হলো সেফ ভার্সন। উপাদান না থাকলেও কোড ক্র্যাশ করবে না, চুপচাপ বসে থাকবে।

pop(): সেট থেকে যেকোনো একটি উপাদান র‍্যান্ডমলি ডিলেট করে দেয় (যেহেতু কোনো ইনডেক্স নেই)।

clear(): পুরো সেট খালি করে ফেলে।

"""







## 11. Fast Search(Most Important)
# list
nums = [1, 2, 3, 4, 5]
print(5 in nums)

# set 
nums = {1, 2, 3, 4, 5}
print(5 in nums)
"""
Set অনেক Faster।

Backend Interview-এ প্রায়ই জিজ্ঞেস করে:
Why use set instead of list for lookup?

উত্তর:
Set uses hashing.
Lookup is very fast.

"""






## 12. Union
# সবগুলো সেটকে মার্জ করে একটি ইউনিক সেট বানায়।
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

# method version
print(A.union(B))






## 13. Intersection
# Common Item বের করে।
A = {1, 2, 3}
B = {2, 3, 4}
print(A & B)

# Real Example
python_users = {"Mamun", "Habib", "Nondita"}
django_users = {"Nondita", "Mamun", "Jhon"}

common = python_users & django_users
print(common)







## 14. Difference
# প্রথম সেটে আছে কিন্তু দ্বিতীয় সেটে নেই এমন ডেটা।
A = {1, 2, 3}
B = {2, 3, 4}
print(A - B)






## 15. Symmetric Difference
# দুই Set-এর Uncommon Elements।
A = {1, 2, 3}
B = {3, 4, 5}

print(A ^ B)


## 16. Subset
# একটি সেটের সব উপাদান অন্য সেটে আছে কিনা তা চেক করা।
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

# রিয়েল লাইফ (RBAC - Role Based Access Control): 
# এপিআই-এর সিকিউরিটি বা পারমিশন হ্যান্ডেল করার জন্য এটি ব্যাকএন্ডে প্রতিনিয়ত ব্যবহৃত হয়।

required_permissions = {"read", "write"}
user_permissions = {"read", "write", "delete"}

if required_permissions.issubset(user_permissions):
   print("Access Granted")
else:
   print("403 Forbidden")





## 17. Superset
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))






## 18. Disjoint
# 
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))


"""
ব্যাকএন্ড রুল অব থাম্ব (Rule of Thumb)তুমি যখন রিয়েল প্রজেক্ট করবে, 

তখন সেটের এই ৬টি জিনিস মাথায় রাখলেই চলবে:

1. set() ➡️ ডুপ্লিকেট ডেটা ক্লিন করতে।
2. in ➡️ ঝড়ের গতিতে ডেটা সার্চ বা লুকআপ করতে।
3. intersection () ➡️ কমন ইউজার/প্রোডাক্ট বের করতে।
4. difference() ➡️ এক তালিকায় আছে কিন্তু অন্য তালিকায় নেই এমন ডেটা ফিল্টার করতে।
5. issubset() ➡️ এপিআই পারমিশন বা রোল চেক করতে।
6. discard() ➡️ ক্র্যাশ না করে সেফলি উপাদান রিমুভ করতে।

"""