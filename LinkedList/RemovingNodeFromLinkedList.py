class Node: 
    def __init__(self, data, next=None):   #Class has 2 variables: data which holds a piece of data , and the second, next contains the next Node in the list
        self.data = data
        self.next = next

class LinkedList:     #Define a class to represent linked list,with an instance variable called head to hold lists's head
    def __init__(self):
        self.head = None

    def remove(self, target): #Your method remove accepts one parameter,target which is the piece of dat that the node you want to remove contains
        if self.head == target:  #You handle what happens if node you want to delete is the head of your list
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next