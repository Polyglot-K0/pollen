# Cashe repplacement policy
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        # OrderedDict() is a class from Pythons standard library 'collections module'
        self.cache = OrderedDict()
            self.capacity = capacity
        
    def get(self, key):
        if key in self.cache:
            # Include notes
            value - self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1
        
    def put(self, key, value):
        if key in self.cache: 