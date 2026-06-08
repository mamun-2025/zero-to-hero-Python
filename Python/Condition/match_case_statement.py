
# Python Match Case Statement
"""
Introduced in Python 3.10, the match case statement offers a powerful mechanism for pattern matching in Python.
It allows us to perform more expressive and readable conditional checks.
Unlike traditional if-elif-else chains, which can become unwieldy with complex conditions,
the match-case statement provides a more elegant and flexible solution.
"""

# Syntax:
"""
match subject:
   case pattern1:
      code block if pattern 1 matches
   case pattern2:
      code block if pattern 2 matches
   case _:
      default case(wildcard) if no other pattern matches
      
"""
# Example 1:
def check_number(x):
   match x :
      case 10:
         print("It's 10")
      case 20:
         print("It's 20")
      case _:
         print("It's neither 10 nor 20")

check_number(30)
check_number(20)

# Example 2:
def greet(person):
   match person:
      case "A":
         print("Hello, A for Ashik.")
      case "R":
         print("Hello, R for Rajib.")
      case "N": 
         print("Hey, Nondita. Do you love me?")
         answer = input("Please say me? Yes or No(y/n):")
         if answer == "y":
            print("Congratulations Mamun.")
         else:
            print("Oh sorrry! Don't give up. Please stand up and carry on your hard-work")
      case _:
         print("Hello, stranger!")
      
greet("N")


# Example 3: Match case statement with or operator
def num_check(x):
   match x:
      case 10 | 20 | 30:
         print(f"Matched {x}")
      case _:
         print("No match found.")

num_check(20)
num_check(30)
num_check(15)


# Example 4: Match case statement on sequences
def process(data):
   match data:
      case [x, y]:
         print(f"Two element list: {x}, {y}")
      case [x, y, z]:
         print(f"Three element list: {x}, {y}, {z}")
      case _:
         print("Unkown data format.")

process((["Mamun", "Nondita"]))
process([1, 2, 3])
process({1, 2, 3, 4})


# Example 5: Match case statement on Mappings (Dictionaries)
def person(person):
   match person:
      case {"name": name, "age": age}:
         print(f"Name: {name}, Age: {age}")
      case {"name": name}:
         print(f"Name: {name}")
      case _:
         print("Unknown format")

person({"name": "Mamun", "age": 25})
person({"name": "Dhaka"})
person({"city": "Dhaka"})


# Example 6: Match case statement on python classes

class Shape:
    pass

class Circle(Shape):
    __match_args__ = ("radius",)
    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    __match_args__ = ("width", "height")
    def __init__(self, width, height):
        self.width = width
        self.height = height

def check_shape(shape):
    match shape:
      
      	# Match Circle and extract the radius
        case Circle(radius):  
            print(f"circle radius {radius}.")
            
        # Match Rectangle and extract width and height
        case Rectangle(width, height):  
            print(f"Rectangle width {width} and height {height}.")
            
        # Default case for any other object
        case _:  
            print("This is an unknown shape.")

# Create objects of Circle and Rectangle
circle = Circle(10)
rectangle = Rectangle(4, 6)

# Test with different shapes
check_shape(circle)     
check_shape(rectangle)

