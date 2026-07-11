

# 1. datetime কী?
"""
datetime হলো Python-এর built-in module যা date এবং time নিয়ে কাজ করার জন্য ব্যবহার হয়।

সহজ ভাষায়:

Date (দিন/মাস/বছর) এবং Time (ঘণ্টা/মিনিট/সেকেন্ড) manage করার জন্য datetime ব্যবহার করি।

Import
import datetime

কিন্তু professional code-এ সাধারণত:

from datetime import datetime

ব্যবহার করা হয়।

"""



# 2. Current Date এবং Time বের করা
from datetime import datetime

now = datetime.now()
print(now)

# Backend Example
# User Registration:
created_at = datetime.now()
print(created_at)




# 3. শুধু Date নেওয়া 
from datetime import datetime

now = datetime.now()
print(now.date())




# 4. শুধু Time নেওয়া
from datetime import datetime

print(now.time())



# 5. Date-এর আলাদা অংশ বের করা
from datetime import datetime

now = datetime.now()

print(now.day)
print(now.month)
print(now.year)

# Backend example: Monthly Report:

from datetime import datetime

order = datetime.now()

if order.month == 7:
   print("July Order")


# 6. নিজের Date তৈরি করা
from datetime import datetime

date = datetime(
   2026,
   8,
   1
)

print(date)



# 7. Date Format করা (খুব গুরুত্বপূর্ণ)
from datetime import datetime

now = datetime.now()
print(now)
# 2026-07-11 15:20:20.801015 = computer format


# 11 july 2026 = user-friendly
# strftime() = string format time

from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d-%m-%Y")
print("User-friendly time format:", formatted)

# Common Format Codes
"""
| Code | Meaning | Example |
| ---- | ------- | ------- |
| %Y   | Year    | 2026    |
| %m   | Month   | 07      |
| %d   | Day     | 11      |
| %H   | Hour    | 19      |
| %M   | Minute  | 30      |
| %S   | Second  | 25      |

"""
minute = now.strftime("%H:%m")
print(minute)


# 8. String থেকে Date বানানো
from datetime import datetime

date_string = "11-10-2027"
# এটা convert করতে হবে।
# strptime = string parse time

date = datetime.strptime(

  date_string,
  "%d-%m-%Y"
)
print(date)


# 9. Date Difference (Timedelta)
from datetime import datetime

order_date = datetime(2026,7,10)
delivery_date = datetime(2026,7,30)

difference = delivery_date - order_date

print(difference)


# 10. timedelta ব্যবহার
from datetime import datetime, timedelta

now = datetime.now()

otp_expire_time = now + timedelta(minutes=5)
print("OTP_EXPIRE_TIME:", otp_expire_time)


# 11. Compare Date
from datetime import datetime

expiry = datetime(2026,7,15)
today = datetime.now()

if today > expiry:
   print("Expire")
else:
   print("Valid")

# Djnago Example 
# created_at = models.DateTimeField(
#    auto_now_add = True
# )


### Problem: Current date print করো
from datetime import datetime

today = datetime.now()

formatted_date = today.strftime("%d-%B-%Y") # %B → Full Month Name

print(formatted_date)


### Problem: Birth Date 
from datetime import datetime

birth_date = datetime.strptime(
   "10-07-1999",
   "%d-%m-%Y"
)

today = datetime.now()

age = today.year - birth_date.year
print(age)

if (today.month, today.day) < (birth_date.month, birth_date.day):
   age -= 1

print(f"My birthday is {age} years old.")



### Problem: OTP System
from datetime import datetime, timedelta

otp = "123456"

created_time = datetime.now()

print("OTP Created:", created_time)

expire_time = created_time + timedelta(minutes=5)

current_time = datetime.now()

# if created_time <= expire_time:
if current_time <= expire_time:
   print("OTP Valid")
else:
   print("OTP Expired")



### Problem: Order System
from datetime import datetime, timedelta


order_time = datetime.now() - timedelta(days=2)

current_time = datetime.now()

difference = current_time - order_time

days = difference.days 

print(f"Order placed {days} days ago")

