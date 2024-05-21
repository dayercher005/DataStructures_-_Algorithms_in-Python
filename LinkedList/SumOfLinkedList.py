class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Iterative Solution
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

#Recursive Solution
    def SumOfLinkedList(self, head):
        if head == None:
            return 0
        return head.data + SumOfLinkedList(head.next)


