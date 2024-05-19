class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Iterative Version
class LinkedList:
    def __init__(self):

    def SumOfLinkedList(head):
        summation = 0
        current = head
        while current:
            current = current.next
            summation += current.val

        return summation


    

