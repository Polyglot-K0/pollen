```Python
# Cache Replacement Policy in Python
# 'collections module implements specialized container datatypes providing alternatives to Python's general purpose built in containers, dict, list, set, and tuple
from collections import OrderdDict


class LRU:
    # 'capacity: int' is a type "hint". It indicates that the variable 'capacity' is expected to be of type 'int' 

    # Our function
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
    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            self.cache[key] = value
            self.cache.move_to_end(key)


```