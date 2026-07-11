


### ✅ Problem 1: Project Folder Creator

from pathlib import Path

def create_project_structure():

   folders = [
      "ecommerce",
      "ecommerce/media",
      "ecommerce/statice",
      "ecommerce/logs",
      "ecommerce/uploads"
   ]

   for folder in folders:

      path = Path(folder)

      path.mkdir(
         parents=True,
         exist_ok=True
      )

      print(f"{folder} created.")

create_project_structure()



### ✅ Problem 2: File Checker
from pathlib import Path

def check_file(file_path):

   file = Path(file_path)

   if file.exists():

      print(
         "File exists"
      )

   else:
      print(
         "File not found."
      )

check_file("check.json")



### ✅ Problem 3: Image Folder Scanner
from pathlib import Path

def image_scanner(folder):

   path = Path(folder)

   for file in path.iterdir():

      if file.suffix in [
         ".jpg",
         ".png"
      ]:
         print(file.name)

image_scanner("uploads/profile")



### ✅ Problem 4: Backup Folder Creator
from pathlib import Path

def create_backup_folder():

   backup = Path(
      "backup"
   )

   backup.mkdir(
      exist_ok=True
   )

   print("Backup folder ready.")

create_backup_folder()



### ✅ Problem 4: File Information

from pathlib import Path

def file_information(file_path):

   file = Path(file_path)

   print(
      "Name",
      file.name 
   )

   print(
      "Extension:",
      file.suffix
   )

   print(
      "Parent:",
      file.parent
   )

   print(
      "Size:",
      file.stat().st_size,
      "bytes"
   )

file_information("test.txt")

