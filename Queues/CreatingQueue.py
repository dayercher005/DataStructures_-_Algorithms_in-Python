class Node:                 #Define a Node class to represent the nodes in your queue's internal linked list:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class Queue:                #In Queue, variables self.front and self.rear keep track of its front and rear items. Track the front and rear of your queue so you can enqueue and dequeue in constant time.
    def __init__(self):     #You can also track queue's size in the variable self._size
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):    #Define method called enqueue that adds an item to rear of queue. Method accepts data you want to store in queue as parameter.
        self._size += 1         #Increment self.size by 1 since we're adding a new item to queue.
        node = Node(item)       #Create a new node to store item in queue's internal linked list.
        if self.rear is None:   #If self.rear is None, means queue is empty, so set self.front and self.rear to the node just created.
            self.front = node
            self.rear = node
        else:                   #Otherwise assign new node to self.rear.next to add it to queue's internal linked list. Then assign new node to self.rear so that its at rear of queue.
            self.rear.next = node
            self.rear = node

    def dequeue(self):          #Method called dequeue to remove item from front of queue.
        if self.front is None:
            raise IndexError('pop from empty queue')    #Throws an exception if you try to dequeue an item when queue is empty.
        self._size -= 1
        temp = self.front       #Calling dequeue: remove and return item at front of queue. Hence we need to store the node at front of queue (self.front) to temp to reference it later after removing it from internal linked list.
        self.front = self.front.next    #Remove item at front of queue from queue's internal linked list by assigning self.front to self.front.next
        if self.front is None:      #If there are no more items in queue after removing item at front of queue, set self.rear to None since no items at rear of queue.
            self.rear = None
        return temp.data
    
    def size(self):     #Method returns the number of items in queue.
        return self._size
