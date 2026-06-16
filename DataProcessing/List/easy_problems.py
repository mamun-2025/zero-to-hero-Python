

# Problem 1:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[2])


# Problem 2:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[-1])


# Problem 3:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
nums.append(90)
print(nums)


# Problem 4:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
nums.insert(1, 200)
print(nums)


# Problem 5:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
nums.extend([90, 100, 110, 120, 130])
print(nums)


# Problem 6:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
nums.remove(20)
print(nums)


# Problem 7:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
nums.pop(1)
print(nums)


# Problem 8:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
del nums[4]
print(nums)


# Problem 9:
nums = [10, 20, 30, 40, 50, 60, 70, 80]
nums.clear()
print(nums)


# Problem 10:
nums = [10, 20, 30, 40, 50, 60, 70, 80]

for num in nums:
   print(num)


# Problem 11:
nums = [1, 2, 3, 4]

total = 0

for num in nums:
   total += num 

print(total)


# Problem 11:
nums = [1, 2, 3, 4]

product = 1

for num in nums:
   product *= num 

print(product)


# Problem 12:
nums = [10, 20, 300, 40, 50, 70]
print(max(nums))


# Problem 13:
nums = [10, 20, 300, 40, 50, 70]
print(min(nums))


# Problem 14:
nums = [10, 20, 300, 40, 50, 70]
print(nums[1:])


# Problem 15:
nums = [10, 20, 300, 40, 50, 70]
print(nums[1:5])


# Problem 16:
nums = [10, 20, 300, 40, 50, 70]
print(nums[:5])


# Problem 17:
nums = [10, 20, 300, 40, 50, 70]
print(nums[::2])


# Problem 17:
nums = [1, 2, 3, 4, 5, 7]
print(nums[-2:])


# Problem 18:
nums = [10, 20, 30, 40, 50, 70]
print(nums[::-1])


# Problem 19:
squares = [i * i for i in range(1, 11)]
print(squares)


# Problem 20:
nums = [10, 20, 300]
double = [num * 2 for num in nums]
print(double)


# Problem 21:
nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if num % 2 == 0]
print(evens)


# Problem 22:
nums = [1, 2, 3, 4, 5, 6]
odds = [num for num in nums if num % 2 != 0]
print(odds)


# Problem 23:
names = [
   "mamun",
   "rahim",
   "karim"
]

result = [name.upper() for name in names]
print(result)


# Problem 24:
nums = [1, 2, 3, 4, 5, 6]
print(len(nums))


# Problem 25:
nums = [1, 3, 2, 3, 4, 5, 3, 6]
print(nums.count(3))


# Problem 26:
nums = [1, 3, 2, 3, 4, 5, 3, 6]
nums.sort()
print(nums)


# Problem 27:
nums = [1, 3, 2, 3, 4, 5, 3, 6]
nums.sort(reverse=True)
print(nums)


# Problem 28:
nums = [1, 3, 2, 3, 4, 5, 3, 6]
print(9 in nums)


# Problem 29:
users = [
   {"name": "Mamun"},
   {"name": "Rahim"},
   {"name": "Karim"}
]

names = [user["name"] for user in users]
print(names)
print(users)


# Problem 29:
products = [
   {"price": 100},
   {"price": 200},
   {"price": 300}
]

total = sum(product["price"] for product in products)
print(total)


# Problem 30:
emails = [
   "a@gmail.com",
   "b@gmail.com",
   "youtube.com"
]

gmails = [
   email
   for email in emails
   if email.endswith("@gmail.com")
]

print(gmails)