

# 1. pathlib কী?
"""
pathlib হলো Python-এর built-in module, যা file system path নিয়ে কাজ করার জন্য ব্যবহার করা হয়।

সহজ ভাষায়:
pathlib দিয়ে আমরা file এবং folder-এর location তৈরি, খোঁজা, check, read, write এবং manage করতে পারি।


"""
# os.path বনাম pathlib
# os দিয়ে:
import os

path = os.path.join(
   "media",
   "products",
   "photo.jpg"
)
print(path)

# pathlib দিয়ে:
from pathlib import Path

path = Path("media") / "products" / "photo.jpg"
print(path)
# দেখতে সহজ এবং readable।




# 2. pathlib Import করা
from pathlib import Path
# Path হলো pathlib-এর main class।



# 3. Current Directory বের করা
# Os
os.getcwd()

# Pathlib
from pathlib import Path

current = Path.cwd()
print(current)


# 4. নতুন Path তৈরি করা
from pathlib import Path

path = Path("media/images/prodile.jpg")
print("make_path:", path)



# 5. Path Join করা (খুব গুরুত্বপূর্ণ)
from pathlib import Path

base = Path("media")

file = base / "products" / "phone.jpg"

print("Path_join:", file)


# Backend Example
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = BASE_DIR / "media"
# এটা Django project-এর standard style।




# 6. File Exist Check করা
from pathlib import Path

file = Path("config.json")

print(file.exists())



# 7. File নাকি Folder?
from pathlib import Path

file = Path("song.py")
print(file.is_file())

folder = Path("Standard_Library")
print(folder.is_dir())



# 8. Folder তৈরি করা
"""
import os

os.mkdir("OS_Folder")


from pathlib import Path

folder = Path("Pathlib_Folder")
folder.mkdir()


# Nested Folder তৈরি করা
folder = Path("Nested_folder/profile/images")
folder.mkdir(
   parents=True
)

কিন্তু যদি আগে থেকেই থাকে?

তাহলে:

folder.mkdir(
    parents=True,
    exist_ok=True
)

এটাই Backend এ বেশি ব্যবহার হয়।

"""


# 9. Folder এর ভিতরের File দেখা 
from pathlib import Path

folder = Path("Functions")

for file in folder.iterdir():
   print(file)



# 10. Specific File খোঁজা
from pathlib import Path

folder = Path("Python")

for file in folder.glob("Loop/for_loop.py"):
   print(file)


# Product image management
images = Path("media/products")

jpg_files = images.glob("*.jpg")



# 11. File Read করা
from pathlib import Path

file = Path("data.txt")
content = file.read_text()
print(content)


# 12. File Write করা
from pathlib import Path

file = Path("data.txt")
content_write = file.write_text(
   "Hello Write Data"
)
print(content_write)



# 13. File Delete করা
# from pathlib import Path

# file = Path("practice.py")
# file.unlink()


# 14. Path থেকে Information নেওয়া
file = Path(
   "media/products/phone.jpg"
)

print(file.name)
print(file.suffix)
print(file.parent)



# Real Backend Example 
from pathlib import Path

MEDIA = Path("media")

image = MEDIA / "image" / "mamun.jpg"

if image.exists():
   print("Profile image found.")
else:
   print("No image ")

"""
os vs pathlib (Interview)
os	                                 pathlib
পুরানো style	                      Modern Python style
অনেক function-based	              Object-oriented
path string হিসেবে কাজ করে	         Path object ব্যবহার করে
বেশি code লাগে	                      কম ও readable

"""




######################################################
# Problem 1: Current directory দেখাবে + ভিতরের সব file/folder print করবে
from pathlib import Path

current_path = Path.cwd()
print("Current Directory:", current_path)

for item in current_path.iterdir():
   print("Files and Folder:", item.name)



# Problem 2: structure তৈরি করো:
# from pathlib import Path

# path = Path("Project/media1/image/user/profile.py")

# path.mkdir(
#    parents=True,
#    exist_ok=True
# )

# path = Path("Project/media2/image/user/profile.py")

# path.mkdir(
#    parents=True,
#    exist_ok=True
# )

# print("Folder Structure created:", path)



# Problem 3: একটি folder থেকে: শুধু .py file print করো।
from pathlib import Path

folder = Path("OOP")

for file in folder.iterdir():
   if file.suffix == ".py":
      print(file.name)



# Problem 4: 
from pathlib import Path

file = Path("confix.txt")

file.write_text(
   "DATABASE=postgresql"
)

content = file.read_text()
print(content)



# Problem 5: Backend Level
from pathlib import Path

def create_user_folder(username):

   folder = Path("media") / "users" / username

   folder.mkdir(
      parents=True,
      exist_ok=True
   )

   print("Created:", folder)

create_user_folder("Mamun")



from pathlib import Path

def user_profile(profile):
   
   folder = Path ("project") / "users" / "mamun"/ profile

   folder.mkdir(
      parents=True,
      exist_ok=True
   )

   print("Profile picture created:", folder)

user_profile("profile.jpg")