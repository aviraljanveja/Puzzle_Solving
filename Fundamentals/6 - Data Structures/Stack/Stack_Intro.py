# A stack is a data structure where the last element added is the first one to be removed.
# This way of organizing elements is called LIFO : Last In First Out.

# Basic operations we can do on a stack are:
# - Push: Adds a new element on top of the stack.
# - Pop: Removes and returns the top element from the stack.
# - Peek: Returns the top (last) element on the stack.
# - Size: Finds the number of elements in the stack.

# Stacks can be used to implement undo mechanisms, to revert to previous states,
# to create algorithms for depth-first search in graphs, or for backtracking.

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print(stack)  # Output = ['A', 'B', 'C']

# Peek
print(stack[-1])  # Output = C

# Pop
print(stack.pop())  # Output = C

# Stack after Pop
print(stack)  # Output = ['A', 'B']

# Size
print(len(stack))  # Output = 2
