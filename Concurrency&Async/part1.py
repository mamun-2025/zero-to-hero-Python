

# ##### 1. First Thread
# import threading

# def hello():
#    print("Hello from thread.")

# thread = threading.Thread(target=hello)
# thread.start()



# ##### 2. Main Thread
# import threading

# def hello():
#    print("Hello")

# thread = threading.Thread(target=hello)
# thread.start()

# print("Main Program")



# ##### 3. Multiple Threads
# import threading

# def task(name):
#    print(f"{name} Started.")

# t1 = threading.Thread(target=task, args=("Task-1", ))
# t2 = threading.Thread(target=task, args=("Task-2", ))

# t1.start()
# t2.start()

# ##
# import threading

# def add(a, b):
#    print(a + b)

# ad1 = threading.Thread(target=add, args=(10, 10))
# ad2 = threading.Thread(target=add, args=(10, 20))

# ad1.start()
# ad2.start()




# ##### 4. join()
# import threading
# import time 

# def work():
#    print("Working...")
#    time.sleep(5)
#    print("Done")

# t = threading.Thread(target=work)
# t.start()
# t.join()
# print("Program Finished.")



# ##### 5. Daemon Thread
# import threading
# import time

# def background():
#    while True:
#       print("Running....")
#       time.sleep(1)

# t1 = threading.Thread(target=background, daemon=True)

# t1.start()

# time.sleep(4)

# print("Main Program End")



# ##### 6. Backend Example 1(Email Sending)
# import threading
# import time 

# def send_email():
#       time.sleep(2)
#       print("Email Send")

# email = threading.Thread(target=send_email)

# email.start()

# print("User Registered")




# ##### 7. Backend Example 2(Notification)
# import threading

# def send_notification():
#    print("Notification Send")

# thread = threading.Thread(target=send_notification)

# thread.start()




# ##### 8. Backend Example 3(File Upload)
# import threading
# import time 

# def upload():
#       time.sleep(3)
#       print("Upload completed")
      

# thread = threading.Thread(target=upload)

# thread.start()

# print("Upload continue working...")




