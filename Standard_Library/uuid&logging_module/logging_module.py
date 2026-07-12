

### 1. Logging কী?

"""
Logging হলো:
Application-এর গুরুত্বপূর্ণ ঘটনা record করার system।

যেমন:
User login করেছে
Payment success হয়েছে
Error হয়েছে
Server start হয়েছে

কেন print ব্যবহার করব না?

অনেকে করে:
print("User login")

কিন্তু production এ সমস্যা:
কোথায় save হবে?
কখন হয়েছে?
কোন level-এর message?
জানা যায় না।

Logging:
2026-07-11 10:30 INFO User logged in
2026-07-11 10:31 ERROR Payment failed

"""
### 2. logging Import
import logging


### 3. Basic Logging
import logging

logging.warning(
   "Low disk space"
)




### 4. Log Levels
# Logging-এর ৫টি গুরুত্বপূর্ণ level:
"""
| Level    | Meaning               |
| -------- | --------------------- |
| DEBUG    | বিস্তারিত information   |
| INFO     | সাধারণ ঘটনা           |
| WARNING  | সতর্কতা                |
| ERROR    | Error হয়েছে           |
| CRITICAL | বড় সমস্যা             |

"""
# Example:
import logging

logging.debug(
   "Checking user."
)

logging.info(
   "User created."
)

logging.warning(
   "Storage low"
)

logging.error(
   "Database failed"
)

logging.critical(
   "Server crashed"
)



### 5. Logger তৈরি করা
# Professional way:
import logging

logger = logging.getLogger(__name__)

logger.info(
   "Application started"
)




### 6. Log File এ Save করা
import logging

logging.basicConfig(
   filename="app.log",
   level=logging.INFO
)

logging.info(
   "Server started"
)



### 7. Format সেট করা
# Professional log:
import logging

logging.basicConfig(
   filename="app.log",
   level=logging.DEBUG,
   format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info(
   "User registered."
)
logging.debug("Debug message")
logging.info("User login successful")
logging.warning("Low disk space")
logging.error("Database connection failed")



### 8. Exception Logging
import logging

def divide():
   
   try:
      result = 10 / 0
      return result
   
   except Exception:

      logging.exception(
         "Something went wrong"
      )

print(divide())


##
import logging

logger = logging.getLogger(__name__)

def process_payment():

   raise Exception("Card declined")


def payment():

   try:
      process_payment()

   except Exception:

      logger.exception(
         "Payment failed."
      )

payment()


# 5 Example(Most important)
"""
UUID + Logging Mini Backend Practice Solutions

এখানে আমরা ব্যবহার করবো:

uuid → Unique ID তৈরি
logging → Activity track
exception() → Error traceback save
Problem 1
Order Class

Features:

order_id → UUID
product
price
Order create হলে INFO log
Solution:
import uuid
import logging


logging.basicConfig(
    filename="order.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Order:

    def __init__(self, product, price):

        self.order_id = str(uuid.uuid4())
        self.product = product
        self.price = price


        logging.info(
            f"Order created: {self.order_id}"
        )


    def show_order(self):

        print("Order ID:", self.order_id)
        print("Product:", self.product)
        print("Price:", self.price)



order = Order(
    "Laptop",
    80000
)


order.show_order()

Output:

Order ID: 8f3b8c4e-...
Product: Laptop
Price: 80000

order.log

2026-07-12 INFO Order created: 8f3b8c4e...
Problem 2
Login System

Requirement:

Success:

INFO User login success

Wrong password:

WARNING Invalid password
Solution:
import logging


logging.basicConfig(
    filename="login.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


USERNAME = "mamun"
PASSWORD = "12345"



def login(username, password):

    if username == USERNAME and password == PASSWORD:

        logging.info(
            "User login success"
        )

        print("Login successful")


    else:

        logging.warning(
            "Invalid password"
        )

        print("Wrong password")



login(
    "mamun",
    "12345"
)
Problem 3
File Upload System

File name UUID দিয়ে তৈরি করবে।

Example:

image_a82f91bc.jpg
Solution:
import uuid


def upload_file(extension):

    filename = (
        uuid.uuid4().hex[:8]
        +
        extension
    )

    return filename



file_name = upload_file(".jpg")


print(
    "Uploaded:",
    file_name
)

Output:

Uploaded: a82f91bc.jpg

Backend এ:

media/
 |
 └── uploads/
       |
       └── a82f91bc.jpg
Problem 4
Error Handler

Exception হলে:

logger.exception()

ব্যবহার করবে।

Solution:
import logging


logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)



def divide(a,b):

    try:

        result = a / b

        return result


    except Exception:

        logger.exception(
            "Division failed"
        )



divide(10,0)

error.log

ERROR Division failed

Traceback:
ZeroDivisionError: division by zero
Problem 5 (Mini Backend Project)
Order Tracking System

Features:

✅ UUID order ID
✅ Create order
✅ Save logs
✅ Error handling
✅ Track order activity

Complete Project
import uuid
import logging


logging.basicConfig(
    filename="order_tracking.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



class Order:

    def __init__(self, product, price):

        self.order_id = str(uuid.uuid4())

        self.product = product

        self.price = price

        self.status = "Created"


        logging.info(
            f"Order Created {self.order_id}"
        )



    def update_status(self, status):

        self.status = status


        logging.info(
            f"Order {self.order_id} status changed to {status}"
        )



    def show(self):

        print(
            "Order ID:",
            self.order_id
        )

        print(
            "Product:",
            self.product
        )

        print(
            "Price:",
            self.price
        )

        print(
            "Status:",
            self.status
        )



def create_order():

    try:

        order = Order(
            "Phone",
            25000
        )


        order.update_status(
            "Shipped"
        )


        order.show()



    except Exception:

        logging.exception(
            "Order creation failed"
        )



create_order()
Log File:

order_tracking.log

INFO Order Created 7ab92c...

INFO Order 7ab92c... status changed to Shipped
Real Django Mapping:

এই project পরে Django-তে গেলে:

Order Model

id(UUID)
product
price
status
created_at
updated_at

আর:

Order Activity Log

order_id
action
timestamp

হবে।

এটাই production e-commerce order tracking system-এর basic foundation।

"""
"""

এটা হলো production Django project-এর একটি professional logging structure।

logs/
 |
 ├── django.log
 ├── error.log
 └── security.log

প্রতিটি file-এর আলাদা কাজ থাকে।

1. django.log

এখানে সাধারণ Django application-এর log রাখা হয়।

Example:

2026-07-12 20:10:01 INFO User visited home page

2026-07-12 20:10:05 INFO Product list loaded

2026-07-12 20:10:10 INFO Order created

ব্যবহার:

User activity
Request information
General application events
2. error.log

এখানে শুধু error save করা হয়।

Example:

2026-07-12 20:15:22 ERROR Database connection failed

Traceback:
OperationalError: connection refused

ব্যবহার:

Database error
API error
Server crash
Exception debugging
3. security.log

Security related event এখানে রাখা হয়।

Example:

2026-07-12 20:20:01 WARNING Failed login attempt

2026-07-12 20:21:15 WARNING Multiple invalid OTP attempts

2026-07-12 20:22:30 INFO Password changed

ব্যবহার:

Login attempt
Permission denied
Suspicious activity
User authentication events
Django settings.py Example
LOGGING = {

    "version": 1,

    "disable_existing_loggers": False,


    "handlers": {

        "django_file": {

            "class": "logging.FileHandler",

            "filename": "logs/django.log",

        },


        "error_file": {

            "class": "logging.FileHandler",

            "filename": "logs/error.log",

        },


        "security_file": {

            "class": "logging.FileHandler",

            "filename": "logs/security.log",

        }

    },


    "loggers": {


        "django": {

            "handlers": [
                "django_file"
            ],

            "level": "INFO",

        },


        "django.request": {

            "handlers": [
                "error_file"
            ],

            "level": "ERROR",

            "propagate": False,

        },


        "security": {

            "handlers": [
                "security_file"
            ],

            "level": "WARNING",

        }

    }

}
Django View থেকে ব্যবহার:
Normal log:
import logging

logger = logging.getLogger("django")


def home(request):

    logger.info(
        "Home page visited"
    )

Save হবে:

logs/django.log
Error log:
logger = logging.getLogger("django.request")


try:
    payment()

except Exception:

    logger.exception(
        "Payment failed"
    )

Save হবে:

logs/error.log
Security log:
security_logger = logging.getLogger("security")


security_logger.warning(
    "Failed login attempt"
)

Save হবে:

logs/security.log

"""
