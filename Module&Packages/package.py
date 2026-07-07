

## Module vs Package
"""
module
calculator.py = module

# Package = utils
utils/
      calculator.py
      math_utils.py
      string_utils.py


one .py file = module
many module file folder = package


suppose:
project/
      main.py

      utils/
            __init__.py
            math_utils.py
            string_utils.py

"""

## 2. __init__.py
import utils


## 3. Package to import
from utils.math_utils import add

print(add(5, 5))


## 4. Package Shortcut
from utils import add 
print(add(10, 10))

from utils.math_utils import add 
print(add(10, 10))


## 5. Nested package
from app.users.models import User

print(User("Nondita"))



##
from utils.string_utils import Product

print(Product("Telephone"))


## 
from utils import Product

print(Product("Keyboard"))


## 
