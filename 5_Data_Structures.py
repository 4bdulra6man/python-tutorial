# More on Lists:

# list.append():
    # Add items to the end of the list, similar to `a[len(a):] = [x]`
myList = [1, 2, 3, 4]

myList.append(5)

print(myList)

# Using **Slice Assignment**
myList[len(myList):] = [7]

print(myList)

# myList[len(myList):] = 8  # TypeError: can only assign an iterable
                            # Because this way of assignment, the list object tries to loop over
                            # that element.

# list.extend(iterable)
# Extending the list by appending all the items from the iterable.
newList = ['a', 'b', 'c']
myList.extend(newList)

print(myList)

# list.insert(i, x)
# Insert an items at the given position of the list.
myList.insert(6, "sep")

print(myList)

myList.insert(len(myList), "end")   # Is equavalent to `list.append("end")`.

print(myList)

# list.remove(x)
# It removes the first items of the list its value is equal to x.
myList.remove(1)
print(myList)

# myList.remove(33) # raises a "ValueError", cause of element not found.

# list.pop([i])
# Removes an element of the given position in the list, and return it.
# If no index was given, it removes the last index of the list.
myList.pop(len(myList) - 1)
print(myList)

# Is also equal to:
myList.pop()
print(myList)

# Raises a "IndexError" if the list is empty, or the given index is outside the range of the list.
# myList.pop(len(myList))

# myList = []
# print(myList)

# list.clear()
# Remove all items from the list, is similar to `del myList[:]`.

myList = [1, 2, 3, 4, 5]
myList.clear()

print(myList)

# list.index()
# Return a zeor-based index of the "first" occurance of 'x' in the list.
# Raises a ValueError if there is no such item.
myList = [1, '2', 3, 4, 5, 1, '2', 3, 4, 5, 1, '2', 3, 4, 5, 1, '2', 3, 4, 5]
index = myList.index(3, 0, 9)
print(index)

index = myList.index(3)
print(index)

# list.count(x)
# Return the number of the times "x" appears in the list.
print(myList.count(5))

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place.
# The arguments can be used for sort customization.

myList = ['Apple', 'Orange', 'Banana', 'IPhone']
print(myList)
myList.sort()
print(myList)

# list.reverse()
# Reverse the element of the list in place.
myList = [2, 3, 5, 4, 7, 1, 6, 8]
myList.sort()
myList.reverse()
print(myList)

# list.copy()
# Return a "shallow copy" of the list. Similar to `myList[:]`
newList = myList.copy()
print(newList)

myList[len(myList):] = [9, 10]
print(newList)
print(myList)

myList = [1, 2, 3]
newList = myList[:]
print(myList)
print(newList)

myList[len(myList):] = [4, 5, 6, 7]
print(myList)
print(newList)

# You might have noticed that methods like insert, remove or sort that only modify the 
# list have no return value printed – they return the default None. 
# This is a design principle for all mutable data structures in Python.


# Using Lists as Stacks:
# The list methods make it very easy to use a list as a stack, where the last 
# element added is the first element retrieved (“last-in, first-out”). To add an item 
# to the top of the stack, use append(). To retrieve an item from the top 
# of the stack, use pop() without an explicit index. For example:
stack = [3, 4, 5]
stack.append(6)
print(stack)

stack.append(7)
print(stack)

stack.pop()
print(stack)


# Using Lists as Queues:
# It is also possible to use a list as a queue, where the first element added is the first 
# element retrieved (“first-in, first-out”); however, lists are not efficient 
# for this purpose. While appends and pops from the end of list are fast, doing 
# inserts or pops from the beginning of a list is slow (because all of the other elements have 
# to be shifted by one).

# To implement a queue, use `collections.deque` which was designed to have 
# fast appends and pops from both ends. For example:
from collections import deque

deque = deque(["Muhammad", "Abdulrahman", "Omar"])
print(deque)

deque.append("Sara")
deque.append("Hajar")
print(deque)

print(deque.popleft())
print(deque)

deque.popleft()
deque.popleft()
print(deque)