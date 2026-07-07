

## Problem 1: Read a file safely
try:
   with open("notes.txt", "r") as file:
      content = file.read()
      print(content)
except FileNotFoundError:
   print("File not found.")




## Problem 2: Write into a file safely
try:
   with open("output.txt", "w") as file:
      file.write("Hello Mamun")
      print("File written successfully.")
except Exception as e:
   print("Error:", e)




## Problem 3: Append data into a file
try:
   with open("output.txt", "a") as file:
      file.write("\nHello Nondita.")
      print("New line added successfully.")
except Exception as e:
   print("Error:", e)




## Problem 4: Count total lines in a file
try:
   with open("output.txt", "r") as file:
      lines = file.readlines()
      print("Total lines:", len(lines))
except FileNotFoundError:
   print("File not found.")




## Problem 5: Only first line read
try:
   with open("output.txt", "r") as file:
      first_line = file.readline()
      print("First Line:", first_line)
except FileNotFoundError:
   print("File not found.")




## Problem 6: Read numbers from file and calculate sum
total = 0
try:
   with open("numbers.txt", "r") as file:
      for line in file:
         line = line.strip() # new line / extra spaces remove
         try:
            num = int(line)
            total += num 
         except ValueError:
            pass 
   print("Sum:", total)

except FileNotFoundError:
   print("File not found")




## Problem 7: Copy content from one file to another file.
try:
   with open("source.txt", "r") as file:
      content = file.read()
   
   with open("backup.txt", "w") as file:
      file.write(content)

   print("File copied successfully.")
except FileNotFoundError:
   print("Source file not found.")
except Exception as e:
   print("Error:", e)

   
   

## Problem 8: Count words in a file 
try:
   with open("test.txt", "r") as file:
      content = file.read()
      words = content.split()
      print("Total words:", len(words))
except FileNotFoundError:
   print("File not found.")


   

## Problem 9: Save user input into file
name = input("Enter your name: ")
try:
   with open("file.txt", "a") as file:
      file.write(name + "\n")
   print("Name saved successfully.")
except Exception as e:
   print("Error:", e)




##### Problem 10: Use try + except + else + finally
try:
   with open("source.txt", "r") as file:
      content = file.read()
except FileNotFoundError:
   print("File not found.")
else:
   print("File Content:")
   print(content)
finally:
   print("Done")




##### Problem 11: Count only valid integers from a file
count = 0
try:
   with open("numbers.txt", "r") as file:
      for line in file:
         line = line.strip()

         try:
            int(line)
            count += 1
         except ValueError:
            pass 
   print("Valid integers:", count)

except FileNotFoundError:
   print("File not found.")




##### Problem 12: Sum only valid floats from a file
total = 0
try:
   with open("numbers.txt", "r") as file:
      for line in file:
         line = line.strip()

         try:
            price = float(line)
            total += price 
         except ValueError:
            pass 

   print("Total:", total)

except FileNotFoundError:
   print("File not found.")




##### Problem 13: Find the largest valid number from a file
numbers = []
try:
   with open("numbers.txt", "r") as file:
      for line in file:
         line = line.strip()

         try:
            num = int(line)
            numbers.append(num)
         except ValueError:
            pass
   if numbers:
      print("Largest:", max(numbers))
   else:
      print("No valid numbers found")

except FileNotFoundError:
   print("File not found.")




##### Problem 14: Find the lowest valid numbers from a file.
numbers = []
try:
   with open("numbers.txt", "r") as file:
      for line in file:
         line = line.strip()

         try:
            num = int(line)
            numbers.append(num)
         except ValueError:
            pass

   if numbers:
      print("Lowest:", min(numbers))
   else:
      print("No valid numbers found.")

except FileNotFoundError:
   print("File not found.")




##### Problem 15: Saved only non-empty user inputs into a file
try:
   with open("numbers.txt", "a") as file:
      for _ in range(3):
         name = input("Enter name: ").strip()

         if name:
            file.write(name + "\n")
   
   print("Valid names saved successfully.")

except Exception as e:
   print("Error:", e)




##### Problem 16: Read a file and count how many lines are empty
empty_count = 0

try:
   with open("numbers.txt", "r") as file:
      for line in file:
         if line.strip() == "":
            empty_count += 1
   print("Empty lines:", empty_count)
except FileNotFoundError:
   print("File not found.")




##### Problem 17: Parse comma-separated numbers from a file
try:
   with open("data.txt", "r") as file:
      content = file.read().strip()

   parts = content.split(",")
   total = 0

   for item in parts:
      item = item.strip()

      try:
         total += int(item)
      except ValueError:
         pass 
   print("Total:", total)

except FileNotFoundError:
   print("File not found.")




##### Problem 18: Find duplicate lines in a file
seen = set()
duplicates = set()

try:
   with open("emails.txt", "r") as file:
      for line in file:
         email = line.strip()

         if not email:
            continue

         if email in seen:
            duplicates.add(email)
         else:
            seen.add(email)
   print("Duplicate emails:", duplicates)

except FileNotFoundError:
   print("File not found.")




##### Problem 19: Create a report file from valid numbers
marks = []

try:
   with open("marks.txt", "r") as file:
      for line in file:
         line = line.strip()

         try:
            mark = int(line)
            marks.append(mark)
         except ValueError:
            pass 
   if not marks:
      print("No valid marks found.")
   else:
      total = sum(marks)
      average = total / len(marks)

      with open("report.txt", "w") as report:
         report.write(f"Total: {total}\n")
         report.write(f"Average: {average}\n")
      print("Report created successfully")

except FileNotFoundError:
   print("marks.txt file not found.")
except Exception as e:
   print("Error:", e)




##### Problem 20:
# 1. valid integer read from file
numbers = []
try:
   with open("numbers.txt", "r") as file:
      for line in file:
         line = line.strip()
         try:
            num = int(line)
            numbers.append(num)
         except ValueError:
            pass 
   print("Numbers is valid.", numbers)
except FileNotFoundError:
   print("File not found.")

# 2. comma-separated values parse
try:
   with open("data.txt", "r") as file:
      content = file.read().strip()

   parts = content.split(",")
   total = 0
   for item in parts:
      item = item.strip()

      try:
         total += int(item)
      except ValueError:
         pass 
   print("Total:", total)

except FileNotFoundError:
   print("File not found.")


# 3. duplicate detect using set
seen = set()
duplicates = set()

try:
   with open("emails.txt", "r") as file:
      for line in file:
         email = line.strip()

         if not email:
            continue

         if email in seen:
            duplicates.add(email)
         else:
            seen.add(email)
   print("Duplicate emails:", duplicates)

except FileNotFoundError:
   print("File not found.")





##### Problem 21: All line read from file and print according to line number
try:
   with open("source.txt", "r") as file:
      for index, line in enumerate(file, start=1):
         print(f"{index}: {line.strip()}")
except FileNotFoundError:
   print("File not found.")
except Exception as e:
   print("Error:", e)





##### Problem 22: Find the longest line from a file:
try:
   with open("source.txt", "r") as file:
      lines = file.readlines()

      if lines:
         longest_line = max(lines, key=len)
         print("Longest Line:", longest_line.strip())
      else:
         print("File is empty.")
except FileNotFoundError:
   print("File not found.")
except Exception as e:
   print("Error:", e)





##### Problem 23: All line alphabetically sort from a file then saved new file
try:
   with open("output.txt", "r") as file:
      lines = file.readlines()

   lines = [line.strip() for line in lines]
   lines.sort()

   with open("sorted_notes.txt", "w") as file:
      for line in lines:
         file.write(line + "\n")
   
   print("Sorted lines written to successfully for sorted_notes.txt file.")

except FileNotFoundError:
   print("Source file not found.")
except Exception as e:
   print("Error:", e)





##### Problem 24: Copy one to another file
try:
   with open("source.txt", "r") as file:
      content = file.read()

   with open("copy.txt", "w") as file:
      file.write(content)

   print("File copied successfully.")

except FileNotFoundError:
   print("File not found.")
except Exception as e:
   print("Error:", e)





##### Problem 25: two file merge then write three file
try:
   with open("file1.txt", "r") as file:
      content1 = file.read()

   with open("file2.txt", "r") as file:
      content2 = file.read()

   with open("merged.txt", "w") as file:
      file.write(content1)
      file.write("\n")
      file.write(content2)
   
   print("Files merged successfully.")

except FileNotFoundError:
   print("Files was not found.")
except Exception as e:
   print("Error:", e)





##### Problem 26: Count a specific word from a file
word_count = "Python"
try:
   with open("output.txt", "r") as file:
      content = file.read()

   count = content.count(word_count)
   print(f"{word_count} appears {count} times.")

except FileNotFoundError:
   print("File not found.")
except Exception as e:
   print("Error:", e)



   
##### Problem 27: CSV-like text file from data read then total
total = 0

try:
   with open("products.txt", "r") as file:
      for line in file:
         name, price = line.strip().split(",")
         total += int(price)
   
   print("Total Price:", total)

except FileNotFoundError:
   print("File not found.")

except ValueError:
   print("Data format error in file.")

except Exception as e:
   print("Error:", e)





##### Problem 28: File numbers to average
try:
   with open("numbers.txt", "r") as file:
      numbers = [int(line.strip()) for line in file if line.strip()]

   if numbers:
      avarage = sum(numbers) / len(numbers)
      print("Average:", avarage)
   else:
      print("File is empty.")

except FileNotFoundError:
   print("File not found.")
except ValueError:
   print("File contains invalid number.")
except Exception as e:
   print("Error:", e)





##### Problem 29: Print files line reverse order
try:
   with open("source.txt", "r") as file:
      lines = file.readlines()
   
   for line in reversed(lines):
      print(line.strip())

except FileNotFoundError:
   print("File not found.")

except Exception as e:
   print("Error:", e)





##### Problem 30: Check whether every line number and print different invalid line
try:
   with open("numbers.txt", "r") as file:
      for line_no, line in enumerate(file, start=1):
         value = line.strip()

         try:
            num = int(value)
            print(f"Line{line_no}: Valid number: {num}")
         except ValueError:
            print(f"Line{line_no}: Invalid number: {value}")
   
except FileNotFoundError:
   print("File not found.")
except Exception as e:
   print("Error:", e)


## Understanding
total = 0
try:
   with open("numbers.txt", "r") as file:
      for line in file:
         lines = line.strip()

         try:
            num = int(lines)
            total += int(num)
         except ValueError:
            pass 

   print("Total:", total)
except FileNotFoundError:
   print("File not found.")
except Exception as e:
 print("Error:", e)









