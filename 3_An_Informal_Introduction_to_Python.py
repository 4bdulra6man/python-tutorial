# Commnets in Python
# Commnets in Python start with a #, and Python will ignore them.
# Commnets can be used to explain code, and to make it more readable.
# Commnets can also be used to prevent execution when testing code.

# Python interpreter acts as a calculator, '()' is used to group expressions.

# Devision always returns a float.

# To get an integer result you can use '//' operator.

# Calculating power is done with '**' operator.

# operators with mixed type operands convert the integer operand to floating point:
print(4 + 3.0)  # output: 7.0

# In interactive mode, the last printed expression is assigned to the variable '_'.
# tax = 12.5 / 100
# price = 100.50
# price * tax  # output: 12.5625
# print(price + _)  # output: 113.0625

# In addition to 'int' and 'float', Python also supports 'complex' numbers.
# Complex numbers are written with a 'j' or 'J' as the imaginary part:
a = 2 + 3j
b = 4 + 5j
print(a * b)  # output: (-7+22j)

# Strings are represented in Python with either single or double quotes:
s = 'Hello, World!'
print(s)  # output: Hello, World!
s = "Hello, World!"
print(s)  # output: Hello, World!

# In interactive mode when printing a string, the quotes will be included in the output:
s = 'Hello, World!'
s  # output: 'Hello, World!'
print(s)  # output: Hello, World!

# r"string" is a raw string where backslashes are not treated as escape characters:
print('C:\some\name')  # output: C:\some
print(r'C:\some\name')  # output: C:\some\name

# String literals can span multiple lines by using triple quotes:
# End-of-line characters are automatically included in the string unless the line ends with a backslash:
print("""\

Usage: thingy [OPTIONS]

     -h                        Display this usage message

     -H hostname               Hostname to connect to\
\
""")

one = 'One'
print(one[-0])

'''
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''

word = 'Python'
# print(word[42]) # Out of Range Error

# Out of range slice indexes are handled gracefully when used for slicing:
print(word[1:42])  # output: ython
print(word[42:])   # output: (empty string)

# Python strings cannot be changed - they are immutable.
# But we can create a new string from a slice of another string:
print(word[:2] + 'py')  # output: Pypy

print(len(word))

# List: which can be written as a list of comma-separated values (items) between square brackets.
# Can contains items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
print(squares)  # output: [1, 4, 9, 16, 25]

# Like strings, lists and other sequences types, lists can be indexed and sliced:
print(squares[0])    # output: 1
print(squares[-1])   # output: 25
print(squares[-3:])  # output: [9, 16, 25]

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(cubes)  # output: [1, 8, 27, 65, 125]
cubes[3] = 64  # fix the error
print(cubes)  # output: [1, 8, 27, 64, 125]
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # add the cube of 7
print(cubes)  # output: [1, 8, 27, 64, 125, 216, 343]

# When assigning a list to a variable, the variable gets a reference to the list, not a copy of it.
# This means that if you change the list using one variable, the change will be visible through the other variable.
list1 = [1, 2, 3, 4, 5]
list2 = list1  # list2 is just another name for list1

print(id(list1), id(list2))  # output: same id for both
print(list1 is list2)  # output: True

list1.append(6)  # modify list1
print(list1)  # output: [1, 2, 3, 4, 5, 6]
print(list2)  # output: [1, 2, 3, 4, 5, 6] - list2 reflects the change

# To make a copy of a list, you can use a slice notation (shallow copy):
# All slice operations return a new list containing the requested elements.
list3 = list1[:]  # make a copy of list1
print(id(list1), id(list3))  # output: different id for both
print(list1 is list3)  # output: False
list1.append(7)  # modify list1
print(list1)  # output: [1, 2, 3, 4, 5, 6, 7]
print(list3)  # output: [1, 2, 3, 4, 5, 6] - list3 does not reflect the change

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)  # output: ['a', 'b', 'c', 'd, 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']  # replace some values
print(letters)  # output: ['a', 'b', 'C', 'D, 'E', 'f', 'g']
letters[2:5] = []  # remove some values
print(letters)  # output: ['a', 'b', 'f', 'g']
letters[:] = []  # clear the list
print(letters)  # output: []

# Also possible to nest lists (create lists containing other lists):
a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)       # output: [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])    # output: ['a', 'b', 'c']
print(x[0][1]) # output: 'b'

a, b = 1, 2
print(a, b)  # output: 1 2

# In python, all the non-zero integers are considered as True, and zero is considered as False.
"""Any non-zero integer value is true; zero is false"""
# This is about how Python (like C) interprets numbers as boolean values:
# 0 → considered False
# Any other number (1, -1, 42, -99, ...) → considered True

if 5:
    print("This is True")
if 0:
    print("This is False")

# 1. Truthiness vs Equality

# In Python, there’s a difference between:
# Truthiness → how a value behaves when used in a condition (if, while, etc.).
# Equality → whether two values are exactly the same (==).

print(0 == False) # output: True
print(1 == True)  # output: True
print(2 == True)  # output: False
print(-1 == True) # output: False
print(-2 == True) # output: False

print(bool(0))   # False
print(bool(1))   # True
print(bool(2))   # True
print(bool(-1))  # True
print(bool(-2))  # True

# The condition may also be a string or a list value.
# In fact any other sequence is considered false if it is empty, and true if it is not empty.

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b