

# import os 

# os.makedirs("Uploads", exist_ok=True)


# Step 1: Curernt working directory
# import os
# print(os.getcwd())

# # Step 2: Directory change
# import os
# os.chdir("Desktop/blog_app")
# print(os.getcwd())

# # Step 3: See the file into folder
# import os 
# print(os.listdir())
# print(os.listdir("Standard_library"))


# # Step 4: make folder
# import os 

# print(os.mkdir("images"))


# # Step 5: Nested folder make
# import os 

# print(os.mkdir("Python/Condition/Yes"))


# # Step 6: Whether folder
# import os 
# check = os.path.exists("My_Roadmap")

# print(check)


# # Step 7: Whether file or folder
# import os 

# print(os.path.isdir("users.json"))

# print(os.path.isfile("My_Roadmap"))


# # Step 8: File Delete
# import os

# os.remove("file1.txt")

# if os.path.exists("users.json"):
#    os.remove("users.json")


# # Step 9: Django Example(os)
# import os 

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# # Step 10: pathlib module (Professional)
# from pathlib import Path

# path = Path("users.json")

# print(path)


# Step 11: Whether file
from pathlib import Path

path = Path("data.json")

print(path.exists())
