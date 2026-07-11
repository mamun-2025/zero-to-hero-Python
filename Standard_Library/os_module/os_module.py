


# 1. os কী?
"""
os হলো Python Standard Library-এর একটি module, যেটা Operating System-এর সাথে কাজ করতে সাহায্য করে।

সহজ ভাষায়:
Python program থেকে computer-এর file, folder, environment variable, path ইত্যাদি control করার জন্য os ব্যবহার করি।

Backend development-এ অনেক কাজে লাগে:

File upload handling
Folder create করা
Environment variable পড়া
Server configuration
File path management
কেন os শিখবো?

ধরো Django project এ:

ecommerce/
│
├── media/
│   └── products/
│        └── phone.jpg
│
├── static/
│
└── settings.py

তোমাকে জানতে হবে:

media folder কোথায়?
file exist করে কিনা?
নতুন folder বানাতে হবে কিনা?
server-এর secret key কোথা থেকে আসবে?

এসব কাজ os দিয়ে করা যায়।

"""



# 2. os import করা
import os



# 3. Current Working Directory
import os 

print(os.getcwd())

location = os.getcwd()
print(location)



# 4. Folder Change করা

# import os 

# print("Before:", os.getcwd())

# os.chdir(r"C:\Users\HP\Desktop\photo")
# এখানে r মানে raw string। Python আর \ কে escape হিসেবে ধরবে না।
# print("After:", os.getcwd())

# os.chdir("C:\\Users\\HP\\Desktop\\photo")
# print("After2:", os.getcwd())



# 5. Folder এবং File List করা
import os 

files = os.listdir()
print(files)




# 6. Folder তৈরি করা
# import os 

# os.mkdir("Os_Folder")




# 7. File/Folder Exist করে কিনা
import os 

result = os.path.exists("data.txt")
print(result)

# User profile image আছে কিনা:
import os 
if os.path.exists("image_path"):
   print("Image Found")

else:
   print("No Image")




# 8. File নাকি Folder?
import os 

print(os.path.isfile("song.py"))
print(os.path.isdir("song.py"))

print(os.path.isdir("Functions"))
print(os.path.isfile("Functions"))




# 9. File Delete করা
# import os 

# os.remove("file.txt")




# 10. Path Join করা (খুব গুরুত্বপূর্ণ)
folder = "media"
file = "photo.jpg"

path = folder + "/" + file 
print(path)
"""
কিন্তু সমস্যা আছে।

Windows:

media\photo.jpg

Linux:

media/photo.jpg

তাই:

import os 

folder= "media"
subfolder = [
   "image",
   "product"
]

for sub in subfolder:
   path = os.path.join(
      folder, 
      sub
   )
   os.makedirs(
      path,
      exist_ok=True
   )

print("Created:", path)

"""


# Django example 
# MEDIA_ROOT = os.path.join(
#    BASE_DIR,
#    "media"
# )



#############################################################
# Problem 1: Current folder দেখাবে এবং সব file দেখাবে
import os 

# Current working directory
current_folder = os.getcwd()
print("Current Folder:", current_folder)

# সব file এবং folder দেখাবে
items = os.listdir()
print("\nFiles and Folders:")

for item in items:
   print(item)


# Problem 2: backend_files folder তৈরি করবে যদি আগে থেকে না থাকে
import os 

folder_name = "backend_files"

if not os.path.exists(folder_name):
   os.mkdir(folder_name)
   print("Folder Created")
else:
   print("Folder Already Exists")



# Problem 3: config.json file আছে কিনা check করবে
import os 

file_name = "config.json"

if os.path.exists(file_name):
   print("Congfig.josn exists")
else:
   print("Config.json not found.")



# Problem 4: os.path.join() দিয়ে path বানাবে
import os 

path = os.path.join(
   "media",
   "products",
   "mobile.jpg"
)

print(path)
"""
Windows:
media\products\mobile.jpg

Linux:
media/products/mobile.jpg

এটাই os.path.join() এর সুবিধা।
"""


# Problem 5: (Backend Thinking)
import os 

folders = [
   "uploads",
   "uploads/profile",
   "uploads/products"
]

for folder in folders:
   if not os.path.exists(folder):
      os.mkdir(folder)
      print(f"{folder} Created.")
   else:
      print(f"{folder} already exists.")



# # Professional Version (Backend Style)
"""

import os 

base_folder = "images"

sub_folders = [
   "profile",
   "photo"
]

for subfolder in sub_folders:
   path = os.path.join(
      base_folder,
      subfolder
   )

   os.makedirs(
      path,
      exist_ok=True
   )
   
   print("Created:", path)

"""



