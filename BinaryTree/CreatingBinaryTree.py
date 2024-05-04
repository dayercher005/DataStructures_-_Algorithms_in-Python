class BinaryTree:  #Define class called BinaryTree to represent tree. It has 3 instance variables. 
    def __init__(self, value):
        self.key = value        #Variable key holds the node's data
        self.left_child = None  #Variable left_child keeps track of the node's left child
        self.right_child = None #Variable right_child keeps track of its right child.
#When you create a child node for your tree, you create a new instance of your BinaryTree class, which also has a key, left child and right child.
#Every child has a subtree. Subtree is a node in a tree, other than the root node, and its descendants. A subtree can have subtrees.

    def insert_left(self, value):       #Define a method called insert_left to create a child node and insert it into the left side of your tree.
        if self.left_child == None:         #Method checks to see whether self.left_child is None. If it is, create new Binary Tree class and assign it to self.left_child.
            self.left_child = BinaryTree(value)
        else:      #Otherwise, create a new BinaryTree object and assign whatever Binary object is currently at self.left_child to new BinaryTree's self.left_child. and then assign the new BinaryTree to self.left_child
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):      #Define method called insert_right which does the same thing as insert_left but adds a new node to the right side of your binary tree.
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree
