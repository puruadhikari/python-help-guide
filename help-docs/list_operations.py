# Basic List Operations
lst = [1, 2, 3, 4, 5]

len(lst)                  # Get length of list
lst.append(6)             # Add element to end of list
lst.insert(2, 2.5)        # Insert element at specific index
lst.remove(3)             # Remove first occurrence of element
lst.pop()                 # Remove and return last element
lst.pop(0)                # Remove and return element at index
lst.clear()               # Remove all elements from list
lst.extend([6, 7, 8])     # Extend list by appending elements from another list
lst.index(4)              # Find index of first occurrence of element
lst.count(2)              # Count occurrences of element
lst.sort()                # Sort list in ascending order
lst.reverse()             # Reverse the order of list

# List Slicing
sliced_lst = lst[1:4]     # Slice list from index 1 to 3
sliced_lst = lst[:3]      # Slice from start to index 2
sliced_lst = lst[2:]      # Slice from index 2 to end
sliced_lst = lst[::-1]    # Reverse list using slicing

# List Comprehensions
squared = [x**2 for x in lst]  # Create new list with squares of elements
evens = [x for x in lst if x % 2 == 0]  # Filter list for even numbers

# Using Lists as Stacks
stack = []
stack.append(1)           # Push element onto stack
stack.append(2)
stack.pop()               # Pop element from stack (LIFO)

# Using Lists as Queues
from collections import deque

queue = deque()
queue.append(1)           # Enqueue element
queue.append(2)
queue.popleft()           # Dequeue element (FIFO)

# List Copying
copy_lst = lst.copy()     # Create a shallow copy of the list
copy_lst = lst[:]         # Another way to copy the list

# List Membership
3 in lst                  # Check if element is in list
10 not in lst             # Check if element is not in list