from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.cache = {}
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Key is not in cache - return None
        if key not in self.cache:
            return None
        else:
            # Key is in cache
            # move it to most recently used
            self.storage.move_to_end(self.cache[key])
            # return value
            return self.cache[key].value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # Add key-value pair to cache
    def set(self, key, value):
        # if item/key already exists
        if key in self.cache:
            # overwrite the value
            # where is the value stored
            node = self.cache[key]
            node.value = (key, value)
            # move to the tail (most recently used)
            self.storage.move_to_end(node)
            return
        
        # size is a at limit  
        if self.storage.length == self.limit:
            # evict the oldest one
            index_of_oldest = self.storage.head.value[0]
            del self.cache[index_of_oldest]
            self.storage.remove_from_head((key, value))
            # add the new one to the end
        
        # size is not a limit  
            # add to order
        self.storage.add_to_tail((key, value))
            # add to cache
        self.cache[key] = self.storage.tail
        
        
          
        
            