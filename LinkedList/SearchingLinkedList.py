class Node: 
    def __init__(self, data, next=None):   #Class has 2 variables: data which holds a piece of data , and the second, next contains the next Node in the list
        self.data = data
        self.next = next

class LinkedList:     #Define a class to represent linked list,with an instance variable called head to hold lists's head
    def __init__(self):
        self.head = None

    def search(self, target): #The search method accepts one parameter called target, which is the piece of data you are looking for. 
        current = self.head
        while current.next:    #You iterate through the linked list and if current node's data matches target value, return True
            if current.data == target:
                return True
            else:          #If current node's data is not a match, you set current to the next node in the linked list and continue iterating
                current = current.next
        return False  #If you reached the end of your linked list without a match, you know it is not in your list and return False
        


