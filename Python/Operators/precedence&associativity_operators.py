

# 1. Operators Precedence
expression = 10 + 20 * 30
print(expression)

# 2. Precedence of Logical Operators
name = "Alex"
age = 0

if name == "Alex" or name == "Jhon" and age >= 2:
   print("Hello! Welcome.")
else:
   print("Good Bye!!")



# 3. Operators Associativity
print(100 / 10 * 20)
# / & * both have the same precedence but left to right (LTR) associativity 

print(5 - 2 + 3)
print(5 - (2 + 3))
# Note: Demonstrates left-to-right associativity for division, multiplication, addtion and subtraction.


print(2 ** 3 ** 2)
# Note: Demonstrates right-to-left associativity for exponentiation(**).


# 4. Operators Precedence and Associativity
expression = 100 + 200 / 10 - 3 * 10


# 5. Operator Precedence and Associativity List in Python
"""
Consider following list of operator precedence and associativity in Python.
It shows all operators from highest precedence to lowest precedence.

1. (): Parentheses(highest precedence) -> Associativity: left to right
2. x[index], x[index:index]: Subscription, slicing -> Associativity: left to right.
3. await x: Await expression
4. **: Exponentiation -> Associativity: Right to left
5. +x, -x, ~x: Unary plus, unary minus, bitwise NOT -> Associativity: Right to left
6. *, @, /, //, %: Multiplication, matrix multiplication, division, floor division, remainder -> Associativity: Left to right
7. +, -: Addition and subtraction -> Associativity : Left to right
8. <<, >>: Bitwise shifts -> Associativity: Left to right
9. & : Bitwise AND -> Associativity: Left to right
10. ^ : Bitwise XOR -> Associativity: Left to right
11. | : Bitwise OR -> Associativity: Left to right
12. in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, membership, identity tests -> Associativity: Left to right
13. not x : Boolean NOT -> Associativity: Right to left
14. and : Boolean AND -> Associativity: Left to right
15. or : Boolean OR -> Associativity: Left to right
16. if-else : Conditional expression -> Associativity: Right to left
17. lambda : Lambda expression
18. := : Assignment expression (Walrus operator) -> Associativity: Right to left

Note: Parentheses () have highest predence and can override default order.
      Some operators, like await and lambda, do not have associativity.
          
"""