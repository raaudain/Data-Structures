import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # Adds value to tail
    def enqueue(self, value):
        # Pushing to the end of the list
        self.storage.add_to_tail(value)

    # Removes value from the start of the list
    def dequeue(self):
        # If the first item in list doesn't exist return null
        if self.storage.head is None:
            return None
        else:
            # Else return the function to remove first item
            return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
