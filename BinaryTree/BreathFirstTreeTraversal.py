class BinaryTree:
    def __init__(self, value):
        self.key= value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self, n):      #Method called breadth_first_search takes one parameter, n, which is the data to search for.
        current = [self]                    #Define 2 lists. Use the first list, current, to keep track of nodes in current level you're searching
        next = []                           #Use second list to keep track of nodes in the next level. Add self to current, so algorithm starts searching tree's root.
        while current:                      #while loop continues as long as current still contains nodes to search.
            for node in current:            #Use for loop to iterate through every node in current
                if node.key == n:           #If node's value matches n, return True.
                    return True
                if node.left_child:         #Otherwise append node's left and right child nodes to next list, if they're not None, so they get searched when you search the next level.
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next                 #Swap your lists current and next when while loop ends. List of nodes to search next becomes the list of nodes to search now, and set next to empty list.
            next = []
        return False                        #If while loop terminates, return False since breadth-first search did not find n in the tree.
