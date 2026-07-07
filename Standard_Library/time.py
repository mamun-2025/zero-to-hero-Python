

##### 1. datetime module
from datetime import datetime

now = datetime.now()

print(now)


##### 2. Different date and time
print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)


##### 3. just date
from datetime import date

today = date.today()

print(today)


##### 4. Define date
from datetime import date 

birthday = date(1999, 7, 10)
print(birthday)


##### 5. timedelta
from datetime import timedelta

today = datetime.now()

after_7_days = today + timedelta(days=7)
before_7_days = today - timedelta(days=7)

print(after_7_days)
print(before_7_days)



##### 6. strftime
from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%m-%d-%y"))
print(now.strftime("%y-%m-%d"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%I:%M %p"))



##### 7. String to Date
from datetime import datetime

date_string = "2026-07-06"

date_obj = datetime.strptime(date_string, "%Y-%m-%d")
print(date_obj)



##### 8. time module
import time 

print("Hello, start time")
time.sleep(2)
print("Hello, end time")


##### 9. Unix Timestamp
import time 

print(time.time())


##### 10. Performance Measure
import time 

start = time.perf_counter()
total = sum(range(10000000))
end = time.perf_counter()

print(end - start)


##### 11. User Registration
from datetime import datetime

user = {
   "user": "Mamun",
   "created_at": datetime.now()
}

print(user)


##### 12. OTP Expiry
from datetime import datetime
otp_expiry = datetime.now() + timedelta(minutes=5)
print(otp_expiry)


##### 13. Order Delivery
from datetime import datetime, timedelta
delivery_date = datetime.now() + timedelta(days=3)
print(delivery_date)


##### 14. Login History
from datetime import datetime

print("Last Login:", datetime.now())


##### 15. Execution time
import time 

start = time.perf_counter()
for i in range(1000000):
   pass 
end = time.perf_counter()
print("Excution Time:", end - start)


# ##### 16. Django example 
# from django.utils import timezone

# created_at = timezone.now()
