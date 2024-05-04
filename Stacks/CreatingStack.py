class Stack:
    def __init__(self):
        self.items = []     #Define an instance variable called items and set it to empty list. This is where we keep track of items in stack.

    def push(self, data):       #Define stack's push method. Use python's build-in append method to ass new piece of data to end if items.
        self.items.append(data)

    def pop(self):              #Define stack's pop method. Use python's built-in pop method to return most recently added item in stack.
        return self.items.pop()
    
    def size(self):             #Define stack's size method. Uses len() method to return length of stack.
        return len(self.items)
    
    def is_empty(self):         # Checks whether stack is empty.
        return len(self.items) == 0
    
    def peek(self):             #Returns last item in stack
        return self.items[-1]

