import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # Adds value to end of list
    def push(self, value):
        # Pushing to the end of the list
        self.storage.add_to_tail(value)

    # Removes value from end of list
    def pop(self):
        # If the tail's value is null return null
        if self.storage.tail is None:
            return None
        else:
            # Return the function to remove the last item
            return self.storage.remove_from_tail()
        
    def len(self):
        return self.storage.length
