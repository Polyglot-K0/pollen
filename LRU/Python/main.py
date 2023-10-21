# Cache Replacement Policy in Python
from collections import OrderdDict

class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache - OrderDict()

    def get(self, ke: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # move accessed item to the end
            self.cache.move_to_end(key)
            return self.cache[key]