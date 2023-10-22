### LRU (Least Recently Used) cache - implemented in Python

## What is happening below?

- The LRU cache has methods 'put' (Least 
- If key is fetched (or updated), it's considered recentely used and moved to othe end.
- When the cache exceeds its copacity and a new key-value pair is to be inserted, the least recently used item (the first item in the cache) is evicted 

```Python
# 'collections module implements specialized container datatypes providing alternatives to Python's general purpose built in containers, dict, list, set, and tuple
from collections import OrderedDict


# Defining a class called 'LRU'
# This will implement the Least Recently Used caching algorithms
class LRU:
    # 'capacity: int' is a type "hint". It indicates that the variable 'capacity' is expected to be of type 'int' 

    # Our function
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
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
        else:

            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value

def main():
    cache = LRU(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
    cache.put(4,4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

if __name__ == "__main__":
    main()

```