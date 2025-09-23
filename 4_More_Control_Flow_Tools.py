# `for` statement in python is used to iterate over a sequence 
# (like a list, tuple, dictionary, set, or string) in the order that they appear in the sequence.

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

# Code over a collection while iterating over the same collection can be tricky to get right. 
# instead, it is usually more straight forward to iterate
#  over a copy of the collection or creating a new collection.

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Iterating over a copy
for user, status in users.copy().items():
    if status == "inactive":
        del(users[user])

# Creating a new collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

for user, status in active_users.items():
    print(user, status)

# In many cases `range()` functions acts as a list, but in facts it isn't.
# Python doesn't immediatly build a list like [1, 2, 3, ..., 9], instead it 
# creates a range-object 
# Saves memory since doesn't store all the members at once.
# Can turned into a list if intended.
print(range(10)) # returns a special object 'range-object'

# break_stmt: breaks out of the innermost enclosing `for` or `while` loop

# continue_stmt: continues with the next iteration of the loop


# Meaning of:

# statement: Is the smallest standalone unit of execution in programming "complete instruction":
"""

x = 5            # assignment statement
print(x)         # function call statement
if x > 3:        # if statement (compound statement)
    print("Yes")

"""

# clause: Is a part of compound statement.
# It is usually a `header` (keyword + condition) + a `suite` (block of indented code).
"""
if x > 3:              # <-- this is an "if clause"
    print("Yes")       # body of the if clause
elif x == 3:           # <-- this is an "elif clause"
    print("Equal")
else:                  # <-- this is an "else clause"
    print("No")

"""

# expression: Is something that produce a value.
# It can be a small part of `statement` or even the whole statement in some cases.
"""
x + 5        # expression (produces a value)
x > 3        # expression (boolean value True/False)
len("abc")   # expression (evaluates to 3)

"""

# suite: Is a block of code that belongs to a clause.
# In Python, a `suite` is one or more indented statement belongs to a clause.
"""
if x > 3:        # <-- if clause
    print("Yes") # <-- suite (contains 2 statements here)
    x += 1       # <-- still part of the same suite

"""

# In the for or while loop the break_stmt may be paired with the `else` cluase, if the loop
# finishes without executing the `break`, the `else` clause executes.
# In a `for` loop, if no `break` occured, the `else` cluase is executed after the loop finishes
# as a final iteration.
# In a while loop, it is executed after the loop's condition become `false`.
# Other ways of ending the loop early, such as a `return` or `raised exception`, will skip
# the execution of the `else` clause.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

else:
    print("Loop is over")   

# As we did above, the `else` clause can be used with a `for` loop to find items that
# meet a certain condition, and if none is found, the `else` clause can be used to
# handle that case.

for i in "anything":
    break
else:
    print("no break")  # won't print since the loop is broken out of

# the else clause has more in common with the else clause of a try statement than 
# it does with that of if statements: a try statement’s 
# else clause runs when no exception occurs, 
# and a loop’s else clause runs when no break occurs. 

# `pass` statement: does nothing, it can be used when a statement is syntactically required
# but no action is needed or when the code will be implemented later.

def function_that_does_nothing():
    pass  # Placeholder for future code

# For this last case, many people use the ellipsis literal ... instead of pass.
def another_function():
    ...

# A match statement takes an expression and compares 
# its value to successive patterns given as one or more case blocks.
# Only the first pattern that matches gets executed and it can
#  also extract components (sequence elements or object attributes) from the value into variables.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Note: the last case _ is a wildcard pattern that matches anything, and never fails to match.

point = (0, 3)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y} axis")
    case (x, 0):
        print(f"X={x} axis")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

point = ('2', 3)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y} axis")
    case (x, 0):
        print(f"X={x} axis")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# If you are using classes to structure your data you can use the class name followed by an argument list resembling a constructor, 
# but with the ability to capture attributes into variables:

# When it comes to classes matching: 
# There are two types of patterns you can use:
# 1. Attribute patterns: which match attributes by name:
# 2. Positional patterns: which match attributes by position.
# Quick Mnemonic
# case Point(..., ...) -> positional pattern → needs __match_args__.
# case Point(x=..., y=...) -> keyword pattern → never needs __match_args__.

# Here is an example of attribute patterns:

class Point:
    # `__init__` is called dunder method.
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(2, 3)

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"Y={y} axis")
    case Point(x=x, y=0):
        print(f"X={x} axis")
    case Point(x=x, y=y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# Here is an example of positional patterns:

class PositionalPoint:
    # `__match_args__` is called dunder attribute.
    __match_args__ = ("x", "y")  # Define the order of attributes for positional matching

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = PositionalPoint(2, 3)

match point:
    case PositionalPoint(0, 0): # Positional pattern need to '__match_args__' to be defined at the class.
        print("Origin")
    case PositionalPoint(0, y):
        print(f"Y={y} axis")
    case PositionalPoint(x, 0):
        print(f"X={x} axis")
    case PositionalPoint(x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# What about mixing positional and keyword patterns?
# You can mix positional and keyword patterns in a single case block, but with some restrictions:
# 1. Positional patterns must come before keyword patterns.
# 2. You cannot use the same attribute in both positional and keyword 
# patterns within the same case block.
# 3. If you use a wildcard (_) in a positional pattern, it must be the last positional pattern.
point = PositionalPoint(2, 3)
match point:
    case PositionalPoint(0, y=0):  # Valid: positional pattern first, then keyword pattern
        print("Origin")
    case PositionalPoint(0, y=y):  # Valid: positional pattern first, then keyword pattern
        print(f"Y={y} axis")
    case PositionalPoint(x=x, y=0):  # Valid: positional pattern first, then keyword pattern
        print(f"X={x} axis")
    case PositionalPoint(x, y=y):  # Valid: positional pattern first, then keyword pattern
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# Note: The following would be invalid and would raise a SyntaxError:
point = PositionalPoint(2, 3)
match point:
    # case PositionalPoint(x=0, y):  # Invalid: keyword before positional
    case PositionalPoint(x=0, y=3):
        print(f"Y={y} axis")
    case PositionalPoint(y=0, x=0):  # Invalid: keyword before positional
        print("Origin")
    case PositionalPoint(y=0, x=x):  # Invalid: keyword before positional
        print(f"X={x} axis")
    # case PositionalPoint(y=y, x):  # Invalid: keyword before positional
    case PositionalPoint(y=3, x=x):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# In the above invalid examples, the keyword patterns (e.g., x=0) are placed before 
# positional patterns (e.g., 0),
# which is not allowed in Python's pattern matching syntax.


class PositionalPoint:
    __match_args__ = ("x", "y")  # Defines the order for positional matching

    def __init__(self, x, y, label=None):
        self.x = x
        self.y = y
        self.label = label  # an extra attribute (not included in positional matching)

    def __repr__(self):
        return f"PositionalPoint(x={self.x}, y={self.y}, label={self.label})"
    
point = PositionalPoint(2, 3, label="A")

# Note: The following would be invalid and would raise a SyntaxError:
match point:
    case PositionalPoint(2, 3, label='A'):
        print("Matched with label A")
    # case PositionalPoint(2, y=3, 'A'):  # Invalid: positional pattern after keyword pattern
    #                                      # here 'A' is positional after keyword patterns
    #     print("Matched with label A")
    # case PositionalPoint(0, y=0, x=0):  # Invalid: same attribute used in both positional and keyword patterns
    #                                     # here x is used in both positional and keyword patterns
    #     print("Origin")
    # case PositionalPoint(0, y=y, x=0):  # Invalid: same attribute used in both positional and keyword patterns
    #                                     # here x is used in both positional and keyword patterns
    #     print(f"Y={y} axis")
    # case PositionalPoint(x=x, y=0, x=0):    # Invalid: same attribute used in both positional and keyword patterns
    #                                         # here x is used in both positional and keyword patterns
    #     print(f"X={x} axis")
    # case PositionalPoint(x, y=y, x=0):  # Invalid: same attribute used in both positional and keyword patterns
    #                                     # here x is used in both positional and keyword patterns
    #     print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
    
# In the above invalid examples, the attribute x is used in both positional and keyword patterns 
# within the same case block, which is not allowed in Python's pattern matching syntax.


# Defining Functions
def fibonacci(n):
    """'Fibonacci sequence' is a series of numbers in which each 
    number is the sum of the two preceding ones. It usually starts with 0 and 1."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

fibonacci(200)

# Function parameter is what we define inside the parenthises.
# Function aragument is what we pass as a value to the function.
# Functions' variables are only available inside thin function, not outside, but can access these
# variables for reading only.
# If you tried to access that variables for extra work, then python will treat it as a new variable.
# When run a function, Python creates a special place ('local symbol table') to store the variable
# that belong only to that function.

# When a function needs a variable, Python looks for it in this order:
# Local symbol table (inside the function)
# Enclosing function’s local table (if the function is inside another function)
# Global symbol table (variables defined outside all functions)
# Built-in names (like len, print, etc.)
# Python searches for variables in: local -> enclosing -> global -> built-in.
# Arguments are passed by value (**object reference**), means Python passes a reference to that object
# not the object itself.
# If the object is mutable (like a list), the function can modify it.
# If the object is immutable (like a number or string), the function cannot change it outside.
# Every time function runs, Python creates a **new local "workspace"** for that call.
# Variable in that work space doesn't affect other calls, even if the same function is called again.
# A function definition associates the function name with the function object in the current symbol table.
# Even the function doesn't return a value, in Python it still return `None`.

a = 10  # 'global' variable

def outer():
    a = 20  # create a new local variable, doesn't touch the global variable from the **global symbole table**
            # outer's local variable
    x = 30  # outer's local variable
    print(f"a equals: {a}")
    print(f"x equals: {x}")

    def middle():
        y = 40  # middle's local variable
        print(f"y equals: {y}")
        print(f"x equals: {x}") # 'middle' function doesn't define 'x' variable, Python looks at
                                # 'outer' **function symbole table**, then the **global symbole table**.
        print(f"a equals {a}")

        def inner():
            z = 50  # middle's local variable
            print(f"z equals: {z}")

        inner()
        
    middle()
    
outer()

print(a)

# Assigning a variable inside a function, creates a new local variable, even if there is a global
# variable with the same name.

x = 40

def changeX():
    x = 5
    print(f"'x' from changeX equals: {x}")

changeX()

print(f"'x' from print equals: {x}")

# `global` keyword is used to modify a global variable inside a function.
def changeXII():
    global x 
    x = 50
    print(f"'x' from changeXII equals: {x}")

changeXII()

print(f"'x' from print equals: {x}")


# `nonlocal` keyword is used to modify a variable inside an enclosing function, like 
# a nested function.

def outer():
    y = 70
    print(f"y from outer equals: {y}")

    def inner():
        nonlocal y
        y = 80
        print(f"y from inner equals: {y}")
    
    inner()

outer()

# More on defining functions:
# 1- Default argument values
def passOnlyOneArg(arg, name="abdulrahman", age=23):
    print(f"name is: {name}, age is: {age}, and the arg that you have passed is: {arg}")

passOnlyOneArg("'message...!'")

# `in` keyword checks if a sequence contain a contains a certain value or not.
message="hello, world"
if "hello" in message:
    print(f"message '{message}' is a greeting.")
else:
    print("not a greeting message.")

# **Important warning**: The default value is evaluated only once.
# This make differnece when working with a mutable object, such as list, dictionary, or an
# instance of most classes.

# Example:
def ex(a, L=[]):
    L.append(a)
    print(L)

ex(1)   # [1]
ex(2)   # [1, 2]
ex(3)   # [1, 2, 3]

# Make the default arguments' values to not be shared between subsequent of calls.
def ex(a, L=None):
    if L is None:
        L=[]
    L.append(a)
    print(L)

ex(1)   # [1]
ex(2)   # [2]
ex(3)   # [3]

# 2- Keyword arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# Invalid calls:
"""
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
"""

def greet(first, *others):
    print("Hello,", first)
    print("Other names:", others)

greet("Alice", "Bob", "Charlie")

# 3- Special parameters
# Restricts the way that the parameters can be passes, so that developer need only to look
# to the function definition to determines if the arguments are passed by position, position 
# or keyword keyword.

"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""

# `*args` collects extra 'positional arguments'.
# `**kwds` collects all the extra 'keyword arguments'.

# def foo(name, **kwds):  # cause a potential error, if the passed keyword argumets to the `**kwds` match the name of the 
#                         # the functions parameters, then python tries to assign it twice 
#     """Check if the passed dictionary contans a 'name' key."""
#     return 'name' in kwds

# print(foo("Alice", name="Bob"))  # True

def foo(name, **kwds):
    """Check if the passed dictionary contans a 'name' key."""
    return 'name' in kwds   # no errors

print(foo("Alice", city="Paris"))  # False

dict = {"AGE":23, "Name":"abdulrahman"}

print(foo("ali", **dict))   # False

# Solve this collision by making the 'name' parameter as a positional-only argument.

def foo(name, /, **kwds):
    """Check if the passed dictionary contans a 'name' key."""
    return 'name' in kwds   # no errors

print(foo("abdulrahman", name="Abdulrahman"))   # True; as we made the first `foo()` parameter as a positional-only.

# Recap:
    # Use positional-only if you want the name of the parameters to not be available to the user. 
    # This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when 
    # the function is called or if you need to take some positional parameters and arbitrary keywords.

    # Use keyword-only when names have meaning and the function definition is more understandable by being explicit with 
    # names or you want to prevent users relying on the position of the argument being passed.

    # For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

sep = '/'
args = ('outer-folder', 'middle-folder', 'inner-folder')

print(sep.join(args))

# Unpacking argument list:
lst = [2, 15, 5]
tpl = (2, 15, 5)

print(list(range(*lst)))
print(list(range(*tpl)))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# lambda expression:
    # Is a syntactic sugar to define a function, where a function is required to do some tasks.
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)

# Function Annotations:

    # Are stored in the `__annotations` attribute of the function as a dictionary, and has no
    # effect on the other part of the function.


    # Parameter Annotations:
    # Are defined by a colon after the parameter name,  followed by an expression evaluating to the value of the annotation.


    # Return Annotation:
    # Are defined by a literal `->` followed by an expression, between the parameter list and the colon denoting the end of `def` stmt.

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

# For better code readability: Intermizzo coding-style
