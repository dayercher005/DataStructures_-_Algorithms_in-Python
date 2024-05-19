class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Iterative Version
class LinkedList:
    def __init__(self):
        self.head = None

    def SumOfLinkedList(self, head):
        summation = 0
        current = head
        while current:
            current = current.next
            summation += current.data

        return summation


    

