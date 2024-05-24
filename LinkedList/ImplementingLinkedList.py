class Node: 
    def __init__(self, data, next=None):   #Class has 2 variables: data which holds a piece of data , and the second, next contains the next Node in the list
        self.data = data
        self.next = next

class LinkedList:     #Define a class to represent linked list,with an instance variable called head to hold lists's head
    def __init__(self):
        self.head = None

    def append(self, data):  #Create append method that adds a new node to list
        if not self.head:    #If list doesn't have a head, create a new node and it becomes the head of your linked list
            self.head = Node(data)
            return
        current = self.head    #If list has a head, find the last node in linked list and create a new node and set its instance variable next to it.
        while current.next:    # Use a while loop that continues as long as current.next is not None because you know you are at the end yof your linked list when it is
            current = current.next  #Inside while loop, continually assign current to current.next until current is None and while loop terminates
        current.next = Node(data)   #The variable current now holds the last node in list so create a new node and assign it to current.next

    def __str__(self):        #You can add the __str__ method to your LinkedList class to print all of the nodes in your list
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


a_list = LinkedList()  #Example of using append to add new nodes to your linked list
a_list.append("Tuesday")
a_list.append("Wednesday")