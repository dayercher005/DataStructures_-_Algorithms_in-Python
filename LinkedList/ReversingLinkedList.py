class Node: 
    def __init__(self, data, next=None):   #Class has 2 variables: data which holds a piece of data , and the second, next contains the next Node in the list
        self.data = data
        self.next = next

class LinkedList:     #Define a class to represent linked list,with an instance variable called head to hold lists's head
    def __init__(self):
        self.head = None

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous