

# Level 1: Basic JSON Access (1-10)

# Problem 1: name প্রিন্ট করো।
response = {
   "name": "Mamun",
   "age": 25
}

# যেহেতু এটি একটি সিঙ্গেল লেয়ার ডিকশনারি, সরাসরি Key ধরে ডেটা অ্যাক্সেস করা যাবে।
# পদ্ধতি ১: Direct Key Access (সবচেয়ে কমন)
print(response["name"])

# পদ্ধতি ২: .get() Method (ব্যাকএন্ডে নিরাপদ, কী না থাকলে ক্র্যাশ করে না)
print(response.get("name"))


# Problem 2: name বের করো।
response = {
   "user": {
      "name": "Mamun"
   }
}

# এটি একটি Nested Dictionary (ডিকশনারির ভেতর ডিকশনারি)। প্রথমে user কী-তে ঢুকতে হবে, তারপর name কী-তে।
# পদ্ধতি ১: Chained Key Access
print(response["user"]["name"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("user", {}).get("name"))


# Problem 3: email বের করো।
response = {
   "user": {
      "email": "mamun@gmail.com"
   }
}

# ঠিক আগের প্রবলেমটির মতোই চেইনড ইনডেক্সিং বা কী (Key) ব্যবহার করতে হবে।
# পদ্ধতি ১: Chained Key Access
print(response["user"]["email"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("user", {}).get("email"))


# Problem 4: price বের করো।
response = {
   "product": {
      "price": 50000
   }
}

# পদ্ধতি ১: Chained Key Access
print(response["product"]["price"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("product", {}).get("price"))


# Problem 5: marks বের করো।
response = {
   "student": {
      "marks": 95
   }
}

print(response.get("student", {}).get("marks"))
print(response["student"]["marks"])


# Problem 6: city বের করো।
response = {
   "user": {
      "address": {
         "city": "Madaripur"
      }
   }
}

# এটি ৩ লেয়ারের ডিকশনারি। প্রথমে user $\rightarrow$ তারপর address $\rightarrow$ তারপর city।

# পদ্ধতি ১: Chained Key Access
print(response["user"]["address"]["city"])

# পদ্ধতি ২: Safe .get() Method (রিয়েল প্রজেক্টে ক্র্যাশ এড়াতে এটি সেরা)
print(response.get("user", {}).get("address", {}).get("city"))


# Problem 7: employee name বের করো।
response = {
   "company": {
      "employee": {
         "name": "Rahim"
      }
   }
}

# পদ্ধতি ১: Chained Key Access
print(response["company"]["employee"]["name"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("company", {}).get("employee", {}).get("name"))


# Problem 8: customer email বের করো।
response = {
   "order": {
      "customer": {
         "email": "abc@gmail.com"
      }
   }
}

print(response["order"]["customer"]["email"])
print(response.get("order", {}).get("customer", {}).get("email"))


# Problem 9: age বের করো।
response = {
    "data": {
        "user": {
            "profile": {
                "age": 22
            }
        }
    }
}

# এটি ৪ লেয়ারের ডিকশনারি। ভয় পাওয়ার কিছু নেই, লজিক একই — data ➡️ user ➡️ profile ➡️ age।
# পদ্ধতি ১: Chained Key Access
print(response["data"]["user"]["profile"]["age"])

# পদ্ধতি ২: Safe .get() Method
print(response.get("data", {}).get("user", {}).get("profile", {}).get("age"))


# Problem 10: theme বের করো।
response = {
    "settings": {
        "theme": "dark"
    }
}

print(response["settings"]["theme"])
print(response.get("settings", {}).get("theme"))

# Level 1 (Basic JSON Access) শেষ হলো!



########################################################################################


# Level 2: JSON List Processing (11-20)

# Problem 11 & 12:
