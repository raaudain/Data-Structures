import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.queue = Queue()
        self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target < self.value and self.left:
            # If target is less than, continue to return
            return self.left.contains(target)
        elif target >= self.value and self.right:
            # If target is more than or equal to, continue to return
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            # Continues to move to the node on the right
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        #If there is a left branch...
        if self.left:
            self.left.for_each(cb)
        # If there is a right branch...
        if self.right:
            self.right.for_each(cb)
        
        # if self.left and self.right:
        #     self.left.for_each(cb)
        #     self.right.for_each(cb)
        # elif self.left:
        #     self.left.for_each(cb)
        # elif self.right:
        #     self.right.for_each(cb)
        # else:
        #     cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            # Print low values
            self.in_order_print(node.left)
            # Print root value
            print(node.value)
            # Print high values
            self.in_order_print(node.right)
        else:
            return
        
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Queue
        
        # Put first node in queue
        self.queue.enqueue(node)
        
        # While queue is not empty
        while self.queue.len() > 0:
            temp = self.queue.dequeue()
            print(temp.value)
            
            # Dequeue node
            if temp.left:
                self.queue.enqueue(temp.left)
                
            if temp.right:
                self.queue.enqueue(temp.right)
                
            # Iterative BFT
            # create queue
            # add root to queue
            # while queue is not empty
            # node = pop head of queue
            # DO THE THING!!! (print)
            # add children of node to queue    
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Stack
        
        # Add first node in stack
        self.stack.push(node)
        
        # while stack is not empty
        while self.stack.len() > 0:
            temp = self.stack.pop()
            print(temp.value)
            
            if temp.left:
                self.stack.push(temp.left)
                
            if temp.right:
                self.stack.push(temp.right)
            
  
        # node = pop top of stack
        # DO THE THING!!! (print)
        # add children of node to stack
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

